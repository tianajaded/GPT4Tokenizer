import requests

api_url = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "titles": "Beyoncé",
    "explaintext": True,
}

# Send a GET request to the Wikipedia API
response = requests.get(api_url, params=params)
data = response.json()

# Extract the page content from the API response
pages = data["query"]["pages"]
page_id = next(iter(pages))  # Get the first (and only) page ID
page_content = pages[page_id]["extract"]

with open("beyonce.txt", "w", encoding="utf-8") as file:
    file.write(page_content)

print("Content saved to beyonce.txt")
