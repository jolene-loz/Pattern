#Problem Set 3, Part II
# Lozano, Jolene
# Duquette, Rachel


def change(initial_letter, final_letter, word):
    n = len(word)
    for index in range(n):
        if word[index] == initial_letter:
            word = word[0:index] + final_letter + word[index + 1:n]
    return word


#test
#change(' ', '#', 'c ta')


def encoder(word):

    result1 = change('a', '&', word)
    result2 = change('b', 'a', result1)
    result3 = change('&', 'b', result2)
    result4 = change('e', '#', result3)
    n = len(result4)
    if n % 2 == 0:
        half = n / 2
        result4 = result4[half:n] + result4[0:half]
    else:
        another_half = ((n + 1) / 2) - 1
        result4 = result4[another_half + 1:
                          n] + result4[another_half] + result4[0:another_half]
    return result4


def decoder(word):

    result1 = change('a', '&', word)
    result2 = change('b', 'a', result1)
    result3 = change('&', 'b', result2)
    result4 = change('#', 'e', result3)
    n = len(result4)
    if n % 2 == 0:
        half = n / 2
        result4 = result4[half:n] + result4[0:half]
    else:
        another_half = ((n + 1) / 2) - 1
        result4 = result4[another_half + 1:
                          n] + result4[another_half] + result4[0:another_half]
    return result4


# encoder('boston college')
# decoder(encoder('boston college'))
#
# encoder('banana')
# decoder(encoder('banana'))
#
# encoder('melissa')
# decoder(encoder('melissa'))
#
# encoder('ram')
# decoder(encoder('ram'))
#
# encoder('how are you today?')
# decoder(encoder('how are you today?'))
