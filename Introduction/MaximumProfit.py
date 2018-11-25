import sys

def main():
    inputs = int(sys.stdin.readline().rstrip())
    maxv = -100000000000
    minv = int(sys.stdin.readline().rstrip())

    # Calc idel
    for i in range(1, inputs):
        compv = int(sys.stdin.readline())
        if compv - minv > maxv:
            maxv = compv - minv
        if compv < minv:
            minv = compv
        

    bigprice = maxv
    print(bigprice)



if __name__ == '__main__':
    main()