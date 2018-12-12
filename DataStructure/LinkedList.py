import sys

class CommandType():
    def __init__(self):
        self.Insert = "insert"
        self.Delete = "delete"
        self.DeleteFirst = "deleteFirst"
        self.DeleteLast = "deleteLast"

def Input_Command():
    # Input length
    readlines = sys.stdin.readline()
    inputlen = int(readlines)
    # inputlen = sys.stdin.readline()
    # Input Command
    inputdata= [sys.stdin.readline() for i in range(inputlen)]
    
    command = CommandType()
    commandname = [0 for i in range(inputlen)]
    number = [0 for i in range(inputlen)]
    for i in range(inputlen):
        if inputdata[i].strip("\n") == command.DeleteFirst or inputdata[i].strip("\n") == command.DeleteLast:
            commandname[i] = inputdata[i].strip("\n")
            number[i] = -1
        else:
            # print(inputdata[i])
            [commandname[i], number[i]] = inputdata[i].split()
        number[i] = int(number[i])
    
    return inputlen, commandname, number
    # For Test
    # print('r')

    # for i in range(inputlen):
    #     print(commandname[i])
    #     print(number[i])

def LinkedList(inputlen, commandname, number):
    command = CommandType()
    linklist = []
    insert_cnt = 0
    for i in range(inputlen):
        if commandname[i] == command.Insert:
            linklist.append(number[i])
            # if linklist[0] == -1:
            #     linklist.pop(0)
            insert_cnt = insert_cnt + 1
        elif commandname[i] == command.Delete:
            # deletelist = linklist.copy()
            # deletelist = []
            for j in range(insert_cnt-1, -1, -1):
                # print('list:{}'.format(linklist[j]))
                if linklist[j] == number[i]:
                    # deletelist.pop(j)
                    # deletelist.append(j)
                    delete_num = j
                    # delete_cnt = insert_cnt - 1
                    break

            # for j in deletelist:
                # linklist.pop(j)
            # print('del:{}'.format(linklist[delete_num]))
            linklist.pop(delete_num)
            insert_cnt = insert_cnt - 1
            delete_num = -1
            # deletelist.clear()

        elif commandname[i] == command.DeleteFirst:
            linklist.pop(-1)
            insert_cnt = insert_cnt - 1
        elif commandname[i] == command.DeleteLast:
            linklist.pop(0)
            insert_cnt = insert_cnt - 1
    
    # print(linklist)
    linklist.reverse()
    # linklist.pop(-1)
    return linklist

def PrintOutPut(linklist):
    printvalue = map(str, linklist)
    print(' '.join(printvalue))
    # for i in linklist:
    #     print('{}'.format(i))
    # print(linklist)

def main():
    [inputlen, commandname, number] = Input_Command()
    linklist = LinkedList(inputlen, commandname, number)
    PrintOutPut(linklist)

if __name__ == '__main__':
    main()