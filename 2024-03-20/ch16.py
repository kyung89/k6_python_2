# p.474

# b.geojson

import json
# https://pypi.org/project/plotly-express/
import plotly.express as px

#json # load : file
#json # loads : str -> dict, dict -> str

# mag, (lat, lon)

# 160개
# mag = []
# lat = []
# lon = []

mag, lon, lat = [], [], []
with open("b.geojson", "r", encoding='UTF8') as f:
    data = json.load(f)
    # print(type(data), type(data['metadata']), type(data['metadata']['count']))
    # print(type(data), type(data['features']), data['features'][0])
    # print()
    # print(data['features'][0]['properties']['mag'])
    # print(data['features'][0]['geometry']['coordinates'])

    for feature in data['features']:
        # print(type(feature['properties']['mag']))
        mag.append(feature['properties']['mag'])
        # print(feature['geometry']['coordinates'])
        lat.append(feature['geometry']['coordinates'][1]) #위도
        lon.append(feature['geometry']['coordinates'][0]) #경도

fig = px.scatter_geo(lat=lat, lon=lon, size=mag, title="Global Earthquakes")
fig.show()

