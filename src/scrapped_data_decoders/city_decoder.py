from src.scrapped_data_decoders.decoder import Decoder
from src.scrapped_data_decoders.utils import get_with_default


class CityDecoder(Decoder):
    def decode(self, user_dict: dict) -> dict[str, int|str]:
        city_id = get_with_default(user_dict, ['city', 'id'], default=0)
        city_name = get_with_default(user_dict, ['city', 'title'], default='Unknown')
        return {'city_id': city_id, 'city_name': city_name}

