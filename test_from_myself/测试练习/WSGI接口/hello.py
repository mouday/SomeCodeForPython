
def application(environ, start_response):
    # 函数接受两个参数: 
    # environ ：包含有CGI 式环境变量的字典，由server负责提供内容 
    # start_response：由server提供的回调函数，其作用是将状态码和响应头返回给server 

    status = "200 OK"  # HTTP 响应码及消息 

    # 提供给客户端的响应头. 
    # 封装成list of tuple pairs 的形式: 
    # 格式要求：[(Header name, Header value)].
    response_headers = [("Content-Type", "text/html")]

    # 将响应码/消息及响应头通过传入的start_reponse回调函数返回给server 
    start_response(status, response_headers)

    # 响应体作为返回值返回 
    # 注意这里被封装到了list中. 
    # response_body = "<h1>Hello %s</h1>" % (environ["PATH_INFO"][1:] or "web")
    
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    response_body = "method: %s \npath: %s" % (method, path)

    # response_body = str(environ)

    return [response_body.encode("utf-8")]
