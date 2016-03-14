CONFIG = {
    'mode': 'wsgi',
    #'environment': {
    #    'PYTHONPATH': '/path/to/custom/python/packages',
    #},
    'working_dir': '/home/box/web',
    'args': (
        '--bind=0.0.0.0:8080',
	#'--daemon',
        '--workers=2',
        # '--worker-class=egg:gunicorn#sync',
        '--timeout=30',
        'hello.app',
    ),
}
