import sys

def GetReadlineData():
    readlines = sys.stdin.readline().rstrip()
    [inputlen, threstime] = readlines.split()
    inputlen = int(inputlen)
    threstime = int(threstime)

    inputdata= [sys.stdin.readline() for i in range(inputlen)]
    #print(inputdata)
    
    prosname = [0 for i in range(inputlen)]
    prostime = [0 for i in range(inputlen)]
    for i in range(inputlen):
        #print(inputdata[i].split())
        [prosname[i], prostime[i]] = inputdata[i].split()
        prostime[i] = int(prostime[i])

    #return threstime, prosname, prostime
    #def DataPros(threstime, prosname, prostime):
    lenpros = len(prosname) - 1
    endtime = sum(prostime)
    nowprostime = 0

    calcedflag = [0 for i in range(inputlen)]
    i = 0
    endcnt = 0
    if inputlen == 1:
        print("{} {}".format(prosname[0], prostime[0]))
    else:
        while nowprostime < endtime:
            #endcnt = endcnt + 1
            #if endcnt > 1000000000:
            #    print("エラー発生")
            #    break
            if prostime[i] > threstime:
                nowprostime = nowprostime + threstime
                prostime[i] = prostime[i] - threstime
            else:
                if calcedflag[i] == 0:
                    nowprostime = nowprostime + prostime[i]
                    print("{} {}".format(prosname[i], nowprostime))
                    calcedflag[i] = 1
                #if lenpros != 0:
                #    del prostime[i]
                #    del prosname[i]
                #    lenpros = lenpros - 1

            if i < lenpros:
                i = i + 1
            else:
                i = 0
        
        

def main():
    #[threstime, prosname, prostime] = GetReadlineData()
    #DataPros(threstime, prosname, prostime)
    GetReadlineData()

if __name__ == '__main__':
    main()