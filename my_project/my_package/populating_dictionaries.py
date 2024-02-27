def read_hiragana_syllable(hiragana):
    '''(file open for reading) -> dict of (str: str)
    Read the syllables from the hiragana alphabet file and return a dictionary
    where each key is a syllable from the Latin alphabet and each value is the
    corresponding symbol in Hiragana.

    Precondition: the hiragana alphabet file starts with a header that contains no blank
    lines, then has a blank line, then lines containing the latin syllables and
    their corresponding Hiragana character.
    '''

    # Skip over the header
    line = hiragana.readline()
    while line != '\n':
        line = hiragana.readline()

    # Read the Latin syllables and corresponding hiragana symbols into a dict

    hiragana_characters = {}
    line = hiragana.readline()

    while line != '':

        latin_syllable = line[:2].strip()

        hiragana_symbol = line[3:].strip()

        if latin_syllable not in hiragana_characters:
            hiragana_characters[latin_syllable] = hiragana_symbol

        line = hiragana.readline()

    return hiragana_characters

def jp_en_words(japanese):
    '''(file open for reading) -> dict of (str: str)
    Read the two-syllable words from the hiragana-english file and return a dictionary
    where each key is a japanese word and each value is its translation in english.

    Precondition: the hiragana english file starts with a header that contains no blank
    lines, then has a blank line, then lines containing the words in japanese and
    their translation in english.
    '''

    # Skip over the header
    line = japanese.readline()
    while line != '\n':
        line = japanese.readline()

    # Read the the words in japanese and their translation in english into a dict

    jp_en_translation = {}
    line = japanese.readline()

    while line != '':

        japanese_word = line[:5].strip()

        english_word = line[6:].strip()

        if japanese_word not in jp_en_translation:
            jp_en_translation[japanese_word] = english_word

        line = japanese.readline()

    return jp_en_translation

def convert_to_hiragana(translation):
    '''(file open for reading) -> dict of (str: str)
    Read the two-syllable words from the hiragana-english file and return a dictionary
    where each key is a japanese word and each value is its translation in english.

    Precondition: the hiragana english file starts with a header that contains no blank
    lines, then has a blank line, then lines containing the words in japanese and
    their translation in english.
    '''

    # Skip over the header
    line = translation.readline()
    while line != '\n':
        line = translation.readline()

    # Read the the words in japanese and their translation in english into a dict

    jp_to_hiragana = {}
    line = translation.readline()

    while line != '':

        latin_word = line[:5].strip()

        hiragana_word = line[6:].strip()

        if latin_word not in jp_to_hiragana:
            jp_to_hiragana[latin_word] = hiragana_word

        line = translation.readline()

    return jp_to_hiragana
