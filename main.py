import re
import os
import traceback
import time

ids = {
    # f2nd id: ft id
    '5': '1',
    '6': '2',
    '7': '3',
    '8': '38',
    '9': '10',
    '11': '5',
    '13': '11',
    '12': '13',
    '14': '8',
    '15': '9',
    '16': '10',
    '17': '11',
    '4': '16',
    '22': '16'
}


def replacement(match, d, group):
    for key in d:
        if re.match(key, match.group(group)):
            return str(d[key])
    return str(match.group(group))


def mg(match, d, group):
    group1 = match.group(1)
    group2 = match.group(2)
    group4 = match.group(4)
    group5 = match.group(5)
    replmouthid = replacement(match, d, group)
    strm = f'MOUTH_ANIM({group1}, {group2}, {replmouthid}, {group4}, {group5})'
    return strm


def main():
    try:
        with open('f2nd.txt', 'r') as inp:
            string = inp.read()
            pattern1 = re.compile(r"MOUTH_ANIM\W(\d+)\, (\d+)\, (?P<mouthid>\d+)\, (\d+)\, (\d+)\W")
            output = pattern1.sub(lambda x: mg(x, ids, 'mouthid'), string)
            if os.path.isfile('ft.txt'):
                os.remove('ft.txt')
                with open('ft.txt', 'w') as outfile:
                    outfile.write(output)
            else:
                with open('ft.txt', 'w') as outfile:
                    outfile.write(output)

    except FileNotFoundError:
        traceback.print_exc()
        print(
            '\n\nmake sure u added a f2nd.txt in the same directory as this script with the dsc commands inside!'.upper())
        time.sleep(8)
        exit()


if __name__ == '__main__':
    main()
