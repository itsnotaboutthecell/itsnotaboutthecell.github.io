#!/usr/bin/env python3
"""
Publish a draft post to the live site.

Usage:
    python publish_draft.py my-draft-post
    python publish_draft.py my-draft-post --date 2026-03-15
    python publish_draft.py my-draft-post --dry-run

The script will:
1. Validate/add required frontmatter metadata
2. Move the post to the correct year/month partition
3. Copy any images from the draft
4. Run a build to verify everything works
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Configuration
DRAFTS_DIR = Path("drafts")
POSTS_DIR = Path("docs/posts")


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {}, content
    
    frontmatter = {}
    for line in parts[1].strip().split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            
            # Handle lists (categories, tags)
            if key in ('categories', 'tags') and not value:
                # Multi-line list format
                continue
            frontmatter[key] = value
    
    # Parse multi-line lists
    in_list = None
    for line in parts[1].strip().split('\n'):
        stripped = line.strip()
        if stripped.endswith(':') and not ':' in stripped[:-1]:
            in_list = stripped[:-1]
            frontmatter[in_list] = []
        elif in_list and stripped.startswith('- '):
            value = stripped[2:].strip().strip('"\'')
            frontmatter[in_list].append(value)
        elif ':' in line and not stripped.startswith('-'):
            in_list = None
    
    return frontmatter, parts[2]


def generate_frontmatter(meta: dict) -> str:
    """Generate YAML frontmatter from dict."""
    lines = ['---']
    
    # Title first
    if 'title' in meta:
        lines.append(f'title: "{meta["title"]}"')
    
    # Date
    if 'date' in meta:
        lines.append(f'date: {meta["date"]}')
    
    # Categories
    if 'categories' in meta and meta['categories']:
        lines.append('categories:')
        for cat in meta['categories']:
            lines.append(f'  - "{cat}"')
    
    # Tags
    if 'tags' in meta and meta['tags']:
        lines.append('tags:')
        for tag in meta['tags']:
            lines.append(f'  - "{tag}"')
    
    # Comments
    lines.append('comments: true')
    lines.append('---')
    
    return '\n'.join(lines)


def validate_metadata(meta: dict, draft_name: str) -> dict:
    """Validate and fill in missing metadata."""
    errors = []
    
    # Title is required
    if not meta.get('title'):
        # Try to generate from draft folder name
        title = draft_name.replace('-', ' ').title()
        print(f"⚠️  No title found, using: {title}")
        meta['title'] = title
    
    # Date is required
    if not meta.get('date'):
        today = datetime.now().strftime('%Y-%m-%d')
        print(f"⚠️  No date found, using today: {today}")
        meta['date'] = today
    
    # Validate date format
    try:
        datetime.strptime(meta['date'], '%Y-%m-%d')
    except ValueError:
        errors.append(f"Invalid date format: {meta['date']} (expected YYYY-MM-DD)")
    
    # Categories - default to empty list if missing
    if 'categories' not in meta:
        meta['categories'] = []
    elif isinstance(meta['categories'], str):
        meta['categories'] = [meta['categories']]
    
    # Tags - default to empty list if missing  
    if 'tags' not in meta:
        meta['tags'] = []
    elif isinstance(meta['tags'], str):
        meta['tags'] = [meta['tags']]
    
    # Comments - default to true
    meta['comments'] = 'true'
    
    if errors:
        for err in errors:
            print(f"❌ {err}")
        sys.exit(1)
    
    return meta


def get_destination_path(meta: dict, slug: str) -> Path:
    """Calculate the destination path based on date."""
    date = datetime.strptime(meta['date'], '%Y-%m-%d')
    year = date.strftime('%Y')
    month = date.strftime('%m')
    
    return POSTS_DIR / year / month / slug


def deploy_site():
    """Deploy site to GitHub Pages using mkdocs gh-deploy."""
    print("\n🚀 Deploying to GitHub Pages...")
    env = {**os.environ, "NO_MKDOCS_2_WARNING": "1"}
    result = subprocess.run(
        ["mkdocs", "gh-deploy", "--force"],
        capture_output=False,
        env=env
    )
    
    if result.returncode != 0:
        print("❌ Deploy failed!")
        sys.exit(1)
    
    print("✅ Deployed to GitHub Pages!")


def publish_draft(draft_name: str, override_date: str = None, dry_run: bool = False):
    """Publish a draft to the live site."""
    
    draft_path = DRAFTS_DIR / draft_name
    
    # Check if draft exists
    if not draft_path.exists():
        print(f"❌ Draft not found: {draft_path}")
        print(f"\nAvailable drafts:")
        for d in DRAFTS_DIR.iterdir():
            if d.is_dir():
                print(f"  - {d.name}")
        sys.exit(1)
    
    # Find the index.md file
    index_file = draft_path / "index.md"
    if not index_file.exists():
        print(f"❌ No index.md found in {draft_path}")
        sys.exit(1)
    
    print(f"📄 Processing draft: {draft_name}")
    
    # Read and parse content
    content = index_file.read_text(encoding='utf-8')
    meta, body = parse_frontmatter(content)
    
    # Override date if provided
    if override_date:
        meta['date'] = override_date
    
    # Validate and fill metadata
    meta = validate_metadata(meta, draft_name)
    
    print(f"   Title: {meta['title']}")
    print(f"   Date: {meta['date']}")
    print(f"   Categories: {meta.get('categories', [])}")
    print(f"   Tags: {meta.get('tags', [])}")
    
    # Generate slug from draft name (already should be good)
    slug = slugify(draft_name)
    
    # Calculate destination
    dest_path = get_destination_path(meta, slug)
    print(f"   Destination: {dest_path}")
    
    if dest_path.exists():
        print(f"❌ Destination already exists: {dest_path}")
        print("   Use a different draft name or delete the existing post.")
        sys.exit(1)
    
    if dry_run:
        print("\n🔍 DRY RUN - No changes made")
        print(f"   Would create: {dest_path}")
        print(f"   Would copy {len(list(draft_path.glob('images/*')))} images")
        return False
    
    # Create destination directory
    dest_path.mkdir(parents=True, exist_ok=True)
    
    # Generate new content with clean frontmatter
    new_frontmatter = generate_frontmatter(meta)
    new_content = new_frontmatter + '\n' + body.lstrip()
    
    # Write to destination
    dest_index = dest_path / "index.md"
    dest_index.write_text(new_content, encoding='utf-8')
    print(f"✅ Created: {dest_index}")
    
    # Copy images folder if it exists
    images_src = draft_path / "images"
    if images_src.exists():
        images_dest = dest_path / "images"
        shutil.copytree(images_src, images_dest)
        image_count = len(list(images_dest.glob('*')))
        print(f"✅ Copied {image_count} images")
    
    # Run build to verify
    print("\n🔨 Building site to verify...")
    env = {**os.environ, "NO_MKDOCS_2_WARNING": "1"}
    result = subprocess.run(
        ["mkdocs", "build"],
        capture_output=True,
        text=True,
        env=env
    )
    
    if result.returncode != 0:
        print(f"❌ Build failed!")
        print(result.stderr)
        print("\n⚠️  Rolling back...")
        shutil.rmtree(dest_path)
        sys.exit(1)
    
    print("✅ Build successful!")
    
    # Clean up draft
    print(f"\n🗑️  Cleaning up draft: {draft_path}")
    shutil.rmtree(draft_path)
    
    print(f"\n🎉 Published! Your post is now at:")
    print(f"   {dest_path}/index.md")
    
    return True  # Indicate success for deploy chain


def list_drafts():
    """List all available drafts."""
    if not DRAFTS_DIR.exists():
        print("No drafts folder found.")
        return
    
    drafts = [d for d in DRAFTS_DIR.iterdir() if d.is_dir() and d.name != '_template']
    
    if not drafts:
        print("No drafts found.")
        print(f"\nCreate a new draft by adding a folder to {DRAFTS_DIR}/")
        print("with an index.md file inside.")
        return
    
    print(f"📝 Available drafts ({len(drafts)}):\n")
    for draft in sorted(drafts):
        index_file = draft / "index.md"
        if index_file.exists():
            content = index_file.read_text(encoding='utf-8')
            meta, _ = parse_frontmatter(content)
            title = meta.get('title', '(no title)')
            date = meta.get('date', '(no date)')
            print(f"  {draft.name}")
            print(f"    Title: {title}")
            print(f"    Date: {date}")
            print()
        else:
            print(f"  {draft.name} (⚠️ missing index.md)")


def create_draft(name: str):
    """Create a new draft with template."""
    slug = slugify(name)
    draft_path = DRAFTS_DIR / slug
    
    if draft_path.exists():
        print(f"❌ Draft already exists: {draft_path}")
        sys.exit(1)
    
    draft_path.mkdir(parents=True)
    (draft_path / "images").mkdir()
    
    today = datetime.now().strftime('%Y-%m-%d')
    title = name.replace('-', ' ').title()
    
    template = f'''---
title: "{title}"
date: {today}
categories:
  - "microsoft-fabric"
tags:
  - "microsoft-fabric"
comments: true
---

Write your introduction here. This will appear on the blog index page.

<!-- more -->

## First Section

Continue writing your content here...

## Second Section

More content...

'''
    
    index_file = draft_path / "index.md"
    index_file.write_text(template, encoding='utf-8')
    
    print(f"✅ Created new draft: {draft_path}")
    print(f"   Edit: {index_file}")
    print(f"   Images: {draft_path / 'images'}/")
    print(f"\nWhen ready, publish with:")
    print(f"   python publish_draft.py {slug}")


def main():
    parser = argparse.ArgumentParser(
        description="Publish draft posts to the live site",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python publish_draft.py --list              List all drafts
  python publish_draft.py --new my-post       Create a new draft
  python publish_draft.py my-post             Publish a draft
  python publish_draft.py my-post --deploy    Publish and deploy to GitHub Pages
  python publish_draft.py my-post --dry-run   Preview without publishing
  python publish_draft.py my-post --date 2026-04-01  Override publish date
  python publish_draft.py --deploy            Deploy site without publishing
        """
    )
    
    parser.add_argument('draft', nargs='?', help='Name of the draft to publish')
    parser.add_argument('--list', '-l', action='store_true', help='List available drafts')
    parser.add_argument('--new', '-n', metavar='NAME', help='Create a new draft')
    parser.add_argument('--date', '-d', help='Override publish date (YYYY-MM-DD)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without making changes')
    parser.add_argument('--deploy', action='store_true', help='Deploy to GitHub Pages after publishing')
    
    args = parser.parse_args()
    
    if args.list:
        list_drafts()
    elif args.new:
        create_draft(args.new)
    elif args.draft:
        success = publish_draft(args.draft, args.date, args.dry_run)
        if args.deploy and success and not args.dry_run:
            deploy_site()
    elif args.deploy:
        deploy_site()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
