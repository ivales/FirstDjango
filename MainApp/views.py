from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class user:
    surname = 'Лескин'
    name = 'Иван'
    second_name = 'Андреевич'
    phone = '+79312867674'
    email = 'ivan.leskin@gs-labs.ru'

items_dict = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def main(request):
    return HttpResponse(f'<h1>"Изучаем django"</h1>'
                        f'<strong>Автор</strong>: <i>{user.surname} {user.name[0]}.{user.second_name[0]}.</i>')


def about(request):
    return HttpResponse(f'Имя: <strong> {user.name} </strong><br>' 
                        f'Отчество: <strong> {user.second_name} </strong><br>'
                        f'Фамилия: <strong> {user.surname} </strong><br>'
                        f'Телефон: <strong> {user.phone} </strong><br>'
                        f'email: <strong> {user.email} </strong>')


def items(request):
    item_id = request.path[request.path.rfind('/')+1:]
    try:
        item_id = int(item_id)
        for data in items_dict:
            if item_id == data['id']:
                return HttpResponse(f'{data["name"]}, количество: {data["quantity"]}</br>'
                                    f'<a href = /items> Вернуться на страницу с товарами</a>')
        return HttpResponse(f'Товар с id={item_id} не найден')
    except ValueError:
        items_str = ""
        for item in items_dict:
            items_str += f'<a href= /items/{item["id"]}> {item["id"]}:{item["name"]}, количество: {item["quantity"]}</a> </br>'
        return HttpResponse(items_str)