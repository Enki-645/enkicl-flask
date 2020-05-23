# coding: utf-8
from app.home.serialize import SerializrableMixin

from app import db



class Magnet(db.Model, SerializrableMixin):

    __tablename__ = 'magnet'

    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(255))
    magnet = db.Column(db.String(255))
    data_list = db.Column(db.String)
    create_time = db.Column(db.Date)
    file_count = db.Column(db.String(255))
    file_size = db.Column(db.String(255))
