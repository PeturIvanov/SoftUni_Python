def forecast(*args):
    unsorted_dict = {}

    for data in args:
        location, weather = data

        unsorted_dict[location] = weather

    sorted_dict = sorted(unsorted_dict.items(), key=lambda x: (x[1] != "Sunny", x[1] != "Cloudy", x[0]))

    return '\n'.join([f"{city_data[0]} - {city_data[1]}" for city_data in sorted_dict])


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))