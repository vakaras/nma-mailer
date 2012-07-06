#!/usr/bin/python3

from distutils.core import setup

# http://docs.python.org/py3k/distutils/setupscript.html

setup(
        name='nma-mailer',
        version='0.1',
        author='Dina Alytė',
        author_email='dina@alytė',
        packages=['nma_mailer',],
        package_dir={'': 'src'},
        #package_data={'{package_name}': []},
                                        # List of data files to be included 
                                        # into package.
        requires=[
            'distribute',
            ],
        install_requires=[              # Dependencies for the package.
            ],
        scripts=[],                     # List of python script files.
        #data_files=[('/etc/init.d', ['init-script'])]
                                        # List of files, which have to
                                        # be installed into specific 
                                        # locations.
        #url='',                        # Home page.
        #download_url='',               # Page from which package could
                                        # be downloaded.
        description='nma-mailer',
        #long_description=(
            #open('README.rst').read()+open('CHANGES.txt').read()),
        # Full list of classifiers could be found at:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 1 - Planning',
            #'Environment :: Console',
            #'Framework :: Django',
            'Intended Audience :: Developers',
            #(
                #'License :: OSI Approved :: '
                #'GNU Library or Lesser General Public License (LGPL)'),
            #'Natural Language :: Lithuanian',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            (
                'Topic :: Software Development :: Libraries :: '
                'Python Modules'),
            ],
        #license='LGPL'
        )
