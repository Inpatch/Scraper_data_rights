import requests
import json
from datetime import datetime
import os



class api_reddit_data():
    def __init__(self,subreddit):
        self.subreddit = subreddit
        self.filename = "authentication.json"
        self.authentication_data = self.authentication()
        self.client_id = self.authentication_data["client_id"]
        self.client_secret = self.authentication_data["client_secret"]
        self.redirect_url = self.authentication_data["redirect_url"]
        self.user_agent = self.authentication_data["user_agent"]
        self.password = self.authentication_data["password"]
        self.user_name = self.authentication_data["user_name"]
        self.token = self.authentication_data["token"]
        self.header = {"Authorization": "bearer "+self.token, "User-Agent": self.user_agent}
    

    def authentication(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
            return data
        

        # This is to test if the connection is valid
    def test(self):
        response = requests.get("https://oauth.reddit.com/api/v1/me", headers=self.header)
        return response.text


    # This get data based on a parameter
    def get_data(self, query:str, sort:str, time:str):

        params = {
            'q': {query},
            'sort': {sort},
            'limit': 100,
            'restrict_sr': 1,  # <-- This restricts search to the subreddit
            't': {time} } # Optional: time filter

        url = f"https://oauth.reddit.com/r/{self.subreddit}/search.json"
        # Fetch posts
        response = requests.get(url, headers=self.header, params= params)
        print(response.status_code)
        

        file_name = f"{params["q"]}_{datetime.now().timestamp()}.json"
        # "data" is the folder name
        file_path = os.path.join("data", file_name)
        with open(file_path, "w") as file:
            json.dump(response.json(), file, indent=4)
        

    def get_comment(self, posts):
        # Iterate through posts and fetch comments
        for post in posts:
            post_data = post["data"]
            print(f"Post Title: {post_data['title']}")
            print(f"Post URL: https://reddit.com{post_data['permalink']}\n")

            # Fetch comments for the post
            comments_url = f"https://oauth.reddit.com{post_data['permalink']}.json"
            comments_response = requests.get(comments_url, headers=self.headers)
            comments = comments_response.json()[1]["data"]["children"]

            # Print comments
            for comment in comments:
                if not comment["data"]["author"]:  # Skip removed comments
                    continue
                print(f"Comment by {comment['data']['author']}: {comment['data']['body']}\n")
            print("---")


if __name__ == "__main__":
    x = api_reddit_data("denmark")
    x.get_data()


