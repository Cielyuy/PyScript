def listGet(a, b, c):
    '''
    输入的三个数字中，前两个是所需生成的数字序列的所属范围，如 500-1000
    第三个数字是等分数量，如，200. 如果不能整除，那么保留最后的b，这里是100
    
    '''
    numList = list()
    if (b - a) % c == 0:
        d = (b - a) / c
        i = 0
        while i <= d:
            numList.append(a + i * c)
            i = i + 1

    else:
        d = (b - a) / c
        i = 0
        while i <= d:
            numList.append(a + i * c)
            i = i + 1

        numList.append(b)

    return numList