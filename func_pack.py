import random
import datetime
import json


# 随机生成唯一编码
def create_random_hash():
    nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    hash_code = hash(nowtime)
    # 绝对值处理
    if hash_code < 0 :
        hash_code = str(abs(hash_code))
    else:
        hash_code = str(hash_code)
    # 再添加随机位确保哈希值不重复
    seed = "abcdef"
    title = ""
    for _ in range(6):
        title = title + random.choice(seed)
    return str(title + hash_code)


# 生成记录唯一编码
def create_rec_hash():
    return "rec" + create_random_hash()


# 将 bytes 转换为 string
def _bytes_to_str(bytes_info):
    return bytes_info.decode("utf-8")


# 将 requests.get 或 post 的结果 result 获取到的信息转为由 dict 构成的 list
def get_api_info(request_result):
    content_str = request_result.content.decode("utf-8")
    list_content = []
    # print("json.loads length=" + str(len(json.loads(content_str))))
    # 若 api 返回的是空值
    if json.loads(content_str) is None:
        # 返回空的 list
        return []
    # 否则对 api 信息进行处理
    else:
        for item in json.loads(content_str):
            list_content.append(item)
        # 返回处理好的 list
        return list_content

