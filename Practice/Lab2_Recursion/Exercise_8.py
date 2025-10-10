def generate_subsets(current, remaining, all_subsets):
    if not remaining: # khi không còn phần tử để xử lý
        all_subsets.append(current) # thêm tập con hiện tại vào danh sách tập con
        return
    # Đệ quy không bao gồm phần tử hiện tại
    generate_subsets(current, remaining[1:], all_subsets)
    # Đệ quy bao gồm phần tử hiện tại
    generate_subsets(current + [remaining[0]], remaining[1:], all_subsets)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    all_subsets = [] # list chứa tất cả các tập con

    generate_subsets([], arr, all_subsets)

    all_subsets.sort(key=lambda x: (len(x), x))
    for subset in all_subsets:
        print("{" + ",".join(map(str, subset)) + "}")