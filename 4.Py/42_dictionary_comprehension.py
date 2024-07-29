cities_temp_F = {
    "New York": 32,
    "Boston": 75,
    "Los Angeles": 100,
    "Chicago": 50,
}

cities_temp_C = {
    key: round(((value - 32) * 5 / 9), 2) for (key, value) in cities_temp_F.items()
}
print(cities_temp_C)

weather = {
    "New York": "Snow",
    "Boston": "Sunny",
    "Los Angeles": "Sunny",
    "Chicago": "Cloudy",
}

sunny_weather = {key: value for key, value in weather.items() if value == "Sunny"}
print(sunny_weather)

cities_temp_description = {
    key: ("WARM" if value >= 50 else "COLD") for key, value in cities_temp_F.items()
}
print(cities_temp_description)

def check_temp(temp):
    if temp >= 70:
        return "HOT"
    elif 69 >= temp >= 40:
        return "WARM"
    else:
        return "COLD"

cities_temp_fun = {
       key: (check_temp(value)) for key, value in cities_temp_F.items()
}
print(cities_temp_fun)