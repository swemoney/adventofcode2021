# Day 16 Part 2

from dataclasses import dataclass
from math import prod

# Had to go back to the drawing board for a lot of this 
# But ended up simplifying a lot of part 1

@dataclass
class Packet:
    version: int
    type_id: int
    offset: int
    value: int
    len_id: int = None

def run(data):
    idx = 0
    pkts = []
    while idx < len(data) and '1' in data[idx:]:
        pkts, idx = parse_packet(data, idx, pkts)
    pkt_graph = packet_graph(pkts)
    return calculate(pkts, pkt_graph)

def packet_graph(pkts):
    stack = []
    graph = [[] for _ in range(len(pkts))] # Keep a graph of relevant indexes
    for idx, pkt in enumerate(pkts):
        if len(stack) > 0:
            pkt_idx = stack[-1]
            graph[pkt_idx].append(idx)
            pkts[pkt_idx].value -= 1
            if pkts[pkt_idx].value == 0:
                stack.pop()

        while len(stack) > 0:
            pkt_idx = stack[-1]
            if pkts[pkt_idx].len_id == 0 and pkts[pkt_idx].value <= pkt.offset - pkts[pkt_idx].offset:
                stack.pop()
            else:
                break

        if pkt.type_id != 4:
            stack.append(idx)

    return graph

def calculate(pkts, graph, idx=0):
    if pkts[idx].type_id == 4:
        return pkts[idx].value

    vals = []
    for pkt_idx in graph[idx]:
        vals.append(calculate(pkts, graph, pkt_idx))
    return get_real_value(vals, pkts[idx].type_id)

def get_real_value(pkts, type_id):
    if type_id == 0:
        val = sum(pkts)
    elif type_id == 1:
        val = prod(pkts)
    elif type_id == 2:
        val = min(pkts)
    elif type_id == 3:
        val = max(pkts)
    elif type_id == 5:
        val = 1 if pkts[0] > pkts[1] else 0
    elif type_id == 6:
        val = 1 if pkts[0] < pkts[1] else 0
    elif type_id == 7:
        val = 1 if pkts[0] == pkts[1] else 0
    return val

def parse_packet(data, idx, pkts):
    version, type_id, idx = parse_meta(data, idx)

    # Literal Packet (Type ID = 4)
    if type_id == 4:
        val, idx = parse_literal(data, idx)
        pkts.append( Packet(version=version, type_id=type_id, offset=idx, value=val) )

    # Operator Packet (Type ID != 4)
    else:
        len_type_id, len_val, idx = parse_operator(data, idx)
        pkts.append( Packet(version=version, type_id=type_id, offset=idx, value=len_val, len_id=len_type_id) )

    return pkts, idx

def parse_meta(data, idx):
    # Get Version (First 3 bits)
    version = int(data[idx:idx+3], 2)
    idx += 3

    # Get Type ID (Next 3 bits)
    type_id = int(data[idx:idx+3], 2)
    idx += 3

    return version, type_id, idx

def parse_literal(data, idx):
    num = ''
    while True:
        num += data[idx+1:idx+5]
        idx += 5
        if data[idx-5] == '0':
            break
    return int(num, 2), idx

def parse_operator(data, idx):
    len_type_id = int(data[idx])
    idx += 1

    if len_type_id == 0:
        len_val = int(data[idx:idx+15], 2)
        idx += 15
    else:
        len_val = int(data[idx:idx+11], 2)
        idx += 11

    return len_type_id, len_val, idx

def parse_input(data):
    return bin(int(data[0], 16))[2:].zfill(len(data[0])*4)

