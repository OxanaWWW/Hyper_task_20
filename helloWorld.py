s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate' \
    ' banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit ' \
    'banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange ' \
    'lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana ' \
    'quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate' \
    ' banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon ' \
    'pomegranate barley plum banana quince barley lime grapefruit pomegranate barley start start start start'

a = [i for i in s.split() if i.startswith('s')]
words_list = {}.fromkeys(a,0)
for word in a:

    words_list[word] += 1


print(words_list)
max_count = max(words_list.values())
x = [k for k,v  in words_list.items() if v == max_count]
print("Наиболее часто встречающееся слово:", sorted(x)[0])

