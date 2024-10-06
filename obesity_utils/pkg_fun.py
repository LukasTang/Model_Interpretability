import pip

def pkg_fun(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])  