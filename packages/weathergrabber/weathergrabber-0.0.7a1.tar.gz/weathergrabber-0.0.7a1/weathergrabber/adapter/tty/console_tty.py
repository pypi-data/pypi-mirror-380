from weathergrabber.usecase.use_case import UseCase
from weathergrabber.domain.adapter.params import Params
from weathergrabber.domain.adapter.icon_enum import IconEnum
from weathergrabber.domain.weather_icon_enum import WeatherIconEnum
from weathergrabber.weathergrabber_application import WeatherGrabberApplication
import logging

class ConsoleTTY:

    def __init__(self, use_case: UseCase):
        self.logger = logging.getLogger(__name__)
        self.use_case = use_case
        pass

    def execute(self, params: Params) -> None:
        self.logger.info("Executing Console output")

        is_fa = params.icons == IconEnum.FA

        forecast = self.use_case.execute(params)

        rain_icon = WeatherIconEnum.RAIN.fa_icon if is_fa else WeatherIconEnum.RAIN.emoji_icon

        city = forecast.current_conditions.location.city
        state_province = forecast.current_conditions.location.state_province
        icon = forecast.current_conditions.icon.fa_icon if is_fa else forecast.current_conditions.icon.emoji_icon
        temperature = forecast.current_conditions.temperature
        
        day_temp_label = WeatherIconEnum.DAY.fa_icon if is_fa else WeatherIconEnum.DAY.emoji_icon
        day_temp_value = forecast.current_conditions.day_night.day.value
        night_temp_label = WeatherIconEnum.NIGHT.fa_icon if is_fa else WeatherIconEnum.NIGHT.emoji_icon
        night_temp_value = forecast.current_conditions.day_night.night.value
        
        moon_icon = forecast.today_details.moon_phase.icon.fa_icon if is_fa else forecast.today_details.moon_phase.icon.emoji_icon
        moon_phase = forecast.today_details.moon_phase.phase
        summary = forecast.current_conditions.summary

        feelslike_icon = WeatherIconEnum.FEEL.fa_icon if is_fa else WeatherIconEnum.FEEL.emoji_icon
        feelslike = forecast.today_details.feelslike.value

        sunrise_icon = forecast.today_details.sunrise_sunset.sunrise.icon.fa_icon if is_fa else forecast.today_details.sunrise_sunset.sunrise.icon.emoji_icon
        sunset_icon = forecast.today_details.sunrise_sunset.sunset.icon.fa_icon if is_fa else forecast.today_details.sunrise_sunset.sunset.icon.emoji_icon

        sunrise_value = forecast.today_details.sunrise_sunset.sunrise.value
        sunset_value = forecast.today_details.sunrise_sunset.sunset.value

        wind_icon = WeatherIconEnum.WIND.fa_icon if is_fa else WeatherIconEnum.WIND.emoji_icon
        wind = forecast.today_details.wind.value

        humidity_icon = WeatherIconEnum.HUMIDITY.fa_icon if is_fa else WeatherIconEnum.HUMIDITY.emoji_icon
        humidity = forecast.today_details.humidity.value

        pressure = forecast.today_details.pressure

        uv_index = forecast.today_details.uv_index

        visibility_icon = WeatherIconEnum.VISIBILITY.fa_icon if is_fa else WeatherIconEnum.VISIBILITY.emoji_icon
        visibility = forecast.today_details.visibility.value

        r, g, b = forecast.air_quality_index.color.red, forecast.air_quality_index.color.green, forecast.air_quality_index.color.blue
        aqi_category = f"\033[38;2;{r};{g};{b}m{forecast.air_quality_index.category}\033[0m"
        aqi_acronym = forecast.air_quality_index.acronym
        aqi_value = forecast.air_quality_index.value

        hourly_predictions = [
            f"{h.title}\t{h.temperature}\t{h.icon.fa_icon if is_fa else h.icon.emoji_icon}\t{rain_icon  if h.precipitation.percentage else ''}  {h.precipitation.percentage}"
            for h in forecast.hourly_predictions
        ]
        daily_predictions = [
            f"{d.title}\t{d.high_low}\t{d.icon.fa_icon if is_fa else d.icon.emoji_icon}\t{rain_icon}  {d.precipitation.percentage}"
            for d in forecast.daily_predictions
        ]

        print_value = (
            "\n"
            f"{city}, {state_province}\n"
            "\n"
            f"{icon}       {temperature}\n"
            "\n"
            f"{summary}\n"
            f"{day_temp_label} {day_temp_value}/{night_temp_label} {night_temp_value}\t{feelslike_icon} {feelslike}\n"
            "\n"
            f"{sunrise_icon} {sunrise_value} • {sunset_icon} {sunset_value}\n"
            "\n"
            f"{moon_icon} {moon_phase}\n"
            "\n"
            f"{wind_icon} {wind}\t {uv_index}\n"
            f"{humidity_icon} {humidity}\t\t {pressure}\n"
            f"{visibility_icon} {visibility}\t {aqi_acronym} {aqi_category} {aqi_value}\n"
            "\n"
            f"{'\n'.join(hourly_predictions)}\n"
            "\n"
            f"{'\n'.join(daily_predictions)}\n"
            "\n"
            f"{forecast.current_conditions.timestamp}"
        )
        
        print(print_value)
        if(params.keep_open):
            lines_count = print_value.count("\n") + 1
            ret_prev_line = f"\033[{lines_count}A"              
            print(ret_prev_line, end='')  # Move cursor back to the beginning for overwriting, the application is responsable for executing again
