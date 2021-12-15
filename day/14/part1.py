# Day 14 Part 1

from collections import Counter

def run(data):
    polymer, rules = data
    for step in range(10):
        polymer = process_step(polymer, rules)
    elements = elements_by_frequency(polymer)
    return elements[0][1] - elements[-1][1]

def elements_by_frequency(polymer):
    return Counter(list(polymer)).most_common()

def process_step(polymer, rules):
    resulting_polymer = list(polymer)
    for idx in range(len(polymer)-2, -1, -1):
        rule = rules.get(polymer[idx:idx+2])
        if rule != None:
            resulting_polymer.insert(idx+1, rule)
    return "".join(resulting_polymer)

def parse_input(data):
    template = data[0]
    rules = {}
    for rule in data[2:]:
        rule_elms, rule_replace = rule.split(" -> ")
        rules[rule_elms] = rule_replace
    return (template, rules)
