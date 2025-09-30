# weatherbuddy

A simple Python package to fetch and process weather data from the OpenWeatherMap API.

## Features
- Get weather forecast for any city or coordinates
- Returns time, temperature (Celsius), and weather description for the next 12 hours
- Easy to use and extend

## Installation
```sh
pip install weatherbuddy
```

## Usage
```python
from weatherbuddy import Weather
import pprint

api_key = "YOUR_API_KEY"
city = "London"
weather = Weather(api_key, city=city)
print(f"Weather forecast for {city} for the next 12 hours:")
pprint.pprint(weather.next_12_hours_simplified())
```

## Example Output
```
Weather forecast for London for the next 12 hours:
[('2023-10-01 12:00:00', 15, 'light rain'),
 ('2023-10-01 15:00:00', 16, 'moderate rain'),
 ('2023-10-01 18:00:00', 14, 'clear sky'),
 ('2023-10-01 21:00:00', 13, 'light rain')]
```

## Requirements
- Python 3.7+
- requests
- python-dotenv

## API Key
Get your free API key from [OpenWeatherMap](https://openweathermap.org/api).

## License
MIT
