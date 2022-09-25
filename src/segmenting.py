from functools import cache

import wordsegment as ws  # type: ignore


@cache
def _load_word_data():
    ws.load()

    # Add HP incantations to the data set
    one_word_incantations = ['aberto', 'accio', 'aguamenti', 'alohomora', 'anapneo', 'anteoculatia', 'aparecium',
                             'apparate', 'ascendio', 'avenseguim', 'avifors', 'avis', 'baubillious', 'bombarda',
                             'calvario', 'cantis', 'cascading', 'caterwauling', 'cheering', 'colloportus', 'colloshoo',
                             'colovaria', 'confringo', 'confundus', 'conjunctivitis', 'crucio', 'cushioning', 'defodio',
                             'deletrius', 'densaugeo', 'deprimo', 'depulso', 'descendo', 'diffindo', 'diminuendo',
                             'dissendium', 'disillusionment', 'duro', 'draconifors', 'drought', 'ducklifors', 'ebublio',
                             'engorgio', 'ennervate', 'entomorphis', 'episkey', 'epoximise', 'erecto', 'evanesce',
                             'evanesco', 'expelliarmus', 'expulso', 'extinguishing', 'ferula', 'fidelius', 'fiendfyre',
                             'finestra', 'finite', 'flagrante', 'flagrate', 'flipendo', 'flying', 'fumos',
                             'furnunculus', 'geminio', 'glacius', 'glisseo', 'gripping', 'herbifors', 'herbivicus',
                             'homonculous', 'homorphus', 'horcrux', 'illegibilus', 'immobulus', 'impedimenta',
                             'imperio', 'impervius', 'incarcerous', 'incendio', 'inflatus', 'informous', 'langlock',
                             'lapifors', 'legilimens', 'levicorpus', 'liberacorpus', 'lumos', 'maledictus', 'melofors',
                             'mimblewimble', 'mobiliarbus', 'mobilicorpus', 'morsmorde', 'muffliato', 'multicorfors',
                             'nebulus', 'nox', 'obliteration', 'obliviate', 'obscuro', 'oppugno', 'orbis', 'orchideous',
                             'pack', 'periculum', 'portus', 'protego', 'quietus', 'reducio', 'reducto', 'relashio',
                             'rennervate', 'reparo', 'revelio', 'rictusempra', 'riddikulus', 'scourgify', 'scurge',
                             'sectumsempra', 'serpensortia', 'silencio', 'sonorus', 'spongify', 'steleus', 'stupefy',
                             'surgito', 'tarantallegra', 'tentaclifors', 'tergeo', 'titillando', 'transmogrify',
                             'ventus', 'verdillious', 'vermillious', 'verdimillious', 'waddiwasi']
    ws.UNIGRAMS.update(map(lambda key: (key, 16000000), one_word_incantations))

    two_word_incantations = ['age line', 'alarte ascendare', 'anti cheating', 'appare vestigium', 'arania exumai',
                             'aqua eructo', 'arresto momentum', 'avada kedavra', 'babbling curse', 'bluebell flames',
                             'bombarda maxima', 'bubble head', 'carpe retractum', 'cave inimicum', 'cistem aperio',
                             'combat bolt', 'cornflake skin', 'ear shriveling', 'engorgio skullus', 'entrail expelling',
                             'everte statum', 'expecto patronum', 'fianto duri', 'finite incantatum', 'flame freezing',
                             'flipendo duo', 'flipendo tria', 'glacius tria', 'homenum revelio', 'incendio duo',
                             'incendio tria', 'lacarnum inflamarae', 'locomotor mortis', 'lumos duo', 'lumos maxima',
                             'lumos solem', 'magicus extremos', 'meteolojinx recanto', 'oculus reparo',
                             'partis temporus', 'permanent sticking', 'peskipiksi pesternomi', 'petrificus totalus',
                             'piertotum locomotor', 'point me', 'priori incantatem', 'prior incantato',
                             'protego diabolica', 'protego horribilis', 'protego maxima', 'protego totalum',
                             'redactum skullus', 'repello muggletum', 'repello inimicum', 'salvio hexia',
                             'slugulus eructo', 'specialis revelio', 'stinging jinx', 'switching spell',
                             'unbreakable vow', 'ventus duo', 'vera verto', 'verdimillious duo', 'vipera evanesca',
                             'vulnera sanentur', 'wingardium leviosa']
    ws.BIGRAMS.update(map(lambda key: (key, 16000000), two_word_incantations))


def segment(input_str: str) -> str:
    _load_word_data()
    segments = ws.segment(input_str)
    return ' '.join(segments)
