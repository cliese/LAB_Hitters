all_subsets = []
my_list =[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
my_cols =[1,2,3]
base_list = [[col] for col in my_cols]
all_subsets.append(base_list)
print(all_subsets[0])
subset = all_subsets[0][0]
remain_col = [col for col in my_cols if col not in subset]
print(remain_col)


test=[]
test.extend(base_list)
print(isinstance(test[0], list))

