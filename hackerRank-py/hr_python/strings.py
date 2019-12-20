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


