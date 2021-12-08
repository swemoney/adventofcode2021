# Day 8 Part 2

def run(data):
    output_sum = 0
    for entry in data:

        digits = {}
        sixes = []
        fives = []

        for digit in entry["digits"]:
            
            l = len(digit)
            if l == 2:
                digits[1] = digit
            elif l == 3:
                digits[7] = digit
            elif l == 4:
                digits[4] = digit
            elif l == 7:
                digits[8] = digit
            elif l == 5:
                fives.append(digit)
            elif l == 6:
                sixes.append(digit)

        # Fives
        for digit in fives:
            if set(digits[7]).issubset(set(digit)): # 3: 7 is subset
                digits[3] = digit
            elif matching(digit, digits[4]) == 2:   # 2: Shares 2 segments with 4
                digits[2] = digit
            else: # 5
                digits[5] = digit

        # Sixes
        for digit in sixes:
            if set(digits[4]).issubset(set(digit)): # 9: 4 is subset
                digits[9] = digit
            elif matching(digit, digits[1]) == 1:   # 6: Shares 1 segment with 1
                digits[6] = digit
            else: # 0
                digits[0] = digit
            
        output = ""
        for out_digit in entry["output"]:
            for num, code in digits.items():
                if sorted(out_digit) == sorted(code):
                    output += str(num)
                    break
        output_sum += int(output)

    return output_sum

def matching(a, b):
    matches = 0
    for x in sorted(b):
        if x in sorted(a):
            matches += 1
    return matches

def parse_input(data):
    return [{
        "digits": ["".join(sorted(digit)) for digit in part[0].split()], 
        "output": ["".join(sorted(digit)) for digit in part[1].split()]
    } for part in [entry.split(" | ") for entry in data]]
