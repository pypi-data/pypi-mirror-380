from odoo import models
from datetime import date


class PaymentReturn(models.Model):
    _inherit = "payment.return"

    def action_confirm(self):
        activity_type_dict = {}
        invoices = self.env["account.move"].browse()
        for return_line in self.line_ids:
            for move_line in return_line.move_line_ids:
                returned_moves = move_line.matched_debit_ids.mapped("debit_move_id")
                invoices |= returned_moves.mapped("move_id")
        for invoice in invoices:
            if invoice.returned_payment:
                activity_type_dict[invoice.id] = self.env.ref(
                    "somconnexio.return_activity_type_n"
                )
            else:
                activity_type_dict[invoice.id] = self.env.ref(
                    "somconnexio.return_activity_type_1"
                )
        super().action_confirm()
        for invoice in invoices:
            invoice._compute_last_return_amount()
            activity_type = activity_type_dict[invoice.id]
            activity = self.env["mail.activity"].create(
                {
                    "res_id": invoice.id,
                    "res_model_id": self.env["ir.model"]
                    .search([("model", "=", "account.move")])
                    .id,
                    "user_id": self.env.user.id,
                    "activity_type_id": activity_type.id,
                }
            )
            if activity_type == self.env.ref("somconnexio.return_activity_type_1"):
                activity.write({"date_done": date.today()})
                activity.action_done()
                if invoice.journal_id == (
                    self.env.ref("somconnexio.subscription_journal")
                ):
                    template = self.env.ref(
                        "somconnexio.invoice_claim_1_capital_template"
                    )
                else:
                    template = self.env.ref("somconnexio.invoice_claim_1_template")
                template.send_mail(invoice.id, False)
        return True
