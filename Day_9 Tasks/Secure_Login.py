from functools import wraps

# Decorator to verify login status before running wrapped function
def login_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get("is_logged_in"):
            return func(user, *args, **kwargs)
        print("Access Denied: Please log in first.")
    return wrapper

@login_required
def view_dashboard(user):
    print(f"Welcome to your dashboard, {user['username']}!")

guest_user = {"username": "Guest", "is_logged_in": False}
auth_user = {"username": "Charan", "is_logged_in": True}

view_dashboard(guest_user)
view_dashboard(auth_user)