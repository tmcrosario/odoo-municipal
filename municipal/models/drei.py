from odoo import models, fields


class Drei(models.Model):

    _name = 'municipal.drei'
    _description = 'DREI Account Information'

    account = fields.Char(size=10, required=True)

    management_code = fields.Char(string='Personal Management Code', size=10)

    business_category_ids = fields.Many2many(
        string='Business Categories',
        comodel_name='municipal.business_category',
        required=True)

    partner_id = fields.Many2one(string='Merchant',
                                 comodel_name='res.partner',
                                 domain=[('merchant', '=', 'True')],
                                 required=True)
