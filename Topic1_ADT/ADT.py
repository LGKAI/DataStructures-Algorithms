def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    queue = []

    for char in expression:
        if char.isalnum(): # nếu là toán hạng, thêm vào queue
            queue.append(char)
        elif char == '(': # nếu là dấu mở ngoặc, đẩy vào stack
            stack.append(char)
        elif char == ')': # nếu là dấu đóng ngoặc, pop khỏi stack cho đến khi gặp dấu mở ngoặc
            while stack and stack[-1] != '(':
                queue.append(stack.pop())
            stack.pop() # bỏ dấu '(' khỏi stack
        else: # nếu là toán tử
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0): # nếu stack ko rỗng và toán tử mới có độ ưu tiên ko cao hơn toán tử trên đỉnh stack
                queue.append(stack.pop()) # pop toán tử từ stack ra kết quả
            stack.append(char) # push toán tử mới vào stack

    while stack: # pop hết toán tử còn lại trong stack
        queue.append(stack.pop())

    return ' '.join(queue)

def calculate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit(): # nếu là số, đẩy vào stack
            stack.append(int(char))
        else: # nếu là toán tử, lấy 2 toán hạng từ stack
            b = stack.pop()
            a = stack.pop()
            if char == '+': stack.append(a + b)
            elif char == '-': stack.append(a - b)
            elif char == '*': stack.append(a * b)
            elif char == '/': stack.append(a / b)
            elif char == '^': stack.append(a ** b)
            
    return stack[0] # kết quả cuối cùng còn lại trong stack

def max_window(arr, w):
    if not arr or w <= 0 or w > len(arr):
        return []
    
    window_sum = sum(arr[:w])  # tổng của cửa sổ đầu tiên
    max_sum = window_sum
    max_window_slice = arr[:w]  # cửa sổ có tổng lớn nhất

    for i in range(len(arr) - w):
        window_sum = window_sum - arr[i] + arr[i + w]  # cập nhật tổng cửa sổ
        if window_sum > max_sum:
            max_sum = window_sum
            max_window_slice = arr[i + 1: i + 1 + w]  # cập nhật cửa sổ tốt nhất
            
    return max_window_slice


if __name__ == "__main__":
    # print(infix_to_postfix("1+2"))
    # print(infix_to_postfix("(A+B)*C-D"))
    # print(calculate_postfix("23+5*"))
    # print(calculate_postfix("52+83-*"))

    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    w = 3
    print(max_window(arr, w))