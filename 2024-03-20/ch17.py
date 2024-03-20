# https://api.github.com/search/repositories?q=language:python+sort:stars

import requests
import plotly.express as px

url = "https://api.github.com/search/repositories?q=language:python+sort:stars"

headers = {"Accept": "application/vnd.github.v3+json"}
res = requests.get(url, headers=headers)
# print(type(res.json()))
# print(res.json()["items"])


res_dict = res.json()["items"]
names, stars = [], []
for r in res_dict:
    names.append(r["name"])
    stars.append(r["stargazers_count"])

fig  = px.bar(x=names,  y=stars)
fig.show()