from src.scrapped_data_decoders.decoder import Decoder
from src.scrapped_data_decoders.utils import get_with_default
from collections import defaultdict

class MainInPeopleDecoder(Decoder):
    def __init__(self):
        self.id2value = defaultdict(lambda: "Unknown")
        self.id2value.update({
            1: "Intelligence and Creativity",
            2: "Kindness and Honesty",
            3: "Beauty and Health",
            4: "Authority and Wealth",
            5: "Courage and Perseverance",
            6: "Humor and Zest",
        })
            
    def decode(self, user_dict: dict) -> dict[str, int|str]:
        id = get_with_default(user_dict, ['personal', 'people_main'], default=0)
        value = self.id2value[id]
        return {'people_main_id': id, 'people_main_value': value}

