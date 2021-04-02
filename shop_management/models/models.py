# -*- coding: utf-8 -*-

from odoo import models, fields, api

 class shop_management(models.Model):
     _name = 'res.shop'

     name = fields.Char('Name')
     Localite = fields.Char('Localité')
     marchand_id = fields.Many2one('res.marchant')
            
 class ResPartnerInherit(models.Model):
    _inherit = "res.partner"
    _name = "res.marchant"