# 2つのリストを用意する
list1 = [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}]
list2 = [{"key3": "new_value3"}, {"key4": "value4"}, {"key5": "value5"}]

# マージする
merged_list = list1 + [d for d in list2 if d not in list1]

# 結果を出力する
print(merged_list)