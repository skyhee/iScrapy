# Request & Response

## Request 父类

generated in the **Spider** and executed by the **Downloader**, and thus generating a **Response**

内部成员：
- 构造方法：**Request(url[, callback, method='GET', headers, body, cookies, meta, encoding='utf-8', priority=0, dont_filter=False, errback])**：


- **url**：
请求链接

- **method**：
请求方法

- **headers**：
请求头

- **body**：
请求体，只读，可通过replace()更改

- **meta**：可以是任意值，copy() 或 replace()请求时隐式复制，内置支持
	- dont_redirect
	- dont_retry
	- handle_httpstatus_list
	- dont_merge_cookies
	- cookiejar: cookie
	- redirect_urls: 
	- bindaddress: IP地址

- **copy()**：
返回一个新的请求

- **replace([url, method, headers, body, cookies, meta, encoding, dont_filter, callback, errback])**：
通过指定参数更改请求

#### FormRequest 
内部成员：

- **构造方法**：
同Request()

- **from_response(response[, formname=None, formnumber=0, formdata=None, formxpath=None, clickdata=None, dont_click=False, ...])**：
用来模拟登陆


## Response 父类
内部成员：

- **url**：
只读字符串，响应中的链接，可通过replace()修改

- **status**：
HTTP响应码，如404

- **headers**：
响应头

- **body**：
只读字符串，可通过replace()修改

- **request**：
生成此响应的请求对象，在处理重定向时可应用，但是只能在 spider 和 spiderMiddleware中获取

- **meta**：
同Request.meta

- **flags**：
用来标记响应，如‘cached’, ‘redirected‘等

- **copy()**：
返回一个新的响应

- **replace([url, status, headers, body, request, flags, cls])**：
根据参数来替换响应中的内容，用以更改响应

#### TextResponse 
内部成员：

- **encoding**：
编码格式，默认None时爬虫会在响应中的header和body中自动识别

- **selector**： 
- **body_as_unicode()**： 
- **xpath(query)**： 
- **css(query)**： 

#### HtmlResponse 
TextResponse子类，会将 <meta http-equiv="XXX">中内容作为encoding

#### XmlResponse  
TextResponse子类，会将 <XML> 节点中内容作为encoding