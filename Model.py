from textblob import TextBlob
import language_tool_python


class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_tool = language_tool_python.LanguageTool('en-US')

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_tool.check(text)

        corrected_text = language_tool_python.utils.correct(text, matches)
        foundmistakes_count = len(matches)
        return corrected_text, foundmistakes_count


if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello world. I like mashine learning. appple. bananana"
    print("Corrected Spelling: ", obj.correct_spell(message))
    corrected_text, mistakes_count = obj.correct_grammar(message)
    print(f"Corrected Grammar: {corrected_text}")
    print(f"Mistakes Found: {mistakes_count}")
