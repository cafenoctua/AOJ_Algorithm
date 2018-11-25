import sys

def main():
    # Get Data Length
    inputslen = int(sys.stdin.readline().rstrip())
    # Get Data
    inputs= sys.stdin.readline()

    stablevalue = inputs.split()
    stablebubble = inputs.split()
    stableselect = inputs.split()
    
    stable = {'C':0, 'D':1, 'H':2, 'S':3}

    # Data cleansing

    sortbubble = [0  for i in range(len(stablevalue))]
    sortselect = [0  for i in range(len(stablevalue))]
    for i in range(0, len(stablevalue)):
        stablesplrit = stablevalue[i]
        if len(stablesplrit) < 3:
            sortvalue[i] = [int(stablesplrit[1])]
            sortbubble[i] = [int(stablesplrit[1])]
            sortselect[i] = [int(stablesplrit[1])]
        else:
            sortvalue[i] = [int(stablesplrit[1] + stablesplrit[2])]
            sortbubble[i] = [int(stablesplrit[1] + stablesplrit[2])]
            sortselect[i] = [int(stablesplrit[1] + stablesplrit[2])]

    # BubbleSort
    flag = 1
    while flag:
        flag = 0
        for i in range(1, inputslen):
            j = inputslen - i
            compvalue = sortbubble[j]
            compstable = stablebubble[j]
            if compvalue < sortbubble[j-1]:
                sortbubble[j] = sortbubble[j-1]
                sortbubble[j-1] = compvalue
                stablebubble[j] = stablebubble[j-1]
                stablebubble[j-1] = compstable
                flag = 1
    # Stable Check
    nostable = 0
    for i in range(1, len(stablebubble)):
        if sortbubble[i] == sortbubble[i-1]:
            if stable[stablebubble[i][0]] < stable[stablebubble[i-1][0]]:
                nostable = 1
    # PrintResult
    printvalue = map(str, stablebubble)
    print(' '.join(printvalue))
    if nostable == 0:
        print('Stable')
    else:
        print('Not stable')

    # Select Sort
    #printvalue = map(str, stableselect)
    #print(' '.join(printvalue))
    for i in range(0, inputslen-1):
        minidx = i
        for j in range(i, inputslen):
            if sortselect[j] < sortselect[minidx]:
                minidx = j
        if sortselect[minidx] != sortselect[i]:
            minvalue = sortselect[minidx]
            sortselect[minidx] = sortselect[i]
            sortselect[i] = minvalue
            minstable = stableselect[minidx]
            stableselect[minidx] = stableselect[i]
            stableselect[i] = minstable
            #printvalue = map(str, stableselect)
            #print(' '.join(printvalue))
    # Stable Check
    nostable = 0
    for i in range(1, len(stablebubble)):
        if sortselect[i] == sortselect[i-1]:
            if stable[stableselect[i][0]] < stable[stableselect[i-1][0]]:
                nostable = 1
    # PrintResult
    printvalue = map(str, stableselect)
    print(' '.join(printvalue))
    if nostable == 0:
        print('Stable')
    else:
        print('Not stable')

if __name__ == '__main__':
    main()