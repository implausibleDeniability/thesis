from src.scrapped_data_decoders.decoder import Decoder
from src.scrapped_data_decoders.utils import get_with_default


class SexDecoder(Decoder):
    id2value = {
        0: "Unknown", 
        1: "Male", 
        2: "Female",
    }
    
    def decode(self, user_dict: dict) -> dict[str, int|str]:
        sex_id = get_with_default(user_dict, ['sex'], default=0)
        sex_value = self.id2value[sex_id]
        return {'sex_id': sex_id, 'sex_value': sex_value}

