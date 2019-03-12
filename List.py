numbers = [1,2,3,6]
def sumOfListNumbers(numbers):
    length = len(numbers)
    limit = 0
    ans = 0
    while limit < length:
        ans = numbers[limit] + ans
        limit += 1

    print(ans)
