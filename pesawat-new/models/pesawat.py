from odoo import api, fields, models, _
from odoo import models, fields, api


class PenumpangPesawat(models.Model):
    _name = "penumpang.pesawat"
    _description = "Penumpang Pesawat"

    name = fields.Char(string='Nama', required=True, tracking = True)
    reference = fields.Char(string='reference', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New'))
    tanggal = fields.Date(string='Tanggal Penerbangan')
    umur = fields.Integer(string='Umur')
    gender = fields.Selection([
        ('male','Laki-laki'),
        ('female', 'Perempuan')], 
        required=True, default = 'male')
    
    asal = fields.Selection([
        ('surabaya','Surabaya'),
        ('tarakan', 'Tarakan'),
        ('jakarta','Jakarta'),
        ('bandung','Bandung')], 
        required=True, default = 'surabaya')

    tujuan = fields.Selection([
        ('surabaya','Surabaya'),
        ('tarakan', 'Tarakan'),
        ('jakarta','Jakarta'),
        ('bandung','Bandung')], 
        required=True, default = 'jakarta')

    kelas = fields.Selection([
            ('ekonomi','Kelas Ekonomi'),
            ('bisnis', 'Kelas Bisnis'),
            ('first','Kelas first')], 
            required=True, default = 'bisnis')
    

    plane = fields.Selection([
        ('garuda','Garuda Indonesia - GI123'),
        ('airasia', 'Air Asia - AA234'),
        ('superjet','Super Jet - SJ876'),
        ('citilink','Citilink - CL870')], 
        required=True, default = 'airasia')
    
    
    note = fields.Text(string='Description')
    state = fields.Selection([('draft','Draft'), ('done','Done'), ('cancel','Cancel')], default='draft', string="Status")

    def action_confirm(self):
        self.state = 'done'
    
    def action_cancel(self):
        self.state = 'cancel'

    def action_done(self):
        self.state = 'done'
    
    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state ='cancel'
        
    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New'
        if vals.get('reference', _('New'))== _('New'):
            #vals['reference'] = self.env['ir.sequence'].next_by_code('penumpang.pesawat') or 'New'
            vals['reference'] = self.env["ir.sequence"].next_by_code('penumpang.pesawat') or _('New')
        res = super(PenumpangPesawat, self).create(vals)
        return res 
