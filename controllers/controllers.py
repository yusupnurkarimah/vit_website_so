# -*- coding: utf-8 -*-
import logging
from odoo import http
from odoo.http import request
import simplejson

logger = logging.getLogger(__name__)

class VitWebsiteSo(http.Controller):
    @http.route('/vit/so', type='http', auth='public', website=True)
    def index(self, **kw):
        sale_orders = request.env['sale.order'].search([])
        return request.render("vit_website_so.index",{
            "sale_orders" : sale_orders
        })

    # @http.route('/vit/so_ajax', type='http', auth='public', website=True)
    # def index_ajax(self, **kw):
    #     return request.render("vit_website_so.index_ajax",{
    #         })
    
    # @http.route('/vit/load_ajax', type='http', auth='public', website=True)
    # def load_ajax(self, **kw):
    #     sale_orders = request.env['sale.order'].search([])
        
    #     result = {}
    #     result['data'] = []

    #     for so in sale_orders:
    #         result['data'].append([
    #             so.name,
    #             so.confirmation_date,
    #             so.partner_id.name,
    #             so.user_id.name,
    #             so.amount_total,
    #             so.invoice_status
    #         ])

    #     return simplejson.dumps(result)


#     @http.route('/vit_website_so/vit_website_so/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_website_so.listing', {
#             'root': '/vit_website_so/vit_website_so',
#             'objects': http.request.env['vit_website_so.vit_website_so'].search([]),
#         })

#     @http.route('/vit_website_so/vit_website_so/objects/<model("vit_website_so.vit_website_so"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_website_so.object', {
#             'object': obj
#         })