# 2�̃��X�g��p�ӂ���
list1 = [{"key1": "value1"}, {"key2": "value2"}, {"key3": "value3"}]
list2 = [{"key3": "new_value3"}, {"key4": "value4"}, {"key5": "value5"}]

# �}�[�W����
merged_list = list1 + [d for d in list2 if d not in list1]

# ���ʂ��o�͂���
print(merged_list)