#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
import re
import logging
import json
import sys
print sys.getdefaultencoding()

#沪深300 中证500 050002 001052
def get_fund_data(fund_list):
    """Get the data of fund.

    :param fund_list: a list contains the codes of fund
    :return: 0 or file result.json
    """
    if not isinstance(fund_list, list):
        logging.error('Parameter fund_list is not a list')
        return 0
    result_all = {}
    for i in fund_list:
        try:
            result = urlopen('http://fundgz.1234567.com.cn/js/{0}.js?'.format(i)).read()
            #result = urlopen('http://fund.eastmoney.com/js/fundcode_search.js').read()
            # http://fund.eastmoney.com/pingzhongdata/000001.js
            print result, type(result)
        except Exception, e:
            logging.error(e)
        else:
            result = eval(re.search('{.*}', result).group())
            result["name"] = result["name"].decode('gbk') #.encode('utf8')
            result_all[result['name']] = result

    print result_all

fund_list = ['050002', '001052']
get_fund_data(fund_list)
