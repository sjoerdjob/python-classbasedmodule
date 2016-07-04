'''
Class based module.

Allow a module to be overtaken by a class.
'''

from weakref import ref
import sys

__all__ = ['class_as_module']

_uniq = 0
_references = {}


def class_as_module(cls):
    global _uniq
    # We need to make sure that there remains a reference to the original
    # module, because otherwise Python is more than happy to clean up the
    # contents of the module by setting all entries to `None`.
    count = _uniq
    def callback():
        del reference[_count]
    _uniq += 1
    inst = cls()
    _references[count] = (ref(inst, callback), sys.modules[cls.__module__])

    # Now that we have made sure that a reference to the old module remains, we
    # can finally overwrite the value in `sys.modules`.
    sys.modules[cls.__module__] = inst
    return cls
