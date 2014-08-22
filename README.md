bikessites
==========

## supervisor files

**/etc/supervisor/bikessites.ini**

	[program:bikessites]
	command=/var/www/envs/bikessites/bin/uwsgi --socket /tmp/bikessites.sock --logto /var/www/envs/bikessites/bikessites/log/uwsgi.log --home /var/www/envs/bikessites --pythonpath /var/www/envs/bikessites --wsgi-file /var/www/envs/bikessites/wsgi.py --callable app  --max-requests 1000 --master --processes 1 --chmod
	directory=/var/www/envs/bikessites
	autostart=true
	autorestart=true



**/etc/supervisor/rqworker.ini**

	[program:rqworker]
	; Point the command to the specific rqworker command you want to run.
	; If you use virtualenv, be sure to point it to
	; /var/www/envs/bikessites/bin/rqworker
	; Also, you probably want to include a settings module to configure this
	; worker.  For more info on that, see http://python-rq.org/docs/workers/
	command=/var/www/envs/bikessites/bin/rqworker
	process_name=%(program_name)s

	; If you want to run more than one worker instance, increase this
	numprocs=1

	; This is the directory from which RQ is ran. Be sure to point this to the
	; directory where your source code is importable from
	directory=/var/www/envs/bikessites/

	; RQ requires the TERM signal to perform a warm shutdown. If RQ does not die
	; within 10 seconds, supervisor will forcefully kill it
	stopsignal=TERM

	; These are up to you
	autostart=true
	autorestart=true


### then as as root:
	/etc/init.d/supervisor restart ; supervisorctl status

## NGINX files

**/etc/nginx/sites-available/bikesites.conf**

	server {
	    listen       80;
	    server_name  localhost;
	    access_log  /var/www/envs/bikessites/bikessites/log/nginx-access.log;
	    error_log /var/www/envs/bikessites/bikessites/log/nginx-error.log;
    	#
	    location / {
	        include uwsgi_params;
	        uwsgi_pass unix:/tmp/bikessites.sock;
	    }
	    location /static {
	        alias /var/www/envs/bikessites/bikessites/static;
	        expires 1y;
	        add_header Cache-Control "public";
	    }
	}

#### then link the config file to sites-enabled and go!

	ln -s /etc/nginx/sites-available/bikesites.conf /etc/nginx/sites-enabled/bikesites.conf
	/etc/init.d/nginx configtest ; /etc/init.d/nginx restart


