import sys

class SlopType():
    def __init__(self):
        self.Up = '/'
        self.Downhill = '\\'
        self.Flat = '_'

def GetReadlineData():
    readlinedata= sys.stdin.readline()
    slop_data = [readlinedata[i] for i in range(len(readlinedata)-1)]

    return slop_data

def Puddle_area(slop_data):
    sloptype = SlopType()
    puddle_subtotal = 0
    puddle_discrete_area = []
    puddle_total_area = 0
    
    slop_rank = 0
    slop_downrank = 0
    slop_uprank = 0
    slop_cnt = 0
    puddle_cnt = 0

    for i in range(len(slop_data)):
        
        if slop_data[i] == sloptype.Downhill:
            slop_rank = 1
            slop_downrank = slop_downrank + 1
            for j in range(i+1,len(slop_data)):
                if slop_data[j] == sloptype.Downhill:
                    slop_rank = slop_rank + 1
                elif slop_data[j] == sloptype.Up:
                    slop_rank = slop_rank - 1
                slop_cnt = slop_cnt + 1
                if slop_rank == 0:
                    break
        elif slop_data[i] == sloptype.Up:
            slop_uprank = slop_uprank + 1
            
        if slop_downrank == slop_uprank and slop_downrank != 0 and slop_uprank != 0:
            puddle_discrete_area.append(slop_cnt)
            puddle_cnt = puddle_cnt + 1
            slop_cnt = 0
            slop_downrank = 0
            slop_uprank = 0
        
    
    if slop_downrank > slop_uprank:
        puddle_discrete_area.append(slop_cnt)
        puddle_cnt = puddle_cnt + 1
    
    puddle_total_area = sum(puddle_discrete_area)
    puddle_discrete_area.insert(0, puddle_cnt)
    
    return puddle_total_area, puddle_discrete_area

def PrintOut(puddle_total_area, puddle_discreate_area):
    print(puddle_total_area)
    puddle_discreate_area_print = map(str, puddle_discreate_area)
    print(' '.join(puddle_discreate_area_print))

def main():
    slop_data = GetReadlineData()
    # print(slop_data)
    [puddle_total_area, puddle_discreate_area] = Puddle_area(slop_data)
    PrintOut(puddle_total_area, puddle_discreate_area)

if __name__ == '__main__':
    main()