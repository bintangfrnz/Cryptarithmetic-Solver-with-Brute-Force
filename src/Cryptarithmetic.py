import os.path
import timeit

NUMERIC = '0123456789'

def getResource(filename):
    operands = []
    result = ""
    with open("../testcase/" + filename) as f:
        line = f.readline()
        while line:
            word = ''.join(c for c in line if c not in " +\n")
            if word[0] != '-':
                operands.append(word)
            else:
                line = f.readline()
                result = ''.join(c for c in line if c not in " +\n")
            line = f.readline()
                
    return operands, result

def Permutation(n_uniq_letters=None):
    tuple_NUMERIC = tuple(NUMERIC)
    n = len(tuple_NUMERIC)

    n_uniq = n if n_uniq_letters is None else n_uniq_letters

    if n_uniq > n:
        return
    
    idx = [x for x in range(n)]
    loop = [x for x in range(n, n-n_uniq, -1)]
    yield tuple(tuple_NUMERIC[i] for i in idx[:n_uniq])

    while n:
        for i in reversed(range(n_uniq)):
            loop[i] -= 1
            if loop[i] == 0:
                idx[i:] = idx[i+1:] + idx[i:i+1]
                loop[i] = n-i
            else:
                j = loop[i]
                idx[i], idx[-j] = idx[-j], idx[i]
                yield tuple(tuple_NUMERIC[i] for i in idx[:n_uniq])
                break
        else:
            return

def ConvertToInt(word, dictCharValue):
    value = ""
    for c in word:
        value += dictCharValue[c]
    return int(value)

def BruteForce(operands, result):
    char_notZero = []
    combined_words = ""

    for operand in operands:
        char_notZero.append(operand[0])
        combined_words += operand

    char_notZero.append(result[0])
    combined_words += result

    unique_letters = ''.join(set(combined_words))
    n_uniq_letters = len(unique_letters)

    n_solution = 1
    n_loop = 0
    for tup in Permutation(n_uniq_letters):
        dictCharValue = {}
        for i in range(n_uniq_letters):
            dictCharValue[unique_letters[i]] = tup[i]
        
        firstChar_Zero = False
        for c in char_notZero:
            if dictCharValue[c] == '0':
                firstChar_Zero = True
                break
        
        if firstChar_Zero:
            continue

        resultValue = ConvertToInt(result,dictCharValue)

        operandsValue = []
        for operand in operands:
            operandsValue.append(ConvertToInt(operand, dictCharValue))

        n_loop += 1
        if (sum(operandsValue) == resultValue):
            n_th = "st" if n_solution==1 else ("nd" if n_solution==2 else ("rd" if n_solution==3 else "th"))
            print("\n{}{} Solution".format(n_solution, n_th))
            print(' '*3 + ' + '.join(operands) + ' = ' + result)
            print('-> ' + ' + '.join([str(operand) for operand in operandsValue]) + ' = ' + str(resultValue))
            n_solution += 1
            print("Iteration: {} x\n".format(n_loop))

    print("Total iteration: {} x".format(n_loop))

def Cryptarithmetic(filename):
    print("\nFile: \"{}\"".format(filename))
    print("Solving...")
    start = timeit.default_timer()

    operands, result = getResource(filename)

    over10 = False
    for operand in operands:
        if len(operand) > 10:
            over10 = True
            break
    
    if not over10:
        BruteForce(operands, result)

    stop = timeit.default_timer()

    print("Time: {} s".format(stop-start))



# MAIN PROGRAM
print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print("┃         Cryptarihmetic Solver (Brute Force)         ┃")
print("┃               by: Bintang Fajarianto                ┃")
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

QnA = input("Check all testcase (y/n)?\n>> ")
if QnA == 'y':
    allfiles = [f for f in os.listdir('../testcase/') if os.path.isfile(os.path.join('../testcase/', f)) and f.endswith('.txt')]

    for current_file in allfiles:
        Cryptarithmetic(current_file)

    print("┏━━━━━━━━━━━━━┓\n┃     END     ┃\n┗━━━━━━━━━━━━━┛")

elif QnA == 'n':
    while 1:
        print("Input filenames (TC1.txt / ... / TC10.txt / eg1.txt / ... / eg3.txt)")
        filename = input(">> ")
        while not os.path.isfile('../testcase/' + filename):
            print("File not found!\n")
            print("Input filenames (TC1.txt / ... / TC10.txt / eg1.txt / ... / eg3.txt)")
            filename = input(">> ")
        
        Cryptarithmetic(filename)

        QnA = input("Check other testcase (y/n)?\n>> ")
        if QnA == 'y':
            print("\n!")
        elif QnA == 'n':
            print("┏━━━━━━━━━━━━━┓\n┃     END     ┃\n┗━━━━━━━━━━━━━┛")
            break
        else:
            print("Come on! u dumb..")
            break
else:
    print("Come on! u dumb..")