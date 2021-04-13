# -*- coding: utf-8 -*-
###################################################################################
#
#    Shorepointsystem Private Limited
#    Author: Roja (08-03-21)
#
#
###################################################################################
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductPerformanceTest(models.Model):
    _name = 'product.performance.test'
    _description = 'Product Performance Testing Standards'
    _rec_name = 'name'
    _order = 'sequence'

    name = fields.Char('Test Reference', required=True)
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence')
    product_categ_id = fields.Many2one('product.category', string='Product Category')
    requirements = fields.Char('Minimum Performance Requirements', required=True)



class ProductCategory(models.Model):
    _inherit = 'product.category'


    performance_test_ids = fields.One2many('product.performance.test', 'product_categ_id', string='Product Test Standards')
    inspection_html = fields.Html('Inspection', translate=True, sanitize=False)
    special_instruction_html = fields.Html('Special Instruction', translate=True, sanitize=False)
    other_details_html = fields.Html('Other Details', translate=True, sanitize=False)
    instruction_html = fields.Html('Instruction', translate=True, sanitize=False)
