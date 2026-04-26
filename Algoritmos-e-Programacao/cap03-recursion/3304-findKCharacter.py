# 3304. Find the K-th Character in String Game I
# em ASCII a = 97 e z = 122
#
import time

def addLetter(k):
    global w
    temp = []    

    for i in range(len(w)):
        # caso base
        if len(w) >= k:
            return w[k-1]
        
        nAtual = ord(w[i])
        if nAtual == 122:
            nProx = 97
        else:
            nProx = nAtual + 1

        temp.append(chr(nProx))

    w = w + temp

    addLetter(k)

    return w[k-1]

startTime = time.time()
w = ['a']
teste = [1, 2, 3, 4, 5, 9, 10, 1000]

print('Se w[0] =', w[0])
for j in teste:
    result = addLetter(j)    
    print('Para k =', j, '->', result)

#result = addLetter(2)
# print(result)
print('tempo de execução: ', time.time()-startTime, 's')
# print(w)


            
