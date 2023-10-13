from odoo import api, fields, models, _

class SuratIjin(models.Model):
    _name = "surat.ijin"
    _description = "Surat Ijin Berobat"

    name = fields.Char(string='Nama Pasien', required=True)
    nip = fields.Integer(string='NIP')
    tanggal = fields.Date(string='Tanggal')
    posisi = fields.Text(string='Job Position')
    kode_work_center = fields.Char(string='Kode Work Center')
    no_kartu = fields.Integer(string='Nomor Kartu')
    keluhan = fields.Text(string='Keluhan Penyakit')
    
   