#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
import re
import logging
import json


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
            result = urlopen('http://fundgz.1234567.com.cn/js/{0}.js?'.format(i)).read().decode("utf-8")
        except Exception, e:
            logging.error(e)
        else:
            result = eval(re.search('{.*}', result).group())
            result_all[result['name']] = result

    with open('result.json', 'w') as f:
        f.write(json.dumps(result_all, ensure_ascii=False))

fund_list = ['050002', '001052', '161725', '270042', '110011']
get_fund_data(fund_list)

