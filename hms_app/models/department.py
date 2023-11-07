from odoo import models,fields

class Department(models.Model):
    _name='hms.department'
    _description = 'Department'
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Department Name should be unique.'),
    ]
    name=fields.Char('Department Name')
    capacity=fields.Integer('Capacity')
    is_open=fields.Boolean('Is open?')
    patient_ids=fields.One2many('hms.patient','department_id',string='Patient')
