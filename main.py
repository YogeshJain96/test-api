import json
import requests
import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
ist_now = utc_now.astimezone(pytz.timezone("Asia/Kolkata"))

url = 'https://jsonplaceholder.typicode.com/todos/1'

access_token = ''
headers = {
 'Authorization': 'Bearer ' + access_token,
 'Content-Type': 'application/json; charset=utf-8'
 }

r = requests.get(url, headers=headers)
files = r.json()
print(files)
md_content = f"""---
userId: "{files.get('userId')}"
title: "{files.get('title')}"
completed: {files.get('completed')}
last_updated: "{ist_now.isoformat()}"
---
"""
print(md_content)

# Writing to md file
with open("sample.md", "w") as outfile:
    outfile.write(md_content)
# Append time
with open("timeline.md", "a") as outfile:
    outfile.write(ist_now.isoformat()+'\n')

# Print timeline
timeline_file = open("timeline.md","r")
print ("Output of timeline.md")
print (timeline_file.readlines())