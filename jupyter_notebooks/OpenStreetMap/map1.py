import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])


map = folium.Map(location=[20.59,78.96], zoom_start=5, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes") # create a feature group and add children in them
# fg.add_child(folium.Marker(location=[21, 79],popup="Hi, This is a marker", icon = folium.Icon(color="green")))
# fg.add_child(folium.Marker(location=[19, 81],popup="Hi, This is a marker", icon = folium.Icon(color="green")))

for lt, ln, el in zip(lat, lon, ele):
    if el<2000:
        fgv.add_child(folium.CircleMarker(location=[lt, ln], popup = str(el) + " m", color="green", fill_opacity=0.6, radius=8, fill_color="Yellow", fill=True))
    elif el>=2000 and el <3000:
        fgv.add_child(folium.Marker(location=[lt, ln], popup = str(el) + " m", icon = folium.Icon(color="orange")))
    else:
        fgv.add_child(folium.Marker(location=[lt, ln], popup = str(el) + " m", icon = folium.Icon(color="magenta")))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x : {'fillColor':'green' if x['properties']['POP2005']< 50000000
else 'orange' if 50000000<=x['properties']['POP2005']<100000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("FirstMap.html")
