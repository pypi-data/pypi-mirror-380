![logo](https://openwrite.io/static/logo.png)

openwrite is a minimalist blogging platform built for writing freely, hosting independently, and publishing without noise.

![PyPI - Downloads](https://img.shields.io/pypi/dw/openwrite)
![PyPI - Version](https://img.shields.io/pypi/v/openwrite)
[![License: AGPL-3.0-or-later](https://img.shields.io/badge/License-AGPL--3.0--or--later-blue.svg)](LICENSE)
![pythonver](https://img.shields.io/badge/python%20version-3.11-blue)

---

## Features

- Multiple blogs per user(limit defined in .env)
- Single-blog mode
- Supports sqlite and mysql databases
- Upload images to local storage or bunny cdn
- Drafts
- Simple markdown editor in posting
- Discover section
- Privacy: 
    - Set if blog should be indexed in search engines
    - Set if post should be listed in "Discover" section
    - Set if username should appear in post page (anonymous posts)
- Lightweight
- No tracking, only data collected is anonymized(hashed) IP for post view counting and likes
- Custom CSS per blog
- Federation using ActivityPub protocol
- Likes system
- Posts importing from xml/csv
- Blog themes
- Gemini protocol
- Statistics per post
- Multilanguage (currently English and Polish)
- Custom favicon per blog
- Subpages per blog
- Valkey support
- Post tags, filtering


## Installation

1. To install openwrite, clone it with `pip`:

```
pip install openwrite
```

2. Then run:

```
openwrite init
```

3. Answer few questions about your instance to generate .env and create all necessary directories.
4. Run:

```
openwrite run
```

to run it in foreground or:

```
openwrite run -d
```

to run it in background.

5. Default user is `admin` with password `openwrite`. You can (and should!) change it in your dashboard. Enjoy!


#### Docker

Docker image is still being prepared. Stay tuned!
