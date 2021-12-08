# -*- coding: utf-8 -*-

from branca.element import MacroElement
from jinja2 import Template

from folium.elements import JSCSSMixin
from folium.utilities import parse_options

class MapCenterGeo(JSCSSMixin, MacroElement):

    _template = Template("""
        {% macro script(this, kwargs) %}
            $.ajaxSetup({async: false});
            var url = 'https://gbank.gsj.jp/seamless/v2/api/1.0/legend.json?point=';
            var geoFormatter = function (lat, lng) { 
                var geoinfo = '';
                var req = url +
                          {{ this._parent.get_name() }}.getCenter().lat + ',' + 
                          {{ this._parent.get_name() }}.getCenter().lng;

                $.getJSON(req, function(data) {
                    if(0 != Object.keys(data).length) {
                        geoinfo = data.group_ja + ' : ' + data.lithology_ja ;
                    }
                })
                return geoinfo;
            };
            var options = {{ this.options|tojson }};
            options.latLngFormatter = geoFormatter;
            L.control.mapCenterCoord(
                options
            ).addTo({{ this._parent.get_name() }});
        {% endmacro %}
    """)

    default_js = [
        ('MapCenterCoord_js',
         'L.Control.MapCenterCoord.js')
    ]
    default_css = [
        ('MapCenterCoord_css',
         'L.Control.MapCenterCoord.css')
    ]

    def __init__(
        self,
        position = 'bottomleft',
        icon = True,
        onMove = False,
        template = '{y} | {x}',
        projected = False,
        formatProjected = '#.##0,000',
        latlngFormat = 'DD',
        latlngDesignators = False,
        latLngFormatter = None
    ):
        super().__init__()
        self._name = 'MapCenterGeo'
        self.options = parse_options(
            position = position,
            icon = icon,
            onMove = onMove,
            template = template,
            projected = projected,
            formatProjected = formatProjected,
            latlngFormat = latlngFormat,
            latlngDesignators = latlngDesignators,
            latLngFormatter = latLngFormatter
        )
