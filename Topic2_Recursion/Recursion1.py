def factorial(n):
    if n <= 1: return 1
    else: return n * factorial(n - 1)

def bunnyEars(bunnies):
    if bunnies == 0: return 0
    else: return 2 + bunnyEars(bunnies - 1)

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)

def bunnyEars2(bunnies):
    if bunnies == 0: return 0
    elif bunnies % 2 == 0: return 3 + bunnyEars2(bunnies - 1)
    else: return 2 + bunnyEars2(bunnies - 1)

def triangle(rows):
    if rows == 0: return 0
    else: return rows + triangle(rows - 1)

def sumDigits(n):
    if n == 0: return 0
    else: return n % 10 + sumDigits(n // 10)

def count7(n):
    if n == 0: return 0
    elif n % 10 == 7: return 1 + count7(n // 10)
    else: return count7(n // 10)

def count8(n):
    if n == 0: return 0
    elif n % 10 == 8 and (n // 10) % 10 == 8: return 2 + count8(n // 10)
    elif n % 10 == 8: return 1 + count8(n // 10)
    else: return count8(n // 10)

def powerN(base, n):
    if n == 0: return 1
    else: return base * powerN(base, n - 1)

def countX(str):
    if len(str) == 0: return 0
    elif str[0] == 'x': return 1 + countX(str[1:])
    else: return countX(str[1:])

def countHi(str):
    if len(str) < 2: return 0
    elif str[:2] == 'hi': return 1 + countHi(str[2:])
    else: return countHi(str[1:])

def changeXY(str):
    if len(str) == 0: return ''
    elif str[0] == 'x': return 'y' + changeXY(str[1:])
    else: return str[0] + changeXY(str[1:])

def changePi(str):
    if len(str) < 2: return str
    elif str[:2] == 'pi': return '3.14' + changePi(str[2:])
    else: return str[0] + changePi(str[1:])

def noX(str):
    if len(str) == 0: return ''
    elif str[0] == 'x': return noX(str[1:])
    else: return str[0] + noX(str[1:])

def array6(nums, index):
    if index == len(nums): return False
    elif nums[index] == 6: return True
    else: return array6(nums, index + 1)

def array11(nums, index):    
    if index == len(nums): return 0
    elif nums[index] == 11: return 1 + array11(nums, index + 1)
    else: return array11(nums, index + 1)

def array220(nums, index):
    if index == len(nums) - 1: return False
    elif nums[index] * 10 == nums[index + 1]: return True
    else: return array220(nums, index + 1)

def allStar(str):
    if len(str) < 2: return str
    else: return str[0] + '*' + allStar(str[1:])

def pairStar(str):
    if len(str) < 2: return str
    elif str[0] == str[1]: return str[0] + '*' + pairStar(str[1:])
    else: return pairStar(str[1:])

def endX(str):
    if len(str) < 2: return str
    elif str[0] == 'x': return endX(str[1:]) + 'x'
    else: return str[0] + endX(str[1:])

def countPairs(str):
    if len(str) < 3: return 0
    elif str[0] == str[2]: return 1 + countPairs(str[1:])
    else: return countPairs(str[1:])

def countAbc(str):
    if len(str) < 3: return 0
    elif str[:3] == 'abc' or str[:3] == 'aba': return 1 + countAbc(str[1:])
    else: return countAbc(str[1:])

def count11(str):
    if len(str) < 2: return 0
    elif str[:2] == '11': return 1 + count11(str[2:])
    else: return count11(str[1:])

def stringClean(str):
    if len(str) < 2: return str
    elif str[0] == str[1]: return stringClean(str[1:])
    else: return str[0] + stringClean(str[1:])

def countHi2(str):
    if len(str) < 2: return 0
    elif str[:2] == 'hi': return 1 + countHi2(str[2:])
    elif str[:3] == 'xhi': return countHi2(str[3:])
    else: return countHi2(str[1:])

def parenBit(str):
    if str[0] == '(': return str[:str.index(')') + 1]
    else: return parenBit(str[1:])

def nestParen(str):
    if len(str) == 0: return True
    elif str[0] == '(' and str[-1] == ')': return nestParen(str[1:-1])
    else: return False

def strCount(str, sub):
    if len(str) < len(sub): return 0
    elif str[:len(sub)] == sub: return 1 + strCount(str[len(sub):], sub)
    else: return strCount(str[1:], sub)

def strCopies(str, sub, n):
    if len(str) < len(sub) * n: return False
    elif str[:len(sub)] == sub: return strCopies(str[1:], sub, n - 1)
    else: return strCopies(str[1:], sub, n)

def strDist(str, sub):
    if len(str) < len(sub) * 2: return 0
    elif str[:len(sub)] == sub and str[-len(sub):] == sub: return len(str)
    elif str[:len(sub)] != sub: return strDist(str[1:], sub)
    else: return strDist(str[:-1], sub)
    

if __name__ == "__main__":
    pass