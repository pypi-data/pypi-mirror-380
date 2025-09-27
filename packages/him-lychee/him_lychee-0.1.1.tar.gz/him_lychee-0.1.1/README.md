Lychee: Language Core
Lychee is a lightweight Python package designed to quickly look up the meanings of common internet abbreviations, text slang, and acronyms in a case-insensitive manner. It is the core utility for cleaning and analyzing user-generated text.

Installation
pip install lychee

Lychee Core Features (SlangDictionary Class)
The core SlangDictionary class provides robust lookups and replacement functionality:

Method

Description

Example

replace_slang_in_text()

Crucial for Data Cleaning. Replaces all recognized slang terms in a string with their full meanings.

slang.replace_slang_in_text(text)

get_meaning()

Finds the meaning of a given slang term (case-insensitive).

slang.get_meaning('BRB')

reverse_lookup()

Finds slang terms based on a keyword in the meaning.

slang.reverse_lookup('laugh')

search_slang()

Searches terms or meanings containing a specific keyword.

slang.search_slang('friend')

Quick Start: Slang Replacement
You can easily apply this function to a single string or a pandas Series/Column.

from lychee import SlangDictionary

# Initialize the Lychee Core Slang Dictionary
slang_lookup = SlangDictionary()

input_text = "TBH, the new game slaps! I'm AFK now, BRB. No cap, it was fire."

# Clean the text using the replacement function
cleaned_text = slang_lookup.replace_slang_in_text(input_text) 

print(cleaned_text)
# Output: To be honest, the new game Describing something as good (e.g. This song slaps)! I'm Away from keyboard now, Be right back. No lie, it was A word to describe something positive (e.g. That game is fire).

Upcoming Text Processing Utilities (Future Release)
The TextCleaner class is a structural placeholder for future feature development, including:

to_lowercase()

remove_html_tags()

remove_urls()

remove_punctuation()

Contributing
We welcome contributions! Feel free to fork the repository on GitHub and submit a pull request.