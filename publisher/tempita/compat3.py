import sys

__all__ = ['b', 'basestring_', 'bytes', 'next', 'is_unicode']

if sys.version < "3":
    b = bytes = str
    basestring_ = basestring
else:

    def b(s):
        return s.encode('latin1') if isinstance(s, str) else bytes(s)
    basestring_ = (bytes, str)
    bytes = bytes
text = str

if sys.version < "3":

    def next(obj):
        return obj.next()
else:
    next = next

if sys.version < "3":

    def is_unicode(obj):
        return isinstance(obj, unicode)
else:

    def is_unicode(obj):
        return isinstance(obj, str)


def coerce_text(v):
    if not isinstance(v, basestring_):
        attr = '__unicode__' if sys.version < "3" else '__str__'
        return str(v) if hasattr(v, attr) else bytes(v)
    return v
