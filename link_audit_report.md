# Link Audit Report

An audit of all outbound and internal links on `index.html` was conducted. We verified that **all links are valid and lead to functioning pages**.

No PR containing code modifications was generated because no links were actually broken.

### Expected Link Behaviors & Soft 404 Notes:
- **Bandcamp / Spotify Links:** Several items, such as tracks/albums on Bandcamp and Spotify, initially appeared as soft 404s via simple GET requests due to API restrictions and bot-mitigation, or returned 406 Not Acceptable when queried without a browser user agent. Running checks via Playwright verified these link directly and all media targets exist.
- **Instagram / LinkedIn:** Social media URLs (e.g., Instagram, LinkedIn) may return HTTP 999, 429, or 403 due to their aggressive bot protections against simple CURL/python requests, but manual/browser verification indicates they correctly resolve to valid profiles.
- **Google Fonts:** The preconnect links for `https://fonts.googleapis.com` and `https://fonts.gstatic.com` inherently respond with HTTP 404 when directly accessed. These are legitimate performance optimizations and should not be modified.
- **YouTube Links:** Checked short films and music videos; all YouTube URLs loaded without errors or missing video tags.
