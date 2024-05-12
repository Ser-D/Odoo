from datetime import datetime, timedelta

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Lesson(models.Model):
    _name = 'lesson'
    _description = 'Description'

    name = fields.Char(string='Lesson Name', required=True)
    course_id = fields.Many2one(comodel_name='course', string='Course', required=True)
    materials = fields.Text(string='Materials')
    start_date = fields.Date(string='Start Date', required=True)
    participant_ids = fields.One2many(comodel_name='lesson.line', inverse_name='lesson_id')

    @api.model
    def create(self, vals_list):

        return super().create(vals_list)

    @api.onchange('start_date')
    def onchange_start_date(self):
        course_id = self.course_id
        course_date = course_id.start_date
        course_duration = timedelta(days=course_id.duration)
        lesson_date = self.start_date
        if lesson_date:
            if not course_date <= lesson_date <= (course_date + course_duration):
                raise ValidationError('Date is not correct')


class LessonLine(models.Model):
    _name = 'lesson.line'
    _description = 'description'

    lesson_id = fields.Many2one(comodel_name='lesson')
    course_id = fields.Many2one(related='lesson_id.course_id')
    participant_id = fields.Many2one(comodel_name='participant',
                                     # domain=[('course_id', '=', course_id)]
                                     )
    rate = fields.Selection(selection=[
        ('none', 'None'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ], default='none')
