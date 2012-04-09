from django.template.context import Context

def context_to_dict(ctxt):
    res={}
    for d in reversed(ctxt.dicts):
        # sometimes contexts will be nested -- oy!
        if isinstance(d, Context):
            res.update(context_to_dict(d))
        else:
            res.update(d)
    return res

