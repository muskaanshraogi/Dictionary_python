import folium
import pandas

data = pandas.read_csv("directory.csv")
lats = list(data["Latitude"])
lons = list(data["Longitude"])
add = list(data["Street Address"])

map = folium.Map(location = [18.5204,73.8567], zoom_start = 10, tiles = "Stamen Watercolor")
fs = folium.FeatureGroup(name="Starbucks")

for lt, lg, ad in zip(lats, lons, add):
        fs.add_child(folium.Marker(location = [lt,lg], popup = ad, icon = folium.Icon(color="green")))

zom = pandas.read_csv("zomato.csv")
latz = list(zom["Latitude"])
lonz = list(zom["Longitude"])
name = list(zom["Name"])

fz = folium.FeatureGroup(name="Zomato Restaurants")

for lt, lg, n in zip(latz, lonz, name):
        fz.add_child(folium.Marker(location = [lt, lg], popup = n, icon=folium.Icon(color="red")))

map.add_child(fs)
map.add_child(fz)
map.add_child(folium.LayerControl());
map.save("map1.html")
