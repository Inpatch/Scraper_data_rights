# Scraper_data_rights



Guide:
- Make a reddit profile at reddit.com
- Make a application, and retrieve a token https://www.reddit.com/prefs/apps (in doubt what to put in see below)
name: Something
redirect url: http://localhost:8080 (only matters if you have created a web app)

- Go into authentication_example.json and populate the following things:
client_id: (can be found under the title of your app in https://www.reddit.com/prefs/apps)
client_secret: (can be found in the same place as before as "Secret")
redirect_url: (can be found in the same place as before as "redirect url")
user_agent: change "yourappname" to the apps name and your username to your developer name (can be found in the same place as before)

- Download python from python.org
- Make .venv file (python -m venv .venv)
- Install libaries (pip install -r requirements.txt)
- Run "get_token.py", and see the rest in get_token.py

