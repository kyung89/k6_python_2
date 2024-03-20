
# import requests

# u = 'https://api.github.com/search/repositories?q=language:python+sort:stars'
# response = requests.get(u)
# print(type(response.json()))
# res = response.json()

from matplotlib import pyplot as plt
import json
names = []
stars = []
with open('github_api_star.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
    print(len(res['items']), type(res['items']))
    for item in res['items']:
        # print(item['name'], type(item['name']))
        # print(item['stargazers_count'], type(item['stargazers_count']))
        names.append(item['name'])        
        stars.append(item['stargazers_count'])

plt.bar(names, stars)
plt.xticks(rotation=45)
plt.show()