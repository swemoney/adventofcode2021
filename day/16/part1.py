# Day 16 Part 1

def run(data):
    idx = 0
    while idx < len(data) and '1' in data[idx:]:
        versions, idx = parse_packet(data, idx)
    return sum(versions)

def parse_packet(data, idx, versions=[]):
    version, type_id, idx = parse_meta(data, idx)
    versions.append(version)

    # Literal Packet (Type ID = 4)
    if type_id == 4:
        num, idx = parse_literal(data, idx)

    # Operator Packet (Type ID != 4)
    else:
        versions, idx = parse_operator(data, idx, versions)

    return versions, idx

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
    last_group = False
    while last_group == False:
        num += data[idx+1:idx+5]
        if data[idx] == '0':
            last_group = True
        idx += 5
    return int(num, 2), idx

def parse_operator(data, idx, versions=[]):
    len_type_id = data[idx]
    idx += 1

    if len_type_id == '0':
        sub_bits_end = int(data[idx:idx+15], 2) + 15
        idx += 15
        while idx < sub_bits_end:
            versions, idx = parse_packet(data, idx, versions)

    else:
        num_pkts = int(data[idx:idx+11], 2)
        idx += 11
        for _ in range(num_pkts):
            versions, idx = parse_packet(data, idx, versions)

    return versions, idx

def parse_input(data):
    return bin(int(data[0], 16))[2:].zfill(len(data[0])*4)
