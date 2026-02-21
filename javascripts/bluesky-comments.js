document.addEventListener("DOMContentLoaded", function () {
  var container = document.getElementById("bsky-comments");
  if (!container) return;

  var postUrl = container.getAttribute("data-bsky-uri");
  if (!postUrl) return;

  var API = "https://public.api.bsky.app/xrpc/";

  function extractAtUri(url) {
    var match = url.match(
      /\/profile\/([^/]+)\/post\/([^/]+)/
    );
    if (!match) return null;
    return { handle: match[1], rkey: match[2] };
  }

  function resolveHandle(handle) {
    return fetch(API + "com.atproto.identity.resolveHandle?handle=" + encodeURIComponent(handle))
      .then(function (r) { return r.json(); })
      .then(function (d) { return d.did; });
  }

  function getThread(uri) {
    return fetch(API + "app.bsky.feed.getPostThread?uri=" + encodeURIComponent(uri) + "&depth=10")
      .then(function (r) { return r.json(); });
  }

  function timeSince(dateStr) {
    var seconds = Math.floor((Date.now() - new Date(dateStr).getTime()) / 1000);
    var intervals = [
      { label: "y", seconds: 31536000 },
      { label: "mo", seconds: 2592000 },
      { label: "d", seconds: 86400 },
      { label: "h", seconds: 3600 },
      { label: "m", seconds: 60 }
    ];
    for (var i = 0; i < intervals.length; i++) {
      var count = Math.floor(seconds / intervals[i].seconds);
      if (count >= 1) return count + intervals[i].label + " ago";
    }
    return "just now";
  }

  function renderReply(reply) {
    if (!reply || reply.$type === "app.bsky.feed.defs#blockedPost" ||
        reply.$type === "app.bsky.feed.defs#notFoundPost") return "";

    var post = reply.post;
    var author = post.author;
    var record = post.record;
    var avatar = author.avatar || "";
    var displayName = author.displayName || author.handle;
    var text = record.text || "";
    var likes = post.likeCount || 0;
    var reposts = post.repostCount || 0;
    var time = timeSince(record.createdAt);
    var postUri = "https://bsky.app/profile/" + author.handle + "/post/" + post.uri.split("/").pop();

    var childrenHtml = "";
    if (reply.replies && reply.replies.length > 0) {
      reply.replies.sort(function (a, b) {
        return (b.post.likeCount || 0) - (a.post.likeCount || 0);
      });
      for (var i = 0; i < reply.replies.length; i++) {
        childrenHtml += renderReply(reply.replies[i]);
      }
    }

    return '<div class="bsky-reply">' +
      '<div class="bsky-reply-header">' +
        (avatar ? '<img class="bsky-avatar" src="' + avatar + '" alt="" />' : '') +
        '<a class="bsky-author" href="https://bsky.app/profile/' + author.handle + '" target="_blank" rel="noopener">' +
          '<strong>' + escapeHtml(displayName) + '</strong>' +
          '<span class="bsky-handle">@' + escapeHtml(author.handle) + '</span>' +
        '</a>' +
        '<span class="bsky-time">' + time + '</span>' +
      '</div>' +
      '<p class="bsky-text">' + escapeHtml(text) + '</p>' +
      '<div class="bsky-stats">' +
        (likes > 0 ? '<span>♥ ' + likes + '</span>' : '') +
        (reposts > 0 ? '<span>⟲ ' + reposts + '</span>' : '') +
        '<a href="' + postUri + '" target="_blank" rel="noopener">reply</a>' +
      '</div>' +
      (childrenHtml ? '<div class="bsky-children">' + childrenHtml + '</div>' : '') +
    '</div>';
  }

  function escapeHtml(str) {
    var div = document.createElement("div");
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  var parts = extractAtUri(postUrl);
  if (!parts) {
    container.innerHTML = '<p class="bsky-error">Invalid Bluesky URL.</p>';
    return;
  }

  var handlePromise = parts.handle.startsWith("did:")
    ? Promise.resolve(parts.handle)
    : resolveHandle(parts.handle);

  handlePromise.then(function (did) {
    var atUri = "at://" + did + "/app.bsky.feed.post/" + parts.rkey;
    return getThread(atUri);
  }).then(function (data) {
    if (!data.thread || !data.thread.replies || data.thread.replies.length === 0) {
      container.innerHTML =
        '<p class="bsky-no-replies">No replies yet. ' +
        '<a href="' + postUrl + '" target="_blank" rel="noopener">Be the first to reply on Bluesky!</a></p>';
      return;
    }

    var replies = data.thread.replies;
    replies.sort(function (a, b) {
      return (b.post.likeCount || 0) - (a.post.likeCount || 0);
    });

    var html = '<p class="bsky-reply-count">' + replies.length + ' replies on Bluesky</p>';
    for (var i = 0; i < replies.length; i++) {
      html += renderReply(replies[i]);
    }
    html += '<a class="bsky-join" href="' + postUrl + '" target="_blank" rel="noopener">Join the conversation on Bluesky</a>';
    container.innerHTML = html;
  }).catch(function () {
    container.innerHTML =
      '<p class="bsky-no-replies">Comments could not be loaded. ' +
      '<a href="' + postUrl + '" target="_blank" rel="noopener">View on Bluesky</a></p>';
  });
});
