from odoo import models, fields


class HospitalMedicalSupply(models.Model):
    _name = "hospital.medical.supply"
    _description = "Hospital Medical Supply"

    name = fields.Char(
        string="Supply Name",
        required=True
    )

    supply_type = fields.Selection([
        ("medicine", "Medicine"),
        ("equipment", "Equipment"),
        ("consumable", "Consumable"),
    ], string="Type", default="medicine", required=True)

    quantity = fields.Float(
        string="Quantity",
        default=1.0
    )

    unit = fields.Char(string="Unit of Measure")

    appointment_id = fields.Many2one(
        "hospital.appointment",
        string="Appointment",
        ondelete="cascade"
    )

    notes = fields.Text(string="Notes")