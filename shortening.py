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

MAPEAR = {
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

def encurta(num):
    r"""
        Dado um valor numérico que pode ser o id de
        uma tupla de uma Base de Dados, retorna-se
        uma string de até 4 caracteres

        >>> encurta(35)
        'z'
        >>> encurta(0)
        '0'
        >>> encurta(14776335)
        'ZZZZ'
        >>> encurta(14776336)
    """
    digito = []
    string_encurtada = ''
    primeira_vez = True

    while primeira_vez or num  > 0:
        if len(digito) >= 4:
            return None

        primeira_vez = False
        resto = num % 62
        digito.append(resto)
        num = num / 62

    digito.reverse()

    for each in digito:
        string_encurtada += MAPEAR[str(each)]

    return string_encurtada

def expande(string):
    r"""
        Dado uma string de até 4 caracteres
        é feita a conversão para o seu equivalente 
        numérico na base decimal, que reflete um id
        de uma tupla presente na Base de Dados

        >>> expande('z')
        35
        >>> expande('0')
        0
        >>> expande('ZZZZ')
        14776335
        >>> expande('10000')
    """
    digito = []

    if len(string) > 4:
        return None

    for each in string:
        digito.append(int([k for k, v in MAPEAR.iteritems() if v == each][0]))

    digito.reverse()
    res = 0
    if digito:
        for ind in range(len(digito), 0, -1):
            res += digito[ind - 1] * (62**(ind - 1)) 

    return res

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__': _test()
