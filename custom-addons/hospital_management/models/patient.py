from odoo import models, fields, api

<<<<<<< HEAD
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string='Blood Group')
    notes = fields.Text(string='Medical Notes')
    active = fields.Boolean(default=True)
    
    appointment_ids = fields.One2many(
        'hospital.appointment',
        'patient_id',
        string='Appointments'
    )

    # 🌟 الحقل الجديد لربط المريض بجدول الـ ERP الأساسي للعملاء
    partner_id = fields.Many2one('res.partner', string='Contact', ondelete='cascade')

    # 🌟 الدالة السحرية لإنشاء كرت العميل (Customer) تلقائياً بالخلفية فور الضغط على حفظ المريض
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('partner_id') and vals.get('name'):
                partner = self.env['res.partner'].sudo().create({
                    'name': vals['name'],
                    'phone': vals.get('phone'),
                    'email': vals.get('email'),
                })
                vals['partner_id'] = partner.id
        return super(HospitalPatient, self).create(vals_list)
=======

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Patient Name", required=True)

    age = fields.Integer(string="Age")

    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        string="Gender"
    )

    phone = fields.Char(string="Phone")

    email = fields.Char(string="Email")

    address = fields.Text(string="Address")

    blood_group = fields.Selection(
        [
            ("a+", "A+"),
            ("a-", "A-"),
            ("b+", "B+"),
            ("b-", "B-"),
            ("ab+", "AB+"),
            ("ab-", "AB-"),
            ("o+", "O+"),
            ("o-", "O-"),
        ],
        string="Blood Group",
    )

    notes = fields.Text(string="Medical Notes")

    active = fields.Boolean(default=True)

    partner_id = fields.Many2one("res.partner", string="Customer")

    appointment_ids = fields.One2many(
        "hospital.appointment",
        "patient_id",
        string="Appointments"
    )

    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:
            partner = self.env["res.partner"].create({
                "name": vals.get("name"),
                "phone": vals.get("phone"),
                "email": vals.get("email"),
            })

            vals["partner_id"] = partner.id

        return super().create(vals_list)
>>>>>>> partner/main
