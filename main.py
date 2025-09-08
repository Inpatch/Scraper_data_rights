import requests

class scrabe():

    def __init__(self, url):
        self.url = url


    def scrabe(self):
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(self.url)
        data = response.json()
        print(data)

x = scrabe("https://www.reddit.com/dev/api")
x.scrabe()