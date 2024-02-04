# gunicorn_config.py

workers = 4  # The number of worker processes for handling requests
bind = "0.0.0.0:8000"  # The IP and port on which Gunicorn will listen for requests
timeout = 60  # The maximum time (in seconds) a worker is allowed to process a request
loglevel = "info"  # The logging level (options: debug, info, warning, error, critical)

# You can customize the following settings based on your application needs
# See Gunicorn documentation for more options: https://docs.gunicorn.org/en/latest/settings.html

# worker_class = "sync"  # The worker processing class (options: sync, eventlet, gevent, tornado)
# errorlog = "/path/to/error.log"  # The path to the error log file
# accesslog = "/path/to/access.log"  # The path to the access log file
# daemon = True  # Run the Gunicorn process in the background
# pidfile = "/path/to/gunicorn.pid"  # The path to the PID file
