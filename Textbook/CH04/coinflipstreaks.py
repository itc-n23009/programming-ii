import random

def count_streaks(num_flips, streak_length):
    number_of_streaks = 0
    for experiment_number in range(num_flips):
        flips = [random.randint(0, 1) for _ in range(streak_length)]
        if all(flips[0] == flip for flip in flips):
            number_of_streaks += 1
    return number_of_streaks

def main():
    num_trials = 10000
    streak_length = 6
    number_of_streaks = count_streaks(num_trials, streak_length)
    probability = number_of_streaks / num_trials * 100
    print(f'同じ面が{streak_length}連続出現する確率: {probability}%')

if __name__ == "__main__":
    main()
