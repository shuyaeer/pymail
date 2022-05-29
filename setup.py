from setuptools import setup

setup(
    name='pymail',
        version='1.0',
        description='Python Gmail Sender',
        author='shuyafukushima',
        author_email='',
        packages=['pymail'],
        install_requires=[],
        entry_points={
            'console_scripts': ['pymail=pymail.send_mail.main']
            }
    )
