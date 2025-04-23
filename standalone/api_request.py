import requests

result = requests.get("https://google.com")

print(result.text)

with open("google.html", "w") as f:
    f.write(result.text)
