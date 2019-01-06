#Problem Set 3, Part I
# Lozano, Jolene


def match(text, pattern):
    n = len(pattern)
    n2 = len(pattern)
    t = len(text)
    begin = 0
    for index in range(begin, t):
        if text[index:n + index] == pattern[0:n2]:
            return True
    return False


def main():
    text = raw_input('Please input a text string: ')
    pattern = raw_input('Please input a pattern string: ')
    while text.upper() != 'QQQ':
        result = match(text, pattern)
        if result == True:
            print 'You found a match!'
        else:
            print 'lol no, try again'
        text = raw_input('Please input a text string: ')
        pattern = raw_input('Please input a pattern string: ')
    print 'Thank you using this program.'


main()
