from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    fix_recipient_address_mail_tracking(cr)


def fix_recipient_address_mail_tracking(cr):
    """TODO: add docstring"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    emails_to_fix = env["mail.tracking.email"].search(
        [("recipient_address", "=", False)]
    )
    emails_to_fix._compute_recipient_address()
