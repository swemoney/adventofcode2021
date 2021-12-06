# Day 6 Part 2

def run(data):
    for day in range(256):
        end_of_day_fish = [0] * 9
        for age, num_fish in reversed(list(enumerate(data))):
            if age == 0:
                end_of_day_fish[6] += num_fish
                end_of_day_fish[8] += num_fish
                continue
            end_of_day_fish[age-1] = num_fish
        data = end_of_day_fish
    return sum(data)

def parse_input(data):
    fish = [int(age) for age in data[0].split(',')]
    return [fish.count(age) for age in range(9)] # Count how many of each fish age we have