# coding=utf-8
import json

from django.http import HttpResponse


def format_to_json(code, msg='', data=''):
    return json.dumps({'code': code, 'msg': msg, 'data': data})


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def response_json(code, msg='', data=''):
    return HttpResponse(format_to_json(code, msg=msg, data=data),
                        content_type='application/ajax')
