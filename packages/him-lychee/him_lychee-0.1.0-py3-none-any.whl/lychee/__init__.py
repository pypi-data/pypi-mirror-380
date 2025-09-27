"""
lychee: Lychee Language Core
Author: Himpadma "Him"
A comprehensive dictionary library for looking up internet and text slang.
Includes dictionary lookup and a function to replace slang with full meanings.
"""
import json
import re

class SlangDictionary:
    """
    Holds the complete mapping of slang terms to their meanings, and provides 
    utility functions for lookup and replacement.
    This class is the core of the Lychee Language capabilities.
    """
    def __init__(self):
        # The main dictionary mapping slang to its meaning (Slang -> Meaning)
        self.slang_map = {
            # A
            'abt': 'About', 'abt2': 'About to', 'acc': 'Actually', 'add': 'Address',
            'afaic': 'As far as I’m concerned', 'afaik': 'As far as I know', 
            'afk': 'Away from keyboard', 'aka': 'Also known as', 'ama': 'Ask me anything',
            'asap': 'As soon as possible', 'asf': 'As f***', 'asl': 'Age, sex, location',
            'atm': 'At the moment',
            # B
            'b': 'Bisexual / Babe', 'b4': 'Before',
            'based': 'Used when agreeing with something; or recognising someone is being themselves',
            'bc': 'Because', 'bet': 'Yes, okay; affirming something', 'bday': 'Birthday',
            'blates': 'Obviously', 'bf': 'Boyfriend/Best friend', 'bf4l': 'Best friends for life',
            'bffl': 'Best friends for life', 'bff': 'Best friends forever',
            'bop': 'Derogatory term for someone who has multiple sexual partners.',
            'boyf': 'Boyfriend', 'brat': 'A strong-willed person who goes against expectations.',
            'brb': 'Be right back', 'btw': 'By the way', 'bussin': 'Really good; delicious',
            # C
            'cap': 'Lie (often used as ‘no cap’, meaning no lie)', 'cba': 'Can’t be bothered',
            'cheugy': 'Tacky, unstylish, trying too hard', 'cmb': 'Call me back', 'cmon': 'Come on', 
            'cringe': 'Embarrassing, awkward', 'ctn': 'Can’t talk now', 'cu': 'See you',
            'cua': 'See you around', 'cul': 'See you later', 'cya': 'See ya',
            # D
            'da f': 'What the f***?', 'dafuq?': 'What the f***?', 'deets': 'Details', 'diss': 'Disrespect',
            'dkdc': 'Don’t know, don’t care', 'dl': 'Download',
            'dm': 'Direct Message, a form of private messaging', 'dm me': 'Direct Message me',
            'dnt': 'Don’t', 'dtf': 'Down to f***',
            # E
            'ema': 'Email address', 'eta': 'Estimated time of arrival', 'ez': 'Easy',
            # F
            'f': 'Female', 'fam': 'Short for ‘family’, similar to ‘bro’',
            'faq': 'Frequently Asked Questions', 'fb': 'Facebook', 'finna': 'I’m going to',
            'fire': 'A word to describe something positive (e.g. That game is fire)',
            'fr': 'For real', 'ftw': 'For the win', 'fuq': 'F***', 'fuqn': 'F***ing',
            'fwb': 'Friends with benefits', 'fwd': 'Forward', 'fyi': 'For your information',
            # G
            'g': 'Gay', 'g2cu': 'Good to see you', 'g2g': 'Got to go', 'g2r': 'Got to run',
            'gamer': 'Video game player', 'gf': 'Girlfriend', 'gg': 'Good game',
            'gj': 'Good job', 'gl': 'Good luck', 'glhf': 'Good luck have fun',
            'goat': 'Greatest of all time', 'gnite': 'Good night', 'gr8': 'Great',
            'gratz': 'Congratulations', 'gtfoh': 'Get the f*** outta here', 'gtg': 'Got to go',
            'gud': 'Good', 'gyat': 'God d***; exclamation of excitement',
            # H
            'h8': 'Hate', 'hella': 'Really', 'hits different': 'Something that affects you in a particular way',
            'hmu': 'Hit me up (contact me)', 'hv': 'Have', 'hw': 'Homework', 'hbd': 'Happy Birthday',
            'hype': 'Extreme excitement; building up buzz',
            # I
            'ib': 'I’m back', 'ic': 'I see', 'icyami': 'In case you missed it', 'idc': 'I don’t care', 
            'idk': 'I don’t know', 'ig': 'I guess or Instagram', 'iirc': 'If I remember correctly', 
            'ik': 'I know', 'ikr': 'I know right?', 'ilu': 'I love you', 'ily': 'I love you', 
            'im': 'Instant message', 'imho': 'In my humble opinion', 'imo': 'In my opinion', 
            'insta': 'Instagram', 'irl': 'In real life',
            'it’s giving…': 'Used to describe something (e.g. ‘It’s giving childhood’ could describe something that reminds you of your childhood)',
            'iykyk': 'If you know, you know; often used to describe inside jokes',
            # J
            'jk': 'Just kidding',
            # K
            'k': 'Okay', 'kewl': 'Cool', 'kthnx': 'OK, thanks',
            # L
            'l': 'Lesbian', '(take the) l': 'Loss', 'l8': 'Late', 'l8r': 'Later',
            'let them cook': 'A supportive phrase; to give someone time and space to do something you know they can do',
            'lit': 'It describes something as positive', 'lmao': 'Laughing my a** off',
            'lol': 'Laugh out loud', 'lolll': 'Laugh out loud a lot', 'luv ya': 'Love you',
            # M
            'm': 'Male', 'm.i.r.l': 'Meet in real life', 'mkay': 'Mmm, okay',
            'mmo': 'Massively multiplayer online', 'mmorpg': 'Massively multiplayer online role-playing game',
            'msg': 'Message', 'mwah': 'To give a kiss',
            # N
            'n/a': 'Not available or not applicable', 'n2m': 'Nothing too much', 'nbd': 'No big deal',
            'ne': 'Any', 'ne1': 'Anyone', 'nft': 'Non-Fungible Token',
            'nm': 'Not much / Nothing much / Never mind', 'no cap': 'No lie', 
            'noob': 'Short for ‘newbie’, refers to an inexperienced gamer or online community user',
            'np': 'No problem', 'nthng': 'Nothing', 'nvr': 'Never', 'nw': 'No worries', 'nvm': 'Nevermind',
            # O
            'oic': 'Oh, I see', 'om': 'Oh my', 'omg': 'Oh my God', 'omw': 'On my way',
            'onl': 'Online', 'ootd': 'Outfit of the day', 'ot': 'Off topic', 'ova': 'Over',
            # P
            'peak': 'Unfortunate', 'peeps': 'People', 'pic': 'Picture', 'pir': 'Parent in room',
            'pk': 'Player kill', 'pls': 'Please', 'plz': 'Please', 'pm': 'Private Message',
            'pmsl': 'Peeing myself laughing', 'pog': 'Play of the game / Excited reaction', 
            'poggers': 'Play of the game / Excited reaction', 'pov': 'Point of view', 'ppl': 'People',
            'prolly': 'Probably', 'pwn': 'Own, as in conquer or defeat',
            'pwned': 'Owned, as in conquered or defeated',
            # Q
            'qt': 'Cutie', 'qtpi': 'Cutie pie',
            # R
            'r': 'Are or our', 'riz': 'Charisma', 'rizz': 'Charisma', 'rn': 'Right now',
            'rizzler': 'Someone who is good at flirting (because they have rizz)',
            'rly': 'Really', 'rofl': 'Rolling on the floor laughing', 'rpg': 'Role playing game',
            'ru': 'Are you?', 'ruok': 'Are you okay?',
            # S
            'sec': 'Second', 'seggs': 'Sex; used as a way to get around language filters',
            'ship': 'Relationship; or imagining people together (e.g. I ship those two)',
            'simp': 'someone who does too much for their crush (often used in sexist context against men)',
            'simping': 'someone who does too much for their crush (often used in sexist context against men)',
            'skibidi': 'A reference to a video about an army of toilets taking over the world',
            'skl': 'School', 'sksksk': 'Representing laughter', 'slaps': 'Describing something as good (e.g. This song slaps)',
            'slay': 'To do something exceptionally well; succeed', 'smh': 'Shaking my head', 'sms': 'Short Message Service', 
            'so': 'Significant other', 'sob': 'Son of a B*tch', 'sos': 'Help', 'spk': 'Speak', 'srs': 'Serious',
            'srsbsns': 'Serious business', 'srsly': 'Seriously', 'sry': 'Sorry',
            'stan': 'being a fan of someone', 'str8': 'Straight', 'sup': 'What’s up',
            'sus': 'Suspicious', 'sux': 'Sucks or “it sucks”',
            'swag': 'Boasting about one’s skills or style',
            # T
            'tbh': 'To be honest', 'tc': 'Take care', 'tea': 'gossip',
            'tfw': 'That feeling when', 'tgif': 'Thank God it’s Friday', 'thanq': 'Thank you', 'thx': 'Thanks',
            'tmi': 'Too much information', 'trans': 'Transsexual', 't*': 'Transsexual',
            't+': 'Transsexual', 'ttfn': 'Ta-ta for now', 'ttyl': 'Talk to you later',
            'tweet': 'Twitter post', 'txt': 'Text', 'ty': 'Thank you',
            # U
            'u': 'You', 'u2': 'You too', 'ul': 'Upload',
            'unalive': 'Kill; used to get around language filters', 'ur': 'Your or you’re',
            # V
            'vm': 'Voicemail', 'vibe check': 'Assessment of someone’s mood or attitude',
            # W
            'w': 'win', 'w@': 'What?', 'w/': 'With', 'w/e': 'Whatever or weekend',
            'w/o': 'Without', 'w8': 'Wait', 'wag1': 'What’s up', 'wbu': 'What about you?',
            'wk': 'Week', 'wip': 'Work in progress', 'wrk': 'Work', 'wtf': 'What the f***', 
            'wtg': 'Way to go', 'wyd': 'What (are) you doing?', 'wysiwyg': 'What you see is what you get',
            # X
            'x': 'Kiss (or the platform formally called Twitter)', 'xoxo': 'Kisses and hugs',
            # Y
            'y?': 'Why?', 'yeet': 'To throw something', 'yktv': 'You know the vibe',
            'yolo': 'You only live once', 'yr': 'Your',
            'yt': 'White (or YouTube)', 'yw': 'You’re welcome',
            # Z
            '(gen) z': 'People born from around 1997-2012', 'za': 'Pizza',
            # #
            '2': 'To', '24/7': 'Twenty-four hours a day, seven days a week',
        }
        
        # 1. Ensure all keys are lowercased for case-insensitive lookup
        self.slang_map = {k.lower(): v for k, v in self.slang_map.items()}

        # 2. Create a reverse map for fast reverse lookup (Meaning -> Slang Terms)
        self.meaning_to_slang = {}
        for slang, meaning in self.slang_map.items():
            if meaning not in self.meaning_to_slang:
                self.meaning_to_slang[meaning] = []
            self.meaning_to_slang[meaning].append(slang)
        
        # 3. Create a list of slang keys sorted by length (longest first) for replacement function.
        self.slang_keys_sorted = sorted(self.slang_map.keys(), key=len, reverse=True)


    def get_meaning(self, slang_term: str) -> str:
        """
        Looks up the meaning of a given slang term (Slang -> Meaning).
        """
        return self.slang_map.get(slang_term.lower(), f"Slang term '{slang_term}' not found.")

    def reverse_lookup(self, keyword_or_meaning: str) -> dict or str:
        """
        Finds slang term(s) based on a meaning or a keyword in the meaning.
        """
        found_terms = {}
        search_lower = keyword_or_meaning.lower()

        for meaning, slang_list in self.meaning_to_slang.items():
            if search_lower in meaning.lower():
                found_terms[meaning] = slang_list
        
        if not found_terms:
             return f"No slang found matching the meaning or keyword: '{keyword_or_meaning}'"
        
        return found_terms

    def search_slang(self, keyword: str) -> dict or str:
        """
        Searches the dictionary for slang terms or meanings containing a keyword.
        """
        found_results = {}
        search_lower = keyword.lower()
        
        for slang, meaning in self.slang_map.items():
            if search_lower in slang or search_lower in meaning.lower():
                found_results[slang] = meaning
        
        if not found_results:
            return f"No slang or meaning found containing the keyword: '{keyword}'"

        return found_results
    
    def replace_slang_in_text(self, text: str) -> str:
        """
        Replaces all recognized slang terms in a given text (sentence/paragraph)
        with their full, original meaning. The replacement is case-insensitive.
        
        This is ideal for data cleaning (e.g., cleaning a pandas column using .apply()).
        """
        if not text:
            return text

        # Iterate over slang terms from longest to shortest
        for slang in self.slang_keys_sorted:
            meaning = self.slang_map[slang]
            
            # Use regex with word boundaries (\b) for accurate, whole-word matching.
            pattern = r'(?<!\w)' + re.escape(slang) + r'(?!\w)'

            # Apply replacement in a case-insensitive manner
            text = re.sub(pattern, meaning, text, flags=re.IGNORECASE)
            
        return text


# --- Future Feature: Text Cleaning Utilities (Placeholders) ---
# Note: This class remains a placeholder structure for future development.

class TextCleaner:
    """
    A class for basic text pre-processing utilities (scheduled for future implementation).
    These methods help clean raw text before processing or analysis.
    """
    def to_lowercase(self, text: str) -> str:
        """
        Placeholder: Converts all characters in the text string to lowercase.
        """
        raise NotImplementedError("to_lowercase is scheduled for a future release.")

    def remove_html_tags(self, text: str) -> str:
        """
        Placeholder: Removes HTML and XML tags from the text using regular expressions.
        """
        raise NotImplementedError("remove_html_tags is scheduled for a future release.")

    def remove_urls(self, text: str) -> str:
        """
        Placeholder: Removes URLs and web links from the text.
        """
        raise NotImplementedError("remove_urls is scheduled for a future release.")

    def remove_punctuation(self, text: str) -> str:
        """
        Placeholder: Removes common punctuation marks from the text.
        """
        raise NotImplementedError("remove_punctuation is scheduled for a future release.")

# Simple example of usage
if __name__ == "__main__":
    slang_finder = SlangDictionary()
    
    # 4. New Slang Replacement Feature Demonstration
    print("\n--- Slang Replacement Demonstration (Lychee Language Core) ---")
    
    input_text = "TBH, the new game slaps! I'm AFK now, BRB. LOL! No cap."
    print(f"Original Text:\n{input_text}")
    
    cleaned_text = slang_finder.replace_slang_in_text(input_text)
    print(f"\nCleaned Text:\n{cleaned_text}")
