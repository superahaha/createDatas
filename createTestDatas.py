#-*- coding:utf-8 -*-

import random
import string

class CreateData(object):
# 随机生成一万条数据
  def get_name(self):
    str_char = ""
    get_char = string.ascii_letters + string.digits
    get_len = random.randint(6, 12)
    for i in range(1, get_len+1):
      str_char += random.choice(get_char)
    return str_char
 
