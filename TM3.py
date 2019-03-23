#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     TM3.py
#

import os
from pagebot.themes import BackToTheCity
from css.nanostyle_css import cssPy
from pagebot.toolbox.color import spot, color
from pagebot.themes import FairyTales
from pagebot.publications import NanoSite

TM3_LOGO = spot(300)

class TM3_Theme(FairyTales):
    NAME = 'Type Magazine 3'
    BASE_COLORS = dict(
        #base2=color('#ACACB8'),
        #base3=TM3_LOGO,
        logo=TM3_LOGO,
    )

theme = TM3_Theme('light')

name = 'Type Magazine 3'
srcPath = [
    'FOB.md',
    'GerritNoordzij.md',
    'PublishingVariables12.md', # Get example markDown file from resources.
]
resourcePaths = ['css', 'images', 'fonts', 'js']

site = NanoSite(name=name, theme=theme)
doc = site.produce(srcPath, cssPy=cssPy, spellCheck=False, resourcePaths=resourcePaths)
