def repeated_string(s, n):
    if 'a' in s:
        print(s.count('a') * (n // len(s)) + s[:n % len(s)].count('a'))
    else:
        print('0')

