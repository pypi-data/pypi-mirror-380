from setuptools import setup, find_packages
from package_is_debug import __version__

# pypi-AgEIcHlwaS5vcmcCJDY3ZWE0MjdkLTgxNTYtNGM4Mi1hMzdmLWRiYTUzMDk2Zjk2MQACKlszLCJmNDUzZDc3Mi01NWE4LTQ0MjEtODZhZS01YWViNzNjZWU3MDAiXQAABiDwKtVfhMpNyRRV3vLovhzZdRQpRhz9JfIWHoQEUyHA3A

setup(
    name='package_is_debug',
    version=__version__,
    author='Маг Ильяс DOMA (MagIlyas_DOMA)',
    license='MIT License',
    url='https://github.com/MagIlyas-DOMA/PackageIsDebug',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
