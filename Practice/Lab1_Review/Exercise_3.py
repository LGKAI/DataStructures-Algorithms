def normalize(text):
    text = text.strip()

    clean_text = ""
    prev = ""
    for char in text:
        if char == " " and prev == " ":
            continue # nếu gặp khoảng trắng mà trước đó cũng là khoảng trắng thì bỏ qua vòng lặp này
        clean_text += char
        prev = char

    res = ""
    for i in range(len(clean_text)):
        if clean_text[i] in ".,!?" and i > 0 and clean_text[i - 1] == " ":
            res = res[:-1] # xoá khoảng trắng trước dấu câu
        res += clean_text[i]
        if clean_text[i] in ".,!?" and i < len(clean_text) - 1 and clean_text[i + 1] != " ":
            res += " " # thêm 1 khoảng trắng sau dấu câu

    return res

def count_word(text):
    if not text:
        return 0
    words = normalize(text).split()
    words = [word.strip(".,!?") for word in words]
    # print(words) # kiểm tra duyệt word đúng chưa
    return len(words)

def find_longest_word(text):
    words = text.split()
    long_word = ""
    for word in words:
        if len(word) > len(long_word):
            long_word = word
    return long_word


if __name__ == '__main__':
    text = input("Enter text: ")
    print("Normalized paragraph:", normalize(text), sep = "\n")
    print("Word count:", count_word(text))
    print("Longest word:", find_longest_word(text))
