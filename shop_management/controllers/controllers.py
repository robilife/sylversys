# -*- coding: utf-8 -*-
from odoo import http

# class ShopManagement(http.Controller):
#     @http.route('/shop_management/shop_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shop_management/shop_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shop_management.listing', {
#             'root': '/shop_management/shop_management',
#             'objects': http.request.env['shop_management.shop_management'].search([]),
#         })

#     @http.route('/shop_management/shop_management/objects/<model("shop_management.shop_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shop_management.object', {
#             'object': obj
#         })