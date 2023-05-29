import re

def parse_number_with_k_suffix(number_str):
    match = re.match(r'^(\d+\.?\d*)([KMB])$', number_str, re.IGNORECASE)
    if match:
        number = float(match.group(1))
        suffix = match.group(2).upper()
        if suffix == 'K':
            return int(number * 1000)
        elif suffix == 'M':
            return int(number * 1000000)
        elif suffix == 'B':
            return int(number * 1000000000)
    else:
        return int(number_str)
