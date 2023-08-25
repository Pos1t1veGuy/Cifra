from itertools import cycle, islice
from typing import Union

import string as s

from .roman import Roman

elements = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '/': ' '
}
decoded_morse_code = {v: k for k, v in morse_code.items()}


class Vigenere:
    @staticmethod
    def encode(key: str, text: str) -> str:
        plaintext = text.upper()
        keyword = key.upper()
        encrypted_text = ""

        for i in range(len(plaintext)):
            if plaintext[i] == " ":
                encrypted_text += " "
                continue

            key_letter = keyword[i % len(keyword)]
            key_shift = ord(key_letter) - ord("A")
            shifted_letter = chr(((ord(plaintext[i]) - ord("A") + key_shift) % 26) + ord("A"))
            encrypted_text += shifted_letter

        return encrypted_text
    
    @staticmethod
    def decode(key: str, text: str) -> str:
        ciphertext = text.upper()
        keyword = key.upper()
        decrypted_text = ""

        for i in range(len(ciphertext)):
            if ciphertext[i] == " ":
                decrypted_text += " "
                continue

            key_letter = keyword[i % len(keyword)]
            key_shift = ord(key_letter) - ord("A")
            shifted_letter = chr(((ord(ciphertext[i]) - ord("A") - key_shift) % 26) + ord("A"))
            decrypted_text += shifted_letter

        return decrypted_text


class Cesar:
    @staticmethod
    def encode(text: str, step: int, chars: Union[str, list] = []) -> str:
        if not chars:
            chars = list(s.ascii_letters + s.digits + s.punctuation)
        else:
            chars = list(chars)
        cycle_chars = cycle(list(chars))

        res = ''
        for char in text:
            res += next(islice(cycle_chars, step % len(chars), (step % len(chars)) + 1))
        
        return res


class a1z26:
    @staticmethod
    def encode(text: str, chars: Union[str, list] = [], sep: str = '-') -> str:
        if not chars:
            chars = list( s.ascii_letters + s.digits + s.punctuation + ' ' )

        return sep.join([ str(chars.index(char)) for char in text ])
    
    @staticmethod
    def decode(text: str, chars: list = [], sep: str = '-') -> str:
        if not chars:
            chars = list( s.ascii_letters + s.digits + s.punctuation + ' ' )

        return ''.join([ chars[int(char)] for char in text.replace(' ', '').split(sep) ])



class Atbash:
    @staticmethod
    def encode(text: str) -> str:
        encoded_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    encoded_char = chr(219 - ord(char))
                else:
                    encoded_char = chr(155 - ord(char))
                encoded_text += encoded_char
            else:
                encoded_text += char
        return encoded_text


class Morse:
    @staticmethod
    def encode(text: str) -> str:
        res = []

        for part in text.split(' '):
            part_res = []

            for char in part.upper():
                if char in morse_code.keys():
                    part_res.append(morse_code[char])

                else:
                    part_res.append(char)

            res.append(' '.join(part_res))

        return '   '.join(res)

    @staticmethod
    def decode(text: str) -> str:
        res = []

        for part in text.split('   '):
            part_res = []

            for char in part.upper().split(' '):
                if char in decoded_morse_code.keys():
                    part_res.append(decoded_morse_code[char])

                else:
                    part_res.append(char)

            res.append(''.join(part_res))

        return ' '.join(res)


def convert_to_base(num, base: int, digits: str = ''):
    if not digits:
        digits = s.digits + s.ascii_letters + s.punctuation
    if base < 2 or base > len(digits):
        raise ValueError(f"Arg1: (int) Unsupported base {base}, base must be int from 2 to {len(digits)} ")
    elif num == 0:
        return "0"
    
    result = ""
    while num > 0:
        result = digits[num % base] + result
        num //= base
    
    return result