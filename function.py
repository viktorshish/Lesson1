## Функции

# Задание №1
def get_summ(one, two, delimiter='&'):
    return(f'{one}{delimiter}{two}')
    
vivod=get_summ('Learn','python').upper()
print(vivod)