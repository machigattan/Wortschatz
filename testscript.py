import sys

new_word = sys.argv[1]

# def send():
#     some_list = []
#     for i in 'string':
#          some_list.append( i )
#     return new_word

for n, a in enumerate(sys.argv):
    # print('arg {} has value {} endOfArg'.format(n, a))
    print("Hello and welcome " + str(new_word) + "!")