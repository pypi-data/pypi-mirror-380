#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import mayan

PACKAGE_NAME = 'mayan-edms'
PACKAGE_DIR = 'mayan'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


def find_packages(directory):
    # Compile the list of packages available, because distutils doesn't have
    # an easy way to do this.
    packages, data_files = [], []
    root_dir = os.path.dirname(__file__)
    if root_dir != '':
        os.chdir(root_dir)

    for dirpath, dirnames, filenames in os.walk(directory):
        if not dirpath.startswith('mayan/media'):
            # Ignore dirnames that start with '.'
            if os.path.basename(dirpath).startswith('.'):
                continue
            if '__init__.py' in filenames:
                packages.append(
                    '.'.join(
                        fullsplit(dirpath)
                    )
                )
            elif filenames:
                data_files.append(
                    [
                        dirpath, [
                            os.path.join(dirpath, filename) for filename in filenames
                        ]
                    ]
                )

    return packages


install_requires = """
django==4.2.24
CairoSVG==2.7.1
Markdown==3.7
Pillow==11.0.0
PyYAML==6.0.2
Whoosh==2.7.4
bleach==6.2.0
boto3==1.35.85
celery==5.4.0
dateparser==1.2.0
django-activity-stream==2.0.0
django-auth-ldap==5.1.0
django-celery-beat==2.7.0
django-cors-headers==4.6.0
django-formtools==2.3
django-mathfilters==1.0.0
django-model-utils==5.0.0
django-mptt==0.16.0
django-qsstats-magic==1.1.0
django-solo==2.4.0
django-storages==1.14.6
django-stronghold==0.4.0
django-widget-tweaks==1.5.0
djangorestframework==3.15.2
djangorestframework-recursive==0.1.2
drf-yasg==1.21.8
elasticsearch==7.17.12
elasticsearch-dsl==7.4.1
extract-msg==0.52.0
flex==6.14.1
furl==2.1.4
fusepy==3.0.1
gevent==24.11.1
google-cloud-storage==2.19.0
graphviz==0.20.3
greenlet==3.1.1
gunicorn==23.0.0
importlib-metadata==8.5.0
jsonschema==4.23.0
mozilla-django-oidc==4.0.1
nh3==0.2.18
node-semver==0.9.0
ollama==0.4.5
pycountry==24.6.1
pycryptodome==3.21.0
pyotp==2.9.0
pypdf==6.0.0
python-dateutil==2.9.0.post0
python_gnupg==0.5.4
pytz==2025.2
qrcode==8.0
requests==2.32.4
sentry-sdk==2.38.0
sh==2.1.0
swagger-spec-validator==3.0.4
whitenoise==6.8.2
""".split()

with open(file='README.rst') as file_object:
    readme = file_object.read()

setup(
    author='Roberto Rosario',
    author_email='roberto.rosario@mayan-edms.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Communications :: File Sharing'
    ],
    description=mayan.__description__,
    include_package_data=True,
    install_requires=install_requires,
    license='"GPL-2.0-only',
    long_description=readme,
    name=PACKAGE_NAME,
    packages=find_packages(PACKAGE_DIR),
    platforms=['any'],
    project_urls={
        'Documentation': 'https://docs.mayan-edms.com/',
        'Forum': 'https://forum.mayan-edms.com/',
        'Changelog': 'https://gitlab.com/mayan-edms/mayan-edms/-/blob/master/HISTORY.rst',
        'Bug Tracker': 'https://gitlab.com/mayan-edms/mayan-edms/-/issues',
        'Source Code': 'https://gitlab.com/mayan-edms/mayan-edms',
        'Support': 'https://www.mayan-edms.com/support/'
    },
    python_requires='>=3.9',
    scripts=['mayan/bin/mayan-edms.py'],
    url=mayan.__website__,
    version=mayan.__version__,
    zip_safe=False
)
