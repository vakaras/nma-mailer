default: bin/django-admin.py

bootstrap.py: 
	wget http://svn.zope.org/*checkout*/zc.buildout/branches/2/bootstrap/bootstrap.py

bin/buildout: bootstrap.py
	python3 bootstrap.py

buildout: bin/buildout django
	bin/buildout -v

django:
	hg clone https://bitbucket.org/vinay.sajip/django
	cd django
	hg checkout django3 
	cd ..
	
bin/django-admin.py: buildout
	head -n -24 bin/python > bin/django-admin.py
	echo 'from django.core import management' >> bin/django-admin.py
	echo 'if __name__ == "__main__":' >> bin/django-admin.py
	echo '  management.execute_from_command_line()' >> bin/django-admin.py
	chmod 755 bin/django-admin.py

run:
	bin/django-admin.py runserver
