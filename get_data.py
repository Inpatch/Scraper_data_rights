from urllib import response
import requests
import json
from datetime import datetime
import os



class api_reddit_data():
    def __init__(self):
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
        return response.status_code


    # This get data based on a parameter
    def get_data(self, query:str, sort:str, time:str, subreddit):

        params = {
            'q': {query},
            'sort': {sort},
            'limit': 100,
            'restrict_sr': 1,  # <-- This restricts search to the subreddit
            't': {time} } # Optional: time filter

        url = f"https://oauth.reddit.com/r/{subreddit}/search.json"
        # Fetch posts
        response = requests.get(url, headers=self.header, params= params)
        print(response.status_code)
        

        file_name = f"{params["q"]}_{subreddit}_{datetime.now().timestamp()}.json"
        # "data" is the folder name
        file_path = os.path.join("data/data_reddit_query", file_name)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)
        
# DU var igang med at finde replies til alle comments, men det ser ud til der er en fejl omrking try 
    def get_comment(self, path):
        for filename in os.listdir(path):
            with open(os.path.join(path, filename), "r", encoding="utf-8") as file:
                data = json.load(file)
                try:
                    data = data["data"]
                    data = data["children"]
                    for post in data:
                        post_id = post["data"]["id"]
                        post_subreddit = post["data"]["subreddit"]
                        url = f"https://oauth.reddit.com/r/{post_subreddit}/comments/{post_id}.json"
                        response = requests.get(url, headers=self.header)
                        comments_data = response.json()
                        comments = []
                        for item in comments_data[1]["data"]["children"]:  # [1] is the comments section
                            comment = item["data"]
                            comments.append({
                                "id": comment["id"],
                                "author": comment["author"],
                                "body": comment["body"],
                                "created_utc": comment["created_utc"],
                                "score": comment["score"],
                                "replies": self.replies(comment["replies"]["data"]["children"]) if comment["replies"] else False
                            })


                        file_name = f"{post_id}.json"
                        file_path = os.path.join(path, file_name)
                        with open(file_path, "w", encoding="utf-8") as file:
                            json.dump(comments, file, indent=4, ensure_ascii=False)
                except:
                    print("error")
            break

    def replies(self, data):
        
        replies = []
        for i in data:
            comment_data = i["data"]
            replies.append({
                "id": comment_data["id"],
                "author": comment_data["author"],
                "body": comment_data["body"],
                "created_utc": comment_data["created_utc"],
                "score": comment_data["score"],
                "replies": self.replies(comment_data["replies"]["data"]["children"]) if comment_data["replies"] else False
            })
        return replies







    def get_posts(self):
        # Source https://wiki.archiveteam.org/index.php/List_of_Reddit_subs_by_country_and_territory#Europe
        reddit_urls = [
        "https://old.reddit.com/r/europe/",
        "https://old.reddit.com/r/AskEurope/",
        "https://old.reddit.com/r/EuropeanCulture/",
        "https://old.reddit.com/r/EuropeanUnion/",
        "https://old.reddit.com/r/albania/",
        "https://old.reddit.com/r/andorra/",
        "https://old.reddit.com/r/austria/",
        "https://old.reddit.com/r/belarus/",
        "https://old.reddit.com/r/belgium/",
        "https://old.reddit.com/r/bosnia/",
        "https://old.reddit.com/r/bih/",
        "https://old.reddit.com/r/bulgaria/",
        "https://old.reddit.com/r/croatia/",
        "https://old.reddit.com/r/cyprus/",
        "https://old.reddit.com/r/czech/",
        "https://old.reddit.com/r/de/",
        "https://old.reddit.com/r/Denmark/",
        "https://old.reddit.com/r/Eesti/",
        "https://old.reddit.com/r/FaroeIslands/",
        "https://old.reddit.com/r/Finland/",
        "https://old.reddit.com/r/france/",
        "https://old.reddit.com/r/germany/",
        "https://old.reddit.com/r/gibraltar/",
        "https://old.reddit.com/r/greece/",
        "https://old.reddit.com/r/greenland/",
        "https://old.reddit.com/r/hungary/",
        "https://old.reddit.com/r/iceland/",
        "https://old.reddit.com/r/ireland/",
        "https://old.reddit.com/r/italy/",
        "https://old.reddit.com/r/italia/",
        "https://old.reddit.com/r/kosovo/",
        "https://old.reddit.com/r/latvia/",
        "https://old.reddit.com/r/liechtenstein/",
        "https://old.reddit.com/r/lithuania/",
        "https://old.reddit.com/r/luxembourg/",
        "https://old.reddit.com/r/macedonia/",
        "https://old.reddit.com/r/malta/",
        "https://old.reddit.com/r/moldova/",
        "https://old.reddit.com/r/Monaco/",
        "https://old.reddit.com/r/montenegro/",
        "https://old.reddit.com/r/thenetherlands/",
        "https://old.reddit.com/r/nederlands/",
        "https://old.reddit.com/r/norge/",
        "https://old.reddit.com/r/norway/",
        "https://old.reddit.com/r/Polska/",
        "https://old.reddit.com/r/poland/",
        "https://old.reddit.com/r/portugal/",
        "https://old.reddit.com/r/romania/",
        "https://old.reddit.com/r/rossiya/",
        "https://old.reddit.com/r/roumania/",
        "https://old.reddit.com/r/russia/",
        "https://old.reddit.com/r/San_Marino/",
        "https://old.reddit.com/r/serbia/",
        "https://old.reddit.com/r/srbija/",
        "https://old.reddit.com/r/slovakia/",
        "https://old.reddit.com/r/slovenia/",
        "https://old.reddit.com/r/spain/",
        "https://old.reddit.com/r/espana/",
        "https://old.reddit.com/r/sweden/",
        "https://old.reddit.com/r/schweden/",
        "https://old.reddit.com/r/switzerland/",
        "https://old.reddit.com/r/suisse/",
        "https://old.reddit.com/r/Transnistria/",
        "https://old.reddit.com/r/transdniestria/",
        "https://old.reddit.com/r/turkey/",
        "https://old.reddit.com/r/Turkiye/",
        "https://old.reddit.com/r/ukraine/",
        "https://old.reddit.com/r/ukraina/",
        "https://old.reddit.com/r/unitedkingdom/",
        "https://old.reddit.com/r/Britain/",
        "https://old.reddit.com/r/TheBritishIsles/",
        "https://old.reddit.com/r/vatican/"
    ]

        subreddit_names = [url.split("/r/")[1].rstrip("/") for url in reddit_urls]
        for i in subreddit_names:
            for j in ["Chat Control", "CSAM"]:
                self.get_data(query=i,sort="top",time="year", subreddit=j)


if __name__ == "__main__":
    x = api_reddit_data()
    x.get_comment("data/test_folder")









