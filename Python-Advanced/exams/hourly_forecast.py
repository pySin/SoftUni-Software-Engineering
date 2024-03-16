# Hourly Forecast


def forecast(*args):
    weather_priority = ["Sunny", "Cloudy", "Rainy"]
    destinations = sorted(args, key=lambda x: (weather_priority.index(x[1]), x))
    destinations_priority_display = [f"{pair[0]} - {pair[1]}" for pair in destinations]
    return "\n".join(destinations_priority_display)


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
