import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
kivy.require('1.0.7')


class KivyApp(App):
    def build(self):
        self.russian_nouns = [word[0:-1] for word in open('russian_nouns.txt', encoding='UTF-8').readlines()]
        self.box = BoxLayout(orientation='vertical')
        self.letters_line = TextInput(hint_text='Letters...')
        self.word_line = TextInput(hint_text='Word...')
        self.start_button = Button(background_color='green', text='Start', on_press=self.WOWgen)
        self.result_label = Label()

        self.box.add_widget(self.letters_line)
        self.box.add_widget(self.word_line)
        self.box.add_widget(self.start_button)
        self.box.add_widget(self.result_label)
        return self.box


    def is_suitable_variation(self, variant, word_letts, main_letts):
        letter_index = 0
        for word_letter in word_letts:
            # Проверка, что буквы из введённого слова есть в проверяемом
            if variant[letter_index] in main_letts:

                if word_letter != '#':
                    # Проверка букв из проверяемого слова на соответствие с введёнными
                    if variant[letter_index] != word_letter:
                        return False
                    letter_index += 1

                else:
                    letter_index += 1
            else:
                return False

        for letter in variant:
            if variant.count(letter) > main_letts.count(letter):
                return False

        return True

    def WOWgen(self, *args):
        # Разбор слов
        variations = [russian_noun for russian_noun in self.russian_nouns if len(russian_noun) == len(self.word_line.text)]

        result = list()
        for variation in variations:
            if self.is_suitable_variation(variation, self.word_line.text.lower(), self.letters_line.text.lower()):
                result.append(variation)
        self.result_label.text = str(result)





if __name__ == '__main__':
    KivyApp().run()
