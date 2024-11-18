# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, n=','):
    set1 = set(participants_first_group.split(n))
    set2 = set(participants_second_group.split(n))
    general = list(set1.intersection(set2))
    general.sort()
    return general



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, n='|'))