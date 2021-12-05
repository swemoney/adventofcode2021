# Day 4 Part 2

NUM_ROWS = 5

def run(data):
    drawn, cards = data
    for i, num in enumerate(drawn):
        cards = list(filter(lambda c: find_winning_line(c) == None, cards))
        for card in cards:
            card = mark_card(card, num)
        if len(cards) == 0:
            return int(drawn[i-1]) * sum(unmarked_squares(card))
    return

def unmarked_squares(card):
    return list(map(lambda n: int(n["num"]), filter(lambda s: s["mark"] == False, card)))

def find_winning_line(card):
    winning_row = check_rows_for_winner(card)
    if not winning_row == None:
        return winning_row
    winning_col = check_cols_for_winner(card)
    if not winning_col == None:
        return winning_col
    return None

def check_rows_for_winner(card):
    i = 0
    while i < len(card):
        row = card[i:i+NUM_ROWS]
        if is_winning_line(row):
            return row
        i += NUM_ROWS
    return None

def check_cols_for_winner(card):
    i = 0
    while i < NUM_ROWS:
        col = card[i::NUM_ROWS]
        if is_winning_line(col):
            return col
        i += 1
    return None

def is_winning_line(line):
    unmarked = list(filter(lambda x: x["mark"] == False, line))
    return not len(unmarked) > 0

def mark_card(card, num):
    mark = next((square for square in card if square["num"] == num), None)
    if not mark == None:
        mark["mark"] = True
    return card

def parse_input(data):
    drawn_numbers = data[0].split(",")
    bingo_cards, card = [], []
    idx = 1
    while idx < len(data) - 1:
        idx += 1
        if data[idx] == '':
            bingo_cards.append(card.copy())
            card = []
            continue
        card.extend([{"num":n, "mark":False} for n in data[idx].split()])
    bingo_cards.append(card)
    return (drawn_numbers, bingo_cards)
