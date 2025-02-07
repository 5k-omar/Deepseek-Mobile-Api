import cloudscraper, json, random, string

def PasswordReset():
    scraper = cloudscraper.create_scraper()
    email = input("Enter your email: ")

    url = "https://chat.deepseek.com/api/v0/users/create_email_verification_code"
    payload = {
        "email": email,
        "locale": "en_US",
        "shumei_verification": {
            "region": "EG",
            "rid": ''.join(random.choices(string.ascii_letters + string.digits, k=18))
        },
        "turnstile_token": "",
        "device_id": "BU6mOuxLxPsFbFlrh+SqpA/aW0wsmdQ4NsYTW+P/BpAvqcGkgaxU87PulDFLkvbhd+WdzrGVKg4YPo8DwWFQzpg==",
        "scenario": "register"
    }
    headers = {
        'User-Agent': "DeepSeek/1.0.6 Android/34",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'x-client-platform': "android",
        'x-client-version': "1.0.6",
        'x-client-locale': "en_US",
        'x-rangers-id': "7884272934146925312",
        'accept-charset': "UTF-8"
    }

    response = scraper.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        verification_code = input("Enter verification code: ")
        password = input("Password: ")
        url = "https://chat.deepseek.com/api/v0/users/email_reset_password"

        payload = {
            "email": email,
            "password": password,
            "email_verification_code": verification_code,
        }

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

        response = scraper.post(url, data=json.dumps(payload), headers=headers)

        print(response.text)
    else:
        print("Error in email verification request:", response.text)

if __name__ == "__main__":
    PasswordReset()
