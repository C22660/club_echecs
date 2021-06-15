import string
import unidecode

""" Créer une vérification de la conformité des saisies manuelles"""


def check_names(text):
    """ Un nom est composé de lettres, mais peut aussi avoir des espaces et/ou trait(s) d'union.
        Par contre, la saisie de doit pas être seulement composée d'espaces
         ni comporter d'autres caractères de ponctuation.
    """

    good_inputs = string.ascii_letters+" "+"-"

    composition = 0

    # suppression des accents éventuels
    unaccented_string = unidecode.unidecode(text)

    # comptabilisation de nombre de caracères de texte trouvés
    for i in unaccented_string:
        if i in good_inputs:
            composition += 1
    # Vérification que tous les caractères de text son acceptés mais qu'il n'y ait
    # pas que des espaces.
    if len(text) == composition:
        if not text.isspace():
            return True

def check_birth_date(date):
    return True

def check_tournament_date(date):
    return True
