from odoo import models, fields, api


class Participant(models.Model):
    _name = 'participant'
    _description = 'Course and Participant'

    status = fields.Selection(selection=[('draft', 'Draft'), ('done', 'Done')], default='draft')
    name = fields.Char(string='Participant name')
    user_id = fields.Many2one(comodel_name='res.partner', string='User', required=True)
    course_id = fields.Many2one(comodel_name='course', string='Course', required=True)

    @api.model
    def create(self, vals_list):
        vals_list['status'] = 'done'
        if user_id := vals_list.get('user_id'):
            user = self.env['res.partner'].browse(user_id)
            vals_list['name'] = user.name if user else ''
        return super().create(vals_list)





