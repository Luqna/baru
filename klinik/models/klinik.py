from odoo import api, fields, models, _

class SuratIjin(models.Model):
    _name = "surat.ijin"
    _description = "Surat Ijin Berobat"

    name = fields.Char(string='Nama Pasien', required=True)
    nip = fields.Char(string='NIP')
    tanggal = fields.Date(string='Tanggal')
    posisi = fields.Text(string='Job Position')
    kode_work_center = fields.Char(string='Kode Work Center')
    no_kartu = fields.Char(string='Nomor Kartu')
    keluhan = fields.Text(string='Keluhan Penyakit')
    rujukan = fields.Text(string='Rumah Sakit Rujukan')
    state = fields.Selection([ 
        ('inprogress', 'Inprogress'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='inprogress', tracking=True)
    tahap_waktu_berobat = fields.Selection([
        ('kamar_kartu', 'Kamar Kartu'),
        ('poli_umum', 'Poli Umum'),
        ('poli_gigi', 'Poli Gigi'),
        ('poli_paru', 'Poli Paru'),
        ('poli_kb', 'Poli KB/BKIA'), 
        ('kamar_dokter', 'Kamar Dokter'),
        ('laboratorium', 'Laborotarium'),
        ('ugada', 'UGADA/CHIRURGIE'),
        ('kamar_suntik', 'Kamar Suntik'),
        ('kamar_rontgen', 'Kamar Rontgen'),
        ('kamar_keuring', 'Kamar Keuring'),
        ('mrs./opname', 'MRS./OPNAME'),
        ('apotik', 'Apotik')
        ], string="Tahap Waktu Berobat") 
    checkup = fields.Date(string='Tanggal Checkup')
    jam = fields.Datetime(string="Jam")
    diagnosa = fields.Text(string="Diagnosa")


    # surat_ijin_ids = fields.One2many('surat.ijin.line', 'tahap_waktu_berobat', string="Problems")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'
    
    def action_inprogress(self):
        self.state = 'inprogress'

    def action_cancel(self):
        self.state = 'cancel'

