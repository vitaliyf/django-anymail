VERSION = (0, 3, 9)
__version__ = '.'.join([str(x) for x in VERSION])
__minor_version__ = '.'.join([str(x) for x in VERSION[:2]])  # Sphinx's X.Y "version"