# -*- coding: utf-8 -*-

# ------------------------------项目配置----------------------------------------

BOT_NAME = "zhihu"

SPIDER_MODULES = ["zhihu.spiders"]
NEWSPIDER_MODULE = "zhihu.spiders"

# -----------------------------参数配置----------------------------------------

# 代理 IP 池链接
DEFAULT_ACCESS = "http://www.zhihu.com/"
PROXY_HOST = "http://proxy-pool.edge.zylliondata.local/get"

# MongoDB 配置
MONGODB_URI = "mongodb://172.25.2.31:27017,172.25.2.32:27017,172.25.2.33:27017"
MONGODB_DATABASE = "DSG2_liuy"
# -----------------------------Redis 单机模式----------------------------------------
# Redis 单机地址
REDIS_HOST = "172.25.2.25"
REDIS_PORT = 6379

# REDIS 单机模式配置参数
REDIS_PARAMS = {
    "password": "sinocbd",
    "db": 0
}

# -----------------------------Redis 哨兵模式----------------------------------------
# Redis 哨兵地址
REDIS_SENTINELS = [
    ('172.25.2.25', 26379),
    ('172.25.2.26', 26379),
    ('172.25.2.27', 26379)
]

# REDIS_SENTINEL_PARAMS 哨兵模式配置参数。
REDIS_SENTINEL_PARAMS = {
    "service_name": "mymaster",
    "password": "sinocbd",
    "db": 0
}

# -----------------------------Redis 集群模式----------------------------------------

# Redis 集群地址
REDIS_MASTER_NODES = [
    {"host": "172.25.2.25", "port": "6379"},
    {"host": "172.25.2.26", "port": "6379"},
    {"host": "172.25.2.27", "port": "6379"},
]

# REDIS_CLUSTER_PARAMS 集群模式配置参数
REDIS_CLUSTER_PARAMS = {
    "password": "sinocbd",
    "db": 0
}

# -----------------------------------全局并发数的一些配置-----------------------------------

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 1、下载器总共最大处理的并发请求数,默认值16
# CONCURRENT_REQUESTS = 10  # 并发数量

# 默认 Item 并发数：100
# CONCURRENT_ITEMS = 100

# The download delay setting will honor only one of:
# 默认每个域名的并发数：8
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 每个IP的最大并发数：0表示忽略
# CONCURRENT_REQUESTS_PER_IP = 0

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 如果没有开启智能限速，这个值就代表一个规定死的值，代表对同一网址延迟请求的秒数
# 最小延迟
# DOWNLOAD_DELAY = 0.7

# The download delay setting will honor only one of:
# 每个域名能够被执行的最大并发请求数目，默认值8
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 能够被单个IP处理的并发请求数，默认值0，代表无限制，需要注意两点
# I、如果不为零，那CONCURRENT_REQUESTS_PER_DOMAIN将被忽略，即并发数的限制是按照每个IP来计算，而不是每个域名
# II、该设置也影响DOWNLOAD_DELAY，如果该值不为零，那么DOWNLOAD_DELAY下载延迟是限制每个IP而不是每个域
# CONCURRENT_REQUESTS_PER_IP = 16


# --------------------------scrapy-redis配置----------------------------------------

# 调度器队列
# 访问URL去重
# 确保所有的爬虫通过Redis去重，使用Scrapy-Redis的去重组件,不再使用scrapy的去重组件
DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RFPDupeFilter"
# 启用Redis调度存储请求队列，使用Scrapy-Redis的调度器,不再使用scrapy的调度器
SCHEDULER = "scrapy_redis_sentinel.scheduler.Scheduler"

# 爬取深度与爬取方式
# 爬虫允许的最大深度，可以通过meta查看当前深度；0表示无深度
# DEPTH_LIMIT = 3

# 爬取时，0表示深度优先Lifo(默认)；1表示广度优先FiFo

# 后进先出，深度优先
# DEPTH_PRIORITY = 0
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleLifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.LifoMemoryQueue'
# 先进先出，广度优先

# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# 指定排序爬取地址时使用的队列，
# 默认的 按优先级排序(Scrapy默认)，由sorted set实现的一种非FIFO、LIFO方式。
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderPriorityQueue'
# 可选的 按先进先出排序（FIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderStack'
# 可选的 按后进先出排序（LIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderStack'
# 在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues
# SCHEDULER_PERSIST = True
# 只在使用SpiderQueue或者SpiderStack是有效的参数，指定爬虫关闭的最大间隔时间
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# -----------------------------robots协议、请求配置---------------------------------------------
# 是否遵循爬虫协议
# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 不遵守网络爬虫规则 :)

# 客户端User-Agent请求头
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 它定义了在抓取网站所使用的用户代理，默认值：“Scrapy / VERSION“
# USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# 对于失败的HTTP请求(如超时)进行重试会降低爬取效率，当爬取目标基数很大时，舍弃部分数据不影响大局，提高效率
RETRY_ENABLED = True

DOWNLOAD_TIMEOUT = 260  # 请求超时时间

# --------------------------------日志文件配置-----------------------------------
# 默认: True,是否启用logging。
# LOG_ENABLED=True
# 默认: 'utf-8',logging使用的编码。
# LOG_ENCODING='utf-8'
# 它是利用它的日志信息可以被格式化的字符串。默认值：'%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# LOG_FORMAT='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# 它是利用它的日期/时间可以格式化字符串。默认值： '%Y-%m-%d %H:%M:%S'
# LOG_DATEFORMAT='%Y-%m-%d %H:%M:%S'
# 日志文件名
# LOG_FILE = "dg.log"
# 日志文件级别,默认值：“DEBUG”,log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG 。
LOG_LEVEL = "DEBUG"  # 日志等级  注意: 调试时可以将此句注释或改为 'DEBUG'；运行为‘INFO’

# ----------------------redis的地址配置-------------------------------------
# 指定redis数据库的连接参数
# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
# 指定用于连接redis的URL（可选）
# 如果设置此项，则此项优先级高于设置的REDIS_HOST 和 REDIS_PORT
# REDIS_URL = 'redis://root:密码@主机ＩＰ:端口'
# REDIS_URL = 'redis://root:123456@127.0.0.1:6379'
# REDIS_URL = 'redis://root:%s@%s:%s' % (password_redis, host_redis, port_redis)
# 自定义的redis参数（连接超时之类的）
# REDIS_PARAMS = {'db': db_redis}
# Specify the host and port to use when connecting to Redis (optional).
# 指定连接到redis时使用的端口和地址（可选）

# ----------------------redis的存储相关配置-------------------------------------

# 序列化项目管道作为redis Key存储
# REDIS_ITEMS_KEY = '%(spider)s:items'

# 默认使用ScrapyJSONEncoder进行项目序列化
# You can use any importable path to a callable object.
# REDIS_ITEMS_SERIALIZER = 'json.dumps'

# 自定义redis客户端类
# REDIS_PARAMS['redis_cls'] = 'zhihu.RedisClient'

# 如果为True，则使用redis的'spop'进行操作。
# 如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
# REDIS_START_URLS_AS_SET = False

# RedisSpider和RedisCrawlSpider默认 start_usls 键
# REDIS_START_URLS_KEY = '%(name)s:start_urls'

# 设置redis使用utf-8之外的编码
# REDIS_ENCODING = 'latin1'

# ---------------------------------------下载参数配置-------------------------------

# 这是响应的下载器下载的最大尺寸，默认值：1073741824 (1024MB)
# DOWNLOAD_MAXSIZE=1073741824
# 它定义为响应下载警告的大小，默认值：33554432 (32MB)
# DOWNLOAD_WARNSIZE=33554432


# ---------------------------------------其它请求配置-----------------------------------

# 是否支持cookie，cookiejar进行操作cookie，默认开启,禁用cookies,有些站点会从cookies中判断是否为爬虫
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
# COOKIES_DEBUG = True

# 禁止重定向
# 除非您对跟进重定向感兴趣，否则请考虑关闭重定向。 当进行通用爬取时，一般的做法是保存重定向的地址，并在之后的爬取进行解析。
# 这保证了每批爬取的request数目在一定的数量， 否则重定向循环可能会导致爬虫在某个站点耗费过多资源。
# REDIRECT_ENABLED = False

# 忽略状态
# HTTPERROR_ALLOWED_CODES = [404]

# FEED_EXPORT_ENCODING = "utf-8"

# Telnet用于查看当前爬虫的信息，操作爬虫等...使用telnet ip port ，然后通过命令操作
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_HOST = '127.0.0.1'
# TELNETCONSOLE_PORT = [6023,]

# Scrapy发送HTTP请求默认使用的请求头
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;"
#               "q=0.8,application/signed-exchange;v=b3",
#     "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,und;q=0.6",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
# }

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR "
    "2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
]

# ---------------------------------------中间件配置-----------------------------------

# 代理 IP 池配置

PROXIES = [
    "1.85.220.195:8118",
    "60.255.186.169:8888",
    "118.187.58.34:53281",
    "116.224.191.141:8118",
    "120.27.5.62:9090",
    "119.132.250.156:53281",
    "139.129.166.68:3128",
]

# 启用或禁用downloader中间件
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "zhihu.middlewares.ZhihuDownloaderMiddleware": None,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": 1,
    "zhihu.middlewares.RandomUserAgentMiddleware": 100,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": None,
    "zhihu.middlewares.RandomProxyMiddleware": None,
}

# 超时沉默关闭机制扩展
MYEXT_ENABLED = True  # True 为开启扩展

# 配置空闲持续时间单位为 60个 ，一个时间单位为5s,也就是五分钟
IDLE_NUMBER = 48

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
    "zhihu.middlewares.RedisSpiderSmartIdleClosedExensions": 500
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# 启用或禁用扩展
# EXTENSIONS = {
#    'zhihu.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# 配置项目管道
ITEM_PIPELINES = {
    "zhihu.pipelines.MyFilesPipeline": None,
    "zhihu.pipelines.MongoDBPipeline": 300,
}

# FILES_STORE = 'file'  # 文件存储路径

# ---------------------------------------限速算法（延迟）配置-----------------------------------

# 自动限速算法基于以下规则调整下载延迟
# 1、spiders开始时的下载延迟是基于AUTOTHROTTLE_START_DELAY的值
# 2、当收到一个response，对目标站点的下载延迟=收到响应的延迟时间/AUTOTHROTTLE_TARGET_CONCURRENCY
# 3、下一次请求的下载延迟就被设置成：对目标站点下载延迟时间和过去的下载延迟时间的平均值
# 4、没有达到200个response则不允许降低延迟
# 5、下载延迟不能变的比DOWNLOAD_DELAY更低或者比AUTOTHROTTLE_MAX_DELAY更高
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html

# Disable Telnet Console (enabled by default)
# 它定义是否启用telnetconsole,默认值：True
# TELNETCONSOLE_ENABLED = False

# 启用并配置自动节流阀扩展(默认禁用)　防止请求过快，将服务器抓崩。
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 起始的延迟
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 最大延迟
# AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
# 每秒并发请求数的平均值，不能高于 CONCURRENT_REQUESTS_PER_DOMAIN或CONCURRENT_REQUESTS_PER_IP，调高了则吞吐量增大强奸目标站点，调低了则对目标站点更加”礼貌“
# 每个特定的时间点，scrapy并发请求的数目都可能高于或低于该值，这是爬虫视图达到的建议值而不是硬限制
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 调试
# AUTOTHROTTLE_DEBUG = False

# ---------------------------------------缓存配置-----------------------------------

# Enable and configure HTTP caching (disabled by default)
# 启用和配置HTTP缓存（默认禁用）
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 是否启用缓存策略
# HTTPCACHE_ENABLED = True

# 缓存策略：所有请求均缓存，下次在请求直接访问原来的缓存即可
# HTTPCACHE_POLICY = "scrapy.extensions.httpcache.DummyPolicy"

# 缓存策略：根据Http响应头：Cache-Control、Last-Modified 等进行缓存的策略
# HTTPCACHE_POLICY = "scrapy.extensions.httpcache.RFC2616Policy"

# 缓存超时时间
# HTTPCACHE_EXPIRATION_SECS = 0

# 缓存保存路径
# HTTPCACHE_DIR = 'httpcache'

# 缓存忽略的Http状态码
# HTTPCACHE_IGNORE_HTTP_CODES = []

# 缓存存储的插件
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# -----------------------------------------其它相关配置-------------------------------------------------------

# 它定义了将被允许抓取的网址的长度为URL的最大极限，默认值：2083
# URLLENGTH_LIMIT=2083
# 爬取网站最大允许的深度(depth)值,默认值0。如果为0，则没有限制
# DEPTH_LIMIT = 3
# 整数值。用于根据深度调整request优先级。如果为0，则不根据深度进行优先级调整。
# DEPTH_PRIORITY=3

# 最大空闲时间防止分布式爬虫因为等待而关闭
# 这只有当上面设置的队列类是SpiderQueue或SpiderStack时才有效
# 并且当您的蜘蛛首次启动时，也可能会阻止同一时间启动（由于队列为空）
# SCHEDULER_IDLE_BEFORE_CLOSE = 10
