from __future__ import absolute_import

from django.conf import settings

import pystache

from ..contextutil import context_to_dict

class PystacheTemplate(object):

    def __init__(self, string):
        self.string = string

    def render(self, context):
        return pystache.render(self.string, context_to_dict(context))

def get_template_from_string(source, origin=None, name=None):
    return PystacheTemplate(source)
