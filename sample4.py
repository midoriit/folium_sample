# -*- coding: utf-8 -*-

import webbrowser
import folium
from folium import Map

class Map2(Map):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    default_js = Map.default_js + [
        ('leafletGestureHandling_js',
         'leaflet-gesture-handling.js')
    ]
    default_css = Map.default_css + [
        ('leafletGestureHandling_css',
         'leaflet-gesture-handling.css')
    ]

def main():
    f_map = Map2(
        location = [35.658099, 139.741357],
        zoom_start = 12,
        gestureHandling = True)

    folium.Marker(
        [35.658099, 139.741357],
        popup="日本経緯度原点",
    ).add_to(f_map)

    f_map.save('map.html')
    webbrowser.open('map.html')

if __name__ == "__main__":
    main()
