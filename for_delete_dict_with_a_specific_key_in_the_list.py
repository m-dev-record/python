# リストの中に辞書が複数入った変数を用意する
list_of_dicts = [{'key1': 'value1', 'key2': 'value2'}, {'key3': 'value3', 'key4': 'value4'}]

# 削除するキー項目を指定する
keys_to_remove = ['key1', 'key4']

# 辞書からキー項目を削除する
for d in list_of_dicts:
    for key in keys_to_remove:
        d.pop(key, None)

# 結果を出力する
print(list_of_dicts)