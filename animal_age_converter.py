# Dog to Cat to Human Age Calculator

animal = input("Enter dog or cat: ").lower()
age = int(input("Enter age of animal: "))

if animal == "dog":
    if age == 1:
        human_age = 12
    elif age == 2:
        human_age = 24
    else:
        human_age = 24 + (age - 2) * 4
    print(f"Human age of {animal} is: {human_age}")

elif animal == "cat":
    if age == 1:
        human_age = 15
    elif age == 2:
        human_age = 24
    else:
        human_age = 24 + (age - 2) * 4
    print(f"Human age of {animal} is: {human_age}")

else:
    print("Invalid option. Please enter 'dog' or 'cat'.")