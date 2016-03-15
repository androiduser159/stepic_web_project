def application(environ,start_response):
	resp="\r\n".join(environ['QUERY_STRING'].split("&"))+"\r\n"
	status='200 OK'
	headers=[('Content-Type','text/plain')]
	start_response(status,headers)
	return iter([resp])

