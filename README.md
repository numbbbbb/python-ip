python-ip
===========
* 基于[全球 IPv4 地址归属地数据库](http://tool.17mon.cn/ipdb.html)修改的Python版本
* 只支持Python2
* 支持域名查询
* 支持IP直接查询


致谢
===========
我自己的代码写的不好，这个风格是参考[lxyu的代码](https://github.com/lxyu/17monip)修改的，大家star他的库比较好~


安装
===========

    $ sudo pip install ip2loc

使用方法
===========

    >>> import ip2loc
    >>> print ip2loc.find("www.langman1dian.com")
    '日本   日本'
    >>> print ip2loc.find("106.186.17.155")
    '日本   日本'


协议
===========
基于[WTFPL](http://en.wikipedia.org/wiki/WTFPL)协议开源。
