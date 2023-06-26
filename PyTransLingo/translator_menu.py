import pyttsx3
from translate import Translator
from PyDictionary import PyDictionary
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

# Color codes for formatting
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
END = '\033[0m'


def check_internet_connection():
    try:
        requests.get('https://www.google.com', timeout=1)
        return True
    except requests.ConnectionError:
        return False


def translate_and_speak(source_lang, target_lang, text):

    try:
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translation = translator.translate(text)

        print(f"{GREEN}The search is now underway......{END}")
        print(f'{GREEN}Translated text: {translation}{END}')

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        engine.say(translation)
        engine.runAndWait()

        # Get the meaning of the entire translated text
        get_text_meaning(translation)

    except Exception as e:
        print(f'{RED}An error occurred during translation: {e}{END}')


def get_text_meaning(text):
    dictionary = PyDictionary()
    print('Meaning of the translated text:')
    meaning = dictionary.meaning(text)

    if meaning:
        for part_of_speech, definitions in meaning.items():
            print(f'{part_of_speech}:')
            for definition in definitions:
                print(f'- {definition}')
    else:
        print('No meaning found for the text.')


def search_google(find):
    url = f"https://www.google.com/search?q={find}"

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    mysearch = soup.find("div", class_="BNeawe").text
    print(mysearch)

    # Initialize the text-to-speech engine for search result
    engine = pyttsx3.init()
    engine.say(mysearch)
    engine.runAndWait()


def translator_menu():
    while True:
        print(f'{BLUE}╔══════════════════════════════════════════════════════════════════╗')
        print('║                           Welcome to My Pip                      ║')
        print('║                     My Name is S.Hari Prasath                    ║')
        print('║                     Pip name is PyTransLingo                     ║')
        print('║                     Version : 1.0.0                              ║')
        print('╚══════════════════════════════════════════════════════════════════╝')
        print(f'{BLUE}╔══════════════════════╗')
        print('║     Choose an option ║')
        print('║ 1. Google            ║')
        print('║ 2. Translator        ║')
        print('║ 3. Exit              ║')  # Add an option to exit the program
        print('╚══════════════════════╝')

        if not check_internet_connection():
            print(f"{RED}Please connect to the internet to use this program.{END}")
            break

        option = input("Enter your choice: ")

        if option == '1':
            search_text = input("Enter the text to search on Google: ")
            print(f"{BLUE}The search is now underway......{END}")
            search_google(search_text)
        elif option == '2':
            language_codes = [
                ['en', 'English', 'fr', 'French'],
                ['es', 'Spanish', 'de', 'German'],
                ['it', 'Italian', 'ta', 'Tamil'],
                ['ru', 'Russian', 'pt', 'Portuguese'],
                # Add more language codes and languages here
            ]
            headers = [' Language Code', ' Language', ' Language Code', ' Language']
            print(f'{BLUE}╔═════════════════════════════════════════════════════════════════════════════════════════╗')
            print(f'║                                  Language Codes                                         ║')
            print(f'╠═════════════════════════════════════════════════════════════════════════════════════════╣')
            print(tabulate(language_codes, headers=headers, tablefmt='grid'))
            source_lang = input('Enter your known language (code): ')
            target_lang = input('Enter the target language code: ')
            text = input('Enter the text to Translate: ')
            print(f"{GREEN}The Translate is now underway......{END}")
            translate_and_speak(source_lang, target_lang, text)
        elif option == '3':
            print('Exiting the program...')
            break  # Break out of the loop to exit the program
        else:
            print(f'{RED}Invalid option. Please try again.{END}')


if __name__ == '__main__':
    translator_menu()
