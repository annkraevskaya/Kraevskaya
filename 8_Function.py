def greet_user(name="Гость"):
    return f"Привет, {name}! Рады видеть тебя снова!"


user_name=greet_user("Anna")
print(user_name)
user_name=greet_user()
print(user_name)