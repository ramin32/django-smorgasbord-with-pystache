try:
    from setuptools import setup
except ImportError:
    from distutils import setup

description="transparent support for multiple templating languages in Django"    

long_description="""\
Smorgasbord makes it possible to use multiple template languages in Django,
even for 3rd party applications that don't use your choice of template
language natively.

Currently supported languages are:

    * mako
    * jinja2
    * cheetah
    * STML 
"""

VERSION='0.3'

setup(author="Jacob Smullyan",
      author_email='jsmullyan@gmail.com',
      description=description,
      long_description=long_description,
      license="BSD",
      platforms='OS Independent',
      name="django-smorgasbord",
      url="http://code.google.com/p/smorgasbord/",
      classifiers=["Development Status :: 3 - Alpha",
                   "Environment :: Web Environment",
                   "Framework :: Django",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Text Processing :: Markup :: HTML',
      ],
      version=VERSION,
      keywords="django jinja2 skunkweb STML cheetah mako templating satimol",
      packages=("smorgasbord", "smorgasbord.languages"),
      package_dir={'' : '.'}
      )
