# Basic Weather App

A simple command-line weather app in Python that retrieves and displays current weather data for a user-specified city. This app uses the OpenWeatherMap API to provide information such as temperature, humidity, and weather conditions.

## Features

- Fetches real-time weather data for any city.
- Displays basic information:
  - City name
  - Temperature in Celsius
  - Humidity percentage
  - Weather description

## Requirements

- Python 3.x
- `requests` library (install it via `pip install requests`)

## Setup

1. **Get an API Key**:
   - Sign up on [OpenWeatherMap](https://openweathermap.org/) to obtain a free API key.
   
2. **Add API Key**:
   - Replace `"your_api_key_here"` in the code with your actual API key.

3. **Run the Script**:
   - Save the file and open a terminal.
   - Navigate to the project directory.
   - Run the script using the command:

    ```bash
    python weather_app.py
    ```

## How to Use

1. When prompted, enter the name of the city for which you want the weather data.
2. The application will display the following details:
   - City name
   - Temperature (in Celsius)
   - Humidity (percentage)
   - Weather description

## Example

```plaintext
Enter the name of the city: London
City: London
Temperature: 15°C
Humidity: 65%
Weather: Light rain
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.