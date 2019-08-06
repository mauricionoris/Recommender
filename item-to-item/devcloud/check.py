
modules_set = ['numpy', 'pandas', 'sklearn', 'nltk','request']
modules = []

for module in modules_set:
    try:
        modules.append(__import__(module))
    except ImportError as e:
        e.__version__ = '-';
        modules.append(e);
        pass

for module in modules:
    print('{} version: {}.'.format(module,module.__version__))
