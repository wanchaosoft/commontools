# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoggedInMixin(object):
    """判断登录,未登录将跳转至登录页面"""
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class EventsPageMixin(object):
    """View mixin include the Event in templates context."""

    def get_event(self):
        if not hasattr(self, 'event'):
            self.event = self.get_event()
        return self.event

    def get_context_data(self, **kwargs):
        context = super(EventsPageMixin, self).get_context_data(**kwargs)
        context['event'] = self.get_event()

        return context


