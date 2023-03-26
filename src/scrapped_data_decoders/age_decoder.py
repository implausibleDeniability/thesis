from src.scrapped_data_decoders.decoder import Decoder
from src.scrapped_data_decoders.utils import get_with_default


class AgeDecoder(Decoder):
    DATA_COLLECTION_YEAR = 2023
    
    def decode(self, user_dict: dict) -> dict[str, int]:
        birthdate: str = get_with_default(user_dict, ['bdate'], default='1.1')
        day_month_year = birthdate.split('.')
        if len(day_month_year) == 3:
            is_present_bit = True
            value = self.DATA_COLLECTION_YEAR - int(day_month_year[2])
        else:
            is_present_bit = False
            value = 0
        return {'age_is_present': is_present_bit, 'age': value}

