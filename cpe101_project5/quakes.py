from quake_funcs import *
import sys

def main():
    if len(sys.argv) != 2:
        raise ValueError("""Must run quakes.py in terminal with the following format:
python3 quakes.py **quakes_file_name**""")
    file_name: str = sys.argv[1]
    try:
        with open(file_name) as file:
            result_quakes: list[Earthquake] = read_quakes_from_file(file)
    except FileNotFoundError or FileExistsError as e:
        print('Make sure the file input exists and contains correctly formatted earthquake data')
        raise e

    output_quakes(result_quakes)
    while True:
        user_choice: str = get_user_input()
        act_on_user_input(user_choice, result_quakes, file_name)

if __name__ == '__main__':
    main()

    # file_name: str = 'quakes1.txt'
    # with open(file_name) as file:
    #     result_quakes: list[Earthquake] = read_quakes_from_file(file)
    #
    # output_quakes(result_quakes)
    # act_on_user_input('n', result_quakes, file_name)