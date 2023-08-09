import sys
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer

def lemmatize_to_tab_separated(input_word, pos=None):
    lemmatizer = FrenchLefffLemmatizer()
    if pos is None:
        lemma = lemmatizer.lemmatize(input_word)
        return f"{input_word}\t{lemma}"
    elif pos == 'all':
        lemmas = lemmatizer.lemmatize(input_word, 'all')
        return '\n'.join([f"{input_word}\t{lemma}" for lemma, _ in lemmas])
    else:
        lemma = lemmatizer.lemmatize(input_word, pos)
        return f"{input_word}\t{lemma}"

def lemmatize_file(input_file_path, output_file_path, pos=None):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        input_words = input_file.read().splitlines()

    lemmatized_lines = [lemmatize_to_tab_separated(word, pos) for word in input_words]

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(lemmatized_lines))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python lemmatize_script.py input_file.txt output_file.txt [pos]")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    pos = None
    if len(sys.argv) >= 4:
        pos = sys.argv[3]

    lemmatize_file(input_file_path, output_file_path, pos)
    print(f"Lemmatized file saved as {output_file_path}")
