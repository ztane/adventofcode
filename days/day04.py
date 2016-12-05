from helpers import *

d = get_aoc_data(day=4)

ascii_l = ascii_lowercase
cribs = [str.maketrans(ascii_l, ascii_l[i:] + ascii_l[:i]) for i in range(26)]


def decrypt(name, sector):
    crib_no = sector % 26
    return name.translate(cribs[crib_no])


def part1():
    sectorsum = 0
    for l in d.lines():
        l = l.replace('-', '').strip()
        m = re.match(r'([a-z]+)(\d+)\[([a-z]+)\]', l)
        id = m.group(1)
        sector = int(m.group(2))
        checksum = m.group(3)

        counts = Counter(id)
        chksum = ''.join(i[0] for i in sorted(counts.items(), key=lambda x: (-x[1], x[0])))[:5]
        if chksum == checksum:
            sectorsum += sector

    print(sectorsum)


def part2():
    for l in d.lines():
        m = re.match(r'([a-z-]+)(\d+)\[([a-z]+)\]', l)
        room_id = m.group(1)
        sector = int(m.group(2))
        checksum = m.group(3)

        counts = Counter(room_id.replace('-', '')).items()
        chksum = ''.join(i[0] for i in sorted(counts, key=lambda x: (-x[1], x[0])))[:5]
        if chksum == checksum:
            room_id = decrypt(room_id.replace('-', ' ').strip(), sector)
            if 'north' in room_id and 'pole' in room_id  and 'object' in room_id:
                print(room_id, 'is room number', sector)
                return