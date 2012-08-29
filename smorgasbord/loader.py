import warnings

from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loader import (
    get_template as _original_get_template,
    get_template_from_string as _original_get_template_from_string
    )
import django.template.loader as djloader

def _get_loader(language):
    assert language!='django'
    modname=language+'support'
    qname='%s.languages.%s' % (__name__[:__name__.rfind('.')], modname)
    # django apps may be relocated underneath the python package of the
    # project, so we can't hardcode the level of nesting
    modlist=qname.split('.')[1:] 
    mod=__import__(qname)
    for n in modlist:
        mod=getattr(mod, n)
    return mod

def get_template_from_string(language, source, origin=None, name=None):
    """
    Returns a compiled Template object for the given template language
    and source code.
    """
    # print "in get_template_from_string with language", language
    if language=='django':
        if not hasattr(source, 'render'):
            return _original_get_template_from_string(source, origin, name)
        else:
            return source
    else:
        loader=_get_loader(language)
        return loader.get_template_from_string(source, origin, name)


def find_template_source(name, dirs=None):
    # Calculate template_source_loaders the first time the function is executed
    # because putting this logic in the module-level namespace may cause
    # circular import errors. See Django ticket #1292.

    if djloader.template_source_loaders is None:
        loaders = []
        for loader_name in settings.TEMPLATE_LOADERS:
            loader = djloader.find_template_loader(loader_name)
            if loader is not None:
                loaders.append(loader)
        djloader.template_source_loaders = tuple(loaders)
    for loader in djloader.template_source_loaders:
        try:
            source, display_name = loader.load_template_source(name, dirs)
            origin = djloader.make_origin(display_name, loader.load_template_source, name, dirs)
            return (source, origin)
        except TemplateDoesNotExist as e:
            pass
    raise TemplateDoesNotExist(name)


def get_template(template_name):
    """
    Returns a compiled Template object for the given template name,
    in any of the template languages listed in settings.TEMPLATE_LANGUAGES,
    looking for each through the directories specified in
    settings.<LANGNAME>_TEMPLATE_DIRS (except for Django templates, which use
    settings.TEMPLATE_DIRS).
    """
    source = None
    languages=getattr(settings, 'TEMPLATE_LANGUAGES', None)

    if languages is None:
        return _original_get_template(template_name)

    for lang in languages:
        if lang=='django':
            dirs=None
        else:
            prefix="%s_" % lang.upper() 
            confvar='%sTEMPLATE_DIRS' % prefix
            dirs=getattr(settings, confvar, ())

            if not dirs:
                warnings.warn("no directories defined for template language %r.  Please define the configuration setting %r." % (lang, confvar))
                continue
        try:
            source, origin = find_template_source(template_name, dirs)
            return get_template_from_string(lang, source, origin, template_name)

        except TemplateDoesNotExist as e:
            pass

    raise TemplateDoesNotExist, template_name

def monkeypatch_loader():
    djloader.get_template=get_template

    
