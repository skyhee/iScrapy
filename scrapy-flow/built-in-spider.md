# scrapy 内置spider

文件如下：

![spider_files](./imgs/spider.PNG)


## Spider： 基类蜘蛛

内部成员：

- **name**： 
定义spider名字，必须定义且唯一

- **allowed_domains**: 
可选。包含了spider允许爬取的域名(domain)列表(list)。 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进。

- **start_urls**：
没有指定特定的URL时，spider将从该列表中开始进行爬取。

- **start_requests()**：
包含了spider用于最初爬取的第一个Request，一般用来处理自定义的登录请求。必须返回一个可迭代对象(iterable)

- **make_requests_from_url(url)**：
接受一个URL并返回 Request 对象， parse() 是其默认回调函数

- **parse(response)**：
负责处理response并返回处理后的数据或提取出的 URL（用以深度爬取）

- **log(message[, level, component])**：
自动带上该spider的 name 属性，日志记录

- **closed(reason)**：
当spider关闭时，该函数被调用

## CrawlSpider： 链接爬取蜘蛛


内部成员：

- **rules**： 
Rule 对象的集合(list)，用以指定自定义链接匹配规则、自定义链接处理回调函数、自定义 request 对象处理回调函数

- **parse_start_url(response)**：
当start_url的请求返回时，该方法被调用

## XMLFeedSpider： XML 订阅蜘蛛

内部成员：

- **iterator**：
用于确定使用哪个迭代器的string，可选项有 iternodes（默认）、html、xml

- **itertag**：
迭代入口的节点名，如 itertag = 'root'

- **namespaces**：
定义了该文档中会被spider处理的可用的namespace, 是由 (prefix, url) 元组(tuple)所组成的list

- **adapt_response(response)**：
在spider分析response前被调用，用以修改响应

- **parse_node(response, selector)**：
当节点符合提供 itertag 的时该方法被调用

- **process_results(response, results)**：
当spider返回结果(item或request)时该方法被调用，目的是在结果返回给框架核心之前做最后的处理


## CSVFeedSpider： CSV 蜘蛛

内部成员：

- **delimiter**：
用于区分字段的分隔符。默认为 ','

- **headers**：
要提取的字段，[]

- **parse_row(response, row)**：
- **adapt_response(response)**：
同 XMLFeedSpider

## SitemapSpider：站点地图蜘蛛

内部成员：

- **sitemap_urls**：
要爬取的url的sitemap的url列表

- **sitemap_rules**：
包含 (regex, callback) 元组的列表(list)

- **sitemap_follow**：
用于匹配要跟进的sitemap的正则表达式的列表

- **sitemap_alternate_links**：
指定当一个 url 有可选的链接时，是否跟进
