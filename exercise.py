# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    letter = input ("Enter a letter (a-z or A-Z):").strip()

    if letter.isalpha() and letter in vowels: 
        print(f'The letter {letter} is a vowel')
    elif letter.isalpha():
        print(f'The letter {letter} is a consonant')
    else:
        print(f'Invalid input! Please enter a letter (a-z or A-Z):')
print('E1 - Complete')
# Call the function
check_letter()


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    vote_age = 18
    age_input = int(input("Please enter your age: ").strip())
    if age_input >= vote_age:
        print("Eligible to vote!")
    elif age_input < 0:
        print("Please enter a valid age!")
    elif age_input < vote_age:
        print("Not eligible to vote!")
    else:
        print("Please enter a valid numerical age!")
print('E2 - Complete')

# Call the function
check_voting_eligibility()


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = int(input ("Input a dog's age: ").strip())

    if dog_age < 0:
        print("Not a valid age")
    elif dog_age <= 2: 
        print(dog_age * 10)
    else:
        dog_age = 20 + (dog_age - 2) * 7
        print(dog_age)

print('E3 - Complete')

# Call the function
calculate_dog_years()


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here    
    is_it_cold = input ("Is the weather cold? yes or no?: ").strip().lower() == "yes"
    is_it_raining = input ("Is it raining? yes or no?: ").strip().lower() == "yes"

    if is_it_cold and is_it_raining:
        print("Wear a waterproof coat.")
    elif not is_it_cold and not is_it_raining:
        print("Wear light clothing.")
    elif is_it_cold and not is_it_raining:
        print("Wear a warm coat.")
    elif not is_it_cold and is_it_raining:
        print("Carry an umbrella.")
    else:
        print("It's t-shirt weather!")
    
    print('E4 - Complete')

# Call the function
weather_advice()


# ----------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    
    month = input ("Enter the month of the year (Jan - Dec): ").strip().lower()
    date = int(input ("Enter the day of the month: ").strip())
    if (month == "dec" and date >= 21) or (month == "jan") or (month == "feb") or (month == "mar" and date <= 19):
        season = "Winter"
    elif (month == "mar" and date >= 20) or (month == "apr") or (month == "may") or (month == "jun" and date <= 20):
        season = "Spring"
    elif (month == "jun" and date >= 21) or (month == "jul") or (month == "aug") or (month == "sep" and date <= 21):
        season = "Summer"
    elif (month == "sep" and date >= 22) or (month == "oct") or (month == "nov") or (month == "dec" and date <= 20):
        season == "Autumn"
    else:
        print("Please enter a valid month and date!")
    print(f"{month} {date} is in {season}.")
print('E5 - Complete')

# Call the function
determine_season()
