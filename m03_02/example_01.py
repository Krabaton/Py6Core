# Hello world! -> { ASCII }

def string_to_codes(string: str) -> dict:
    codes = {}
    for ch in string:
        if not(ch in codes):
            codes[ch] = ord(ch)  # { "H": 72 }
    return codes


result = string_to_codes("Hello world!")
print(result)
