products = [
    ("键盘", 299),
    ("鼠标", 129),
    ("显示器", 1599)
]

# enumerate 同时获得序号和元素
for rank, (item, value) in enumerate(products, start=1):
    print("第",rank,"名", item, "显示",value,"元")