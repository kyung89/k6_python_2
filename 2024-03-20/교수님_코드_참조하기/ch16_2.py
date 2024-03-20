import json
import plotly.express as px

mag, lat, lon = [], [], []

with open('b.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(type(data), type(data['features']), data['features'][0])
    for feature in data['features']:
        mag.append(feature['properties']['mag'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])

fig = px.scatter_geo(lat=lat, lon=lon, size=mag)
fig.show()