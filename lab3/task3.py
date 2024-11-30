# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    num_leters = 0
    dict_ = {}
    for char in text:
        if char.isalpha():
            num_leters += 1
            if char in dict_:
                dict_[char] += 1
            else:
                dict_[char] = 1
    return num_leters, dict_

# TODO Напишите функцию calculate_frequency

def calculate_frequency(dict_, num_letters):
    for key, value in dict_.items():
        dict_[key] = value / num_letters
    return dict_


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_, num_leters = count_letters(main_str)
lettter_frequency = calculate_frequency(num_leters, dict_)
for key, value in lettter_frequency.items():
    print(f"{key}: {value:.2f}")