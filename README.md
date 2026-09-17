# Keep Invoice Bank Account

Stops Odoo from silently resetting a manually chosen **Recipient Bank**
account on an invoice/bill.

## The problem

Core Odoo recomputes `partner_bank_id` on `account.move` every time a
dependency changes - most commonly the partner. That recompute always picks
the partner's *first* bank account, overwriting whatever a user deliberately
selected instead.

## How it works

`account.move._compute_partner_bank_id()` is patched to skip records that
already have `partner_bank_id` set - the field is left alone until someone
clears it by hand, at which point Odoo's normal computation takes over again.

## Technical

- `models/account_move_bank.py` - `account.move._compute_partner_bank_id()`
  override.
- No new models, no views, no data, no security rules.
- Depends on: `account`.

## Status

Extracted from a client-specific module (`hfb_bannerstop_invoice_total`) as
part of the generic app extraction workflow. Missing
`static/description/icon.png` (and optionally a `*_screenshot.png`) before
it can be submitted to Odoo Apps.
