from odoo import models, fields


class Course(models.Model):
    _name = 'course_management.course'
    _description = 'The best of the best course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    teacher_id = fields.Many2one('res.users', string='Teacher', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    duration = fields.Integer(string='Duration (days or hours)', required=True)
