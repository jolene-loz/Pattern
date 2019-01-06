#pylint disable=c

# def reverse_str_forward(string):
#     length = len(string)
#     temp = ''
#     for index in range(length):
#         char = string[index]
#         temp = char + temp
#     return temp
#
#
# def reverse_str_forward1(string):
#     temp = ''
#     for char in string:
#         temp = char + temp
#     return temp
#
#
# result = reverse_str_forward1('Computer')
# print result

#to see if a string is in another string
# string = 'Computer Science'
# sub = 'Computer'
# sub in string

# if x == false is EQUIVALENT TO " IF NOT X"
# x = True
# # not x
# x= False
# if not x:
#     print 'x must be False if I land here'

#confused about the not thing
# x = False
# 1 != 2
# not False
# if not x:
#     print 'x must be False if I land here'
#
# #do this life, if ask if the substring is in string
# sub = 'afdj'
# sub not in string


def find_char(string, char):
    # Iterate over the indices associated with the caracters in the string and for every individual character, compare it to the given character.
    #1. Either they match. Return the index.
    #2. They don't match. Wait until you're done with all the characters.
    # if none of them match, return -1
    length = len(string)
    for index in range(length):
        current_char = string[index]
        if current_char == char:
            return index
    return -1


result = find_char('Computer', 'o')
print result

string = 'Computer'
sub = 'o'
string.find(sub)

string = 'Boston University'
string.replace('University', 'College')
print string
