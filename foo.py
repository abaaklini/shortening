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
import shortening as sho

print '----------------------------------------'
print '    Value   |    Short   |    Expanded  '

for ind in range(14776336):
    short = sho.shortened(ind)
    expan = sho.expanded(short)
    print '----------------------------------------'
    print ' '+str(ind)+'  |   '+short+'  |  '+str(expan)

