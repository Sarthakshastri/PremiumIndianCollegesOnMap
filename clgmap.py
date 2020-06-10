import pandas as pd
import folium as fl

data=pd.read_csv("college.csv") #encoding="cp1252"
fg=fl.FeatureGroup('India')
#fg.add_child(fl.GeoJson(data=(open('india_states','r',encoding="utf-8-sig").read())))

LAT=list(data['Latitude'])
LON=list(data['Longitude'])
name=list(data['College Name'])
location=list(data['Location'])
website=list(data['Website'])
image=list(data['Image'])

for lt,ln,nm,loc,web,img in zip(LAT,LON,name,location,website,image):
    fg.add_child(fl.Marker(location=[lt,ln],tooltip=nm, popup="<h4><b>Name: </b></h4><h4>"+nm+"</h4><br><h4><b>City: </b></h4><h4>"+loc+
    "</h4><br><h4><b>Website: </b></h4><a href="+web+"><h4> Click Here</h4></a>"+"<br><img src="+img+" height=90 width=150>", icon=fl.Icon(color='darkblue')))

map=fl.Map(location=[21.14,79.08], zoom_start=5)
map.add_child(fg)
map.save('CollegeLocation.html')