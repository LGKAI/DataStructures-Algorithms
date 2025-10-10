def solve_n_queens(n):
    def place_queens(row, board):
        if row == n: # nếu đã đặt hết quân hậu trên các hàng
            print(board) # in ra một cách bố trí hợp lệ
            return
        for col in range(n): # thử đặt quân hậu ở các cột
            if is_safe(row, col, board):
                board[row] = col # đặt quân hậu tại hàng `row`, cột `col`
                place_queens(row + 1, board) # đệ quy để xử lý hàng tiếp theo
                board[row] = -1 # quay lui (xóa vị trí đã đặt quân hậu)
    
    def is_safe(row, col, board):
        for prev_row in range(row):
            # Kiểm tra cùng cột hoặc cùng đường chéo
            if board[prev_row] == col or \
               abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True

    board = [-1] * n # khởi tạo bàn cờ rỗng (-1 là không có quân hậu)
    place_queens(0, board) # gọi đệ quy bắt đầu từ hàng 0

if __name__ == '__main__':
    n = int(input())
    solve_n_queens(n)