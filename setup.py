from distutils.core import setup

setup(
    name="django-generic-mail",
    version=__import__("generic_mail").get_version(),
    description="Easy to use, class based email for Django",
    long_description=open("README.md").read(),
    author="Kevin Renskers",
    author_email="info@mixedcase.nl",
    url="https://github.com/kevinrenskers/django-generic-mail",
    packages=[
        "generic_mail",
    ],
    package_dir={"generic_mail": "generic_mail"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Framework :: Django",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
