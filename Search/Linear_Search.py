import sys

def InputData():

    data_len = int(input())
    data = input().split()
    

    searchdata_len = int(input())
    searchdata = input().split()
    
    data = int(data)
    searchdata = int(searchdata)

    return data_len, data, searchdata_len, searchdata

def Liner_Search(data_len, data, searchdata_len, searchdata):

    contained_cnt = 0
    for i in range(searchdata_len):
        for j in range(data_len):
            if data[j] == searchdata[i]:
                contained_cnt = contained_cnt + 1
    
    return contained_cnt

def PrintOut(contained_cnt):
    print(int(contained_cnt))

def main():
    [data_len, data, searchdata_len, searchdata] = InputData()
    contained_cnt = Liner_Search(data_len, data, searchdata_len, searchdata)
    PrintOut(contained_cnt)

if __name__=='__main__':
    main()