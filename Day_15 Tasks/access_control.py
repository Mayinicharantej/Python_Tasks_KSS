user_roles = {
    "alice": "admin",
    "bob": "editor",
    "charlie": "viewer"
}


# Decorator factory accepting allowed roles
def require_role(allowed_roles):
    def decorator(func):
        def wrapper(username, *args, **kwargs):
            role = user_roles.get(username)
            if role not in allowed_roles:
                print(f"Access denied for '{username}' (role: {role}).")
                return None
            return func(username, *args, **kwargs)
        return wrapper
    return decorator


@require_role(["admin"])
def delete_database(username):
    print(f"Database deleted by {username}.")


@require_role(["admin", "editor"])
def edit_article(username, title):
    print(f"'{title}' edited by {username}.")


delete_database("alice")
delete_database("bob")
edit_article("bob", "Python Guide")
edit_article("charlie", "Python Guide")