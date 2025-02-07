import cloudscraper, random, string

def main():
    print("Supported Domains: gmail.com, outlook.com, hotmail.com")
    email = input("\nEnter your email: ")
    rid = ''.join(random.choices(string.ascii_letters + string.digits, k=18))

    scraper = cloudscraper.create_scraper()
    url = "https://chat.deepseek.com/api/v0/users/create_email_verification_code"
    payload = {
        "email": email,
        "locale": "en_US",
        "shumei_verification": {"region": "EG", "rid": rid},
        "turnstile_token": "",
        "device_id": "BU6mOuxLxPsFbFlrh+SqpA/aW0wsmdQ4NsYTW+P/BpAvqcGkgaxU87PulDFLkvbhd+WdzrGVKg4YPo8DwWFQzpg==",
        "scenario": "register"
    }
    headers = {
        "User-Agent": "DeepSeek/1.0.6 Android/34",
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json",
        "x-client-platform": "android",
        "x-client-version": "1.0.6",
        "x-client-locale": "en_US",
        "x-rangers-id": "7884272934146925312",
        "accept-charset": "UTF-8"
    }

    response = scraper.post(url, json=payload, headers=headers)
    #print(response.text)

    if "Just a moment" in response.text:
        print("Protected By Cloudflare")

    verification_code = input("Enter verification code: ")

    register_url = "https://chat.deepseek.com/api/v0/users/register"
    reg_headers = {
        "User-Agent": "DeepSeek/1.0.6 Android/34",
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json",
        "x-client-platform": "android",
        "x-client-version": "1.0.6",
        "x-client-locale": "en_US",
        "x-rangers-id": "7884272934146925312",
        "x-ds-guest-pow-response": "eyJzYWx0IjoiZjQyMmMxODZjODgwNTQ1MWViZDYiLCJhbnN3ZXIiOjU0MDMxfQ==",
        "accept-charset": "UTF-8"
    }
    register_payload = {
        "region": "EG",
        "locale": "en_US",
        "os": "android",
        "device_id": "BU6mOuxLxPsFbFlrh+SqpA/aW0wsmdQ4NsYTW+P/BpAvqcGkgaxU87PulDFLkvbhd+WdzrGVKg4YPo8DwWFQzpg==",
        "payload": {
            "email": email,
            "email_verification_code": verification_code,
            "password": "CatrineGen"
        }
    }

    register_response = scraper.post(register_url, json=register_payload, headers=reg_headers)
    print(register_response.text)

if __name__ == "__main__":
    main()
