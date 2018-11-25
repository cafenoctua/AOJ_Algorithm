import sys

def GetReadlineData():
    readlines = sys.stdin.readline().rstrip()
    [inputlen, threstime] = readlines.split()
    inputlen = int(inputlen)
    threstime = int(threstime)

    inputdata= [sys.stdin.readline() for i in range(inputlen)]
    
    prosname = [0 for i in range(inputlen)]
    prostime = [0 for i in range(inputlen)]
    for i in range(inputlen):
        [prosname[i], prostime[i]] = inputdata[i]
        prostime[i] = int(prostime[i])

    return threstime, prosname, prostime

def DataPros(threstime, prosname, prostime):

    endtime = sum(prostime)
    nowprostime = 0
    while nowprostime <= endtime:
        

def main():

if __name__ == '__main__':
    main()