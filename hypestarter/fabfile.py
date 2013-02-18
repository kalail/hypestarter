from fabric.api import *

# Import settings
import hypestarter.settings as settings

cmd = {
	'development': (
		'd',
		'dev',
		'development'
	),

	'production': ()
}


def push(environment=None):
	"""
	Push the app to heroku.
	"""
	if not environment:
		print "No environment declared!"
		return
	# Push to heroku
	if environment in cmd['development']:
		cmd_env = 'heroku'
	elif environment in cmd['production']:
		cmd_env = 'heroku-production'
	else:
		print "Incorrect environment declared!"
		return

	local('git push %s' % cmd_env)


def add_config_vars(environment=None):
	"""
	Add given config variables as environment variables.
	
	"""
	if not environment:
		print "No environment declared!"
		return

	if environment in cmd['development']:
		cmd_env = 'hypestarter-dev'
		config_vars = settings.CONFIG_VARS['DEVELOPMENT']
	elif environment in cmd['production']:
		cmd_env = 'hypestarter'
		config_vars = settings.CONFIG_VARS['PRODUCTION']
	else:
		print "Incorrect environment declared!"
		return

	config_commands = ['%s="%s"' % (name, var) for name, var in config_vars.items()]
	config_command = ' '.join(config_commands)
	local('heroku config:add %s --app %s' % (config_command, cmd_env))

def syncdb(environment=None):
	"""
	Run syncdb on the server.
	
	"""
	if not environment:
		print "No environment declared!"
		return

	if environment in cmd['development']:
		cmd_env = 'hypestarter-dev'
	elif environment in cmd['production']:
		cmd_env = 'hypestarter'
	else:
		print "Incorrect environment declared!"
		return

	local('heroku run python hypestarter/manage.py syncdb --app %s' % cmd_env)

def migrate(environment=None):
	"""
	Migrate the database on the server.
	
	"""
	if not environment:
		print "No environment declared!"
		return

	if environment in cmd['development']:
		cmd_env = 'hypestarter-dev'
	elif environment in cmd['production']:
		cmd_env = 'hypestarter'
	else:
		print "Incorrect environment declared!"
		return

	local('heroku run python hypestarter/manage.py migrate --app %s' % cmd_env)

def collectstatic(environment=None):
	if not environment:
		print "No environment declared!"
		return

	if environment in cmd['development']:
		cmd_env = 'hypestarter-dev'
	elif environment in cmd['production']:
		cmd_env = 'hypestarter'
	else:
		print "Incorrect environment declared!"
		return

	local('heroku run python hypestarter/manage.py collectstatic --app %s' % cmd_env)


def deploy(environment=None):
	"""
	Fully deploy the app to heroku, running all the steps.
	"""
	if not environment:
		print "No environment declared!"
		return

	if environment in cmd['development']:
		env_name = 'development'
	elif environment in cmd['production']:
		env_name = 'production'
	else:
		print "Incorrect environment declared!"
		return

	push(env_name)
	add_config_vars(env_name)
	syncdb(env_name)
	migrate(env_name)
	collectstatic(env_name)


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