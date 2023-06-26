from setuptools import setup, find_packages

setup(
    name='PyTransLingo',
    version='1.0.0',
    author='Hari Prasath .S',
    author_email='harishreehp80@gmail.com',
    license='MIT',
    description='PyTransLingo is a command-line translation and text-to-speech tool. Translate text between languages, get the meaning of translated text, perform Google searches, and listen to search results using text-to-speech.Run "PyTransLingo" in the terminal or command prompt to use the pip. ',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'PyTransLingo = PyTransLingo.translator_menu:translator_menu',
        ],
    },
    install_requires=[
        'pyttsx3',
        'translate',
        'PyDictionary',
        'requests',
        'beautifulsoup4',
        'tabulate',
    ],

)