import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        print("Error: Could not retrieve data. Please check the city name or try again later.")
        return None

def main():
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    city = input("Enter the name of the city: ")

    weather = get_weather(city, api_key)
    
    if weather:
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Weather: {weather['description'].capitalize()}")

if __name__ == "__main__":
    main()
