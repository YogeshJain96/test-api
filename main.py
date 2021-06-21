import json
import requests
import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())

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
time: {utc_now.isoformat()}
---
"""
print(md_content)
# Writing to md file
with open("sample.md", "w") as outfile:
    outfile.write(md_content)