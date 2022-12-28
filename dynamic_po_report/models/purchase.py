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

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    inspection_html = fields.Html('Inspection', translate=True, sanitize=False)
    special_instruction_html = fields.Html('Special Instruction', translate=True, sanitize=False)
    other_details_html = fields.Html('Other Details', translate=True, sanitize=False)
    instruction_html = fields.Html('Instruction', translate=True, sanitize=False)
    season = fields.Char('Season')
    buyer_id = fields.Many2one('res.partner', string='Buyer')



    def _get_approver_lines(self):
        final_list = []
        if self.approver_ids:
            sub_lst = []
            for approver in self.approver_ids:
                if len(sub_lst) == 3:
                    final_list.append(sub_lst)
                    sub_lst = []
                else:
                    sub_lst.append(approver)
                    if len(sub_lst) == 3:
                        final_list.append(sub_lst)
                        sub_lst = []
        return final_list

    @api.onchange('partner_id')
    def onchange_partner_id_standards(self):
        if not self.partner_id:
            return
        if not self.partner_id.po_report_template_id:
            self.update({
                'inspection_html': False,
                'special_instruction_html': False,
                'other_details_html': False,
                'instruction_html': False,
            })
        else:
            self.update({
                'inspection_html': self.partner_id.po_report_template_id.inspection_html,
                'special_instruction_html': self.partner_id.po_report_template_id.special_instruction_html,
                'other_details_html': self.partner_id.po_report_template_id.other_details_html,
                'instruction_html': self.partner_id.po_report_template_id.instruction_html,
            })
        return {}

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


    

