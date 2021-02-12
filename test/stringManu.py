tmp_arr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
tmp_str = ''
for i in range(len(tmp_arr)):
    tmp = tmp_arr[i]
    if i == len(tmp_arr)-1:
        tmp_str = tmp_str + tmp[0:3]
    else:
        tmp_str = tmp_str + tmp[0:3] + ','

print(tmp_str)