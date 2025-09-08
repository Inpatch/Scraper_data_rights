import requests
import webbrowser

# Replace these with your app details
client_id = "WakMn1Kbq7OMQsNQVSR4Aw"
client_secret = "aiUHlNuxLpfu5zj7oveGxpUVvU0w8w"
redirect_uri = "http://localhost:8080"
user_agent = "script:my_bot:v1.0 (by /u/Successful_Cable_545)"

# Step 1: Get user authorization
auth_url = f"https://www.reddit.com/api/v1/authorize?client_id={client_id}&response_type=code&state=random_string&redirect_uri={redirect_uri}&duration=permanent&scope=identity"
webbrowser.open(auth_url)

# After authorizing, Reddit will redirect you to http://localhost:8080?code=AUTH_CODE&state=random_string
# Copy the AUTH_CODE from the URL bar and paste it below:
code = input("Paste the 'code' from the URL here: ")

# Step 2: Exchange the code for an access token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_uri,
}
headers = {"User-Agent": user_agent}

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
    "User-Agent": user_agent,
}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
print("Your Reddit username:", response.json()["name"])