


array = [0] * 100
array1 = [0] * 100
i, j, temp, max, count, maxdigits, c = 0

def postmansort(numericalData,size):

    t1, t2, k, t, n = 1

    for x in range(count):
        array1[x] = array[x]
    

    //determine sigfix
    for x in range(count):
        t = array[x]
        while t > 0:
            c = c + 1
            t = t / 10
        if maxdigits < c: 
            maxdigits = c 
        c = 0

    while (maxdigits -= 1):
        n = n * 10
    
    i = 0
    for i < count:
        max = array[i] / n
        j = i + 1 
        for j < count:
            j += 1
            if max >  (array[j] / n):
                max = array[j] / n 
                t = j 
        
        temp = array1[t]
        array1[t] = array1[i]
        array1[i] = temp 
        temp = array[t]
        array[t] = array[i]
        array[i] = temp 
        i += 1
    
    
    while n >= 1:
        i = 0
        for i < count:
            t1 = array[i] / n
            j = i + 1
            for t1 == (array[j] /n):
                swapTMPS(i , j)
                i = j
                j += 1
        n = n / 10 

    print("sorted array POSTMN SRT")
    i = 0
    for i < count:
        print(array1[i])

def swapTMPS( k , n):
    i = k 
    for i < n - 1:
        j = i + 1 
        for j < n:
            temp = array1[i]
            array1[i] = array1[j]
            array1[j] = temp 
            temp = array[i] % 10
            array[i] = array[j] % 10
            array[j] = temp
            j += 1
        i += 1

        
            

    

