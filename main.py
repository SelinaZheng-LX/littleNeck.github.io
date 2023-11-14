import folium
import pandas as pd


df = pd.read_csv("clean_heat_dataset.csv")
# print(df["Latitude"])
qu = df[df['Borough'].isin(['Queens'])]
lNeck = df.groupby('Postcode').get_group(11362 and 11363)
print("Number of entries in Little Neck: ", lNeck)
zipCodes_lNeck = [11362, 11363]
lNeck_zip = df[df['Postcode'].isin(zipCodes_lNeck)]
lNeck_map = folium.Map(location=[40.7662, 73.7316], zoom_start=10)
for index,row in lNeck_zip.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Building Type"]
    if row["Building Type"] == "Elevator Apartments":
        buildingType_Icon = folium.Icon(color="purple")
    elif row["Building Type"] == "Walk-Up Apartments":
        buildingType_Icon = folium.Icon(color="red")
    elif row["Building Type"] == "Condominiums":
        buildingType_Icon = folium.Icon(color="blue")
    elif row["Building Type"] == "Educational Structures":
        buildingType_Icon = folium.Icon(color="green")
    elif row["Building Type"] == "Factory & Industrial Buildings":
        buildingType_Icon = folium.Icon(color="yellow")
    elif row["Building Type"] == "Warehouses":
        buildingType_Icon = folium.Icon(color="black")
    else:
        buildingType_Icon = folium.Icon(color="pink")
    newMarker = folium.Marker([lat,lon], popup=name, icon=buildingType_Icon)
    newMarker.add_to(lNeck_map)


lNeck_map.save(outfile='lNeck.html')