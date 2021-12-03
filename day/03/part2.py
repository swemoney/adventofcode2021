# Day 3 Part 2

def run(data):
    o2_rating = get_rating(data.copy())
    co2_rating = get_rating(data.copy(), True)
    return int(o2_rating, 2) * int(co2_rating, 2)

def get_rating(data, co2=False):
    idx = 0
    while idx < len(data[0]):
        bit = get_prominent_bit_at_index(data, idx)
        if co2 == True:
            bit = "1" if bit == "0" else "0"
        data = list(filter(lambda b: b[idx] == bit, data))
        if len(data) == 1: break
        idx += 1
    return data[0]

def get_prominent_bit_at_index(data, idx):
    one_bits = len(list(filter(lambda b: b[idx] == "1", data)))
    return "1" if one_bits >= len(data)/2 else "0"

def parse_input(data):
    return data