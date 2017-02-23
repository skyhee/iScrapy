# -*- coding: utf-8 -*-

# Scrapy settings for coolscrapy project
# Scrapy设定(settings)提供了定制Scrapy组件的方法。
# 您可以控制包括核心(core)，插件(extension)，pipeline及spider组件
# 
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import logging

# 【---- 项目 ----】
# 如果启用，Scrapy将会尊重 robots.txt策略
# ROBOTSTXT_OBEY = False
# bot的名字
BOT_NAME = 'nodejsPKG'
# 使用 startproject 命令创建项目时查找模板的目录(默认scrapy模块内部的 templates)
# TEMPLATES_DIR = ''


# 【---- 数据库 ----】
# 数据库 windows install http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
# linux pip install MySQL-python
# DATABASE = {
#     'drivername': 'mysql',
#     'host': '192.168.0.150',
#     'port': '3306',
#     'username': 'iscrapy',
#     'password': 'iscrapy',
#     'database': 'iscrapy',
#     'query': {'charset': 'utf8'}
# }

# 【---- 日志 ----】
# 是否启用logging,启用后控制台不再打印日志，而是输出到日志文件中
# LOG_ENABLED = True
# logging使用的编码
# LOG_ENCODING = 'utf-8'
# logging输出的文件名
# LOG_FILE = "d:/tmp/spider.log"
# 日志级别：CRITICAL、 ERROR、WARNING、INFO、DEBUG
# LOG_LEVEL = 'DEBUG'
# 日志格式
# LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
# 如果为 True ，标准输出(及错误)将会被重定向到log中
# LOG_STDOUT = False


# 【---- item 管道 ----】
# item管道及其顺序 - Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'app.nodejs.pipelines.MDExporterPipeline': 1
    # 'coolscrapy.pipelines.DuplicatesPipeline': 1,
    # 'coolscrapy.pipelines.FilterWordsPipeline': 2,
    # 'coolscrapy.pipelines.JsonWriterPipeline': 3,
    # 'coolscrapy.pipelines.JsonExportPipeline': 4,
    # 'coolscrapy.pipelines.ArticleDataBasePipeline': 5,
    # 'coolscrapy.pipelines.MyImagesPipeline': 6,
}
# 默认启用的pipeline(不要修改)
# ITEM_PIPELINES_BASE = {}
# Scrapy shell 中实例化item使用的默认类
# DEFAULT_ITEM_CLASS = 'scrapy.item.Item'


# 【---- SPIDER ----】
# Scrapy搜索spider的模块列表
SPIDER_MODULES = ['app.nodejs.spiders']
# 使用 genspider 命令创建新spider的模块
# NEWSPIDER_MODULE = 'coolscrapy.spiders'
# 蜘蛛中间件及其顺序 Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'coolscrapy.middlewares.MyCustomSpiderMiddleware': 543,
#    'coolscrapy.middlewares.UrlUniqueMiddleware': 543
# }
# # 默认启用的spider中间件(不要更改)
# SPIDER_MIDDLEWARES_BASE = {
#     'scrapy.contrib.spidermiddleware.httperror.HttpErrorMiddleware': 50,
#     'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 500,
#     'scrapy.contrib.spidermiddleware.referer.RefererMiddleware': 700,
#     'scrapy.contrib.spidermiddleware.urllength.UrlLengthMiddleware': 800,
#     'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': 900,
# }
# 用于 spider 单元测试的scrapy contract及其顺序
# SPIDER_CONTRACTS = {}
# 默认启用的scrapy contract(不要更改)
# SPIDER_CONTRACTS_BASE = {
#     'scrapy.contracts.default.UrlContract' : 1,
#     'scrapy.contracts.default.ReturnsContract': 2,
#     'scrapy.contracts.default.ScrapesContract': 3,
# }

# 【---- 下载器 ----】
# 下载中间件 Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'coolscrapy.middlewares.MyCustomDownloaderMiddleware': 543,
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 'coolscrapy.middlewares.RotateUserAgentMiddleware': 400,
    # 'scrapy_splash.SplashCookiesMiddleware': 723,# js 渲染页面的cookie中间件
    # 'scrapy_splash.SplashMiddleware': 725,# js 渲染页面的下载中间件
    # 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
# 默认启用的下载中间件（不要更改）
# DOWNLOADER_MIDDLEWARES_BASE = {
#     'scrapy.contrib.downloadermiddleware.robotstxt.RobotsTxtMiddleware': 100,
#     'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware': 300,
#     'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 350,
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
#     'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
#     'scrapy.contrib.downloadermiddleware.defaultheaders.DefaultHeadersMiddleware': 550,
#     'scrapy.contrib.downloadermiddleware.redirect.MetaRefreshMiddleware': 580,
#     'scrapy.contrib.downloadermiddleware.httpcompression.HttpCompressionMiddleware': 590,
#     'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 600,
#     'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 750,
#     'scrapy.contrib.downloadermiddleware.chunked.ChunkedTransferMiddleware': 830,
#     'scrapy.contrib.downloadermiddleware.stats.DownloaderStats': 850,
#     'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 900,
# }
# 是否收集下载器数据
# DOWNLOADER_STATS = True
# 请求延时（默认为0）Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY=3
# 下载器超时时间(单位: 秒)，默认180
DOWNLOAD_TIMEOUT = 20
# 默认启用的下载处理器(不要更改)
# DOWNLOAD_HANDLERS_BASE = {
#     'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
#     'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
#     'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
#     's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
# }
# 用于crawl的downloader
# DOWNLOADER = 'scrapy.core.downloader.Downloader'
# 启用的下载处理器
# DOWNLOAD_HANDLERS = {}

# 【---- 调度器 ----】
# 用于爬取的调度器
# SCHEDULER = 'scrapy.core.scheduler.Scheduler'

# 【---- 扩展插件 ----】
# 启用的插件及其顺序 Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
# }
# 可用的插件列表
# EXTENSIONS_BASE = {
#     'scrapy.contrib.corestats.CoreStats': 0,
#     'scrapy.webservice.WebService': 0,
#     'scrapy.telnet.TelnetConsole': 0,
#     'scrapy.contrib.memusage.MemoryUsage': 0,
#     'scrapy.contrib.memdebug.MemoryDebugger': 0,
#     'scrapy.contrib.closespider.CloseSpider': 0,
#     'scrapy.contrib.feedexport.FeedExporter': 0,
#     'scrapy.contrib.logstats.LogStats': 0,
#     'scrapy.contrib.spiderstate.SpiderState': 0,
#     'scrapy.contrib.throttle.AutoThrottle': 0,
# }

# 【---- 防 Ban ----】
# 自动限速 Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
# AUTOTHROTTLE_ENABLED=True
# 初始下载延时 The initial download delay
# AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
# 最大延时 AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG=False
# 下载随机延时-若 DOWNLOAD_DELAY 为0(默认值)，该选项将不起作用
# RANDOMIZE_DOWNLOAD_DELAY = True
# 覆盖默认请求头-Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
# 默认USER_AGENT - Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'coolscrapy (+http://www.yourdomain.com)'
# 禁用 cookie- Disable cookies (enabled by default)
# COOKIES_ENABLED=False

# 【---- 环境配置 ----】
# 图片下载设置
# IMAGES_STORE = '/tmp/'
# IMAGES_EXPIRES = 30  # 30天内抓取的都不会被重抓
# 图片链接前缀
# URL_PREFIX = 'http://dev.wingarden.net/tpl/static/pushimgs/'
# js异步加载支持
# SPLASH_URL = 'http://192.168.203.91:8050'
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
# 禁用 Telnet- Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED=False
# telnet终端使用的端口范围
# TELNETCONSOLE_PORT = [6023, 6073]
# 执行 edit 命令编辑spider时使用的编辑器
# EDITOR = 'vi'

# 【---- 请求缓存 ----】
# HTTP 缓存 Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=0
# HTTPCACHE_DIR='httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES=[]
# HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
# 是否启用DNS内存缓存
# DNSCACHE_ENABLED = True

# 【---- 请求重复 ----】
# 是否记录所有重复的requests
# DUPEFILTER_DEBUG = False
# 检测过滤重复请求的类
# DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'

# 【---- 请求重定向 ----】
# 修改重定向请求相对于原始请求的优先级。 负数意味着更多优先级
# REDIRECT_PRIORITY_ADJUST = +2
# 限制自动重定向最大延迟
# REDIRECT_MAX_METAREFRESH_DELAY = 100
# request允许重定向的最大次数
# REDIRECT_MAX_TIMES = 20

# 【---- 并发 ----】
# Item Processor(即 Item Pipeline) 同时处理(每个response的)item的最大值
# CONCURRENT_ITEMS = 100
# 最大并发请求量Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS=32
# 对单个网站进行并发请求的最大值
# CONCURRENT_REQUESTS_PER_DOMAIN=16
# 对单个IP进行并发请求的最大值
# CONCURRENT_REQUESTS_PER_IP=16
# 扩展-定义爬取数量
# CLOSESPIDER_ITEMCOUNT = 10
# url 最大长度（默认2083）
# URLLENGTH_LIMIT = 2083

# 【---- 爬取深度 ----】
# 爬取网站最大允许的深度
# DEPTH_LIMIT = 0
# 根据深度调整request优先级，如果为0，则不根据深度进行优先级调整
# DEPTH_PRIORITY = 0
# 是否收集最大深度数据
# DEPTH_STATS = True
# 是否收集详细的深度数据
# DEPTH_STATS_VERBOSE = False

# 【---- 状态数据 ----】
# spider完成爬取后发送Scrapy数据
# STATSMAILER_RCPTS = []
# 当spider结束时dump Scrapy状态数据到Scrapy log
# STATS_DUMP = True
# 收集数据的类。该类必须实现状态收集器(Stats Collector) API.
# STATS_CLASS = 'scrapy.statscol.MemoryStatsCollector'

# 【---- 内存调试 ----】
# 是否启用内存调试
# MEMDEBUG_ENABLED = False
# 内存调试时将会发送一份内存报告到指定的地址,否则该报告将写到log中。
# MEMDEBUG_NOTIFY = ['user@example.com']
# 是否启用内存使用插件,内存超出限制时，该插件将会关闭Scrapy进程
# MEMUSAGE_ENABLED = False
# 关闭Scrapy之前所允许的最大内存数(单位: MB)
# MEMUSAGE_LIMIT_MB = 0
# 达到内存限制时通知的email列表(默认 False)
# MEMUSAGE_NOTIFY_MAIL = ['user@example.com']
# 每个spider被关闭时是否发送内存使用报告
# MEMUSAGE_REPORT = False
# 发送警告email前所允许的最大内存数(单位: MB)
# MEMUSAGE_WARNING_MB = 0
