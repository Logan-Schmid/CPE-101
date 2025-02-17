
def make_in_txt_file():
    with open('in.txt', 'w') as f:
        my_lines: list[str] = ['I am a file.\n',
                            'This is a line.\n',
                            'This is the last line.\n']
        f.writelines(my_lines)


def output_lines_with_details(file_name: str) -> None:
    with open(file_name, 'r') as f:
        for line_index, line in enumerate(f.readlines()):
            print(f'Line {line_index} ({len(line) - 1} chars): {line}')

if __name__ == '__main__':
    make_in_txt_file()
    output_lines_with_details('in.txt')