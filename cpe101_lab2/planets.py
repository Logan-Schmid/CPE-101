
def weight_on_plants():
    user_weight_earth: int
    ask_weight: bool = True
    while ask_weight:
        user_weight_earth_str: str = input('What do you weigh on Earth? >>> ')
        try:
            user_weight_earth = int(user_weight_earth_str)
            ask_weight = False
        except ValueError as e:
            print(f'{e} -- Please input a integer as your weight!\n')

    user_weight_mars: float = 0.38 * user_weight_earth
    user_weight_jupiter: float = 2.53 * user_weight_earth

    print(f'\nOn Mars you would weigh {round(user_weight_mars, 2)} pounds.\n'
          f'On Jupiter you would weigh {round(user_weight_jupiter, 2)} pounds.')


def main():
    weight_on_plants()



if __name__ == '__main__':
    main()