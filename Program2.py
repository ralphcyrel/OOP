def print_color(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    end_color = '\033[0m'
    print_color = f"{colors[color]}{'*' * len(text)}\n{text}\n{'*' * len(text)}{end_color}"
    print(print_color)

def main ():
    name = input("Enter your name: ")
    dream_job = input("Enter your dream job: ")

    print_color(f"Hello, my name is {name}", 'cyan')
    print_color(f"My dream job is {dream_job}", 'purple')

if __name__ == '__main__':
    main()
