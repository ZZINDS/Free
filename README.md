＃ 自由
获取免费的ip
get：获取并检测代理有效性。

可选参数包括：

num(需要的免费代理数量)；

api(指定代理抓取的网站，比如你只想要西刺代理，你可以令api='xici'，默认为随机抓取某个网站上的代理)；

retry(尝试抓取代理的次数，默认值为5)；

page(抓取某网站指定页的所有代理，默认抓取第一页，一般网站第一页的代理是最新且有效可能性最高的)；

proxy_type(抓取http代理还是https代理还是都要，默认是都抓取)；

quality(代理是高匿还是普通的还是都要，默认是都抓取)；

headers(测试代理有效性时使用的请求头，默认是只加了user-agent的请求头)；

method(使用GET还是POST方法测试代理的有效性)；

host(利用代理请求host来测试代理是否有效，默认的测试host为百度)。

get_proxy：只获取代理，而不检测代理的有效性。

可选参数包括：

page, proxy_type, quality, api。

含义同上。

③check_proxy：只测试代理的有效性。

可选参数包括

ip_port((ip, port)格式的数据)；

host, headers, method。

含义同上。

print_help()：打印使用帮助

print_about()：打印作者信息
