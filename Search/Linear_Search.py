import sys

def InputData():
    # inputslen = int(sys.stdin.readline().rstrip())
    # inputs= sys.stdin.readline()

    # sortvalue = [int(i) for i in inputs.split()]
    
    # readlines = sys.stdin.readline()

    deta_len = int(sys.stdin.readline().rstrip())
    datas = sys.stdin.readline()
    data = [int(i) for i in datas.split()]

    searchdata_len = int(sys.stdin.readline().rstrip())
    searchdatas = sys.stdin.readline()
    searchdata = [int(i) for i in searchdatas.split()]

    return deta_len, data, searchdata_len, searchdata

def Liner_Search(data_len, data, searchdata_len, searchdata):

    contained_cnt = 0
    for i in range(searchdata_len):
        for j in range(data_len):
            if searchdata[i] == data[j]:
                contained_cnt = contained_cnt + 1
    
    return contained_cnt

def PrintOut(contained_cnt):
    print(contained_cnt)

def main():
    [deta_len, data, searchdata_len, searchdata] = InputData()
    contained_cnt = Liner_Search(deta_len, data, searchdata_len, searchdata)
    PrintOut(contained_cnt)

if __name__=='__main__':
    main()