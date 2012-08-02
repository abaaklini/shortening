#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
"""Copyright (C) 2012 Alexandre Baaklini, abaaklini@gmail.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

"""
Fornece funções de encurtamento e de expansão
para aplicações de encurtamento de URL.
O método utilizado é semelhante ao da conversão entre
números que se encontrão em base numérica diferente,
(ex. Base Decimal para Base Hexadecimal), neste caso a 
conversão seria entre a Base Decimal e Base 62 e vice-e-versa.
"""

MAPPING = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'a',
        '11': 'b',
        '12': 'c',
        '13': 'd',
        '14': 'e',
        '15': 'f',
        '16': 'g',
        '17': 'h',
        '18': 'i',
        '19': 'j',
        '20': 'k',
        '21': 'l',
        '22': 'm',
        '23': 'n',
        '24': 'o',
        '25': 'p',
        '26': 'q',
        '27': 'r',
        '28': 's',
        '29': 't',
        '30': 'u',
        '31': 'v',
        '32': 'w',
        '33': 'x',
        '34': 'y',
        '35': 'z',
        '36': 'A',
        '37': 'B',
        '38': 'C',
        '39': 'D',
        '40': 'E',
        '41': 'F',
        '42': 'G',
        '43': 'H',
        '44': 'I',
        '45': 'J',
        '46': 'K',
        '47': 'L',
        '48': 'M',
        '49': 'N',
        '50': 'O',
        '51': 'P',
        '52': 'Q',
        '53': 'R',
        '54': 'S',
        '55': 'T',
        '56': 'U',
        '57': 'V',
        '58': 'W',
        '59': 'X',
        '60': 'Y',
        '61': 'Z',
        }

def shortened(num):
    r"""
        Given a numeric value that could be a database
        tuple key, the function returns an up to 4 character string

        >>> shortened(35)
        'z'
        >>> shortened(0)
        '0'
        >>> shortened(14776335)
        'ZZZZ'
        >>> shortened(14776336)
    """
    digit = []
    shotened_string = ''
    first_time = True

    while first_time or num  > 0:
        if len(digit) >= 4:
            return None

        first_time = False
        remain = num % 62
        digit.append(remain)
        num = num / 62

    digit.reverse()

    for each in digit:
        shotened_string += MAPPING[str(each)]

    return shotened_string

def expanded(string):
    r"""
        Given a string up to 4 character
        the function returns it equivalent
        tuple database primary key

        >>> expanded('z')
        35
        >>> expanded('0')
        0
        >>> expanded('ZZZZ')
        14776335
        >>> expanded('10000')
    """
    digit = []

    if len(string) > 4:
        return None

    for each in string:
        digit.append(int([k for k, v in MAPPING.iteritems() if v == each][0]))

    digit.reverse()
    res = 0
    if digit:
        for ind in range(len(digit), 0, -1):
            res += digit[ind - 1] * (62**(ind - 1)) 

    return res

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__': _test()
