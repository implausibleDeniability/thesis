class Decoder:
    def decode(self, user_dict: dict) -> dict[str, bool|int|float|str]:
        """Takes the unstructured user description and 
        returns the data, relevant to that decoder
        """
        raise NotImplementedError("Abstract class is used")
