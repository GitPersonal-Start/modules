from odoo import models, fields, api
class producto(models.Model):
    _name = 'mgpp.producto'
    _inherit = ['stock.picking']

    name = fields.Char(string='Nombre del Producto', required=True)
    lot_id = fields.Many2one('stock.production.lot', string='Lote')
    fecha_caducidad = fields.Date(string='Fecha de Caducidad', required=True)
    precio_original = fields.Float(string='Precio Original', required=True)
    estado = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('descuento', 'Con Descuento'),
        ('agotado', 'Agotado'),
        ('vendido', 'Vendido')
    ], string='Estado del Producto', default='nuevo')
    rebaja_aplicada = fields.Boolean(string='Rebaja Aplicada', default=False)
    rebaja_porcentaje = fields.Float(string='Porcentaje de Rebaja')
    # ciclo_alerta = fields.Many2one('gestion.ciclo.rebajas', string='Ciclo de Rebaja')
    usuario_registro = fields.Many2one('res.users', string='Registrado por', required=True)

    def aplicar_rebaja(self):
        # Lógica para aplicar rebajas automáticas
        pass

    def verificar_caducidad(self):
        # Lógica para verificar productos próximos a vencer
        pass

    def generar_codigo_23(self):
        # Lógica para generar código único
        pass
