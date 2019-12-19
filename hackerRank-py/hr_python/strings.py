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
