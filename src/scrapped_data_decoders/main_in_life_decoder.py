from collections import defaultdict
from src.scrapped_data_decoders.decoder import Decoder
from src.scrapped_data_decoders.utils import get_with_default

class MainInLifeDecoder(Decoder):
    def __init__(self):
        self.id2value = defaultdict(lambda: "Unknown")
        self.id2value.update({
            1: "Family and Kids",
            2: "Career and Money",
            3: "Entertainment and Rest",
            4: "Science and Research",
            5: "World Optimization",
            6: "Self-development",
            7: "Beauty and Art",
            8: "Fame and Influence",
        })
            
    def decode(self, user_dict: dict) -> dict[str, int|str]:
        id = get_with_default(user_dict, ['personal', 'life_main'], default=0)
        value = self.id2value[id]
        return {'life_main_id': id, 'life_main_value': value}

