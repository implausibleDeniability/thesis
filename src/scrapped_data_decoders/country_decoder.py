from src.scrapped_data_decoders.decoder import Decoder
from src.scrapped_data_decoders.utils import get_with_default

class CountryDecoder(Decoder):
    def decode(self, user_dict: dict) -> dict[str, int|str]:
        city_id = get_with_default(user_dict, ['country', 'id'], default=0)
        city_name = get_with_default(user_dict, ['country', 'title'], default='Unknown')
        return {'country_id': city_id, 'country_name': city_name}

