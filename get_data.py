import requests

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzU3NDQ0MzM2LjIzMDA3MSwiaWF0IjoxNzU3MzU3OTM2LjIzMDA3MSwianRpIjoiRnFXRnNuMTZ1VkpvT0dGY2NONnB2c2F3QWFXZnp3IiwiY2lkIjoiV2FrTW4xS2JxN09NUXNOUVZTUjRBdyIsImxpZCI6InQyXzFveHI3cXkzenMiLCJhaWQiOiJ0Ml8xb3hyN3F5M3pzIiwibGNhIjoxNzQ2NzAzNDI4Mzk1LCJzY3AiOiJlSnlLVnNwTVNjMHJ5U3lwVklvRkJBQUFfXzhjTHdSbiIsInJjaWQiOiJkQ3dIWjFnWnUyU0RRZkVLcHZ2anFoMmpGVDV2MUwxdjN3TTBaY1YyaW04IiwiZmxvIjo4fQ.eVSsAwVzX0RXEqajehzo5Dz4Kr38Mc0ySbOw3T49lI4NaK0OkYQMHXNb5M4Uz85s9tFf7rEvufs4wkfm_F6QXRp0KdSNvC75C-OENczyEF9NcOANI71Qy0hRoiY7GYiOs-VvnsgfONChV8X5TzLakBSlAcgKX0lNL29DiXO-0Rx50f62zgoDaUHo45-Q4xc5-zdOes9RxohQd742dcJnJ7j6T0l9D0Ldlu7xhazCgGEehZuYNMw0AsXEBGLwl_NmEhpjsNH0iQfGwyiD0zTz3bxovuIbVVBnO5TSJbnadJRPHBZRYTar7X2TfdhBgrExuYDdBbxy4QSSFKCUbM3Tdg"  # Replace with your token
headers = {
    "Authorization": f"bearer {token}",
    "User-Agent": "script:my_bot:v1.0 (by /u/Successful_Cable_545)"
}

subreddit = "denmark"
response = requests.get(f"https://oauth.reddit.com/r/{subreddit}/hot?limit=5", headers=headers)

if response.status_code == 200:
    posts = response.json()["data"]["children"]
    for post in posts:
        print(post["data"]["title"])
else:
    print("Error:", response.status_code, response.json())
