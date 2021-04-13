# -*- coding: utf-8 -*-
###################################################################################
#
#    Shorepointsystem Private Limited
#    Author: Roja (11-02-20)
#
#
###################################################################################
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class POReportTemplate(models.Model):
    _name = 'po.report.template'
    _description = 'Purchase Order Report Template'

    name = fields.Char('Template Name', required=True)
    report_attribute_line_ids = fields.Many2many('product.attribute', string='Report Product Attributes', copy=True)
    layout_id = fields.Many2one('ir.ui.view', string='Report Layout')
    



