# -*- coding: utf-8 -*-
###################################################################################
#
#    Shorepointsystem Private Limited
#    Author: Roja (09-03-21)
#
#
###################################################################################
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons.mail.models.mail_render_mixin import MailRenderMixin

class POPerformanceTest(models.Model):
    _name = 'po.performance.test'
    _description = 'Purchase Order Performance Testing Standards'
    _rec_name = 'name'
    _order = 'sequence'

    name = fields.Char('Test Reference', required=True)
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence')
    po_order_id = fields.Many2one('purchase.order', string='Purchase Order')
    requirements = fields.Char('Minimum Performance Requirements', required=True)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    performance_ids = fields.One2many('po.performance.test', 'po_order_id', string='Test Performance')
    inspection_html = fields.Html('Inspection', translate=True, sanitize=False)
    special_instruction_html = fields.Html('Special Instruction', translate=True, sanitize=False)
    other_details_html = fields.Html('Other Details', translate=True, sanitize=False)
    instruction_html = fields.Html('Instruction', translate=True, sanitize=False)
    season = fields.Char('Season')
    buyer_id = fields.Many2one('res.partner', string='Buyer')

    def get_office_details(self):
        if self.company_id.apply_parent_info and self.company_id.parent_id:
            return self.company_id.parent_id
        else:
            return self.company_id

    def render_html_content(self, rec):
        converted_content = MailRenderMixin._render_field(rec).render({
            'objects': self,
            'o': self,         
            })

        return converted_content

    def grp_lines_by_product_tmpl(self):
        grouped = dict()
        for line in self.order_line.filtered(lambda o: not o.display_type):  
            if line.product_id.product_tmpl_id.type != 'service':  
                key = (line.product_id.product_tmpl_id)
                grouped.setdefault(key, [])
                grouped[key].append(line)
        return grouped


    

