from django.core.paginator import Paginator
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:

def recipes_views(request, recipe:str):
    count_person = int(request.GET.get('person', 1))
    dict_person = {}
    context = {}

    data = DATA.get(recipe)
    for name, ingr in data.items():
        dict_person[name] = ingr * count_person
        context.setdefault('recipe', dict_person)



    return render(request, 'calculator/index.html', context )












    # count_person = int(request.GET.get('person', 1))
    # dict_person = {}
    # final_dish = {}
    # data = DATA.get(recipe)
    # for name, dish in data.items():
    #     dict_person[name] = dish * count_person
    # final_dish.setdefault('recipe', dict_person)
    #
    #
    #
    #
    # return render(request, 'calculator/index.html', final_dish)
