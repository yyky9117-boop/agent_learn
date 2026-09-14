# ==============================================
# 练习1：输入状态码列表，统计每种状态码出现次数
# 例如输入 [200,200,404,500,200,404] → {200:3, 404:2, 500:1}
# ==============================================
def count_status_code(code_list):
    # 定义空字典，字典用来【存储状态码:出现次数】
    result_dict = {}

    # for循环：逐个取出code_list里面的每一个状态码
    for code in code_list:
        # 判断：如果这个状态码已经在字典的key里面
        if code in result_dict:
            # 次数 +1
            result_dict[code] = result_dict[code] + 1
        else:
            # 如果字典里没有这个状态码，就新增一条，次数初始化为1
            result_dict[code] = 1

    # 函数最后，把统计好的字典返回出去
    return result_dict


# ==============================================
# 练习2：输入接口路径列表，返回出现最多的前3个接口
# ==============================================
def top3_api_path(path_list):
    # 第一步：统计每个接口出现多少次，空字典用于计数
    count_dict = {}
    for path in path_list:
        # dict.get(key, 默认值)：如果path不存在就返回0，然后+1
        # 等价于练习1的if判断写法，更简洁
        count_dict[path] = count_dict.get(path, 0) + 1

    # 第二步：排序
    # count_dict.items() 取出字典所有内容，格式：(接口名, 次数)
    # key=lambda x:x[1] 代表：按照【次数】排序（x[1]是元组第二个元素=次数）
    # reverse=True 代表 降序，从大到小排
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    # 第三步：列表推导式，取出前3个的接口名称
    # sorted_items[:3] 切片，取前3个元素；x[0]代表接口名字
    top3_list = [item[0] for item in sorted_items[:3]]

    return top3_list


# ==============================================
# 练习3：输入延迟列表，返回平均值；空列表返回0.0
# ==============================================
def calc_avg_delay(delay_list):
    # if not delay_list：判断列表是否为空，空列表在布尔判断里为False
    if not delay_list:
        return 0.0

    # sum()：内置函数，计算列表里面所有数字总和
    total_sum = sum(delay_list)
    # len()：内置函数，获取列表里面元素个数
    element_count = len(delay_list)
    # 平均值 = 总和 / 数量
    average = total_sum / element_count

    return average


# ===================== 测试代码 =====================
# 只有直接运行这个practice.py文件时，下面代码才执行
if __name__ == "__main__":
    # ===== 测试练习1 =====
    status_codes = [200, 200, 404, 500, 200, 404]
    res1 = count_status_code(status_codes)
    print("====练习1 状态码统计结果====")
    print(res1)

    # ===== 测试练习2 =====
    api_list = ["/api/login", "/api/get", "/api/login", "/api/info", "/api/login", "/api/get", "/api/set"]
    res2 = top3_api_path(api_list)
    print("\n====练习2 访问最多前3个接口====")
    print(res2)

    # ===== 测试练习3 =====
    delay_data1 = [12.5, 20.0, 17.5]
    res3_1 = calc_avg_delay(delay_data1)
    print("\n====练习3 延迟平均值（正常列表）====")
    print(res3_1)

    delay_data2 = []
    res3_2 = calc_avg_delay(delay_data2)
    print("\n====练习3 延迟平均值（空列表）====")
    print(res3_2)
