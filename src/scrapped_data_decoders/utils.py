def get_with_default(dict_: dict, keys: list[str], default: object) -> object:
    assert len(keys) > 0
    try:
        for key in keys[:-1]:
            dict_ = dict_[key]
        value = dict_[keys[-1]]
    except (KeyError, TypeError):
        value = default 
    return value

