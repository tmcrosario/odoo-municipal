# -*- coding: utf-8 -*-

from odoo import models, fields, _


class BusinessCategory(models.Model):

    _name = 'municipal.business_category'

    name = fields.Char(
        required=True
    )

    _sql_constraints = [(
        'name_unique',
        'UNIQUE(name)',
        _('Business Category must be unique')
    )]
