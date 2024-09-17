from bs4 import BeautifulSoup
from googletrans import Translator
import requests

def get_inglish_words():
    url = 'http://randomword.com/'
    try:
        translator = Translator()
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id ='random_word').text.strip()
        word_definision = soup.find('div', id ='random_word_definition').text.strip()
        return {
            "english_words": translator.translate(english_words, dest='ru').text,
            "word_definision": translator.translate(word_definision, dest='ru').text
        }
    except:
            print("Something went wrong")
def word_game():
    print('Добро пожаловать в игру')
    while True:
        word_dict = get_inglish_words()
        word = word_dict.get('english_words')
        word_definision = word_dict.get('word_definision')

        print(f'Значение слова - {word_dict.get("word_definision")}')
        user = input('Что это за слово? ')
        if user == word:
            print('Все верно')
        else:
            print(f'Ответ неверный, было загадано - {word}')
        play_again = input('Хотите сыграть еще раз? y/n ')
        if play_again != 'y':
            print('Спасибо за игру')
            break

word_game()












