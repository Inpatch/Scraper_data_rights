import requests
import webbrowser
import json
import requests.auth


class token():
    def __init__(self):
        self.filename = "authentication.json"
        self.authentication_data = self.authentication()
        self.client_id = self.authentication_data["client_id"]
        self.client_secret = self.authentication_data["client_secret"]
        self.redirect_url = self.authentication_data["redirect_url"]
        self.user_agent = self.authentication_data["user_agent"]
        self.password = self.authentication_data["password"]
        self.user_name = self.authentication_data["user_name"]

    def authentication(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
            return data


    def get_token(self):

        # Step 1: Get user authorization
        headers = {"User-Agent": self.user_agent}
        post_data = {"grant_type": "password", "username": self.user_name, "password": self.password }

        client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
        print(response.status_code)

        if response.status_code == 400:
            print("Error ",response.status_code)
            print(response.json)
            return response.status_code
        response = response.json()
        token = response["access_token"]
        headers = {
        "Authorization": f"bearer {token}",
        "User-Agent": self.user_agent,
        }
        response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
        
        if response.status_code == 200:
            print("Your Reddit username:", response.json()["name"])
            print("Succesfull got a token")
            data = {"token":token,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "redirect_url": self.redirect_url,
                "user_agent" : self.user_agent,
                "password": self.password,
                "user_name": self.user_name}



            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"File '{self.filename}' has been created/overwritten with the following content:")
            print(json.dumps(data, indent=4))

        if response.status_code == 400:
            print("Error ", response.status_code)

if __name__ == "__main__":
    x = token()
    x.get_token()
