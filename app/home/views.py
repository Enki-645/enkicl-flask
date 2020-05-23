from flask import jsonify
from app.models import Magnet
from app import api
from flask_restful import reqparse, abort, Resource
import operator



class MagnetList(Resource):
    """
    磁力链接
    """
    def get(self, title, ordering='create_time', page=1):
        # 页码错误处理
        try:
            page = int(page)
        except ValueError:
            abort(404)

        title = title
        # 从数据库获取磁力列表
        magnet_list = Magnet.query.filter(
            Magnet.title.ilike('%' + title + '%'),
        ).order_by(
            Magnet.create_time.desc()
        ).all()
        # 获取结果转化字典，将字典加入列表
        date_list = []
        for v in magnet_list:
            date_list.append(v.to_dict())

        # 获取总数
        count = len(magnet_list)

        # 对结果进行排序
        if ordering in ['create_time', 'file_size']:
            date_list = sorted(date_list, key=operator.itemgetter(ordering), reverse=True)
        else:
            abort(404)
        # 数据序列化
        date = {
            'count': count,
            'results': date_list[page*10-9: page*10],
        }
        return jsonify(date)

    def post(self):
        pass

class MagnetDetail(Resource):
    """
    磁力详情
    """
    def get(self, id):
        magnet_id = id
        magnet = Magnet.query.filter(
            Magnet.id==magnet_id
        ).first()
        date = magnet.to_dict()
        # 数据序列化
        date = {
            'results': date,
        }
        return jsonify(date)



api.add_resource(MagnetList, '/api/magnet/<title>/<ordering>/<page>')
api.add_resource(MagnetDetail, '/api/magnet/<id>')