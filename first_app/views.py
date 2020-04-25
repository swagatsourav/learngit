from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<p style="font-size:100px;color:cyan;">Hello World!</p>')


def index2(request):
    return HttpResponse('<p style="font-size:100px;color:cyan;">Hello World of index2!</p>')


def first(request):
    value = {
        'key1': 'id1',
        'key2': 'id2',
        'key3': {'in1key1': 'id4', 'in1key2': 'id5', 'in1key3':
                 {'in2key1': 'id6', 'in2key2': 'id7', 'in3key3': 'id8'}},
        'key4': 'id9',
        'key5': 'id10',
        'key6': {'in1key1': 'id11', 'in1key2': 'id12', 'in1key3':
                 {'in2key1': 'id13', 'in2key2': 'id14', 'in3key3': 'id15'}},
    }
    prep_string = ''

    def createLebel(arg, level=0):
        nonlocal prep_string
        prep_string += "  <ul>"
        for i in arg.keys():
            if isinstance(arg[i], dict):
                prep_string += '    <li class="headings">'
                prep_string += f"      <a href=\"#\">{i}</a>"
                createLebel(arg[i])
                prep_string += "    </li>"
            else:
                prep_string += f'    <li class="items" id="{arg[i]}">'
                prep_string += f"      <a href=\"#\">{i}</a>"
                prep_string += "    </li>"
        prep_string += "  </ul>"

    createLebel(value)

    first_dict = {'unordered_list': prep_string,
                  'name_insert': 'Swagat'}

    return render(request, 'first_app/first.html', context=first_dict)
