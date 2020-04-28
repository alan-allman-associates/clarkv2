# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Speed(models.Model):
    """
    """
    _name = "speed"
    _description = "Datas speed"
    _rec_name = "user_id"

    user_id = fields.Many2one('res.users', string="User")
    partner_id = fields.Many2one('res.partner', related='user_id.partner_id', string="Partner", store=True, compute_sudo=True)
    event_ids = fields.One2many('calendar.event', 'speed_id', string="Speeds")
    year = fields.Integer(string="Year")
    month = fields.Integer(string="Month")
    week = fields.Integer(string="Week")
    speed_week = fields.Integer(compute='_compute_speed_week', string="Speed", store=True, compute_sudo=True)
    prospecting = fields.Integer(compute='_compute_speed_week', string="Prospecting", store=True, compute_sudo=True)
    candidate = fields.Integer(compute='_compute_speed_week', string="Candidate", store=True, compute_sudo=True)
    qualification = fields.Integer(compute='_compute_speed_week', string="qualification", store=True, compute_sudo=True)
    commercial = fields.Integer(compute='_compute_speed_week', string="Commercial", store=True, compute_sudo=True)
    project = fields.Integer(compute='_compute_speed_week', string="Project", store=True, compute_sudo=True)

    @api.multi
    @api.depends('event_ids', 'event_ids.categ_ids', 'event_ids.user_id',
                 'event_ids.start_datetime', 'event_ids.speed_id')
    def _compute_speed_week(self):
        for speed in self:
            vals = {'project': 0,
                    'commercial': 0,
                    'qualification': 0,
                    'candidate': 0,
                    'prospecting': 0,
                    'speed_week': 0}
            for event in speed.event_ids:
                coefficient = event.coefficient or 0
                vals['speed_week'] += coefficient
                speed_type = event.categ_ids.speed_type
                if speed_type:
                    vals[speed_type] += coefficient
            speed.update(vals)