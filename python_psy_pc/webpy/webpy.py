import web
        
render=web.template.render('templates')        
urls = (
    '/index', 'index',
    '/blog/\d+','blog',
    '/(.*)', 'hello',
)

app = web.application(urls, globals())
class index:
	def GET(self):
		#http://127.0.0.1:8080/index?name=jack&age=12
		query=web.input()
		return web.seeother('http://www.baidu.com')

class blog:
	def POST(self):
		query=web.input()#获取请求参数
		return query
	def GET(self):
		return web.ctx.env#获取请求头

class hello:        
    def GET(self, name):
        # if not name: 
        #     name = 'World'
        # return 'Hello, ' + name + '!'
        #return open(r'index.html','r').read()
        return render.hello1(name)
# class article:
# 	def GET(self):
# 		#@"Server=(localdb)\Projects;integrated security=SSPI;Initial Catalog=NewDB";
# conn=MySQLdb.connect(host='localhost',user='root',passwd='guahao',db='world',port=3306)

#     cur=conn.cursor()
#         cur.execute('select  * from city limit 0,10')
#         r=cur.fetchall()
#         cur.close()
#         conn.close()
#         print r
#         return render.city(r)

if __name__ == "__main__":
    app.run()