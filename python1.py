def encode_text(text, mapping):
    encoded_text = ""
    for s in text:
        if s.isalpha():
            encoded_text += mapping.get(s.lower(), s)

        else:
            encoded_text += s
    return encoded_text
mapping = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p",
           "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e",
           "w": "d", "x": "c", "y": "b", "z": "a"}
word = input(print("enter the words"))
text = word
encoded_text = encode_text(text, mapping)
print(encoded_text)
