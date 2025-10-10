def read_exam(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    m = int(lines[0].strip())  # số nguyện vọng
    quota = {}  # chỉ tiêu mỗi nguyện vọng
    candidates = []  # danh sách thí sinh

    for i in range(1, m + 1):
        option, count = map(int, lines[i].strip().split())
        quota[option] = count

    for line in lines[m + 1:]:
        parts = line.strip().split(",")
        name = parts[0].strip('"')
        score1, score2 = map(float, parts[1:3])
        choices = list(map(int, parts[3:]))
        avg_score = round((score1 + score2) / 2, 2)
        candidates.append((name, avg_score, score1, score2, choices))

    return m, quota, candidates

def assign_candidates(m, quota, candidates):
    # Sắp xếp danh sách thí sinh theo thứ tự ưu tiên:
    # 1. Điểm trung bình giảm dần
    # 2. Nếu bằng nhau, xét điểm bài thi 1 giảm dần
    # 3. Nếu bằng nhau, xét điểm bài thi 2 giảm dần
    candidates.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    
    accepted = {i: [] for i in range(1, m + 1)}  # danh sách trúng tuyển
    rejected = []  # danh sách rớt

    for name, avg, s1, s2, choices in candidates:
        placed = False
        for choice in choices:
            if quota[choice] > 0:  # nếu còn slot cho nguyện vọng này
                accepted[choice].append((name, avg))
                quota[choice] -= 1
                placed = True
                break
        if not placed:
            rejected.append((name, avg))
    
    return accepted, rejected

def print_result(accepted, rejected):
    for option, lst in accepted.items():
        print(f"Successful candidates for option {option}")
        if lst:  # nếu có thí sinh trúng tuyển
            for i, (name, avg) in enumerate(lst, 1):  # danh sách đánh số bắt đầu từ 1
                print(f"{i}. {name} {avg}")
        else:
            print("No candidates accepted")
        print()
    
    print("Unsuccessful candidates")
    if rejected:  # nếu có thí sinh bị loại
        rejected.sort(key=lambda x: -x[1])  # sắp xếp danh sách trượt theo điểm trung bình
        for i, (name, avg) in enumerate(rejected, 1):
            print(f"{i}. {name} {avg}")
    else:
        print("No unsuccessful candidates")


if __name__ == '__main__':
    filename = "exam.txt"
    m, quota, candidates = read_exam(filename)
    accepted, rejected = assign_candidates(m, quota, candidates)
    print_result(accepted, rejected)