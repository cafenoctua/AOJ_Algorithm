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

    lenpros = len(prosname)
    endtime = sum(prostime)
    nowprostime = 0
    i = 0
    endcnt = 0

    while nowprostime <= endtime:
        endcnt = endcnt + 1
        if endcnt > 100:
            print("エラー発生")
            break
        if prostime[i] > threstime:
            nowprostime = nowprostime + 100
            prostime[i] = prostime[i] - 100
        else:
            nowprostime = nowprostime + prostime[i]
            print("{} {}".format(prosname[i], prostime[i]))
            prostime.remove[i+1]
            prosname.remove[i+1]
            lenpros = lenpros - 1

        if i < lenpros:
            i = i + 1
        else:
            i = 0
    
        

def main():
    [threstime, prosname, prostime] = GetReadlineData()
    DataPros(threstime, prosname, prostime)


if __name__ == '__main__':
    main()