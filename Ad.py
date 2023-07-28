import colorama
from colorama import Fore, Style

# Function to display the calculator banner
def display_banner():
    print(Fore.BLUE + """
 _______  _______  _______           _______  _______  _______ 
(  ____ \(  ____ )(  ___  )|\     /|(  ____ \(  ____ \(  ____ \\
| (    \/| (    )|| (   ) |( \   / )| (    \/| (    \/| (    \/
| (_____ | (____)|| |   | | \ (_) / | (__    | (_____ | (_____ 
(_____  )|  _____)| |   | |  \   /  |  __)   (_____  )(_____  )
      ) || (      | |   | |   ) (   | (            ) |      ) |
/\____) || )      | (___) |   | |   | (____/\/\____) |/\____) |
\_______)|/       (_______)   \_/   (_______/\_______)\_______)
                                                               
""" + Style.RESET_ALL)

# Function to perform basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

# Main calculator function
def calculator():
    display_banner()
    while True:
        print(Fore.YELLOW + "Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Goodbye!")
            break

        if choice not in ('1', '2', '3', '4', '5'):
            print(Fore.RED + "Invalid choice! Please try again." + Style.RESET_ALL)
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter valid numbers." + Style.RESET_ALL)
            continue

        if choice == '1':
            print(Fore.GREEN + "Result:", add(num1, num2))
        elif choice == '2':
            print(Fore.GREEN + "Result:", subtract(num1, num2))
        elif choice == '3':
            print(Fore.GREEN + "Result:", multiply(num1, num2))
        elif choice == '4':
            print(Fore.GREEN + "Result:", divide(num1, num2))
        elif choice == '5':
            print(Fore.GREEN + "Result:", power(num1, num2))
        
        print(Style.RESET_ALL)

if __name__ == "__main__":
    colorama.init(autoreset=True)
    calculator()
    
