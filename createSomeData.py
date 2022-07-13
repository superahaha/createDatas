#-*- coding:utf-8 -*-

from asyncio.windows_events import NULL
import random
import string

class CreateData(object):
# 随机生成一万条数据
  def __init__(self):
    self.name = NULL
  
  # 生成姓名，由字母、数字、符号组成，6~12位
  def get_name(self):
    str_char = ""
    get_char = string.ascii_letters + string.digits
    get_len = random.randint(6, 12)
    for i in range(1, get_len+1):
      str_char += random.choice(get_char)
    self.name = str_char
    return str_char

  def get_sex(self):
    return random.choice(["男", "女"])

  def get_age(self):
    return random.randint(18, 120)

  def get_email(self):
    return self.name + random.choice(["@qq.com", "@126.com", "@163.com"])
  
  # 以列表形式返回数据
  def get_one_data(self):
    return [self.get_name(), self.get_sex(), self.get_age(), self.get_email()]

  # 测试代码
if __name__ == "__main__":
  create = CreateData()
  print("姓名是：", create.get_name())
  print("性别是：", create.get_sex())
  print("年龄是：", create.get_age())
  print("邮箱是：", create.get_email())
