#!/usr/bin/env python3
#
# Copyright (C) 2014-2015  Codethink Limited
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# =*= License: GPL-2 =*=

'''A module to build a definition.'''

import os
import sys
from definitions import Definitions
import cache
import app
from assembly import assemble
import sandbox

print
target = sys.argv[1]
arch = sys.argv[2]
with app.setup(target, arch):
    with app.timer('TOTAL', 'YBD starts'):
        with app.timer('DEFINITIONS', 'Parsing'):
            defs = Definitions()
        with app.timer('CACHE-KEYS', 'Calculating'):
            cache.get_cache(app.settings['target'])
        defs.save_trees()
        assemble(app.settings['target'])
app.log(app.settings['target'], 'Finished')
