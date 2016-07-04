# Class based module

Python modules don't allow for descriptors. Classes do. Sometimes you just
really want to use descriptors (or something similar) in a module.

This decorator is for that purpose.

    @class_as_module
    class Whatever(object):
        pass

Now importing the module containing `Whatever` will give a (shared) instance of
`Whatever` instead of the module.
