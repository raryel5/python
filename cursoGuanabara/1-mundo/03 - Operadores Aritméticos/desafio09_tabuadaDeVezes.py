tabuada = int(1)
while True:
    num = int(1)
    while True:
        print('{} x {} = {}.'.format(tabuada, num, tabuada*num))
        num += 1
        if num == 11:
            break
    tabuada += 1
    if tabuada == 11:
        break
