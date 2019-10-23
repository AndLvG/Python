# Это пишем в папке controllers файл default
def index():
    # Создаём формочку
    form1 = SQLFORM.factory(
        Field('visitor_surname', label='Фамилия',
                                 requires = IS_MATCH('^[абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ -]+$',
                                 error_message='Формат: Только кириллица')),
        Field('visitor_name', label='Имя',
                              requires = IS_MATCH('^[абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ -]+$',
                              error_message='Формат: Только кириллица')),
        Field('visitor_patronymic', label='Отчество',
                                    requires = IS_MATCH('^[абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ -]*$',
                                    error_message='Формат: Только кириллица')),
        Field('date_birth', label='Дата рождения'),
                            buttons=[],
                            table_name='tab1')
        # Вставим кнопки в форму
        form1.insert(1,DIV(INPUT(_class='button button-red', _id='click_search', _type='submit', _value='Найти'),  _class='btn1'))
        form1.insert(2,DIV(INPUT(_class='button button-red btn', _id='click_search', _type='button', _onclick='CLN();', _value='Очистить')))

    # Создадим табличку
    tab = TABLE(TR(TD('Имя'), TD('Фамилия'), TD('Отчество')), _CLASS="response_style_valid")
    # Обработчик формы
    if form1.process(keepvalues=True).accepted:
        # Так получаем доступ к полям формы после заполнения и нажатия кнопки Найти
        session._surname = form1.vars.visitor_surname
    # Так передаём формочку и табличку во вьюшку
    return dict(form1=form1, tab=tab)


# Так пишем во вьюшке \views\default\index.html
{{=form1}}
{{=tab}}