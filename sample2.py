# -*- coding: utf-8 -*-

import webbrowser
import folium

from map_center_coord import MapCenterCoord

def main():
    f_map = folium.Map(
        location = [35.658099, 139.741357],
        zoom_start = 12)

    folium.Marker(
        [35.658099, 139.741357],
        popup="日本経緯度原点",
    ).add_to(f_map)

    MapCenterCoord().add_to(f_map)

    f_map.save('map.html')
    webbrowser.open('map.html')

if __name__ == "__main__":
    main()
