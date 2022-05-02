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

class ResPartner(models.Model):
    _inherit = 'res.partner'

    po_report_template_id = fields.Many2one('po.report.template', string='PO Report Template')
