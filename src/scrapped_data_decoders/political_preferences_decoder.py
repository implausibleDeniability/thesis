from collections import defaultdict
from src.scrapped_data_decoders.decoder import Decoder
from src.scrapped_data_decoders.utils import get_with_default

class PoliticalPreferencesDecoder(Decoder):
    def __init__(self):
        self.id2value = defaultdict(lambda: "Unknown")
        self.id2value.update({
            1: "Communist",
            2: "Socialist",
            3: "Moderate",
            4: "Liberal",
            5: "Conservative",
            6: "Moharchical",
            7: "Indifferent",
            8: "Libertarian",
        })
            
    def decode(self, user_dict: dict) -> dict[str, int|str]:
        id = get_with_default(user_dict, ['personal', 'political'], default=0)
        value = self.id2value[id]
        return {'political_pref_id': id, 'polit_pref_value': value}

