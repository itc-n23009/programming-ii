def collatz(number):
    return number // 2 if number % 2 == 0 else 3 * number + 1

def print_collatz_sequence(starting_number):
    while starting_number != 1:
        print(starting_number)
        starting_number = collatz(starting_number)
    print(1)

def main():
    starting_number = int(input("整数を入力してください: "))
    if starting_number <= 0:
        print("正の整数を入力してください。")
    else:
        print_collatz_sequence(starting_number)

if __name__ == "__main__":
    main()
