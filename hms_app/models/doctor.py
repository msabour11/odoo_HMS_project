from odoo import fields,models

class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Doctor'
    fname = fields.Char('First Name')
    lname = fields.Char('Last Name')
    image=fields.Binary('Image')
    patient_ids = fields.Many2many('hms.patient', string='Patients')
