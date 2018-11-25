def main():
    data = []
    while 1:
        n = input().split()
        ans = int(n[0])
 
        if ans == 0:
            break
 
        data.append(ans)
 
 
    length = len(data)
    what_large = length > 100000
 
    if what_large:
        print("Too Large")
    else:
        for i in range(len(data)):
            d_val = data[i]
 
            if d_val != 0:
                print("Case {0}: {1}".format(i+1,d_val))
            else:
                break
 
if __name__ == '__main__':
    main()