import requests
import webbrowser
import json
import os



class token():
    def __init__(self):
        self.filename = "authentication.json"
        self.authentication_data = self.authentication()
        self.client_id = self.authentication_data["client_id"]
        self.client_secret = self.authentication_data["client_secret"]
        self.redirect_url = self.authentication_data["redirect_url"]
        self.user_agent = self.authentication_data["user_agent"]

    def authentication(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
            return data


    def get_token(self):

        # Step 1: Get user authorization
        auth_url = f"https://www.reddit.com/api/v1/authorize?client_id={self.client_id}&response_type=code&state=random_string&redirect_uri={self.redirect_uri}&duration=permanent&scope=identity"
        webbrowser.open(auth_url)

        # After authorizing, Reddit will redirect you to http://localhost:8080/?state=random_string&code=AUTH_CODE#_
        # Copy the AUTH_CODE from the URL bar and paste it below:
        code = input("Paste the 'code' from the URL here: ")

        # Step 2: Exchange the code for an access token
        auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": self.redirect_uri,
        }
        headers = {"User-Agent": self.user_agent}

        response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=auth,
        data=data,
        headers=headers,
        )

        token = response.json()["access_token"]
        print("Access token:", token)

        # Step 3: Use the token to fetch your user info
        headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": self.user_agent,
        }
        response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
        
        if response.status_code == 200:
            print("Your Reddit username:", response.json()["name"])
            print("Succesfull got a token")
            data = {"token":token}

            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"File '{self.filename}' has been created/overwritten with the following content:")
            print(json.dumps(data, indent=4))

if __name__ == "__main__":
    x = token()
    x.get_token()
