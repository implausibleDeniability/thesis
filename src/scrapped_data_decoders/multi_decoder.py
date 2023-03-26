from src.scrapped_data_decoders.age_decoder import AgeDecoder
from src.scrapped_data_decoders.alcohol_attitude_decoder import AlcoholAttitudeDecoder
from src.scrapped_data_decoders.city_decoder import CityDecoder
from src.scrapped_data_decoders.country_decoder import CountryDecoder
from src.scrapped_data_decoders.is_closed_profile_decoder import IsClosedProfileDecoder
from src.scrapped_data_decoders.main_in_life_decoder import MainInLifeDecoder
from src.scrapped_data_decoders.main_in_people_decoder import MainInPeopleDecoder
from src.scrapped_data_decoders.political_preferences_decoder import PoliticalPreferencesDecoder
from src.scrapped_data_decoders.sex_decoder import SexDecoder
from src.scrapped_data_decoders.decoder import Decoder


class MultiDecoder(Decoder):
    def __init__(self, decoders: list[Decoder]=None):
        if decoders:
            self.decoders = decoders
        else:
            self.decoders = [
                IsClosedProfileDecoder(),
                CityDecoder(),
                CountryDecoder(),
                SexDecoder(),
                AgeDecoder(),
                PoliticalPreferencesDecoder(),
                MainInLifeDecoder(),
                MainInPeopleDecoder(),
                AlcoholAttitudeDecoder(),
            ]
            
    def decode(self, user_dict: dict) -> dict[str, bool|int|float|str]:
        decoded_dict = dict()
        for decoder in self.decoders:
            decoded_dict.update(decoder.decode(user_dict))
        return decoded_dict

