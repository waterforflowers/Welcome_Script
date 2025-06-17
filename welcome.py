import datetime # Import the datetime module to work with dates and times

def greet_user(name, time_of_day): # time_of_day is kept for function signature consistency, but not used in the new logic
    """
    Prints a personalized welcome message based on the name.
    Special greeting for "Darryl", general greeting for others.

    Args:
        name (str): The name of the person to greet.
        time_of_day (str): (Not used in this version due to specific name-based greeting).
    """
    if name.lower() == "darryl": # Using .lower() to make it case-insensitive for "darryl"
        print("OH SNAP! IT'S DARRYL! (fangirls and faints) 🤩😵‍💫")
    else:
        print(f"WELCOME TO THE PAGE, {name.upper()}! 🎉") # Using .upper() for a more enthusiastic welcome
    print("Let's make some magic happen! ✨") # This line will always print after the initial name-based greeting


def print_farewell_message(name, favorite_item):
    """
    Prints a personal and friendly farewell message, incorporating a favorite item.

    Args:
        name (str): The name of the person saying goodbye to.
        favorite_item (str): The user's favorite item to include in the message.
    """
    print(f"\nThanks for hanging out, {name}! Hope you have a fantastic time with your {favorite_item}. See you around! 👋")

def get_time_of_day_greeting():
    """
    Determines the appropriate time-based greeting.

    Returns:
        str: A greeting like "Good morning", "Good afternoon", or "Good evening".
    """
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# --- Main Script Logic Starts Here ---

# 1. Ask the user for their name and store it in a variable.
user_name = input("What's your name? ")

# Basic validation to ensure a name is entered
while not user_name.strip(): # .strip() removes leading/trailing whitespace
    user_name = input("Oops! You didn't enter a name. What's your name? ")

# 2. Get the personalized time-of-day greeting.
#    Although the greet_user function no longer uses this directly for the main greeting,
#    we keep this call for potential future use or if other parts of the script were to need it.
current_greeting = get_time_of_day_greeting()

# 3. Print the personalized welcome message using the greeting function.
#    The 'time_of_day' argument is passed, but the function's internal logic now prioritizes the name check.
greet_user(user_name, current_greeting)

# 4. Ask the user for their favorite thing.
favorite_thing = input("What's one of your favorite things? ")

# Basic validation for favorite thing
while not favorite_thing.strip():
    favorite_thing = input("Come on, tell me! What's one of your favorite things? ")

# 5. Interactive Menu
while True: # This loop will continue until the user decides to exit
    print("\n--- What would you like to do? ---")
    print("1. Get another welcome message")
    print("2. Hear a fun fact about Python")
    print("3. Exit")
    
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        # Re-greet the user
        # Note: The 'time_of_day' greeting logic is still available through get_time_of_day_greeting()
        # but the greet_user function will apply the Darryl-specific logic.
        current_greeting = get_time_of_day_greeting() # Get updated time of day
        greet_user(user_name, current_greeting)
    elif choice == '2':
        # Provide a fun fact
        print("Did you know? Python was named after the British comedy group Monty Python! 🐍")
    elif choice == '3':
        # Exit the loop and print farewell message
        print_farewell_message(user_name, favorite_thing)
        break # This breaks out of the 'while True' loop
    else:
        # Handle invalid input
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Script finished. Goodbye!") # This will print after the loop breaks