# Odd or Even Program with Error Handling inside a Function

def add_or_even():
    try:
        num = int(input("Enter a number: "))
        
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
