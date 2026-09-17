# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=0 shiftwidth=4 smarttab expandtab fileformat=unix
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
{
    'name': "Keep Invoice Bank Account",
    'summary': "Stop Odoo from resetting a manually picked bank account on invoices",
    'description': """
Keep Invoice Bank Account
==========================

Odoo recomputes the recipient bank account (Recipient Bank in the Other Info
tab) on every invoice/bill whenever a dependency changes - most commonly the
partner - always resetting it to the partner's first bank account. If someone
picked a *different* one on purpose, that choice silently disappears.

This app leaves a manually chosen bank account alone: once it's set, it's
never recomputed until someone clears it themselves.
""",
    'version': "17.0.1.0.0",
    'author': "Hadron for Business sp. z o.o.",
    'website': "http://hadronforbusiness.com",
    'license': "OPL-1",
    'category': "Accounting/Accounting",
    'depends': [
        'account',
    ],
    'data': [],
    'installable': True,
    'application': False,
}
