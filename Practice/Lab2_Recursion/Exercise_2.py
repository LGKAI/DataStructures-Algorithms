def sumOfDigits(n):
    if n == 0: return 0
    else: return (n % 10) + sumOfDigits(n // 10)
    
if __name__ == '__main__':
    n = int(input())
    print(sumOfDigits(n))