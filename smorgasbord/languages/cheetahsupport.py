from Cheetah.Template import Template


class CheetahTemplate(object):
    def __init__(self, source):
        self._source=source

    def render(self, context):
        tmpl=Template(source=self._source, searchList=[context])
        return unicode(tmpl)

def get_template_from_string(source, origin=None, name=None):
    return CheetahTemplate(source)
