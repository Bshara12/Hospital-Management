from odoo import models, fields


class HospitalAppointment(models.Model):
    _inherit = "hospital.appointment"

    supply_ids = fields.One2many(
        "hospital.medical.supply",
        "appointment_id",
        string="Medical Supplies"
    )