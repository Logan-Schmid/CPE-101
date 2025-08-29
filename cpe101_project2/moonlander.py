from lander_funcs import *
import time
import keyboard

class Moonlander():
    def __init__(self, altitude, fuel, fuel_rate):
        self.elapsed_time: int = 0
        self.velocity: float = 0
        self.acceleration: float = -1.62
        self.altitude: float = altitude
        self.fuel: int = fuel
        self.fuel_rate: int = fuel_rate

    def display_state(self) -> None:
        display_lm_state(self.elapsed_time, self.altitude, self.velocity, self.fuel, self.fuel_rate)
        # print(f'    Acceleration: {self.acceleration} m/s2')
        print('\n')

    def update_altitude(self) -> None:
        self.altitude = update_altitude(self.altitude, self.velocity, self.acceleration)

    def update_velocity(self) -> None:
        self.velocity = update_velocity(self.velocity, self.acceleration)

    def update_acceleration(self) -> None:
        self.acceleration = update_acceleration(1.62, self.fuel_rate)

    def update_fuel(self) -> None:
        self.fuel = update_fuel(self.fuel, self.fuel_rate)
        if self.fuel_rate >= self.fuel:
            self.fuel_rate = self.fuel


if __name__ == '__main__':
    show_welcome()

    initial_altitude = get_altitude()
    initial_fuel = get_fuel()
    initial_fuel_rate = get_fuel_rate(initial_fuel)
    moonlander: Moonlander = Moonlander(initial_altitude, initial_fuel, initial_fuel_rate)

    print('\nPress ctrl+c at any point to half the simulation and adjust the fuel consumption rate\n')
    time.sleep(1)
    print('\n--------------- Lunar Module Starting State ---------------')

    while moonlander.altitude > 0:
        try:
            if moonlander.elapsed_time % 1 == 0:
                moonlander.display_state()
                time.sleep(0.25)

            moonlander.elapsed_time += 1
            moonlander.update_altitude()
            moonlander.update_fuel()
            moonlander.update_acceleration()
            moonlander.update_velocity()
        except KeyboardInterrupt:
            moonlander.fuel_rate = get_fuel_rate(moonlander.fuel)

    print('\n--------------- Lunar Module has Landed ---------------\n')
    display_lm_landing_status(moonlander.velocity)
    print('\n')
    time.sleep(1)
    moonlander.display_state()

print('\n--------------- Lunar Module Landing Simulation End ---------------')
