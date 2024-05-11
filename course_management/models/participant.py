from odoo import models, fields


class Participant(models.Model):
    _name = 'course_management.participant'
    _description = 'Course and Participant'

    name = fields.Char(string='Participant name', required=True)
    user_id = fields.Many2one('res.users', string='Users', required=True)
    course_id = fields.Many2one('course_management.course', string='Course', required=True)
