def replace_words(text, replacements):
    for word, replacement in replacements.items():
        text = text.replace(word, replacement)
    return text

def main():
    file_path = 'input.txt'

    with open(file_path, 'r') as file:
        text = file.read()

    replacements = {
        'ADJECTIVE': '',
        'NOUN': '',
        'ADVERB': '',
        'VERB': ''
    }

    for word in replacements.keys():
        replacement = input(f'Enter an {word.lower()}: ')
        replacements[word] = replacement

    replaced_text = replace_words(text, replacements)

    print(replaced_text)

    with open('output.txt', 'w') as file:
        file.write(replaced_text)

if __name__ == "__main__":
    main()

