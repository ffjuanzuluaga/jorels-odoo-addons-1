# -*- coding: utf-8 -*-
#
# Jorels S.A.S. - Copyright (2024)
#
# This file is part of l10n_co_freight_route.
#
# l10n_co_freight_route is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# l10n_co_freight_route is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with l10n_co_freight_route.  If not, see <https://www.gnu.org/licenses/>.
#
# email: info@jorels.com
#

from odoo import fields, models


class VehicleConfigurationSemitrailer(models.Model):
    _name = 'l10n_co_freight_route.configuration_semitrailer'
    _description = 'Vehicle Configuration Semitrailer'

    name = fields.Char(string='Name', required=True)
    configuration_id = fields.Many2one(comodel_name='l10n_co_freight_route.configuration', string="Configuration",
                                       required=True, index=True)
    semitrailer_id = fields.Many2one(comodel_name='l10n_co_freight_route.semitrailer', string="Semitrailer",
                                     required=True, index=True)
    max_weight = fields.Integer(string="Maximum weight", required=True)
    min_weight = fields.Integer(string="Minimum weight", required=True)
    minimum_gallons = fields.Integer(string="Minimum gallons", required=True)
    maximum_gallons = fields.Integer(string="Maximum gallons", required=True)
