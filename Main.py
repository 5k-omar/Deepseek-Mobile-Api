import AccountCreator, Login, Chat, password_reset, os, sys, subprocess

try:
    import cloudscraper
except ImportError:
    print("cloudscraper not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cloudscraper"])
    import cloudscraper

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Select an option:")
    print("1. Account Gen")
    print("2. Login")
    print("3. Chat")
    print("4. Password Reset")
    
    choice = input("Enter your choice (1 or 2 or 3 or 4): ")
    
    if choice == "1":
        Clear()
        AccountCreator.main()
    elif choice == "2":
        Clear()
        Login.main()
    elif choice == "3":
        Clear()
        Chat.Chat()
    elif choice == "4":
        Clear()
        password_reset.PasswordReset()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3 or 4.")

if __name__ == "__main__":
    main()
