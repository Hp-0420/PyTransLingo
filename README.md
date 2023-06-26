# PyTransLingo

PyTransLingo is a Python package that provides translation and search functionality using various APIs. It allows you to translate text between different languages and search for information on Google.

## Installation

To install PyTransLingo, use the following command:

pip install PyTransLingo

## Dependencies

PyTransLingo requires the following dependencies, which can be installed using pip:

pip install pyttsx3 translate PyDictionary requests bs4 tabulate

## Usage

Import the necessary modules:

```python
import pyttsx3
from translate import Translator
from PyDictionary import PyDictionary
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
```

Use the `translator_menu()` function to interact with the translation and search functionalities:

```python
translator_menu()
```

Examples:

1. Translating text:

```python
source_lang = 'en'
target_lang = 'fr'
text = 'Hello, how are you?'
translate_and_speak(source_lang, target_lang, text)
```

2. Searching on Google:

```python
search_text = 'Python programming
search_google(search_text)
```

## Contributing

Contributions to PyTransLingo are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.

### Setting up a virtual environment

If you prefer to work in a virtual environment, follow these steps:

1. In the command prompt or terminal, navigate to the project directory.

2. Run the following command to create a virtual environment named "myenv" and activate it:

For Unix/macOS/Linux:

```
python3 -m venv myenv
source myenv/bin/activate
```

For Windows:

```
python3 -m venv myenv
myenv\Scripts\activate.bat
```

This will create a virtual environment and activate it, allowing you to work within an isolated Python environment.

Note: Make sure you have Python 3.x installed before creating the virtual environment.
```
```

You can copy the entire content above and paste it into your GitHub README file.
