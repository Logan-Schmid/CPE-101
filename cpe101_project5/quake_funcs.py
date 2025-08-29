from datetime import datetime
import sys
import requests
from requests import Response
import json


class Earthquake:
    def __init__(self,  place: str, mag: float, longitude: float, latitude: float, time: int):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"{self.mag} {self.longitude} {self.latitude} {self.time} {self.place}"

def read_quakes_from_file(file) -> list[Earthquake]:
    """
    Takes in an already opened file and returns a list of Earthquakes
    """
    if not file:
        raise FileExistsError(f"File {file} does not exist!")

    quake_list: list[Earthquake] = []

    for line in file:
        contents: list[str] = line.split(' ')
        if len(contents) < 5:
            raise ValueError(f"""The file imported, {file}, was not formatted correctly!
Please format each earthquake as its own line in the following format:
Magnitude longitude latitude time(in seconds since the Unix Epoch) place""")
        contents = [content.strip() for content in contents]

        try:
            mag: float = float(contents[0])
            longitude: float = float(contents[1])
            latitude: float = float(contents[2])
            time: int = int(contents[3])
        except ValueError:
            raise ValueError(f"Imported file {file} contains incorrectly formatted data!")
        place: str = ' '.join(contents[4:])

        quake_list.append(Earthquake(place, mag, longitude, latitude, time))

    return quake_list

def output_quakes(quake_list: list[Earthquake]) -> None:
    print("\nEarthquakes:\n------------")
    for quake in quake_list:
        date: datetime = datetime.fromtimestamp(quake.time)
        place_str: str = " " * (40 - len(quake.place)) + quake.place
        print(f"({quake.mag:.2f}){place_str} at {date} ({quake.longitude:.3f}, {quake.latitude:.3f})")

def get_user_input() -> str:
    valid_options: list[str] = ['s', 'f', 'n', 'q']
    while True:
        user_input: str = input("\nOptions:\n  (s)ort\n  (f)ilter\n  (n)ew quakes\n  (q)uit\n\nChoice: ")
        if user_input.lower() in valid_options:
            return user_input
        else:
            print('Input was not one of the valid options! Please re-enter your choice.')

def act_on_user_input(user_input: str, quakes: list[Earthquake], file_name: str) -> None:
    match user_input.lower():
        case 's':
            sorted_quakes: list[Earthquake] = sort_quakes(quakes)
            output_quakes(sorted_quakes)

        case 'f':
            filtered_quakes: list[Earthquake] = filter_quakes(quakes)
            output_quakes(filtered_quakes)

        case 'n':
            potentially_new_quakes: list[Earthquake] = read_new_quakes()
            new_quake_found: bool = False
            for potentially_new_quake in potentially_new_quakes:
                if potentially_new_quake not in quakes:
                    quakes.append(potentially_new_quake)
                    new_quake_found = True

            if new_quake_found:
                print("\nNew quakes found!!!")
            output_quakes(quakes)

        case 'q':
            with open(file_name, 'w') as file:
                lines: list[str] = []
                for quake in quakes:
                    lines.append(str(quake) + '\n')
                file.writelines(lines)
            print(f"Earthquake data was rewritten in {file_name}")
            sys.exit()

def read_new_quakes() -> list[Earthquake]:
    url: str = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson'
    response: Response = requests.get(url)

    decoded_str: str = response.content.decode(response.encoding)
    data_dict: dict = json.loads(decoded_str)
    features: list = data_dict["features"]

    new_quakes: list[Earthquake] = []
    for feature in features:
        new_place = feature["properties"]["place"]
        new_mag = feature["properties"]["mag"]
        new_long = feature["geometry"]["coordinates"][0]
        new_lat = feature["geometry"]["coordinates"][1]
        new_time = int(round(feature["properties"]["time"] / 1000, 0))
        new_quake: Earthquake = Earthquake(new_place, new_mag, new_long, new_lat, new_time)
        new_quakes.append(new_quake)

    return new_quakes

def sort_quakes(quakes: list[Earthquake]) -> list[Earthquake]:
    sort_choice: str = ''
    while True:
        sort_choice = input("Sort by (m)agnitude, (t)ime, (l)ongtiude, or l(a)titude? ")
        if sort_choice.lower() in ['m', 't', 'l', 'a']:
            break
        else:
            print('Invalid sort choice!\n')

    match sort_choice.lower():
        case 'm':
            sorted_quakes: list[Earthquake] = sort_quakes_helper(quakes, 'mag')
            return sorted_quakes[::-1]
        case 't':
            sorted_quakes: list[Earthquake] = sort_quakes_helper(quakes, 'time')
            return sorted_quakes[::-1]
        case 'l':
            sorted_quakes: list[Earthquake] = sort_quakes_helper(quakes, 'longitude')
            return sorted_quakes
        case 'a':
            sorted_quakes: list[Earthquake] = sort_quakes_helper(quakes, 'latitude')
            return sorted_quakes
        case _:
            raise LookupError('Somehow there was an error in the sorting method')

def sort_quakes_helper(quakes: list[Earthquake], attribute: str) -> list[Earthquake]:
    # sort by first making a dict with the keys as mag, index in unsorted list as value
    # then put keys into a list

    attr_dict: dict = {}
    for i, quake in enumerate(quakes):
        quake_attr_key: str = str(quake.__dict__[attribute])
        attr_dict[quake_attr_key] = i

    attr_list: list[type(attribute)] = [cast_to_type_of_variable(key, quakes[0].__dict__[attribute]) for key in attr_dict.keys()]
    attr_list.sort()
    sorted_quakes: list[Earthquake] = []
    for key in attr_list:
        quake_to_append: Earthquake = quakes[attr_dict[str(key)]]
        sorted_quakes.append(quake_to_append)

    return sorted_quakes

def cast_to_type_of_variable(object_to_cast, variable):
    return type(variable)(object_to_cast)

def filter_quakes(quakes: list[Earthquake]) -> list[Earthquake]:
    filter_choice: str = ''
    while True:
        filter_choice = input('Filter by (m)agnitude or (p)lace? ')
        if filter_choice.lower() in ['m', 'p']:
            break
    if filter_choice.lower() == 'm':
        low_mag: float = 0
        high_mag: float = 0
        while True:
            try:
                low_mag = float(input("Lower bound: "))
                high_mag = float(input("Upper bound: "))
            except ValueError:
                print('Bounds must be numeric!')
            if low_mag <= high_mag:
                break
            else:
                print('Lower bound must be below Upper bound!')
        filtered_quakes: list[Earthquake] = filter_by_mag(quakes, low_mag, high_mag)
    else:  # user_choice == 'p'
        search_term: str = input("Search for what string? ")
        filtered_quakes: list[Earthquake] = filter_by_place(quakes, search_term)
    return filtered_quakes

def filter_by_mag(quakes: list[Earthquake], low: float, high: float) -> list[Earthquake]:
    return list(filter(lambda quake: low <= quake.mag <= high, quakes))

def filter_by_place(quakes: list[Earthquake], word: str) -> list[Earthquake]:
    return list(filter(lambda quake: word.lower() in quake.place.lower(), quakes))