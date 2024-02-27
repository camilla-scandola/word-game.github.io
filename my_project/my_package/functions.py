hiragana_dictionary = {'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お', 'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ', 'sa': 'さ', 'sh': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ', 'ta': 'た', 'ch': 'ち', 'ts': 'つ', 'te': 'て', 'to': 'と', 'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の', 'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ', 'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も', 'ya': 'や', 'yu': 'ゆ', 'yo': 'よ', 'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ', 'wa': 'わ', 'wo': 'を', 'n': 'ん'}

def check_syllable(syllable):

    dakuten = ['ga', 'gi', 'gu', 'ge', 'go', 'za', 'ji', 'zu', 'ze', 'zo','da', 'de', 'do', 'ba', 'bi', 'bu', 'be', 'bo']

    handakuten = ['pa', 'pi', 'pu', 'pe', 'po']


    if syllable in hiragana_dictionary:

        return True

    elif syllable in dakuten:

        return 'This is a Dakuten variation of Hiragana'

    elif syllable in handakuten:

        return 'This is a Handakuten variation of Hiragana'

    else:

        return False


two_syllable_words = {'kise': 'きせ', 'haru': 'はる', 'natsu': 'なつ', 'fuyu': 'ふゆ', 'aki': 'あき', 'yuki': 'ゆき', 'ame': 'あめ', 'sora': 'そら', 'ten': 'てん', 'hoshi': 'ほし', 'nami': 'なみ', 'yama': 'やま', 'kai': 'かい', 'sui': 'すい', 'kusa': 'くさ', 'kumo': 'くも', 'nichi': 'にち', 'tsuki': 'つき', 'rai': 'らい', 'yoru': 'よる', 'hiru': 'ひる', 'yuu': 'ゆう', 'iro': 'いろ', 'aka': 'あか', 'ao': 'あお', 'kuro': 'くろ', 'kin': 'きん', 'nashi': 'なし', 'momo': 'もも', 'hana': 'はな', 'ran': 'らん', 'saku': 'さく', 'kan': 'かん', 'ai': 'あい', 'koi': 'こい', 'shin': 'しん', 'koe': 'こえ', 'hito': 'ひと', 'reki': 'れき', 'neko': 'ねこ', 'tori': 'とり'}


def check_word(word):

    if word in two_syllable_words:

        return True

    else:

        return 'This word is not part of the dictionary'


hiragana_dictionary = {'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お', 'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ', 'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ', 'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と', 'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の', 'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ', 'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も', 'ya': 'や', 'yu': 'ゆ', 'yo': 'よ', 'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ', 'wa': 'わ', 'wo': 'を', 'n': 'ん'}

def latin_to_hiragana(jpword):

    latin = ''
    hiragana = ''

    for char in jpword:
        if char == 'n':
            if latin:
                hiragana = hiragana + hiragana_dictionary['n']
                latin = ''
            latin = 'n'
        else: 
            latin = latin + char
            if latin in hiragana_dictionary:
                hiragana = hiragana + hiragana_dictionary[latin]
                latin = ''
    if latin == 'n':
        hiragana = hiragana + hiragana_dictionary['n']
    return hiragana


jpword = 'haru'

result = latin_to_hiragana(jpword)

print(result)


def english_translation(jpword):

    two_syllable_words = {'kise': 'きせ', 'haru': 'はる', 'natsu': 'なつ', 'fuyu': 'ふゆ', 'aki': 'あき', 'yuki': 'ゆき', 'ame': 'あめ', 'sora': 'そら', 'ten': 'てん', 'hoshi': 'ほし', 'nami': 'なみ', 'yama': 'やま', 'kai': 'かい', 'sui': 'すい', 'kusa': 'くさ', 'kumo': 'くも', 'nichi': 'にち', 'tsuki': 'つき', 'rai': 'らい', 'yoru': 'よる', 'hiru': 'ひる', 'yuu': 'ゆう', 'iro': 'いろ', 'aka': 'あか', 'ao': 'あお', 'kuro': 'くろ', 'kin': 'きん', 'nashi': 'なし', 'momo': 'もも', 'hana': 'はな', 'ran': 'らん', 'saku': 'さく', 'kan': 'かん', 'ai': 'あい', 'koi': 'こい', 'shin': 'しん', 'koe': 'こえ', 'hito': 'ひと', 'reki': 'れき', 'neko': 'ねこ', 'tori': 'とり'}

    japanese_to_english = {'kise': 'season', 'haru': 'spring', 'natsu': 'summer', 'fuyu': 'winter', 'aki': 'autumn', 'yuki': 'snow', 'ame': 'rain', 'sora': 'sky', 'ten': 'heaven', 'hoshi': 'star', 'nami': 'wave', 'yama': 'mountain', 'kai': 'sea', 'sui': 'water', 'kusa': 'grass', 'kumo': 'cloud', 'nichi': 'sun', 'tsuki': 'moon', 'rai': 'thunder', 'yoru': 'night', 'hiru': 'daytime', 'yuu': 'evening', 'iro': 'color', 'aka': 'red', 'ao': 'blue', 'kuro': 'black', 'kin': 'gold', 'gin': 'silver', 'nashi': 'pear', 'momo': 'peach', 'hana': 'flower', 'bara': 'rose', 'ran': 'orchid', 'saku': 'bloom', 'kan': 'feeling', 'ai': 'love', 'koi': 'love', 'shin': 'heart', 'koe': 'voice', 'hito': 'person', 'reki': 'history', 'neko': 'cat', 'tori': 'bird'}

    while jpword in two_syllable_words and jpword in japanese_to_english:

        hiraganaword = two_syllable_words[jpword]

        enword = japanese_to_english[jpword]

        hiragana_and_english = f'{hiraganaword}, {enword}'

        return hiragana_and_english

jpword = 'sora'

result = english_translation(jpword)

print(result)
