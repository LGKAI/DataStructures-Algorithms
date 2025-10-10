def checkStrictlyIncreasing(n, lst, index=0):
    if index == n - 1:
        return "Yes"
    if lst[index] >= lst[index + 1]:
        return "No"
    return checkStrictlyIncreasing(n, lst, index + 1)

if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    print(checkStrictlyIncreasing(n, lst))