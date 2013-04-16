# Copyright (c) 2013 - Network Box
#
# This file is part of Uptrack.
#
# Uptrack is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Uptrack is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Uptrack.  If not, see <http://www.gnu.org/licenses/>.


import colander
import deform

class ReleaseSchema(colander.Schema):
    id = colander.SchemaNode(colander.Integer(),
                             widget=deform.widget.HiddenWidget(),
                             missing=colander.null)
    name = colander.SchemaNode(colander.String())
    koji_tag = colander.SchemaNode(colander.String())
    git_url = colander.SchemaNode(colander.String(), title="Git URL")


class UpstreamSchema(colander.Schema):
    id = colander.SchemaNode(colander.Integer(),
                             widget=deform.widget.HiddenWidget(),
                             missing=colander.null)
    name = colander.SchemaNode(colander.String())
    base_url = colander.SchemaNode(colander.String(), title="Base URL")


class UserSchema(colander.Schema):
    id = colander.SchemaNode(colander.Integer(),
                             widget=deform.widget.HiddenWidget(),
                             missing=colander.null)
    login = colander.SchemaNode(colander.String())
    name = colander.SchemaNode(colander.String())
    email = colander.SchemaNode(colander.String())
    password = colander.SchemaNode(colander.String(),
                                   widget=deform.widget.PasswordWidget())
