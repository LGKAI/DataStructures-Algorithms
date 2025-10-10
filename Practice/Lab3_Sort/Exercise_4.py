import datetime

def correct_birth_year(birth_year):
    cur_year = datetime.datetime.now().year
    birth_year = str(birth_year)

    # Nếu năm sinh đã có 4 chữ số thì giữ nguyên
    if len(birth_year) == 4: 
        return int(birth_year)

    # Nếu năm sinh có hơn 4 chữ số, lấy 2 số cuối
    if len(birth_year) > 4: 
        birth_year = int(birth_year[-2:])
        if birth_year > (cur_year % 100):
            birth_year += 1900
        else:
            birth_year += 2000

    return birth_year

def calculate_age(birth_year):
    cur_year = datetime.datetime.now().year
    return cur_year - birth_year

def read_write_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    employees = []
    for line in lines:
        parts = line.strip().split()
        employees_id = parts[0]
        name = parts[1]
        birth_year = parts[2]

        fixed_birth_year = correct_birth_year(birth_year)
        age = calculate_age(fixed_birth_year)

        employees.append((employees_id, name, fixed_birth_year, age))

    # Sắp xếp theo tuổi giảm dần, nếu tuổi bằng nhau thì sắp xếp theo tên
    employees.sort(key=lambda x: (-x[3], x[1]))

    with open('sorted_employees.txt', 'w') as file:
        for employee in employees:
            file.write(f"{employee[0]} {employee[1]} {employee[2]}\n")


if __name__ == '__main__':
    filename = 'employees.txt'
    read_write_file(filename)