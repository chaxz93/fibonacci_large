def get_fibonacci_huge(a, b, n, m):
    if n == 0:
        return a
    elif n == 1:
        return b
    arr = [a, b]
    previousMod = a % m
    currentMod = b % m

    for i in range(n - 1):
        tempMod = previousMod
        previousMod = currentMod % m
        currentMod = (tempMod + currentMod) % m
        arr.append(currentMod)
        if currentMod == 1 and previousMod == 0:
            index = ((n + 1) % (i + 1))
            return arr[index]
        break
    return currentMod

if __name__ == '__main__':
    print(get_fibonacci_huge(2,3,5,8))
