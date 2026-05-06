from distutils.version import LooseVersion

print(LooseVersion('1.14.3') >= LooseVersion('1.14dev'))
