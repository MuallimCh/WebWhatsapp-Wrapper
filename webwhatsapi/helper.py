import six


def safe_str(text):
    if not bool(text):
        return "(empty)"
    assert isinstance(text, six.string_types), "obj is not a string: %r" % text
    return str(text.encode('utf-8').decode('ascii', 'ignore')) if bool(text) else "(empty)"
