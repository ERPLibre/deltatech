# -*- coding: utf-8 -*-
# ©  2015-2019 Deltatech
# See README.rst file on addons root folder for license details

from odoo import _, api, fields, models
from email.utils import formataddr
from odoo.exceptions import UserError, AccessError


class Message(models.Model):
    _inherit = 'mail.message'

    @api.model
    def _get_default_from(self):
        use_company_email = self.env["ir.config_parameter"].sudo().get_param("mail.use_company_email")
        if not use_company_email:
            return super(Message, self)._get_default_from()
        if self.env.user.company_id.email:
            return formataddr((self.env.user.company_id.name, self.env.user.company_id.email))
        raise UserError(_("Unable to post message, please configure the company's email address."))
