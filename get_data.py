import requests
import json



class api_reddit_data():
    def __init__(self,subreddit):
        self.subreddit = subreddit
        self.filename = "authentication.json"
        # Check if this works
        self.authentication_data = self.authentication()
        self.token = self.authentication_data["token"]
        self.user_agent = self.authentication_data["user_agent"]


        self.headers = {
        "Authorization": f"bearer {self.token}",
        "User-Agent": self.user_agent,
        }
    
    def authentication(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
            return data

        
    def test(self):
        response = requests.get("https://oauth.reddit.com/api/v1/me", headers=self.headers)
        return response.text

    def get_data(self):
        query = "Chat Control"
        url = f"https://oauth.reddit.com/r/{self.subreddit}/search.json?q={query}&sort=new&limit=100"
        #url = f"https://oauth.reddit.com/r/{self.subreddit}/search.json?q={query}"
        print(url)
        # Fetch posts
        #response = requests.get(url, headers=self.headers)
        #print(response.status_code)
        #print(response.text)
        
        
        #posts = response.json()["data"]["children"]

        # Iterate through posts and fetch comments
"""         for post in posts:
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
            print("---") """


if __name__ == "__main__":
    x = api_reddit_data("all")
    x.get_data()


