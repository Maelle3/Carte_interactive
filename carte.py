import folium

lat_marseille = 43.2969500
lon_marseille = 5.3810700


def creation_carte():
    return folium.Map(location=[lat_marseille, lon_marseille], zoom_start=12, min_zoom=11)


def creation_marker(carte, x , y, message):
    return folium.Marker([x, y], popup=message, icon=folium.Icon(icon='info-sign')).add_to(carte)
