# coding=utf-8
import json

from django.db import connection
from django.http import HttpResponse

# Create your views here.


# cursor=connection.cursor()
# #插入操作
# cursor.execute("insert into hello_author(name) values('郭敬明')")
# #更新操作
# cursor.execute('update hello_author set name='abc' where name='bcd'')
# #删除操作
# cursor.execute('delete from hello_author where name='abc'')
# #查询操作
# cursor.execute('select * from hello_author')
# raw=cursor.fetchone() #返回结果行游标直读向前，读取一条
# cursor.fetchall() #读取所有


# 200 ok - 成功状态，对应，GET,PUT,PATCH,DELETE.
# 500 faild - 失败状态
# 304 not modified - HTTP缓存有效。
# 400 bad request - 请求格式错误。可以标识参数错误或参数缺失
# 401 unauthorized - 未授权。
# 403 forbidden - 鉴权成功，但是该用户没有权限。
# 404 not found - 请求的资源或接口不存在
# 405 method not allowed - 该http方法不被允许。
# 410 gone - 这个url对应的资源现在不可用。
# 415 unsupported media type - 请求类型错误。
# 422 unprocessable entity - 校验错误时用。
# 429 too many request - 请求过多。
from django.views.generic import View

from main.utils import dictfetchall, format_to_json


def get_poem_by_title(request):
    title = request.GET.get('title', '')

    page = request.GET.get('page', '1')
    limit = request.GET.get('limit', '10')

    start_raw = int(limit) * (int(page) - 1)

    cursor = connection.cursor()
    cursor.execute(
        "select * from poems where title='{title}' limit {start},{end} ".format(
            title=title, start=start_raw, end=limit))

    all = dictfetchall(cursor)
    cursor.close()

    print(all)

    json_data = format_to_json(200, data=all)

    return HttpResponse(json_data, content_type='application/ajax')



