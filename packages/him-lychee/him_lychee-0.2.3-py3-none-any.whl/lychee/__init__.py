import re
import string
import warnings
from typing import Union, Dict, Any, List

# --- External Libraries (Soft Imports for Compatibility) ---

try:
    from textblob import TextBlob
except ImportError:
    # If not found, set a placeholder and warn
    warnings.warn("TextBlob not found. Spelling correction will not work.")
    TextBlob = None

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize, sent_tokenize
except ImportError:
    warnings.warn("NLTK not found. Stopword removal, tokenization, stemming, and lemmatization will not work.")
    nltk = None

try:
    import emoji
except ImportError:
    warnings.warn("Emoji library not found. Emoji functions will not work.")
    emoji = None

try:
    import spacy
    # Load the small model once on class initialization
    try:
        NLP_MODEL = spacy.load("en_core_web_sm")
    except OSError:
        warnings.warn("SpaCy 'en_core_web_sm' model not found. Run 'python -m spacy download en_core_web_sm'.")
        NLP_MODEL = None
except ImportError:
    warnings.warn("SpaCy not found. SpaCy tokenization will not work.")
    NLP_MODEL = None

# --- Core Data (Slang Dictionary) ---

# Dictionary contains all slang terms in lowercase
SLANG_MAP: Dict[str, str] = {
    # A
    'abt': 'About', 'abt2': 'About to', 'acc': 'Actually', 'add': 'Address', 'afaik': 'As far as I know', 
    'afk': 'Away from keyboard', 'aka': 'Also known as', 'asap': 'As soon as possible', 'asf': 'As f***', 
    'asl': 'Age, sex, location', 'atm': 'At the moment',
    # B
    'b': 'Bisexual / Babe', 'b4': 'Before', 'based': 'Used when agreeing with something; or recognising someone is being themselves', 
    'bc': 'Because', 'bet': 'yes, okay; affirming something', 'bday': 'Birthday', 'blates': 'Obviously', 
    'bf': 'Boyfriend/Best friend', 'bf4l': 'Best friends for life', 'bffl': 'Best friends for life', 
    'bff': 'Best friends forever', 'bop': 'Derogatory term for someone who has multiple sexual partners. Usually used against women. Sometimes used as ‘lala bop’ or ‘school bop’', 
    'boyf': 'Boyfriend', 'brat': 'A strong-willed person who goes against expectations.', 'brb': 'Be right back', 
    'btw': 'By the way',
    # C
    'cap': 'Lie (often used as ‘no cap’, meaning no lie)', 'cba': 'Can’t be bothered', 'cmb': 'Call me back', 
    'cmon': 'Come on', 'ctn': 'Can’t talk now', 'cu': 'See you', 'cua': 'See you around', 
    'cul': 'See you later', 'cya': 'See ya',
    # D
    'da f': 'What the f***?', 'dafuq?': 'What the f***?', 'diss': 'Disrespect', 'dkdc': 'Don’t know, don’t care', 
    'dl': 'Download', 'dm': 'Direct Message, a form of private messaging', 'dnt': 'Don’t',
    # E
    'ema': 'Email address', 'eta': 'Estimated time of arrival', 'ez': 'Easy',
    # F
    'f': 'Female', 'fam': 'Short for ‘family’, similar to ‘bro’', 'faq': 'Frequently Asked Questions', 'fb': 'Facebook', 
    'finna': 'I’m going to', 'fire': 'A word to describe something positive', 'fr': 'for real', 
    'fuq': 'F***', 'fuqn': 'F***ing', 'fwb': 'Friends with benefits', 'fwd': 'Forward', 
    'fyi': 'For your information',
    # G
    'g': 'Gay', 'g2cu': 'Good to see you', 'g2g': 'Got to go', 'g2r': 'Got to run', 'gamer': 'Video game player', 
    'gf': 'Girlfriend', 'gg': 'Good game', 'gj': 'Good job', 'gl': 'Good luck', 
    'glhf': 'Good luck have fun', 'goat': 'greatest of all time', 'gnite': 'Good night', 'gr8': 'Great', 
    'gratz': 'Congratulations', 'gtfoh': 'Get the f*** outta here', 'gtg': 'Got to go', 'gud': 'Good', 
    'gyat': 'God d***; exclamation of excitement',
    # H
    'h8': 'Hate', 'hella': 'Really', 'hits different': 'Something that affects you in a particular way', 
    'hv': 'Have', 'hw': 'Homework', 'hbd': 'Happy Birthday',
    # I
    'ib': 'I’m back', 'ic': 'I see', 'idc': 'I don’t care', 'idk': 'I don’t know', 'ig': 'I guess or Instagram', 
    'iirc': 'If I remember correctly', 'ik': 'I know', 'ikr': 'I know right?', 'ilu': 'I love you', 
    'ily': 'I love you', 'im': 'Instant message', 'imho': 'In my humble opinion', 'imo': 'In my opinion', 
    'insta': 'Instagram', 'irl': 'In real life', 'it’s giving…': 'Used to describe something', 
    'iykyk': 'If you know, you know; often used to describe inside jokes',
    # J
    'jk': 'Just kidding',
    # K
    'k': 'Okay', 'kewl': 'Cool', 'kthnx': 'OK, thanks',
    # L
    'l': 'Lesbian', '(take the) l': 'Loss', 'l8': 'Late', 'l8r': 'Later', 'let them cook': 'A supportive phrase', 
    'lit': 'It describes something as positive', 'lmao': 'Laughing my a** off', 'lol': 'Laugh out loud', 
    'lolll': 'Laugh out loud a lot', 'luv ya': 'Love you',
    # M
    'm': 'Male', 'm.i.r.l': 'Meet in real life', 'mkay': 'Mmm, okay', 'mmo': 'Massively multiplayer online', 
    'mmorpg': 'Massively multiplayer online role-playing game', 'msg': 'Message', 'mwah': 'To give a kiss',
    # N
    'n/a': 'Not available or not applicable', 'n2m': 'Nothing too much', 'nbd': 'No big deal', 'ne': 'Any', 
    'ne1': 'Anyone', 'nm': 'Not much / Nothing much / Never mind', 'no cap': 'No lie', 
    'noob': 'Short for ‘newbie’', 'np': 'No problem', 'nthng': 'Nothing', 'nvr': 'Never', 'nw': 'No worries',
    # O
    'oic': 'Oh, I see', 'om': 'Oh my', 'omg': 'Oh my God', 'omw': 'On my way', 'onl': 'Online', 'ot': 'Off topic', 
    'ova': 'Over',
    # P
    'peak': 'Unfortunate', 'peeps': 'People', 'pic': 'Picture', 'pir': 'Parent in room', 'pk': 'Player kill', 
    'pls': 'Please', 'plz': 'Please', 'pm': 'Private Message', 'pmsl': 'Peeing myself laughing', 'pov': 'Point of view', 
    'ppl': 'People', 'prolly': 'Probably', 'pwn': 'Own, as in conquer or defeat', 'pwned': 'Owned, as in conquered or defeated',
    # Q
    'qt': 'Cutie', 'qtpi': 'Cutie pie',
    # R
    'r': 'Are or our', 'riz': 'Charisma', 'rizz': 'Charisma', 'rizzler': 'Someone who is good at flirting', 
    'rly': 'Really', 'rofl': 'Rolling on the floor laughing', 'rpg': 'Role playing game', 'ru': 'Are you?', 
    'ruok': 'Are you okay?',
    # S
    'sec': 'Second', 'seggs': 'Sex', 'ship': 'Relationship', 'simp': 'someone who does too much for their crush', 
    'simping': 'someone who does too much for their crush', 'skibidi': 'A reference to a video about an army of toilets taking over the world', 
    'skl': 'School', 'sksksk': 'Representing laughter', 'slaps': 'Describing something as good', 
    'smh': 'Shaking my head', 'sms': 'Short Message Service', 'so': 'Significant other', 'sob': 'Son of a B*tch', 
    'sos': 'Help', 'spk': 'Speak', 'srs': 'Serious', 'srsbsns': 'Serious business', 'srsly': 'Seriously', 
    'sry': 'Sorry', 'stan': 'being a fan of someone', 'str8': 'Straight', 'sup': 'What’s up', 
    'sus': 'Suspicious', 'sux': 'Sucks or “it sucks”', 'swag': 'Boasting about one’s skills or style',
    # T
    'tbh': 'To be honest', 'tc': 'Take care', 'tea': 'gossip', 'tgif': 'Thank God it’s Friday', 
    'thanq': 'Thank you', 'thx': 'Thanks', 'tmi': 'Too much information', 'trans': 'Transsexual', 
    't*': 'Transsexual', 't+': 'Transsexual', 'ttfn': 'Ta-ta for now', 'ttyl': 'Talk to you later', 
    'tweet': 'Twitter post', 'txt': 'Text', 'ty': 'Thank you',
    # U
    'u': 'You', 'u2': 'You too', 'ul': 'Upload', 'unalive': 'Kill', 'ur': 'Your or you’re',
    # V
    'vm': 'Voicemail',
    # W
    'w': 'win', 'w@': 'What?', 'w/': 'With', 'w/e': 'Whatever or weekend', 'w/o': 'Without', 'w8': 'Wait', 
    'wag1': 'What’s up', 'wbu': 'What about you?', 'wk': 'Week', 'wrk': 'Work', 'wtf': 'What the f***', 
    'wtg': 'Way to go', 'wyd': 'What (are) you doing?', 'wysiwyg': 'What you see is what you get',
    # X
    'x': 'kiss (or the platform formally called Twitter)',
    # Y
    'y?': 'Why?', 'yeet': 'To throw something', 'yktv': 'You know the vibe', 'yolo': 'You only live once', 
    'yr': 'Your', 'yt': 'white (or YouTube)', 'yw': 'You’re welcome',
    # Z
    '(gen) z': 'People born from around 1997-2012', 'za': 'Pizza',
    # #
    '2': 'To', '24/7': 'Twenty-four hours a day, seven days a week',
}

# --- Lychee Core Class ---

class SlangDictionary:
    """
    The core dictionary for common internet and text slang.
    Provides lookup and highly optimized text replacement features.
    """
    def __init__(self):
        self.slang_map = SLANG_MAP

        # 1. Create a Reverse Map for meaning lookup
        self._reverse_map = self._create_reverse_map()

        # 2. Create the fast regex pattern for text replacement
        self._replacement_pattern = self._create_replacement_pattern()

    def _create_reverse_map(self) -> Dict[str, List[str]]:
        """Internal function to build the reverse map for reverse_lookup."""
        reverse_map: Dict[str, List[str]] = {}
        for slang, meaning in self.slang_map.items():
            if meaning not in reverse_map:
                reverse_map[meaning] = []
            reverse_map[meaning].append(slang)
        return reverse_map

    def _create_replacement_pattern(self) -> re.Pattern:
        """Internal function to build a single, highly optimized regex pattern."""
        # Sort terms by length (longest first) to avoid replacing 'lol' inside 'lolll' incorrectly
        sorted_slang = sorted(self.slang_map.keys(), key=len, reverse=True)
        # Create a non-capturing group pattern (?:term1|term2|...)
        pattern_str = r'\b(?:' + '|'.join(re.escape(term) for term in sorted_slang) + r')\b'
        # Compile with IGNORECASE flag for case-insensitive replacement
        return re.compile(pattern_str, re.IGNORECASE)

    def get_meaning(self, slang_term: str) -> str:
        """
        Looks up the meaning of a given slang term (case-insensitive).

        :param slang_term: The slang term (e.g., 'lol', 'tbh').
        :return: The meaning of the term or a not-found message.
        """
        return self.slang_map.get(slang_term.lower(), f"Slang term '{slang_term}' not found.")

    def reverse_lookup(self, meaning: str) -> Dict[str, List[str]]:
        """
        Looks up all slang terms that match a given meaning.

        :param meaning: The full meaning to search for (e.g., 'Best friends for life').
        :return: Dictionary with the meaning and a list of matching slang terms.
        """
        if meaning in self._reverse_map:
            return {meaning: self._reverse_map[meaning]}
        return {meaning: ["No matching slang terms found."]}

    def search_slang(self, keyword: str) -> Dict[str, str]:
        """
        Finds all slang terms whose meaning contains the given keyword (case-insensitive).

        :param keyword: The keyword to search within the meanings.
        :return: Dictionary of matching slang terms and their meanings.
        """
        keyword_lower = keyword.lower()
        results = {}
        for slang, meaning in self.slang_map.items():
            if keyword_lower in meaning.lower():
                results[slang] = meaning
        return results

    def replace_slang_in_text(self, text: Union[str, Any]) -> Union[str, Any]:
        """
        [Optimized for Speed] Replaces all recognized slang terms in a single
        string with their full, original meaning. The replacement is case-insensitive.

        NOTE: When cleaning a Pandas DataFrame column (e.g., df['review']),
        you must use the .apply() method:
        df['review'] = df['review'].apply(slang_core.replace_slang_in_text)

        :param text: A single string to process.
        :return: The processed string with slang replaced.
        """
        # We need to import pandas locally only to check for Series/Index types gracefully
        try:
            import pandas as pd
        except ImportError:
            pd = None

        if pd and isinstance(text, (pd.Series, pd.Index, list, dict)):
            # Explicitly block list/Series input to avoid ambiguity error
            raise TypeError(
                "Input must be a single string. For lists/Pandas Series, use the .apply() method (e.g., df['col'].apply(function))."
            )
        
        if not isinstance(text, str):
            # Allows for processing of non-string data (e.g., NaN which pandas converts to float)
            return text 

        if not text:
            return text
        
        # Define the replacement function for re.sub()
        def replacer(match):
            # The match group is the found slang term (e.g., 'OMG', 'brb').
            slang = match.group(0).lower()
            return self.slang_map.get(slang, match.group(0))

        # Use the pre-compiled pattern for fast, single-pass replacement
        return self._replacement_pattern.sub(replacer, text)


# --- Text Cleaning Class (for NLP Prep) ---

class TextCleaner:
    """
    A utility class providing a powerful suite of text cleaning and preprocessing
    functions required for tasks like Sentiment Analysis and NLP modeling.
    """
    def __init__(self):
        # Initialize NLTK resources and other tools
        try:
            if nltk:
                # Use download only if resources are not present, suppresses unnecessary downloads
                try:
                    nltk.data.find('corpora/stopwords')
                except nltk.downloader.DownloadError:
                    nltk.download('stopwords', quiet=True)
                try:
                    nltk.data.find('tokenizers/punkt')
                except nltk.downloader.DownloadError:
                    nltk.download('punkt', quiet=True)
                try:
                    nltk.data.find('corpora/wordnet')
                except nltk.downloader.DownloadError:
                    nltk.download('wordnet', quiet=True)
            
                self.stopwords_set = set(stopwords.words('english'))
                self.stemmer = PorterStemmer()
                self.lemmatizer = WordNetLemmatizer()
            else:
                self.stopwords_set = set()
                self.stemmer = None
                self.lemmatizer = None
        except Exception:
            self.stopwords_set = set()
            self.stemmer = None
            self.lemmatizer = None
            warnings.warn("NLTK resource initialization failed. Stopword/Stem/Lemma functions disabled.")

        self.nlp_model = NLP_MODEL
        # Optimized punctuation removal table
        self.exclude_punctuation = str.maketrans('', '', string.punctuation)

    def _handle_non_string(self, text: Any) -> Any:
        """Helper to handle non-string inputs gracefully."""
        # Gracefully handle Pandas NaN check if Pandas is available
        if not isinstance(text, str):
            try:
                import pandas as pd
                if pd.isna(text):
                    return text
            except ImportError:
                pass
            
            # Warn only for unexpected types that aren't typical Pandas nulls
            if text is not None:
                warnings.warn(f"Function received non-string input of type {type(text)}. Returning input unchanged.")
            return text
        return text

    def remove_html_tags(self, text: str) -> str:
        """Removes HTML tags (e.g., <b>, <br/>) using a regular expression."""
        text = self._handle_non_string(text)
        if text:
            clean = re.compile('<.*?>')
            return re.sub(clean, '', text)
        return text

    def remove_urls(self, text: str) -> str:
        """Removes any type of URL (http/https, www) from the text."""
        text = self._handle_non_string(text)
        if text:
            url_pattern = re.compile(r'https?://\S+|www\.\S+')
            return url_pattern.sub('', text)
        return text

    def remove_punctuation(self, text: str) -> str:
        """Removes all standard punctuation marks."""
        text = self._handle_non_string(text)
        if text:
            return text.translate(self.exclude_punctuation)
        return text

    def spelling_correction(self, text: str) -> str:
        """Corrects spelling mistakes using TextBlob. Note: This can be slow."""
        if not TextBlob:
            warnings.warn("TextBlob is not installed. Returning original text.")
            return text
        try:
            return str(TextBlob(text).correct())
        except Exception as e:
            warnings.warn(f"TextBlob correction failed: {e}. Returning original text.")
            return text

    def remove_stopwords(self, text: str, language: str = 'english') -> str:
        """Removes common stop words (e.g., 'the', 'a', 'is') using NLTK."""
        if not self.stopwords_set:
            warnings.warn("NLTK Stopwords not initialized. Returning original text.")
            return text
        
        text = self._handle_non_string(text)
        if text:
            # Using set lookup for speed
            words = [word for word in text.split() if word.lower() not in self.stopwords_set]
            return " ".join(words)
        return text

    def clean_emojis(self, text: str, mode: str = 'replace') -> str:
        """
        Processes emojis.
        mode='remove': removes emojis completely.
        mode='replace': replaces emojis with their text description (:thumbs_up:).
        """
        text = self._handle_non_string(text)
        if not text:
            return text
        
        if mode == 'replace':
            if not emoji:
                warnings.warn("Emoji library not installed. Falling back to 'remove' mode.")
                mode = 'remove'
            else:
                return emoji.demojize(text)

        if mode == 'remove':
            # Pattern to match and remove common Unicode emoji blocks
            emoji_pattern = re.compile(
                "["
                "\U0001F600-\U0001F64F"  # emoticons
                "\U0001F300-\U0001F5FF"  # symbols & pictographs
                "\U0001F680-\U0001F6FF"  # transport & map symbols
                "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                "\U00002702-\U000027B0"
                "\U000024C2-\U0001F251"
                "]+",
                flags=re.UNICODE,
            )
            return emoji_pattern.sub(r'', text)
        
        return text

    def tokenize(self, text: str, library: str = 'nltk') -> List[str]:
        """
        Tokenizes text into words or sentences using NLTK or SpaCy.

        :param text: The text string to tokenize.
        :param library: 'nltk' (default) or 'spacy'.
        :return: List of word tokens.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string.")
        
        if library == 'nltk':
            try:
                return word_tokenize(text)
            except NameError:
                raise ImportError("NLTK not properly installed/configured for word tokenization.")
        
        elif library == 'spacy':
            if self.nlp_model:
                doc = self.nlp_model(text)
                return [token.text for token in doc]
            else:
                raise ImportError("SpaCy model not loaded. Please ensure SpaCy is installed and 'en_core_web_sm' is downloaded.")
        
        else:
            raise ValueError("Invalid library specified. Choose 'nltk' or 'spacy'.")

    def stem_words(self, text: str) -> str:
        """Reduces words to their root form (e.g., 'running' -> 'run')."""
        if not self.stemmer:
            warnings.warn("NLTK Stemmer not initialized. Returning original text.")
            return text
        
        text = self._handle_non_string(text)
        if text:
            # Tokenize first for clean stemming
            try:
                words = word_tokenize(text)
                stemmed_words = [self.stemmer.stem(word) for word in words]
                return " ".join(stemmed_words)
            except Exception:
                 return text
        return text

    def lemmatize_text(self, text: str) -> str:
        """Reduces words to their dictionary form (e.g., 'better' -> 'good')."""
        if not self.lemmatizer:
            warnings.warn("NLTK Lemmatizer not initialized. Returning original text.")
            return text
        
        text = self._handle_non_string(text)
        if text:
            # Tokenize first for clean lemmatization
            try:
                words = word_tokenize(text)
                lemmatized_words = [self.lemmatizer.lemmatize(word) for word in words]
                return " ".join(lemmatized_words)
            except Exception:
                return text
        return text

# --- Main function for direct file execution (Testing) ---

if __name__ == "__main__":
    # Note: Requires Pandas to be imported, but we don't include it in the source to avoid dependency
    # For testing, you must have all dependencies installed:
    # pip install textblob emoji spacy nltk pandas
    
    # Initialize the core components
    slang_finder = SlangDictionary()
    cleaner = TextCleaner()

    print("--- Him-Lychee v0.2.1 Core Testing ---")
    
    # --- 1. Slang Replacement and Dictionary Demo ---
    print("\n--- 1. Slang Replacement (Optimized) ---")
    input_text = "TBH, the GOAT's new track slaps! I'm AFK now, BRB. LOL! No cap."
    print(f"Original: {input_text}")
    
    cleaned_slang = slang_finder.replace_slang_in_text(input_text)
    print(f"Cleaned:  {cleaned_slang}")
    
    # --- 2. TextCleaner NLP Pipeline Demo ---
    print("\n--- 2. TextCleaner Full Pipeline Demo ---")
    
    nlp_text = "I havv runing to the store! It was great. Check out my site: https://test.com/new. We bought cats and mice. 🤩"
    print(f"Original Text: {nlp_text}")
    
    # Step 1: Remove URL and HTML (clean formatting)
    text_clean = cleaner.remove_urls(nlp_text)
    
    # Step 2: Fix spelling
    text_clean = cleaner.spelling_correction(text_clean)
    
    # Step 3: Remove Punctuation and Emojis (clean noise)
    text_clean = cleaner.remove_punctuation(text_clean)
    text_clean = cleaner.clean_emojis(text_clean, mode='remove')
    
    # Step 4: Stopwords and Tokenization (linguistic reduction)
    text_clean = cleaner.remove_stopwords(text_clean)
    
    # Step 5: Lemmatization (standardize words)
    text_clean = cleaner.lemmatize_text(text_clean)
    
    tokens = cleaner.tokenize(text_clean, library='nltk')

    print(f"Final Cleaned Text: {text_clean}")
    print(f"Final Tokens: {tokens}")
    
    # --- 3. Robustness Check (Should raise TypeError) ---
    print("\n--- 3. Robustness Check (Series Input) ---")
    try:
        # Pass a list which simulates a Pandas Series
        slang_finder.replace_slang_in_text(['brb', 'lol'])
    except TypeError as e:
        print(f"SUCCESS: Robustness check caught the error: {e}")
