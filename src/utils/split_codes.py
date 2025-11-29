def split_codes(text: str) -> list[str]:
    codes = text.split('., ')
    codes[-1] = codes[-1].replace('.', '')
    return codes
