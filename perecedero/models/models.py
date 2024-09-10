# -*- coding: utf-8 -*-
from odoo import models, fields, api
class almacen(models.Model):
    _inherit = 'stock.warehouse'

# class lote(models.Model):
#     _inherit = 'stock.production.lot'

class stock(models.Model):
    _inherit = 'res.company'

class categoria(models.Model):
    _inherit = 'product.category'

class categoria(models.Model):
    _inherit = 'product.product'