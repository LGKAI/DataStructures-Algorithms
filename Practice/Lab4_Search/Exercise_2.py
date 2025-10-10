import sys

def read_dict(path):
    dictionary = {}
    with open(path, 'r') as file:
        for line in file:
            if ':' in line:
                word, definition = line.strip().split(':', 1)
                dictionary[word.lower()] = definition.strip()
    return dictionary

def define_words(path):
    if len(sys.argv) < 3:
        print("Usage: python Exercise_2.py word1 word2 ... output.txt")
        return

    *words, output = sys.argv[1:]
    dictionary = read_dict(path)

    with open(output, 'w') as file:
        for word in words:
            definition = dictionary.get(word.lower(), "Definition not found")
            file.write(f"{word}: {definition}\n")


if __name__ == '__main__':
    path = 'English-Vietnamese Dictionary.txt'
    define_words(path)
