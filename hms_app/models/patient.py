import datetime

from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'
    _order = 'fname'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _sql_constraints = [
        ('fname_unique', 'unique(fname)', 'fname  should be unique.'),
    ]
    fname = fields.Char('First Name', required=True, copy=0, tracking=1)
    lname = fields.Char('Last Name', required=True)
    birth_date = fields.Date('Birth')
    age = fields.Integer('Age', compute='_compute_age')
    address = fields.Char('Address')
    image = fields.Binary('Image')
    blode = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], string='Blod')
    pcr = fields.Boolean('PCR')
    cr = fields.Float('CR Ratio')
    state = fields.Selection([
        ('UN', 'Undetermined'),
        ('G', 'Good'),
        ('F', 'Fair'),
        ("S", "Serious")
    ], defualt="UN")
    history = fields.Html('History')
    department_id = fields.Many2one('hms.department', string='Department')
    department_capacity = fields.Integer(string='Department Capacity', related='department_id.capacity')
    doctor_ids = fields.Many2many('hms.doctor', string='Doctors')
    doctor_fnames = fields.Char(string='Doctor First Names', related='doctor_ids.fname')
    birth_date = fields.Date(string='Birth Date')
    ref = fields.Char('Ref. No.', copy=False, default='new')
    email = fields.Char(string='Email', unique=True)
    line_ids = fields.One2many('hms.patient.line', 'patient_id')

    # doctor_lnames = fields.Text(string='Doctor Last Names', related='doctor_ids.lname')
    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                birth_date = rec.birth_date
                today = fields.Date.today()
                delte = today - birth_date
                rec.age = delte.days // 365
            else:
                rec.age = 0

    # method to handle ref
    @api.model
    def create(self, vals):
        res = super(Patient, self).create(vals)
        res.ref = self.env['ir.sequence'].sudo().next_by_code('patient_ref_seq')
        return res


# hostory log
class PatientLine(models.Model):
    _name = 'hms.patient.line'
    _description = 'Patient Line'

    patient_id = fields.Many2one('hms.patient')

    fname = fields.Char('Name', required=1)
    birth_date = fields.Date()
    note = fields.Char()
