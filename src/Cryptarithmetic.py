import os.path
import timeit

# e.g.
#           S E N D                   9 5 6 7
#       +   M O R E               +   1 0 8 5
#         ---------                 ---------
#         M O N E Y                 1 0 6 5 2

NUMERIK = '0123456789'

def Resource(namafile):
    operands = []
    result = ""
    with open("../testcase/" + namafile) as f:
        line = f.readline()
        while line:
            word = ''.join(c for c in line if c not in " +\n")
            line = f.readline()
            if word[0] == '-':
                result = ''.join(c for c in line if c not in " +\n")
            else:
                operands.append(word)
    return operands, result
    