def checkPalindrome(s):
    if len(s) < 2: return "Yes"
    elif len(s) == 2:
        if s[0] == s[1]: return "Yes"
        else: return "No"
    else:
        if s[0] == s[-1]: return checkPalindrome(s[1:-1])
        else: return "No"

if __name__ == '__main__':
    s = input()
    print(checkPalindrome(s))