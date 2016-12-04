import re
from operator import itemgetter

sectorsum = 0
for l in input_lines():
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
