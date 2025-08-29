import math

def pounds_to_kg(pounds: int or float) -> float:
    if pounds < 0:
        raise ValueError('Weight cannot be negative!')

    return pounds * 0.453592


def get_mass_object(object: str) -> float:
    match object:
        case 't':
            return 0.1
        case 'p':
            return 1.0
        case 'r':
            return 3.0
        case 'g':
            return 5.3
        case 'l':
            return 9.07
        case _:
            return 0.0


def get_velocity_object(distance: int or float) -> float:
    gravity: float = 9.8
    return math.sqrt(gravity * distance * 0.5)


def get_velocity_skater(mass_skater: int or float,
                        mass_object: int or float,
                        velocity_object: int or float) -> float:
    if mass_skater < 0 or mass_object < 0:
        raise ValueError('Masses cannot be negative!')

    try:
        velocity_skater: float = mass_object * velocity_object / mass_skater
        return velocity_skater
    except ZeroDivisionError as e:
        print(f'Error: Mass of skater cannot be zero! Error message is: {e}')
        return 0