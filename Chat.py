import cloudscraper, json

scraper = cloudscraper.create_scraper()

Authorization = input("\nAuthorization (Token): ")
ask = input("Ask: ")

def Session_Creation():
    payload = {
        "agent": "chat"
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
        'authorization': f"Bearer {Authorization}",
        'accept-charset': "UTF-8"
    }
    try:
        response = scraper.post("https://chat.deepseek.com/api/v0/chat_session/create", data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            session_id = response_data.get("data", {}).get("biz_data", {}).get("id")

            if session_id:
                print(f"Session_Id : {session_id}")
                return session_id
            else:
                print("Session ID not found in response!")
        else:
            print(f"Session creation failed, response code: {response.status_code}")
            print("Error details:", response.text)

    except Exception as e:
        print("Connection Error:", e)
        return None


def Chat(session_id):
    if session_id is None:
        print("No valid session ID, cannot proceed with chat.")
        return

    payload = {
        "chat_session_id": session_id,
        "parent_message_id": None,
        "prompt": ask,
        "ref_file_ids": [],
        "thinking_enabled": True,
        "search_enabled": False,
        "legacy_format": True
    }

    headers = {
        'User-Agent': "DeepSeek/1.0.6 Android/34",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'x-ds-pow-response': "eyJhbGdvcml0aG0iOiJEZWVwU2Vla0hhc2hWMSIsImNoYWxsZW5nZSI6Ijg0YjA1YTM1OGRhNmE3OGE2OTZhNzMwMzYzYzcxMGVhM2ZiOWU4MWM2NjI3YWFhZWIxOTRmZjQ4YTE2OTk0MDYiLCJzYWx0IjoiMGVmMGM4OTU0M2Q3NGEyZThkOGIiLCJzaWduYXR1cmUiOiJkMGM4MzljZTk4YjRlMmI2OWM2NjE3ZmM3ODYxYmE5Y2ViYTQzOTNmMDQwOTMyZjU4MzE3ZmQ1ZTIwMDI3YWQyIiwiYW5zd2VyIjoxMTUxODQsInRhcmdldF9wYXRoIjoiL2FwaS92MC9jaGF0L2NvbXBsZXRpb24ifQ==",
        'x-client-platform': "android",
        'x-client-version': "1.0.6",
        'x-client-locale': "en_US",
        'x-rangers-id': "7884272934146925312",
        'authorization': f"Bearer {Authorization}",
        'accept-charset': "UTF-8"
    }

    response = scraper.post("https://chat.deepseek.com/api/v0/chat/completion", data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        for line in response.text.split("\n"):
            if line.startswith("data: "):
                json_data = json.loads(line[6:])  
                if "choices" in json_data and json_data["choices"]:
                    content = json_data["choices"][0]["delta"].get("content", "")
                    if content:
                        print(content, end="")  
    else:
        print("\nResponseCode: ", response.status_code)
        print("\nResponse: ", response.text)

session_id = Session_Creation()
Chat(session_id)
