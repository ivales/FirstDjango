from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item


class user:
    surname = 'Лескин'
    name = 'Иван'
    second_name = 'Андреевич'
    phone = '+79312867674'
    email = 'ivan.leskin@gs-labs.ru'


def main(request):
    return HttpResponse(f'<h1>"Изучаем django"</h1>'
                        f'<strong>Автор</strong>: <i>{user.surname} {user.name[0]}.{user.second_name[0]}.</i>')


def index(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse(f'Имя: <strong> {user.name} </strong><br>'
                        f'Отчество: <strong> {user.second_name} </strong><br>'
                        f'Фамилия: <strong> {user.surname} </strong><br>'
                        f'Телефон: <strong> {user.phone} </strong><br>'
                        f'email: <strong> {user.email} </strong>')


def items(request):
    items = list(Item.objects.values())
    return render(request, "items.html", {"items":items})


def item(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse(f'Товар с id={id} отсутствует')
    return render(request, "item.html", {"item":item})
