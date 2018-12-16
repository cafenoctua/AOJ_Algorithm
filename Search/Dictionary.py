class Command():
    def __init__(self):
        self.Insert = 'insert'
        self.Find = 'find'

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

def Dictionary():
    command = Command()

    input_len = int(input())

    dict_list = []
    find_list=[]
    find_flag = 'no'
    for i in range(input_len):
        input_command = input().split()
        if input_command[0] == command.Insert:
            dict_list.append(input_command[1]) 
            
        elif input_command[0] == command.Find:
            if input_command[1] in dict_list:
                find_flag = 'yes'

            find_list.append(find_flag)
    
    return find_list

def PrintOut(find_list):
    for i in find_list:
        print(i)

def main():
    find_list = Dictionary()
    PrintOut(find_list)

if __name__ == '__main__':
    main()