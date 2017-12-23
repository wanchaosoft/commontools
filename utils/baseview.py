#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

__project__ = 'commontools'
__author__ = 'wanchao'
__create_time__ = '2017/12/11 16:56'

"""

from __future__ import unicode_literals
from rest_framework.views import APIView
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as ValidationError2
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from django.http.response import HttpResponseBase
import json
import logging
from django.db.utils import OperationalError
import re
logger = logging.getLogger(__name__)

ERR_MSG = "info_manage error occurred, please contact administrator!"


class FBApiView(APIView):
    ALLOWED_METHOD = None

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        info = {"msg": "ok",
                "code": "-1",
                "data": {}}
        # super(FBApiView, self).dispatch(request, *args, **kwargs)
        if request.method in [item.upper() for item in self.ALLOWED_METHOD]:
            try:
                method = getattr(self, request.method.lower())
                request = self.initialize_request(request, *args, **kwargs)
                respose = method(request, *args, **kwargs)
            except (ValidationError, ValidationError2) as e:
                logger.error("validators_error")
                logger.debug(e.message)
                logger.error(request.data)
                logger.error(request.query_params)
                info.update({"msg": "参数错误"})
                return HttpResponse(json.dumps(info, ensure_ascii=False), status=200,
                                    content_type=" application/json")
            except Exception as e:
                logger.exception("custom_error_for_pro")
                logger.error(request.data)
                logger.error(request.query_params)
                info.update({"msg": e.message,
                             "code": str(e.code),
                             "data": e.data})
            except OperationalError as e:
                logger.error("database operation error")
                logger.exception(e)
                ec = str(e)
                if "1054" in ec:
                    table = re.findall("'.+\.", ec)
                    if table:
                        info.update({"msg": "please update database columns for {table}.".format(table=table[0][1:-1]),
                                     "code": "1002"})
                    else:
                        info.update({"msg": ERR_MSG,
                                     "code": "1002"})
            except Exception as e:
                logger.exception("have_a_system_error")
                logger.error(request.data)
                logger.error(request.query_params)

                if isinstance(e, OperationalError):
                    pass
                if request.user:
                    logger.error(request.user)
                info.update({"msg": e.message if e.message else ERR_MSG,
                             "code": "1002"})
            else:
                if isinstance(respose, HttpResponse):
                    return respose
                if isinstance(respose, dict) or isinstance(respose, list):
                    info.update({"code": "1"})
                    info.update(respose)
                elif isinstance(respose, tuple):
                    if isinstance(respose[0], dict) or isinstance(respose[0], list):
                        info.update(**{"msg": respose[1], "code": "1"})
                else:
                    info.update({"msg": respose,
                                 "code": "1002"})
            return HttpResponse(json.dumps(info, ensure_ascii=False), status=200,
                                content_type=" application/json")
        else:
            return HttpResponse(json.dumps({"detail": u"请求'{0}'方法不允许".format(request.method)}, ensure_ascii=False),
                                status=405,
                                content_type=" application/json")

    # def finalize_response(self, request, response, *args, **kwargs):
    #     """
    #     Returns the final response object.
    #     """
    #
    #     response = Response(response)
    #     assert isinstance(response, HttpResponseBase), (
    #         'Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` '
    #         'to be returned from the view, but received a `%s`'
    #         % type(response)
    #     )
    #
    #     if isinstance(response, Response):
    #         if not getattr(request, 'accepted_renderer', None):
    #             neg = self.perform_content_negotiation(request, force=True)
    #             request.accepted_renderer, request.accepted_media_type = neg
    #
    #         response.accepted_renderer = request.accepted_renderer
    #         response.accepted_media_type = request.accepted_media_type
    #         response.renderer_context = self.get_renderer_context()
    #
    #     for key, value in self.headers.items():
    #         response[key] = value
    #     return response

