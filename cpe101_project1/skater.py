# Project 1
#
# Name: Logan Schmid
# Instructor: Brian Jones
# Section: N/A

from funcs import pounds_to_kg, get_mass_object, get_velocity_object, get_velocity_skater


def main():
    weight_lbs: float = float(input('How much do you weigh (pounds)? '))
    distance: float = float(input('How far away is your professor (meters)? '))
    object_thrown: str = input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ')

    weight_kg: float = pounds_to_kg(weight_lbs)
    object_mass: float = get_mass_object(object_thrown)

    if object_mass <= 0.1:
        message_1: str = 'You\'re going to get an F!'
    elif 0.1 < object_mass <= 1.0:
        message_1: str = 'Make sure your professor is OK.'
    else:
        if distance < 20:
            message_1: str = 'How far away is the hospital?'
        else:
            message_1: str = 'RIP professor.'

    print(f'\nNice throw! {message_1}')

    vel_object: float = get_velocity_object(distance)
    vel_skater: float = get_velocity_skater(weight_kg, object_mass, vel_object)

    if vel_skater < 0.2:
        message_2: str = 'My grandmother skates faster than you!'
    elif 0.2 <= vel_skater < 1.0:
        message_2: str = ''
    else:
        message_2: str = 'Look out for that railing!!!'


    print(f'Velocity of skater: {round(vel_skater, 3)} m/s')
    if message_2:
        print(message_2)

if __name__ == '__main__':
    main()