#Author:ithuplion
#多字典嵌套操作
ac_catalog = {
    "中国":{
        "www.baidu.com":["搜索引擎技术网站","很好"],
        "www.jd.com":["电商网站","很好"],
        "www.tx.com":["互联网公司","很好"],
    },
    "美国":{
            "www.goole.com":["搜索引擎技术网站","很好"],
            "www.yamaxun.com":["电商网站","很好"],
            "www.facebook.com":["互联网公司","很好"],
        }
}
print(ac_catalog)
print(ac_catalog["中国"])
print(ac_catalog["中国"]["www.baidu.com"])
print(ac_catalog["中国"]["www.baidu.com"][0])
print(ac_catalog["中国"]["www.baidu.com"][1])
a=ac_catalog["美国"]["www.goole.com"][0]
print(a)
b=ac_catalog["美国"]["www.goole.com"][1]
print(b)