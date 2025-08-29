
def show_welcome() -> None:
    print("""-----------------------------------------------------------------
--------- Welcome to the moon lander simulation program ---------
-----------------------------------------------------------------\n""")

def get_altitude() -> int:
    while True:
        user_input = input('Enter the altitude that the lander starts at (between 1 and 1-9999) >>> ')
        try:
            altitude = int(user_input)
            if 1 <= altitude <= 9999:
                return altitude
            else:
                print('Error: Input must be between 1 and 9999!')
        except ValueError:
            print('Error: Input must be an integer!')

def get_fuel() -> int:
    while True:
        user_input: str = input("Input a positive integer value for the amount of starting fuel >>> ")
        try:
            fuel: int = int(user_input)
            if fuel > 0:
                return fuel
            else:
                print('Error: input must be greater than 0!')

        except ValueError:
            print('Error: must input an integer!')

def display_lm_state(elapsed_time: int,
                     altitude: float,
                     velocity: float,
                     fuel_amount: int,
                     fuel_rate: int) -> None:
    print(f"""The current state of the lunar module is:
    Elapsed Time: {elapsed_time} seconds
    Altitude: {altitude} meters
    Velocity: {velocity} m/s
    Fuel Remaining: {fuel_amount} Liters
    Rate of Fuel Consumption: {fuel_rate} L/s""")

def get_fuel_rate(current_fuel: int) -> int:
    while True:
        user_input: str = input("Input the fuel consumption rate of the lunar module (an integer between 0-9, inclusive) >>> ")
        try:
            fuel_rate: int = int(user_input)
            if 0 <= fuel_rate <= 9:
                return fuel_rate if fuel_rate < current_fuel else current_fuel
            else:
                print('Error: input must be between 0-9, inclusive!')
        except ValueError:
            print('Error: input must be an integer!')


def display_lm_landing_status(velocity: float) -> None:
    if -1 <= velocity <= 0:
        print('Status at landing - The eagle has landed!')
    elif -10 < velocity < -1:
        print('Status at landing - Enjoy your oxygen while it lasts!')
    elif velocity <= -10:
        print('Status at landing - Ouch - that hurt!')
    else:
        print(f'Error: Somehow the Velocity was positive?: Velocity: {velocity} m/s')


def update_acceleration(gravity: float, fuel_rate: int) -> float:
    try:
        return gravity * ( (fuel_rate / 5) - 1 )
    except TypeError as e:
        raise TypeError

def update_altitude(altitude: float, velocity: float, acceleration: float):
    updated_altitude: float = altitude + velocity + acceleration / 2
    if updated_altitude > 0:
        return updated_altitude
    else:
        return 0

def update_velocity(velocity: float, acceleration: float):
    return velocity + acceleration

def update_fuel(fuel: int, fuel_rate: int):
    new_fuel: int = fuel - fuel_rate
    if new_fuel <= 0:
        return 0
    else:
        return new_fuel

