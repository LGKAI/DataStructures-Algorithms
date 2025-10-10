def generate_binary_strings(n, current = ""):
    if len(current) == n:
        print(current) # in chuỗi nhị phân khi đạt đến độ dài n
        return
    # Gọi đệ quy thêm '0' hoặc '1' vào chuỗi hiện tại
    generate_binary_strings(n, current + "0")
    generate_binary_strings(n, current + "1")

if __name__ == '__main__':
    n = int(input())
    generate_binary_strings(n)