#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:47'

"""
from collections import OrderedDict

from django.db import connection
from django.db.models import Case, IntegerField
from django.db.models import Sum
from django.db.models import Value
from django.db.models import When
from django.http import HttpResponse
from datetime import datetime, date, timedelta

from rest_framework import serializers

now = datetime.now()


def get_users(request):
    """
    查询用户姓名（按首字母排列，数字放在其他当中）

    :param request: HttpRequest
    :return: JSON data
    """
    with connection.cursor() as cursor:
        cursor.execute(('select user_id, name, role, work_phone, '
                        'ELT(INTERVAL(CONV(HEX(left(CONVERT(name USING gbk),1)),16,10),0xB0A1,'
                        '0xB0C5,0xB2C1,0xB4EE,0xB6EA,0xB7A2,0xB8C1,0xB9FE,0xBBF7, 0xBFA6,0xC0AC,'
                        '0xC2E8,0xC4C3,0xC5B6,0xC5BE,0xC6DA,0xC8BB,0xC8F6, 0xCBFA,0xCDDA,0xCEF4,'
                        '0xD1B9,0xD4D1), "A","B","C","D","E","F","G","H","J","K","L","M","N","O",'
                        '"P", "Q","R","S","T","W","X","Y","Z") as PY  FROM user_info '
                        ' order by convert(name using gbk) '
                        'COLLATE gbk_chinese_ci'), )
        res = {"#": [], "A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [],
               "H": [], "J": [], "K": [], "L": [], "M": [], "N": [], "O": [], "P": [],
               "Q": [], "R": [], "S": [], "T": [], "W": [], "X": [], "Y": [], "Z": []}
        row = cursor.fetchall()
        # 组合为JSON数据返回
        return HttpResponse()

# #############################################################################################
# 按天统计: Case, When
# queryset.aggregate(
#     Monday=Sum(Case(When(receive_time__date=dates[0], then=1),
#                     output_field=IntegerField(), default=Value(0))),
#     Tuesday=Sum(Case(When(receive_time__date=dates[1], then=1),
#                      output_field=IntegerField(), default=Value(0))),
#     Wednesday=Sum(Case(When(receive_time__date=dates[2], then=1),
#                        output_field=IntegerField(), default=Value(0))),
#     Thursday=Sum(Case(When(receive_time__date=dates[3], then=1),
#                       output_field=IntegerField(), default=Value(0))),
#     Friday=Sum(Case(When(receive_time__date=dates[4], then=1),
#                     output_field=IntegerField(), default=Value(0))),
#     Saturday=Sum(Case(When(receive_time__date=dates[5], then=1),
#                       output_field=IntegerField(), default=Value(0))),
#     Sunday=Sum(Case(When(receive_time__date=dates[6], then=1),
#                     output_field=IntegerField(), default=Value(0))),
# )


# #############################################################################################

# 按小时统计

# aggregate(
#     a=Sum(Case(When(receive_time__hour__lt=2, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     b=Sum(Case(When(receive_time__hour__lt=4, receive_time__hour__gte=2, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     c=Sum(Case(When(receive_time__hour__lt=6, receive_time__hour__gte=4, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     d=Sum(Case(When(receive_time__hour__lt=8, receive_time__hour__gte=6, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     e=Sum(Case(When(receive_time__hour__lt=10, receive_time__hour__gte=8, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     f=Sum(Case(When(receive_time__hour__lt=12, receive_time__hour__gte=10, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     g=Sum(Case(When(receive_time__hour__lt=14, receive_time__hour__gte=12, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     h=Sum(Case(When(receive_time__hour__lt=16, receive_time__hour__gte=14, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     i=Sum(Case(When(receive_time__hour__lt=18, receive_time__hour__gte=16, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     j=Sum(Case(When(receive_time__hour__lt=20, receive_time__hour__gte=18, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     k=Sum(Case(When(receive_time__hour__lt=22, receive_time__hour__gte=20, then=1),
#                output_field=IntegerField(), default=Value(0))),
#     l=Sum(Case(When(receive_time__hour__gte=22, then=1),
#                output_field=IntegerField(), default=Value(0))),
# )
# 然后根据字母排序

# ================> 同理：
'SELECT sss.timeBlock, sss.alarmtype, sum(sss.countvalue) as sumvalue \
FROM (SELECT "1:00-3:00" as timeBlock, "f" as alarmtype,0 as countvalue FROM DUAL  \
UNION SELECT "3:00-5:00" as timeBlock, "f" as alarmtype,0 as countvalue FROM DUAL \
UNION SELECT "5:00-7:00" as timeBlock, "f" as alarmtype,0 as countvalue FROM DUAL  \
UNION SELECT "7:00-9:00" as timeBlock, "f" as alarmtype,0 as countvalue FROM DUAL \
UNION SELECT "9:00-11:00" as timeBlock, "f" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "11:00-13:00" as timeBlock, "f" as alarmtype,0 as countvalue  FROM DUAL \
UNION SELECT "13:00-15:00" as timeBlock, "f" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "15:00-17:00" as timeBlock, "f" as alarmtype,0 as countvalue  FROM DUAL \
UNION SELECT "17:00-19:00" as timeBlock, "f" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "19:00-21:00" as timeBlock, "f" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "21:00-23:00" as timeBlock, "f" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "23:00-1:00" as timeBlock, "f" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "1:00-3:00" as timeBlock, "ff" as alarmtype,0 as countvalue FROM DUAL  \
UNION SELECT "3:00-5:00" as timeBlock, "ff" as alarmtype,0 as countvalue FROM DUAL  \
UNION SELECT "5:00-7:00" as timeBlock, "ff" as alarmtype,0 as countvalue FROM DUAL   \
UNION SELECT "7:00-9:00" as timeBlock, "ff" as alarmtype,0 as countvalue FROM DUAL   \
UNION SELECT "9:00-11:00" as timeBlock, "ff" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "11:00-13:00" as timeBlock, "ff" as alarmtype,0 as countvalue  FROM DUAL \
UNION SELECT "13:00-15:00" as timeBlock, "ff" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "15:00-17:00" as timeBlock, "ff" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "17:00-19:00" as timeBlock, "ff" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "19:00-21:00" as timeBlock, "ff" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "21:00-23:00" as timeBlock, "ff" as alarmtype,0 as countvalue  FROM DUAL  \
UNION SELECT "23:00-1:00" as timeBlock, "ff" as alarmtype,0 as countvalue  FROM DUAL   \
UNION SELECT st.timeBlock, st.alarmtype, COUNT(st.timeBlock) AS timeBlockCount \
FROM ( SELECT  case t.modHour when 0 then "23:00-1:00" when 1 then "1:00-3:00" \
when 2 then "1:00-3:00" when 3 then "3:00-5:00" when 4 then "3:00-5:00" when 5 then "5:00-7:00" \
when 6 then "5:00-7:00" when 7 then "7:00-9:00"  when 8 then "7:00-9:00" when 9 then "9:00-11:00" \
when 10 then "9:00-11:00" when 11 then "11:00-13:00" when 12 then "11:00-13:00"  \
when 13 then "13:00-15:00" when 14 then "13:00-15:00" when 15 then "15:00-17:00" \
when 16 then "15:00-17:00" when 17 then "17:00-19:00"  when 18 then "17:00-19:00" \
when 19 then "19:00-21:00" when 20 then "19:00-21:00" when 21 then "21:00-23:00" \
when 22 then "21:00-23:00"  when 23 then "23:00-1:00" end timeBlock, \
"f"   AS alarmtype from ( select substring(fi.receive_time,12,2)%%24 as modHour \
from rt_alarm fi, (SELECT dtu_id FROM relation_company_dtu WHERE company_id = %s)  dci  \
WHERE  fi.dtu_id = dci.dtu_id AND    fi.confirm_type = 1 \
AND EXTRACT(YEAR_MONTH FROM fi.receive_time) \
BETWEEN EXTRACT(YEAR_MONTH FROM date_sub(NOW(), INTERVAL 3 MONTH)) \
AND EXTRACT(YEAR_MONTH FROM date_sub(NOW(), INTERVAL 1 MONTH)) ) t  ) st  \
GROUP BY st.alarmtype, st.timeBlock \
UNION SELECT stf.timeBlock, stf.alarmtype, COUNT(stf.timeBlock) AS timeBlockCount \
FROM ( SELECT  case t.modHour when 0 then "23:00-1:00" when 1 then "1:00-3:00" \
when 2 then "1:00-3:00"  when 3 then "3:00-5:00" when 4 then "3:00-5:00" when 5 then "5:00-7:00" \
when 6 then "5:00-7:00" when 7 then "7:00-9:00"  when 8 then "7:00-9:00" when 9 then "9:00-11:00" \
when 10 then "9:00-11:00" when 11 then "11:00-13:00" when 12 then "11:00-13:00"  \
when 13 then "13:00-15:00" when 14 then "13:00-15:00" when 15 then "15:00-17:00" \
when 16 then "15:00-17:00" when 17 then "17:00-19:00"  when 18 then "17:00-19:00" \
when 19 then "19:00-21:00" when 20 then "19:00-21:00" when 21 then "21:00-23:00" \
when 22 then "21:00-23:00"  when 23 then "23:00-1:00" end timeBlock, "ff"   AS alarmtype \
from ( select substring(fa.receive_time,12,2)%%24 as modHour  \
from rt_fault fa, (SELECT dtu_id FROM relation_company_dtu WHERE company_id = %s)  dc \
WHERE  fa.dtu_id = dc.dtu_id AND    fa.confirm_type = 3 AND EXTRACT(YEAR_MONTH FROM fa.receive_time) \
BETWEEN EXTRACT(YEAR_MONTH FROM date_sub(NOW(), INTERVAL 3 MONTH)) \
AND EXTRACT(YEAR_MONTH FROM date_sub(NOW(), INTERVAL 1 MONTH))  ) t ) stf \
GROUP BY stf.alarmtype, stf.timeBlock) sss group by sss.alarmtype, sss.timeBlock;'


# #############################################################################################

# SQL
"SELECT    ttt.d_component_type,    ttt.statisticCount,    ttt.percentvalue \
FROM    (    SELECT    t.d_component_type,    t.statisticCount,    \
CONCAT(    ROUND(t.statisticCount / tt.totalStatisticCount * 100,    1    ), '%%') \
AS percentvalue    FROM (    SELECT    d.component_type AS d_component_type,  \
  r.component_type AS r_component_type,    COUNT(r.component_type) AS statisticCount   \
   FROM    rt_alarm r    JOIN dic_component_type d ON r.component_type = d.id   \
    WHERE  dtu_id in (select dtu_id from relation_company_dtu where company_id = %s)  \
     AND  confirm_type > 0  AND EXTRACT(YEAR_MONTH FROM receive_time) \
    BETWEEN EXTRACT(    YEAR_MONTH    FROM    \
    DATE_SUB(    NOW(), INTERVAL 6 MONTH    )    )    \
    AND EXTRACT(    YEAR_MONTH    FROM    \
    DATE_SUB(    NOW(),    INTERVAL 0 MONTH    ) )   \
    GROUP BY r.component_type    ) t, \
     (    SELECT COUNT(r.component_type) AS totalStatisticCount    \
     FROM    rt_alarm r    JOIN dic_component_type d ON r.component_type = d.id    \
     WHERE  dtu_id in (select dtu_id from relation_company_dtu where company_id = %s) \
     AND   confirm_type > 0    AND EXTRACT(YEAR_MONTH FROM receive_time) \
     BETWEEN EXTRACT(    YEAR_MONTH    FROM    \
     DATE_SUB(    NOW(),INTERVAL 6 MONTH    )    )   \
      AND EXTRACT(YEAR_MONTH    FROM \
      DATE_SUB(NOW(), INTERVAL 0 MONTH))) tt) ttt \
      ORDER BY    ttt.statisticCount DESC ;"


# #############################################################################################


# 这里一般用于`Model`本身字段比较多的情况，就用__all__代替，但是不属于该Model的字段可以通过下述
# `get_field_names`来获得
class BuildingSerializer(serializers.ModelSerializer):
    building_name = serializers.CharField(read_only=True, source='get_building_name')
    building_height = serializers.CharField(read_only=True, source='get_building_height')
    control_room_location = serializers.CharField(
        read_only=True, source='get_control_room_location')
    fire_level = serializers.CharField(
        read_only=True, source='get_building_fire_level')
    fire_resistance = serializers.CharField(
        read_only=True, source='get_building_fire_resistance')
    property = serializers.CharField(
        read_only=True, source='get_building_property')
    building_structure = serializers.CharField(
        read_only=True, source='get_building_structure')
    building_type = serializers.CharField(
        read_only=True, source='get_building_type')
    company_name = serializers.CharField(
        read_only=True, source='get_company_name')
    sectional_elevation = serializers.SerializerMethodField()
    fire_equipment_layout_image = serializers.SerializerMethodField()
    ichnography = serializers.SerializerMethodField()

    class Meta:
        model = 'Your Model Name(not str)'
        fields = '__all__'
        # 通过extra_fields来声明额外获取的字段名称
        extra_fields = ['building_name', 'building_height', 'control_room_location',
                        'fire_level', 'fire_resistance', 'property',
                        'building_structure', 'building_type', 'company_name']

    def get_field_names(self, declared_fields, info):  # 这个是重点
        expanded_fields = super(BuildingSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

    def to_representation(self, instance):
        def revalue(dict_):  # 重新赋值，可以统一用来格式化字符串操作（或者重命名）
            pass
        ret = super(BuildingSerializer, self).to_representation(instance)
        return OrderedDict(list(map(lambda x: (x[0], revalue(x)), ret.items())))


# #############################################################################################


# ClassBaseView 禁用csrf验证
from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        pass


def cbv_csrf_exempt(cls):  # 装饰cbv
    cls.authentication_classes = (CsrfExemptSessionAuthentication, )
    return cls
