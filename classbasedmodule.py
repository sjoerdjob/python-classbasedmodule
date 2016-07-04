'''
Class based module.

Allow a module to be overtaken by a class.
'''

import sys

__all__ = ['class_as_module']


def class_as_module(cls):
    inst = cls()
    # We need to make sure that there remains a reference to the original
    # module, because otherwise Python is more than happy to clean up the
    # contents of the module by setting all entries to `None`.
    setattr(inst, '\0', sys.modules[cls.__module__])
    sys.modules[cls.__module__] = inst
    return cls
