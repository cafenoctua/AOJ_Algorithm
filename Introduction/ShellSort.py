import sys
import math

def InsertionSort(sortvalue, inputslen, g, sortcnt):
    for i in range(g, inputslen):

        compvalue = sortvalue[i]
        j = i - g
        while j >= 0 and sortvalue[j] > compvalue:
            sortvalue[j+g] = sortvalue[j]
            j = j - g
            #if g != 1:
            sortcnt = sortcnt + 1
        sortvalue[j+g] = compvalue
    
    return sortcnt

def ShellSort(sortvalue, inputslen):
    cnt = 0
    m = math.ceil(inputslen/4)
    
    G = [i*3+1  for i in range(0, m)]
    G.reverse()
    
    sortcnt = 0
    for i in range(0, m):
        sortcnt = InsertionSort(sortvalue, inputslen, G[i], sortcnt)
    
    print('{}'.format(m))
    printG = map(str, G)
    print(' '.join(printG))
    print(sortcnt)
    for i in range(0,inputslen):
        printvalue = sortvalue[i]
        #print(printvalue)
        sys.stdout.write(printvalue)

def main():
    inputslen = int(sys.stdin.readline().rstrip())
    sortvalue= [sys.stdin.readline() for i in range(inputslen)]

    #sortvalue = [int(i) for i in inputs.split()]

    ShellSort(sortvalue, inputslen)

if __name__ == '__main__':
    main()