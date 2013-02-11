from fabric.api import *
import hypestarter.settings as settings

def deploy():
	# Push to heroku
	local('git push heroku')

	config_vars = settings.CONFIG_VARS['DEVELOPMENT']
	config_commands = ['%s="%s"' % (name, var) for name, var in config_vars.items()]
	config_command = ' '.join(config_commands)

	local('heroku config:add %s --app hypestarter-dev' % config_command)
	local('heroku run python hypestarter/manage.py syncdb --app hypestarter-dev')
	local('heroku run python hypestarter/manage.py migrate --app hypestarter-dev')
	local('heroku run python hypestarter/manage.py collectstatic --app hypestarter-dev')

def compile_coffee():
	"""
	Compiles coffeescript files to javascript
	"""
	# Get files with .coffee extension
	files = local("find static/js -name *.coffee", capture=True).split("\n")
	for f in files:
		print('compiling %s...' % f)
		local('coffee -c %s' % f)

def watch_coffee():
	"""
	Watches and automatically compiles coffeescript files to javascript
	"""
	# Get files with .coffee extension
	coffee_folder = 'static/coffee'
	js_folder = 'static/js'
	print('watching %s for changes' % coffee_folder)
	local('coffee -o %s -wc %s' % (js_folder, coffee_folder))

def watch_less():
	"""
	Watches and automatically compiles coffeescript files to javascript
	"""
	# Get files with .less extension
	less_folder = 'static/css'
	print('watching %s for changes' % less_folder)
	local('watch-less -d %s -e .css' % less_folder)