from flask import Flask, render_template, request
from random import randint, sample

app = Flask(__name__)

STUDENTS = {
    'Вихорева Софья': 'fdgs3gfhj4',
    'Ермашенкова Светлана': 'vggnfj3458',
    'Жихор Катарина': 'fdsger4121',
    'Иванова Полина': 'aaaaaa21425',
    'Камаева Кира': '1314gbfb',
    'Нестерова Яна': 'lgner57',
    'Ошевская Маргарита': 'fjdspf000',
    'Поливанова Екатерина': 'wfdgmdf92',
    'Протасов Тимофей': 'dsgjdsgg3',
    'Пятицкая Полина': 'sflsdg930',
    'Самохина Полина': 'zxcvxzvf1',
    'Фомичев Мирон': 'sf3033321',
    'Фролова Ольга': '00732423df',
    'Чивикова Любовь': 'sffsxvbxcgf2',
    'Шахиди Рустам': '1232fdslfs',
    'Шелепова Светлана': '214sxmzzpaz',
    'Бузанов Антон': 'key_for_lost_souls',
    'demo': 'DEMO_KEY'
}

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/rocket')
def rocket():
    return render_template('rocket.html')

@app.route('/rocket/api')
def rocket_api():
    args = request.args
    key = args.get('apikey')
    format = args.get('format')
    count = args.get('count')
    if not key or key not in STUDENTS.values():
        return 'ОШИБКА ДОСТУПА: проверьте правильность указания ключа.\nДержи жабу: https://ru.wikipedia.org/wiki/%D0%96%D0%B0%D0%B1%D1%8B'
    if args['apikey'] == 'DEMO_KEY':
        return 'Это демо-запрос, так не получится! Держи жабу: https://ru.wikipedia.org/wiki/%D0%96%D0%B0%D0%B1%D1%8B'
    if not format or format not in ['json', 'img']:
        return 'ОШИБКА ФОРМАТА: проверьте правильность поля format'
    if not count or not count.isdigit() or int(count) > 254 or int(count) < 1:
        return 'ОШИБКА КОЛИЧЕСТВА: проверьте правильность поля count'
    
    count = int(count)

    if count == 1:
        n = randint(1, 254)
        img = str(n) + '.jpg' if n < 55 else str(n) + '.png'

        if format == 'json':
            return ['/static/toads/' + img]
        else:
            return render_template('image.html', path='/static/toads/' + img)
    else:
        ns = sample(range(1, 254), count)
        if format == 'img':
            return 'ОШИБКА ФОРМАТА: не могу отобразить больше одной картинки'
        else:
            return ['/static/toads/' + str(n) + 'jpg' if n < 55 else '/static/toads/' + str(n) + '.png' for n in ns]

@app.route('/rocket/api/instruction', methods=['GET', 'POST'])
def rocket_api_instructions():
    args = request.form
    name = args['name'].capitalize().strip()
    surname = args['surname'].capitalize().strip()
    key = STUDENTS.get(f'{surname} {name}', 'В журнале нет такого ученика, проверьте правильность введённых данных!')
    return render_template('rocket_api.html', key=key)


@app.route('/dove')
def dove():
    return render_template('dove.html')

@app.route('/dove/api')
def dove_api():
    args = request.args
    key = args.get('apikey')
    format = args.get('format')
    count = args.get('count')
    if not key or key not in STUDENTS.values():
        return 'ОШИБКА ДОСТУПА: проверьте правильность указания ключа.\nМыш кродеться: https://ru.wikipedia.org/wiki/%D0%9B%D0%B5%D1%82%D1%83%D1%87%D0%B8%D0%B5_%D0%BC%D1%8B%D1%88%D0%B8'
    if args['apikey'] == 'DEMO_KEY':
        return 'Это демо-запрос, так не получится! Мыш кродеться: https://ru.wikipedia.org/wiki/%D0%9B%D0%B5%D1%82%D1%83%D1%87%D0%B8%D0%B5_%D0%BC%D1%8B%D1%88%D0%B8'
    if not format or format not in ['json', 'img']:
        return 'ОШИБКА ФОРМАТА: проверьте правильность поля format'
    if not count or not count.isdigit() or int(count) > 293 or int(count) < 1:
        return 'ОШИБКА КОЛИЧЕСТВА: проверьте правильность поля count'
    
    count = int(count)

    if count == 1:
        n = randint(1, 293)
        img = str(n) + '.png'

        if format == 'json':
            return ['/static/bats/' + img]
        else:
            return render_template('image.html', path='/static/bats/' + img)
    else:
        ns = sample(range(1, 293), count)
        if format == 'img':
            return 'ОШИБКА ФОРМАТА: не могу отобразить больше одной картинки'
        else:
            return ['/static/bats/' + str(n) + '.png' for n in ns]

@app.route('/dove/api/instruction', methods=['GET', 'POST'])
def dove_api_instructions():
    args = request.form
    name = args['name'].capitalize().strip()
    surname = args['surname'].capitalize().strip()
    key = STUDENTS.get(f'{surname} {name}', 'В журнале нет такого ученика, проверьте правильность введённых данных!')
    return render_template('dove_api.html', key=key)



if __name__ == '__main__':
    app.run(debug=True)