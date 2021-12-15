# Day 14 Part 2

from collections import defaultdict

def run(data):
    polymer, elements, rules = data
    for step in range(40):
        process_step(polymer, elements, rules)
    sorted_elements = sorted(elements.values())
    return sorted_elements[-1] - sorted_elements[0]

def process_step(polymer, elements, rules):
    old_polymer = polymer.copy()
    for rule in rules:
        if old_polymer[rule] > 0:
            num = old_polymer[rule]
            polymer[rule] -= num
            polymer[rule[0]+rules[rule]] += num
            polymer[rules[rule]+rule[1]] += num
            elements[rules[rule]] += num

def parse_input(data):
    template = defaultdict(int)
    elements = defaultdict(int)
    rules = {}
    for rule in data[2:]:
        rule_elms, rule_replace = rule.split(" -> ")
        rules[rule_elms] = rule_replace
        template[rule_elms] = data[0].count(rule_elms)
    for element in data[0]:
        elements[element] += 1
    return (template, elements, rules)
