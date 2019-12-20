from collections import OrderedDict


def minion_game(s):
    scores = {'stuart': 0, 'kevin': 0}
    for i in range(len(s)):
        if s[i] in 'AEIOU':
            scores['kevin'] += len(s) - i
        else:
            scores['stuart'] += len(s) - i

    if scores['kevin'] > scores['stuart']:
        ('{} {}'.format('Kevin', scores['kevin']))
    elif scores['kevin'] < scores['stuart']:
        print('{} {}'.format('Stuart', scores['stuart']))
    else:
        print('Draw')


def swap_case(s):
    result = ''
    for i in s:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()
    return result


def merge_the_tools(s, k):
    i = 0
    while i < len(s):
        # Python 3.7+, dict.fromkeys returns (from list) a dict in sorted order
        print(''.join([str(i) for i in list(dict.fromkeys(list(s[i:i + k])))]))
        i += k






merge_the_tools('AABCAAADA', 3)

