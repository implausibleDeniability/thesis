from enum import Enum
class ConvType(Enum):
    gcn = 1
    gat = 2
    res = 3
    gin = 4

    @classmethod
    def from_string(cls, conv_type: str) -> ConvType:
        if conv_type == 'gcn':
            return cls.gcn
        elif conv_type == 'gat':
            return cls.gat
        elif conv_type == 'res':
            return cls.res
        elif conv_type == 'gin':
            return cls.gin
        else:
            raise NotImplementedError()
