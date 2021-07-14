import sys

my_name = sys.argv[1]

$PSScriptRoot

for n, a in enumerate(sys.argv):
    print('arg {} has value {} endOfArg'.format(n, a))
print("Hello and welcome " + str(my_name) + "!")