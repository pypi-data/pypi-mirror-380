from enum import Enum

class WeatherIconEnum(Enum):
    CLEAR = ('clear', chr(0xF0599), '☀️')
    CLEAR_NIGHT = ('clear-night', chr(0xF0594), '🌙')
    CLOUDY = ('cloudy', '\uf0c2', '☁️')
    CLOUDY_FOGGY_DAY = ('cloudy-foggy-day', '\u200B', '\u200B')
    CLOUDY_FOGGY_NIGHT = ('cloudy-foggy-night', '\u200B', '\u200B')
    DAY = ('day', '\uf185', '🌞')
    FEEL = ('feel', '\uf2c9', '🥵')
    HUMIDITY = ('humidity', '\uf043', '💧')
    MOSTLY_CLEAR_DAY = ('mostly-clear-day', chr(0xF0599), '☀️')
    MOSTLY_CLEAR_NIGHT = ('mostly-clear-night', chr(0xF0594), '🌙')
    MOSTLY_CLOUDY_DAY = ('mostly-cloudy-day', chr(0xf013), '☁️')
    MOSTLY_CLOUDY_NIGHT = ('mostly-cloudy-night', chr(0xf013), '☁️')
    NIGHT = ('night', '\uf186', '🌜')
    PARTLY_CLOUDY_DAY = ('partly-cloudy-day', chr(0xF0595), '⛅')
    PARTLY_CLOUDY_NIGHT = ('partly-cloudy-night', chr(0xF0F31), '☁️')
    RAIN = ('rain', '\uf0e9', '🌧️')
    RAINY_DAY = ('rainy-day', chr(0x1F326), '🌧️')
    RAINY_NIGHT = ('rainy-night', chr(0x1F326), '🌧️')
    SCATTERED_SHOWERS_DAY = ('scattered-showers-day', chr(0x1F326), '🌦️')
    SCATTERED_SHOWERS_NIGHT = ('scattered-showers-night', chr(0x1F326), '🌦️')
    SEVERE = ('severe', '\ue317', '🌩️')
    SHOWERS = ('showers', '\u26c6', '🌧️')
    SNOW = ('snow', '\uf2dc', '❄️')
    SNOWY_ICY_DAY = ('snowy-icy-day', '\uf2dc', '❄️')
    SNOWY_ICY_NIGHT = ('snowy-icy-night', '\uf2dc', '❄️')
    SUNNY = ('sunny', chr(0xF0599), '☀️')
    SUNRISE = ('sunrise', '\ue34c', '🌅')
    SUNSET = ('sunset', '\ue34d', '🌇')
    THUNDERSTORM = ('thunderstorm', '\uf0e7', '⛈️')
    VISIBILITY = ('visibility', '\uf06e', '👁️')
    WIND = ('wind', chr(0xf059d), '🌪️')

    def __init__(self, name: str, fa_icon: str, emoji_icon: str):
        self._name = name
        self._fa_icon = fa_icon
        self._emoji_icon = emoji_icon

    @property
    def name(self):
        return self._name
    
    @property
    def fa_icon(self):
        return self._fa_icon
    
    @property
    def emoji_icon(self):   
        return self._emoji_icon

    @staticmethod
    def from_name(name: str):
        for item in WeatherIconEnum:
            if item._name == name:
                return item
        return None