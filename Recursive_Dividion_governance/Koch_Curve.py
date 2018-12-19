import math

def koch(d, p1, p2):
    if d == 0:
        return

    s_x = (2 * p1[0] + 1 * p2[0])/3
    s_y = (2 * p1[1] + 1 * p2[1])/3
    s = [s_x, s_y]
    t_x = (1 * p1[0] + 2 * p2[0])/3
    t_y = (1 * p1[1] + 2 * p2[1])/3
    t = [t_x, t_y]
    rotated = math.pi * 60 / 180
    u_x = (t_x - s_x) * math.cos(rotated) - (t_y - s_y) * math.sin(rotated) + s_x
    u_y = (t_x - s_x) * math.sin(rotated) + (t_y - s_y) * math.cos(rotated) + s_y
    u = [u_x, u_y]

    koch(d-1, p1, s)
    print(' '.join(map(str, s)))
    koch(d-1, s, u)
    print(' '.join(map(str, u)))
    koch(d-1, u, t)
    print(' '.join(map(str, t)))
    koch(d-1, t, p2)
    

def main():
    n  = int(input())
    p1 = [0.00000000,0.00000000]
    p2 = [100.00000000,0.00000000]
    print(' '.join(map(str, p1)))
    koch(n, p1, p2)
    print(' '.join(map(str, p2)))
if __name__=='__main__':
    main()