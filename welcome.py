def print_welcome_message(name):
    """
    Prints a fun, personal, friendly, and concise welcome message.

    Args:
        name (str): The name of the person to welcome.
    """
    print(f"Hey there, {name}! So glad you're here. Let's make some magic happen! ✨")

# --- Modified Code Starts Here ---

# 1. Ask the user for their name using the 'input()' function
#    The user's response is then stored directly into the 'user_name' variable.
user_name = input("What's your name? ")

# 2. Call the 'print_welcome_message' function
#    We pass the value stored in the 'user_name' variable to the function.
print_welcome_message(user_name)