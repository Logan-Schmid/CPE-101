import sys

def wrong_usage_exit():
    print('usage: parse_file.py [-s] file_name')
    sys.exit()

def parse_file(file: str, flag_s: bool=False) -> dict:
    type_counts: dict = {'int': 0,
                           'float': 0,
                           'other': 0}
    if flag_s:
        type_counts['sum'] = 0

    with open(file, 'r') as f:
        print(f'{file} was opened!')
        for line in f.readlines():
            terms: list = line.split()
            for term in terms:
                current_type: str = return_type(term)
                type_counts[current_type] += 1
                # print(f'{term} is: {return_type(term)}')
                if flag_s and current_type != 'other':
                    type_counts['sum'] += float(term)

    return type_counts

def return_type(term: str) -> str:
    """
    Returns 'int', 'float', or 'other'
    """
    if len(term) == 0:
        raise Warning('An empty string was counted as a term, something is off')
    if term[0] == '-':
        term = term[1:]

    if term.isnumeric():
        return 'int'
    elif term.replace('.', '').isnumeric():
        return 'float'
    else:
        return 'other'


if __name__ == '__main__':
    arguments: list[str] = sys.argv[1:]  # ignore this script's name
    file_to_parse: str = ''
    flags: list[str] = []

    if len(arguments) == 0 or len(arguments) > 2:
        wrong_usage_exit()

    arguments_without_flag_ctr: int = 0
    for argument in arguments:
        if argument[0] == '-':
            flags.append(argument)
        else:
            arguments_without_flag_ctr += 1
            if arguments_without_flag_ctr > 1:
                wrong_usage_exit()
            file_to_parse = argument
    else:
        if file_to_parse == '':
            wrong_usage_exit()

    [wrong_usage_exit() for flag in flags if flag != '-s']

    try:
        file_type_counts: dict = parse_file(file_to_parse, flag_s=('-s' in flags))
    except FileNotFoundError:
        print(f'Unable to open {file_to_parse}')
        sys.exit()

    for key, value in list(file_type_counts.items()):
        print(f'{key.title()}s: {value if type(value) == int else round(value, 2)}')


