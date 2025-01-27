# coding: utf-8

# maposmatic, the web front-end of the MapOSMatic city map generation system
# Copyright (C) 2009  David Decotigny
# Copyright (C) 2009  Frédéric Lehobey
# Copyright (C) 2009  David Mentré
# Copyright (C) 2009  Maxime Petazzoni
# Copyright (C) 2009  Thomas Petazzoni
# Copyright (C) 2009  Gaël Utard

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, sys

sys.path.append("/home/maposmatic/maposmatic")
sys.path.append("/home/maposmatic/ocitysmap")

os.environ["DJANGO_SETTINGS_MODULE"] = 'www.settings'
os.environ["MAPOSMATIC_LOG_FILE"] = "/tmp/maposmatic-www.log"
os.environ["PGCONNECT_TIMEOUT"] = 1

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
