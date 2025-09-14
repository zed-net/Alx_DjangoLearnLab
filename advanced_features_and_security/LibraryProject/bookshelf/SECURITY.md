# Security measures

## Settings
- `DEBUG` must be False in production. Use `DJANGO_DEBUG` env var in production.
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` set to True — requires HTTPS.
- `X_FRAME_OPTIONS = "DENY"` prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF` and `SECURE_BROWSER_XSS_FILTER` enabled.

## CSRF
All form templates include `{% csrf_token %}`. Views handling POST requests use Django Forms.

## Input validation / SQL
All user input validated through Django `Form` / `ModelForm`. Use ORM filters instead of string concatenation. Raw SQL must use parameterized queries.

## CSP
Configured via `django-csp` (or a custom middleware). Check CSP settings in `settings.py`.

## Permission system
Custom permissions (e.g. `bookshelf.can_edit`) are enforced in views using `@permission_required`.

Testing steps listed in /docs/testing_security.md
