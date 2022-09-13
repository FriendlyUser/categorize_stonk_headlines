from enum import Enum, unique

@unique
class Categories(str, Enum):
    USELESS = "useless"
    EARNINGS = "earnings"
    EVENT_DATE = "event_date"
    COMMENTARY = "commentary" # ZACKS, MOTLEY FOOL
    FINANCIAL  = "financial" #  (DIVIDEND/ STONK BUYBACK) OUTSIDE OF EARNINGS
    NEWS = "news" # general updates that I am not interested in
    CRITICAL = "critical" # general updates that I am interested in
