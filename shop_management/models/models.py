# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import requests
import logging
from odoo.exceptions import ValidationError
_logger = logging.getLogger('__name__')

class shopManagement(models.Model):
    _name = 'res.shop'

    name = fields.Char('Name', required=True)
    localite = fields.Char('Localité')
    marchand_id = fields.Many2one('res.marchand', required=True)
    
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('check', 'Vérifié'),
        ('validate', 'Validé'),
        ('active', 'Active'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    
    def send_to_fillout(self):
        for rec in self:
            rec.write({'state': 'draft'})
        
    def send_to_validate(self):
        for rec in self:
            rec.write({'state': 'validate'})
        
    def send_to_check(self):
        for rec in self:
            rec.write({'state': 'check'})
        
    def action_validate(self):
        for rec in self:
            response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
            if response.status_code == 200:
                rec.write({'state': 'active'})
            else:
                raise ValidationError(_("API ERROR, TRY AGAIN :-("))
            
class ResPartnerInherit(models.Model):
    _inherit = ['res.partner','portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _name = "res.marchand"
    
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('check', 'Vérifié'),
        ('validate', 'Validé'),
        ('active', 'Active'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    ref = fields.Char('Ref')
    
    def send_to_fillout(self):
        for rec in self:
            rec.write({'state': 'draft'})
        
    def send_to_validate(self):
        for rec in self:
            rec.write({'state': 'validate'})
        
    def send_to_check(self):
        for rec in self:
            rec.write({'state': 'check'})
        
    def action_validate(self):
        for rec in self:
            response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
            if response.status_code == 200:
                rec.write({'state': 'active'})
            else:
                raise ValidationError(_("API ERROR, TRY AGAIN :-("))
        
        
class SaleOrderInherit(models.Model):
    _inherit = "sale.order"
    
    marchand_id = fields.Many2one('res.marchand', string='Marchand', required=True)
    
    @api.model
    def create(self, values):
        res = super(SaleOrderInherit, self).create(values)
        if res.marchand_id.state != 'active':
            raise ValidationError(_("Vous ne pouvez pas creer de devis avec un marchand pas actif."))
        return res