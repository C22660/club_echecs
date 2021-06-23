from datetime import datetime
import locale


locale.setlocale(locale.LC_TIME, '')


class TimeStamp:
    """Génère l'horodatage des parties (rounds) sous une forme francisée
        exemple : "le lundi 07/06/2021 à 15:42:46"
    """

    def time_date_now():
        # renvoi un horodatage à la demande
        now = datetime.now()
        return now.strftime('%A %d/%m/%Y à %H:%M:%S')
