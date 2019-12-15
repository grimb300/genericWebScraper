import json

# Import the JSON data
with open('twitterData.json') as json_data:
  jsonData = json.load(json_data)

# Print the entries
for i in jsonData:
  print("At " + i["date"] + ", " + i["author"] + " wrote")
  print(i["tweet"])
  print("-------------------")