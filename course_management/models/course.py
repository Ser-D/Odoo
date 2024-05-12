from odoo import models, fields, api


class Course(models.Model):
    _name = 'course'
    _description = 'The best of the best course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    teacher_id = fields.Many2one(comodel_name='res.partner', string='Teacher', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    duration = fields.Integer(string='Duration (days or hours)', required=True)
    participant_ids = fields.One2many(comodel_name='participant', inverse_name='course_id')
    lesson_ids = fields.One2many(comodel_name='lesson', inverse_name='course_id')


# @api.depends
# @api.onchange
# @api.constrains
