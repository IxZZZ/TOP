#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests,json

n = 2022
xY = ["# Table of Contents"]
xOut = []

def log(s):
    global xOut
    xOut+=[s]

aA = []
cmpfun = lambda x:x["stargazers_count"]
for _ in range(10):
    log(f"## {str(n)}")
    r = requests.get(
        f'https://api.github.com/search/repositories?o=desc&q=CVE-{str(n)}-&s=updated&type=Repositories'
    )
    a = json.loads(r.text)
    if "items" in a:
        a = a["items"]
        xY += [f"* [{str(n)} year top total {len(a)}](#{str(n)})"]
        log("|star|updated_at|name|url|des|")
        log("|---|---|---|---|---|")
        #a.sort(key=cmpfun,reverse=True)
        aA += a
        # a = x1
        for x in a:
            try:
            # print(json.dumps(x))
            # if x:
                szDes = x["description"]
                if szDes is None:
                    szDes = ""
                log("|" +"|".join([str(x["stargazers_count"]),x["updated_at"],x["name"],x["html_url"],szDes])+"|")
            except Exception as e:
                pass
                # print(x)
                    # break
        n = n - 1
if len(xY) > 1:
    print("\n".join(xY))
    print("\n".join(xOut))

class Info():
    def __init__(self,description,stargazers_count,name,html_url):
        self.description = description
        self.stargazers_count = stargazers_count
        self.name = name
        self.html_url = html_url
    def __hash__(self):
        return hash(self.name + self.html_url)
    def __eq__(self, other):
        return self.html_url == other.html_url and self.name == other.name

xY = []
# 也许这里去重会有问题
temp = [
    Info(x["description"], x["stargazers_count"], x["name"], x["html_url"])
    for x in aA
]
aA = list(set(temp))
cmpfun = lambda x:x.stargazers_count
# aA.sort(key=cmpfun,reverse=True)
xY += ["# Top"]
xY += ["|star|updated_at|name|url|des|"]
xY += ["|---|---|---|---|---|"]
for x in aA:
    try:
        szDes = x.description
        if szDes is None:
            szDes = ""
        xY += ["|" +"|".join([str(x.stargazers_count),x["updated_at"],x.name,x.html_url,szDes])+"|"]
    except Exception as e:
        pass
if aA:
    with open("Top.md","wb") as f11:
        f11.write("\n".join(xY).encode('utf-8'))
# ?q=user%3Ahktalent&type=Repositories')
