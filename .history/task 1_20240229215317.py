import nltk
from nltk.corpus import words
from nltk.metrics import edit_distance

nltk.download('words')

class AutoCorrect:
    def __init__(self):
        self.vocabulary = set(words.words())

    def correct_phrase(self, phrase):
        mots = phrase.split()
        mots_corriges = [self.correct_word(mot) for mot in mots]
        return ' '.join(mots_corriges)

    def correct_word(self, word):
        if word.lower() in self.vocabulary:
            return word  # Le mot est correct, pas besoin de correction

        suggestions = self.get_suggestions(word)
        if suggestions:
            return min(suggestions, key=lambda x: edit_distance(word, x))

        return word  # Si aucune suggestion n'est trouvée, retourner le mot d'origine

    def get_suggestions(self, word):
        return [w for w in self.vocabulary if edit_distance(word, w) < 3]

# Exemple d'utilisation
auto_corrector = AutoCorrect()

while True:
    user_input = input("Entrez une phrase (ou 'exit' pour quitter) : ")
    if user_input.lower() == 'exit':
        break

    corrected_phrase = auto_corrector.correct_phrase(user_input)
    print(f"Correction : {corrected_phrase}")
