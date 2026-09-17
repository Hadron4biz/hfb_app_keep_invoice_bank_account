# -*- coding: utf-8 -*-
#################################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2017-2026 Hadron for Business sp. z o.o. (http://hadronforbusiness.com)
#
# This program is proprietary software, licensed under the Odoo Proprietary
# License v1.0 (OPL-1). Its use is governed by the Odoo Apps terms available
# at https://www.odoo.com/documentation/user/legal/licenses.html and the
# license agreement accepted at purchase / installation.
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the
# Software or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in
# all copies or substantial portions of the Software.
#
#################################################################################
""" @version	17.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.09.17

	Keep Invoice Bank Account
	Stops Odoo core from silently overwriting a manually chosen recipient
	bank account on an invoice/bill whenever a recompute dependency changes
	(e.g. the partner). Once partner_bank_id is set by hand, it is left
	alone until someone clears it.
"""
from odoo import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _compute_partner_bank_id(self):
        """Core Odoo always overwrites partner_bank_id with the partner's
        first bank account whenever anything in the compute's dependencies
        changes (the partner itself, among others) - wiping out a manual
        choice of a different account in the process. Here we simply skip
        the recompute for records that already have the field set - the
        manual choice sticks until someone clears it.
        """
        already_set = self.filtered('partner_bank_id')
        to_compute = self - already_set
        super(AccountMove, to_compute)._compute_partner_bank_id()

#EoF
