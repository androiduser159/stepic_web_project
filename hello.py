def application(environ,start_response):
	resp="\r\n".join(environ['QUERY_STRING'].split("&"))+"\r\n"
	#resp=[item + "\r\n" for item in environ['QUERY_STRING'].split(&)]
	status='200 OK'
	headers=[('Content-Type','text/plain')]
	start_response(status,headers)
	return iter([resp])

