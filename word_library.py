import random

def get_dutch_five_letter_words():
    # List of Dutch 5-letter words
    return [
        'appel', 'brood', 'schaap', 'stoel', 'tafel', 'vader', 'moeder', 'huisje', 'kamer', 'vuurp',
        'piano', 'aarde', 'vliegt', 'blauw', 'licht', 'molen', 'plant', 'rebus', 'schaal', 'rugzak',
        'wereld', 'wijn', 'friet', 'kaas', 'storm', 'vogel', 'pasta', 'stoep', 'boek', 'schaar',
        'kleur', 'taart', 'krant', 'grond', 'olijf', 'water', 'lepel', 'afwas', 'wolk', 'droom',
        'acryl', 'affix', 'aftyp', 'ampex', 'accus', 'axels', 'acces', 'addax', 'afbik', 'afduw',
        'afhap', 'afpik', 'afwis', 'afzag', 'afzak', 'afzeg', 'bobby', 'buggy', 'babys', 'baggy',
        'buddy', 'buxus', 'bitch', 'blijf', 'bodys', 'bogey', 'bytes', 'batch', 'cycli', 'campy',
        'crazy', 'crypt', 'chick', 'citys', 'curry', 'check', 'chijl', 'chimp', 'click', 'cocci',
        'cyste', 'chips', 'cinch', 'codex', 'dizzy', 'dolby', 'dummy', 'derby', 'dolly', 'dixit',
        'dicht', 'ducht', 'dacht', 'dandy', 'derny', 'detox', 'docht', 'douch', 'drijf', 'dwaze',
        'epoxy', 'enzym', 'ethyl', 'exact', 'exces', 'echec', 'exlid', 'expat', 'expos', 'echel',
        'essay', 'exman', 'extra', 'echos', 'echte', 'edoch', 'guppy', 'gipsy', 'gymde', 'gyros',
        'gijpt', 'glimp', 'grijp', 'gejij', 'geluw', 'gepuf', 'glijd', 'glipt', 'gluip', 'gruwt',
        'gulpt', 'gabbe', 'happy', 'hobby', 'husky', 'hyper', 'hypes', 'hypet', 'hypos', 'hysop',
        'hapax', 'heavy', 'helix', 'hypen', 'hyven', 'hydra', 'hymen', 'hymne', 'intyp', 'ijzig',
        'inbox', 'ijzel', 'ijsco', 'ijzer', 'index', 'icing', 'ijlst', 'ijsje', 'ijver', 'ijzen',
        'ijdel', 'ijker', 'ijkte', 'ijlde', 'jazzy', 'jurys', 'jicht', 'juich', 'jacht', 'jacks',
        'jozef', 'jawel', 'jouwt', 'jubel', 'jumbo', 'jajem', 'jalap', 'jambe', 'javel', 'jemig',
        'kinky', 'kwijl', 'kruch', 'kucht', 'kwijt', 'kwips', 'kicks', 'kickt', 'kijft', 'kocht',
        'krach', 'kuche', 'kwelm', 'kwijn', 'kicke', 'kijkt', 'lynch', 'lobby', 'lycra', 'lymfe',
        'lolly', 'lycea', 'laque', 'lysol', 'ladys', 'licht', 'lucht', 'luxer', 'luxes', 'lacht',
        'latex', 'lijft', 'mythe', 'mixed', 'mixer', 'mixes', 'mixte', 'macht', 'match', 'mezzo',
        'mixen', 'mocht', 'macho', 'meluw', 'mikwa', 'mikwe', 'muffe', 'murwt', 'nimby', 'nicht',
        'nylon', 'nacht', 'niche', 'nijpt', 'nixen', 'nabij', 'nanny', 'nihil', 'nijgt', 'nipje',
        'nufje', 'nabob', 'naijl', 'napje', 'opzij', 'omwip', 'ofwel', 'olijf', 'opduw', 'opheb',
        'ophef', 'oppik', 'opvul', 'opwek', 'opwel', 'opzag', 'opzak', 'opzeg', 'opzit', 'oxers',
        'proxy', 'puppy', 'pique', 'pixel', 'paddy', 'party', 'pitch', 'pizza', 'pylon', 'pacht',
        'panty', 'patch', 'pijpt', 'pocht', 'ponys', 'prach', 'query', 'quilt', 'quark', 'quads',
        'quasi', 'quant', 'queue', 'quota', 'quote', 'rugby', 'rally', 'remix', 'riyal', 'radix',
        'relax', 'richt', 'rouxs', 'ready', 'recht', 'rijft', 'rijpt', 'ruche', 'rabbi', 'ranch',
        'rayon', 'squaw', 'schuw', 'sulky', 'sylfe', 'schip', 'schub', 'sfinx', 'shoyu', 'spray',
        'syrah', 'schab', 'schaf', 'schap', 'schep', 'schik', 'schil', 'thyrs', 'tipsy', 'tyfus',
        'tommy', 'types', 'typte', 'toque', 'twijg', 'typen', 'taxis', 'taxol', 'taxus', 'teddy',
        'telex', 'tjilp', 'toddy', 'uzelf', 'unzip', 'upper', 'uglis', 'uilig', 'uitje', 'uiver',
        'unica', 'uwent', 'uiige', 'uitga', 'ukken', 'ultra', 'unief', 'ureum', 'urmde', 'vinyl',
        'vieux', 'vacht', 'vecht', 'vlijm', 'vocht', 'vijlt', 'vipje', 'vlijt', 'vlouw', 'vamps',
        'vazal', 'vezel', 'views', 'vijst', 'vleze', 'wicht', 'wacht', 'wijze', 'winch', 'wrijf',
        'wazig', 'weckt', 'wijkt', 'wijlt', 'wippe', 'wulps', 'webbe', 'welft', 'wezel', 'whist',
        'wigje', 'xerox', 'xeres', 'xenon', 'yucca', 'yells', 'yogis', 'yanks', 'yards', 'yelde',
        'yuans', 'zloty', 'zwijg', 'zwijm', 'zicht', 'zucht', 'zwalp', 'zwamp', 'zwilk', 'zacht',
        'zocht', 'zwalk', 'zwelg', 'zwerf', 'zwiep', 'zwijn', 'zwikt'
    ]

def get_random_word():
    words = get_dutch_five_letter_words()
    return random.choice(words)
