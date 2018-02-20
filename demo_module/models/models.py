# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

class demo_module(models.Model):
    _name = 'demo.module'

    @api.depends('value1','value2')
    def _value_sum(self):
        # self.value2 = float(self.value) / 100
        self.sum = self.value1 + self.value2
        return sum

    @api.depends('dob')
    def _age_diff(self):
        if self.dob:
            d1 = datetime.strptime(self.current_date, "%Y-%m-%d")
            d2 = datetime.strptime(self.dob, "%Y-%m-%d")
            self.current_age = (d1 - d2).days / 365.25
        return self.current_age


    # name = fields.Char()
    partner_id = fields.Many2one('res.partner')
    mobile = fields.Char(related="partner_id.mobile")
    email = fields.Char(related="partner_id.email")
    value1 = fields.Integer()
    value2 = fields.Integer()
    sum = fields.Float(compute="_value_sum", store=True)
    current_date = fields.Date(string='Current Date', default=lambda self: fields.Datetime.now())
    dob = fields.Date(string="DOB")
    current_age = fields.Integer(string="Current Age", compute="_age_diff", store=True)
    description = fields.Text()


class ProductTemplate(models.Model):
    _inherit = 'product.template'





