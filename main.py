import requests
from send_email import send_email

key = "049137c2a49c4436b95a85ed73dc587b"
url = "https://newsapi.org/v2/everything?q=apple&from="\
      "2024-09-12&to=2024-09-12&sortBy=popularity&"\
      "apiKey=049137c2a49c4436b95a85ed73dc587b"
#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()
#print(type(content))

#source, author, title, description, url, urlToImage, publishedAt, content, __len__
#Access the article data
body = ""
for article in content["articles"]:
      if article["title"] in not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
