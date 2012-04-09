from __future__ import absolute_import

from django.conf import settings

import jinja2

from ..contextutil import context_to_dict

class Jinja2Template(object):

    def __init__(self, template_obj):
        self.template_obj=template_obj

    def render(self, context):
        return self.template_obj.render(context_to_dict(context))

def get_template_from_string(source, origin=None, name=None):

    opts=getattr(settings, 'JINJA2_TEMPLATE_OPTS', {})
    if opts:
        opts=opts.copy()
        if not 'loader' in opts:
            opts['loader']=jinja2.FileSystemLoader(settings.JINJA2_TEMPLATE_DIRS)

    environment=jinja2.Environment(**opts)
    template=environment.from_string(source)
    template.name=name
    return Jinja2Template(template)
