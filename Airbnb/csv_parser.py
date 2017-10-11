# 举个例子:
# 给定一个CSV文件，格式是 “some_name|some_address|some_phone|some_job”
# 要求输出Json format “{name:some_name, address:some_addres,phone:some_phone, job:some_job}”
# 输入内容中有些特殊符号要注意处理

def parseCSV(file):
    