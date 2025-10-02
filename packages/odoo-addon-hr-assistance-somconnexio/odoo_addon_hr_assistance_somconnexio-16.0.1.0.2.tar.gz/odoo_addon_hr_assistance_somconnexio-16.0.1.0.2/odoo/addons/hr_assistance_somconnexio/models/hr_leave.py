from odoo import models


class HolidaysRequest(models.Model):
    _inherit = "hr.leave"

    def _get_leaves_on_public_holiday(self):
        """
        Overwrite to allow employees to request leaves on public holidays
        """
        return False
