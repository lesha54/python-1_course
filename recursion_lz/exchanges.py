def get_permutations(list):
    if len(list) <= 1:
        return [list]
    result = []
    for i in range(len(list)):
        value = list[i]
        other = list[:i] + list[i + 1:]
        for j in get_permutations(other):
            result.append([value] + j)
    return result

print("uенерация всех перестановок")
print("введите элементы списка: ")
ready_list = input().split()

all_variants = get_permutations(ready_list)
print("все возможные перестановки:")
for c in all_variants:
    print(c)
