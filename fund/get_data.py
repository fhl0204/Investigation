#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
import logging
import json

result = request.urlopen('http://fundgz.1234567.com.cn/js/050002.js?').read().decode("utf-8")
#result = urlopen('http://fund.eastmoney.com/pingzhongdata/004473.js?').read()

result = eval(re.search('{.*}', result).group())
logging.critical(result)

with open('result.json', 'w') as f:
    f.write(json.dumps(result, ensure_ascii=False))










# soup = BeautifulSoup(result, 'html.parser', from_encoding = 'utf-8')
# for i in soup.find_all('td', class_='alignLeft'):
#     print i.get_text()
#     #print i.parent
#     try:
#         print i.next_sibling().get_text()
#     except:
#         pass