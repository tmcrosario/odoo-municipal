from odoo import models, fields, _


class BusinessCategory(models.Model):

    _name = 'municipal.business_category'
    _description = 'Business Category'

    name = fields.Char(required=True)

    color = fields.Char(default="0", readonly=True)

    _sql_constraints = [('name_unique', 'UNIQUE(name)',
                         _('Business Category must be unique'))]
