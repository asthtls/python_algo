# 1085_직사각형에서 탈출


x, y, w, h = map(int, input().split())

def Min(x, y, w, h):
    if x<=y and x<=w and x<=h:
        return x
    elif y<=x and y<=w and y<=h:
        return y
    elif w<=x and w<=y and w<=h:
        return w
    else :
        return h

min_reslut = Min(x,y,w-x,h-y)

print(min_reslut)