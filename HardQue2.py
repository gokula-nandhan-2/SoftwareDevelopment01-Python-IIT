def fibonacci(num):
    f = 0
    s = 1
    t = 0
    numbers=[0,1]
    if num > 0:
        if num == 1:
            numbers.pop()
            return numbers
        elif num == 2:
            return numbers
        else:
            for i in range(2,num):
                t = f + s
                f = s
                s = t
                numbers.append(t)
            return numbers

fibonacci(10)