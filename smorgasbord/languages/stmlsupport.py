from __future__ import absolute_import
import warnings

from skunk.components import stringcomp
from skunk.config import Configuration
import skunk.stml

from django.conf import settings

from ..contextutil import context_to_dict

def get_docroot():
    stmlroots=settings.STML_TEMPLATE_DIRS
    if not stmlroots:
        return
    if len(stmlroots)>1:
        warnings.warn("multiple STML template directories defined.  Only first will be used")
    return stmlroots[0]


class STMLTemplate(object):
    def __init__(self, path):
        self._path=path

    def render(self, context):
        data=context_to_dict(context)
        return stringcomp(self._path, **data)

def get_template_from_string(source, origin=None, name=None):
    # we are going to ignore source here because
    # the STML api doesn't make it convenient.
    Configuration.componentRoot=get_docroot()
    if not name.startswith('/'):
        name='/%s' % name
    print name
    return STMLTemplate(name)
