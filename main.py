import requests
from send_email import send_email

topic = "tesla"
key = "049137c2a49c4436b95a85ed73dc587b"
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&"\
      "from=2024-09-12&to=2024-09-12&"\
      "sortBy=popularity&"\
      "apiKey=049137c2a49c4436b95a85ed73dc587b&"\
      "language=en"


#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()
#print(type(content))

#source, author, title, description, url, urlToImage, publishedAt, content, __len__
#Access the article data
body = ""
for article in content["articles"]:
      if article["title"] and article["description"] is not None:
          body = "Subject: Today's news" \
          + body + article["title"] + "\n" \
          + article["description"] + "\n" \
          + article["url"] \
          + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
