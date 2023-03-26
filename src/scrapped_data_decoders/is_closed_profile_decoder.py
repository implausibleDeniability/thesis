from src.scrapped_data_decoders.decoder import Decoder


class IsClosedProfileDecoder(Decoder):
    def decode(self, user_dict: dict) -> dict[str, bool]:
        return {'is_closed_profile': user_dict['is_closed']}

