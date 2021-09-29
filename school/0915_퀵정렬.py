def quickSort(ary):
    n=len(ary)
    if n<1:
        return ary
    pivot=ary[n//2]
    leftAry, midAry, rightAry=[],[],[]
    
    for num in ary:
        if num<pivot:
            leftAry.append(num)
        elif num>pivot:
            rightAry.append(num)
        else:
            midAry.append(num)
    return quickSort(leftAry)+midAry+quickSort(rightAry)

dataAry=[120, 188, 168, 50, 162, 105, 120, 177]
print('정렬 전>', dataAry)
dataAry=quickSort(dataAry)
print('정렬 후>', dataAry)
# #
# 정렬 전> [120, 188, 168, 50, 162, 105, 120, 177]
# 정렬 후> [50, 105, 120, 120, 162, 168, 177, 188]