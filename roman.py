from typing import Union

class Roman:
    def __init__(self, num: Union[str, int, float]):
        if isinstance(num, str):
            self.int = self.roman_to_int(num)
            self.roman = self.int_to_roman(self.int)

        elif isinstance(num, int) or isinstance(num, float):
            self.roman = self.int_to_roman(num)
            self.int = self.roman_to_int(self.roman)

        else:
            raise ValueError(f'Arg0: (Union[str, int, float]) must be number (int or float for highlight the integer part) or string (roman number str), not {type(num)} {num}')


    @staticmethod
    def roman_to_int(roman: str) -> int:
        total = 0

        for i, part in enumerate(roman.replace(' ', '').split('+')):
            if Roman.is_valid_roman(part):
                m = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                }
                
                for i in range(len(part)):
                    if i < len(part) - 1 and m[part[i]] < m[part[i+1]]:
                        total -= m[part[i]]
                    else:
                        total += m[part[i]]

            else:
                raise ValueError(f'Arg0: (str) number {part} at {i}th augmentation is incorrect')
            
        return total

    @staticmethod
    def int_to_roman(num: Union[str, int, float]) -> str:
        num = int(num)
        roman_numerals = {
            1000: "M",
            900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV",
            1: "I"
        }
        
        roman_num = ''
        augments = num//3999
        normal = num - augments*3999

        if num < 0:
            raise ValueError(f"Arg0: (Union[str, int, float]) number must be more than 0, not {num}")
        
        for value, symbol in roman_numerals.items():
            while normal >= value:
                roman_num += symbol
                normal -= value
        
        return augments * "MMMCMXCIX + " + roman_num

    @staticmethod
    def is_valid_roman(roman: str) -> bool:
        roman_numerals = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        
        prev_value = 0
        consecutive_occurrences = 0

        for part in roman.replace(' ', '').split('+'):
            for numeral in reversed(part):
                if numeral not in roman_numerals:
                    return False
                
                value = roman_numerals[numeral]
                
                if value < prev_value:
                    consecutive_occurrences = 0
                elif value == prev_value:
                    consecutive_occurrences += 1
                    if consecutive_occurrences > 2:
                        return False
                else:
                    consecutive_occurrences = 0
                
                prev_value = value
        
        return True


    def __add__(self, other: Union[str, int, 'Roman']):
        if isinstance(other, Roman):
            return Roman(other.int + self.int)
        
        elif isinstance(other, int):
            return Roman(other + self.int)

        elif isinstance(other, float):
            return Roman(int(self.int + other))
        
        elif isinstance(other, str):
            return Roman(Roman(other).int + self.int)
        
        else:
            raise ValueError(f"Unsupported {type(other)} for addition and subtraction: {other}")
            
    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return Roman(self.int - other) if self.int - other > 0 else self.int - other
    def __rsub__(self, other):
        return Roman(other - self.int) if other - self.int > 0 else other - self.int
        
    def __mul__(self, other: Union[str, int, 'Roman']):
        if isinstance(other, Roman):
            return Roman(other.int * self.int)
        
        elif isinstance(other, int):
            return Roman(self.int * other)

        elif isinstance(other, float):
            return Roman(int(self.int * other))
        
        elif isinstance(other, str):
            return Roman(Roman(other).int * self.int)
        
        else:
            raise ValueError(f"Unsupported {type(other)} for multiplication and division: {other}")
    def __rmul__(self, other):
        return self * other
        
    def __floordiv__(self, other):
        return self * (1 // other)
    def __truediv__(self, other):
        return Roman(other / self.int)
    def __rfloordiv__(self, other):
        return Roman(other // self.int) if other // self.int > 0 else other // self.int
    def __rtruediv__(self, other):
        return Roman(other / self.int) if int(other / self.int) > 0 else other / self.int
    
    def __pow__(self, other):
        if isinstance(other, Roman):
            return Roman(self.int**other.int)
        
        elif isinstance(other, int):
            return Roman(self.int**other)
        
        elif isinstance(other, str):
            return Roman(Roman(other).int**self.int)

        else:
            raise ValueError(f"Unsupported {type(other)} for exponentiation: {other}")
        
    def __eq__(self, other):
        if isinstance(other, Roman):
            return other.int == self.int
        
        elif isinstance(other, int):
            return other == self.int
        
        elif isinstance(other, str):
            return Roman(other).int == self.int
        
        else:
            raise ValueError(f"Unsupported {type(other)} for comparison: {other}")
    
    def __neg__(self):
        return -self.int

    def __len__(self):
        return len(list(self.roman.split(' + '))) - 1
    
    def __mod__(self, other):
        return other % self.int
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        return self.int < other
    def __le__(self, other):
        return other > self.int
    def __gt__(self, other):
        return other <= self.int
    def __ge__(self, other):
        return self.int >= other
    
    def __reversed__(self):
        return Roman( int(''.join(reversed(str(self.int)))) )
    
    def __str__(self):
        return self.roman
    def __int__(self):
        return self.int
    def __repr__(self):
        return f"{self.__class__.__name__}(int={self.int},value='{self.roman}',augments={len(self)})"