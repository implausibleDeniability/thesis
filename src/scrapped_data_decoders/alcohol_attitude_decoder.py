from src.scrapped_data_decoders.decoder import Decoder
from src.scrapped_data_decoders.utils import get_with_default
from collections import defaultdict

class AlcoholAttitudeDecoder(Decoder):
    def __init__(self):
        self.id2value = defaultdict(lambda: "Unknown")
        self.id2value.update({
            1: "Strongly Negative",
            2: "Negative",
            3: "Comromise",
            4: "Neutral",
            5: "Positive",
        })
            
    def decode(self, user_dict: dict) -> dict[str, int|str]:
        id = get_with_default(user_dict, ['personal', 'alcohol'], default=0)
        value = self.id2value[id]
        return {'alcohol_attitude_id': id, 'alcohol_attitude_value': value}

