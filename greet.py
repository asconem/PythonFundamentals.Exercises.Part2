def name_input():
    """
    This function requests a user to enter their name via an input prompt
    """
    user_name = input("Please enter your name: ")
    return user_name

def greet(name):
    """
    This function takes in a person's name as a parameter and returns a customized greeting
    """
    print("Hello " + name + "! How are you today?")

greet(name_input())