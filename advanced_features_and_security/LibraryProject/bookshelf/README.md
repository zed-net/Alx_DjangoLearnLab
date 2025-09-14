# Permissions & Groups Setup

## Custom Permissions
Defined in `Book` model (`bookshelf/models.py`):
- `can_view`: Can view books
- `can_create`: Can create books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

## Groups
Created automatically via `bookshelf/signals.py`:
- **Editors**: can_create, can_edit
- **Viewers**: can_view
- **Admins**: all custom permissions

## Usage in Views
Protected with `@permission_required`:
- `book_list` → requires `can_view`
- `book_create` → requires `can_create`
- `book_edit` → requires `can_edit`
- `book_delete` → requires `can_delete`
