from odoo import fields, models, api,_


class Company(models.Model):
    _inherit="hr.news"

    

    def cancel_pay(self):
        for line in self:
            if line.state=="draft":
                line.button_to_approve()
                line.button_approved()

            

   