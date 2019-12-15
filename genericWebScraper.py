from bs4 import BeautifulSoup
import requests
import json

# Grab the website to scrape
url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

# Iterate over the tweets...
#   <div class="tweetcontainer">
tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
  # ...and put the contents into a JSON object
  tweetObject = {
    "author": tweet.find('h2', attrs={"class": "author"}).text, # <h2 class="author">
    "date": tweet.find('h5', attrs={"class": "dateTime"}).text, # <h5 class="dateTime">
    "tweet": tweet.find('p', attrs={"class": "content"}).text,  # <p class="content">
    "likes": tweet.find('p', attrs={"class": "likes"}).text,    # <p class="likes">
    "shares": tweet.find('p', attrs={"class": "shares"}).text   # <p class="shares">
  }
  tweetArr.append(tweetObject)

# Write the array out to file
with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)