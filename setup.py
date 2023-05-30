from setuptools import setup

setup(
    name='m3_project',
    version='1.0.0',
    py_modules=['manage'],  # Включить manage.py
    packages=['app', 'app.migrations', 'm3_project'],
    install_requires=[  # Зависимости
        'django~=2.2.2',
        'm3-django-compat~=1.9.2',
        'm3-objectpack~=2.2.47',
    ],
    url='',
    license='',
    author='Capaldi12',
    author_email='artem.shebarshov.1@gmail.com',
    description='m3 project'
)
