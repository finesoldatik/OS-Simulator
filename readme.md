<h1>Краткая документация возможностей API psevdoOS</h1>
<h1>Краткая документация по созданию приложений.</h1>
<h2>План и начало работы</h2>
<hr>
<div>
    <h3>Для создания вашего первого приложения потребуется:</h3>
    <ul>
    <li><h3>Создать новую папку внутри директории psevdoOS, название папки=название пакета программ, в ней вы можете создать целое множество приложений и даже по желанию делиться ими с друзьями и знакомыми</h3></li>
    <li><h3>Создать первый файл вашего приложения. (создайте python файл с любым названием)</h3></li>
    <li><h3>Написать код для приложения.</h3></li>
    <li><h3>Приложение готово.</h3></li>
    </ul>
    <h4>*План с небольшими пояснениями*</h4>
</div>
<hr>
<div>
    <h3>Первый шаг: подготовка рабочего места.</h3>
    <h3>Отлично, надеюсь вы прочитали план и готовы начинать! Для начала нам нужно создать наш пакет программ, зайдем в директорию проекта "psevdoOS" и создадим папку, назовем её к примеру "my_best_programs" (название может быть почти любым, самый главный критерий - оно должно быть на английском языке). После этого перейдем в нее и создадим наш первый файл приложения (здесь тоже все пишем на английском языке), назовём его к примеру "program.py". Подготовка закончена, давай приступим к следующим шагам?</h3>
    <h4>*Документация расчитана для тех, кто уже имел дело с кодом и уже имеет установленные python и редактор кода*</h4>
</div>
<hr>
<div>
    <h2>Второй шаг: Работа с кодом.</h2>
    <h3>Как же все таки хорошо у нас все получается! Надеюсь приложение будет зачетным! На этом шаге тебе будет труднее всего, но ты не сдавайся, я в тебя верю! Для начала откроем редактор и напишем пару строчек кода.</h3>
    <div style="background-color: #1f2024; padding: 10px 20px; border-radius: 10px;">
        <h4><p>from tkinter import *</p>
        <p>from modules.app import app</p>
        <p>class App(app):</p>
        <p style="margin-left: 30px;">def __init__(self, win):</p>
        <p style="margin-left: 60px;">super().__init__(win=win, main_func="main", name="Калькулятор")</p>
        <p style="margin-left: 60px;">self.set_size(width=30, height=20.3)</p>
        <p style="margin-left: 60px;">self.expression = ""</p></h4>
    </div>
    <h3>В этом примере мы будем писать простенький калькулятор, такой же, как в psevdoOS. Как видите мы импортировали tkinter и "app" (этот модуль написан для упрощения написания программ для psevdoOS, пока что он в разработке и многие вещи не работают так, как надо, но вы можете переписать его сами, если захотите). После импортов мы создали класс App и инициализировали его и класс-родитель, аргументами мы передали окно (оно всегда передается приложениям), главную функцию и название приложения. "self.set_size(width=30, height=20.3)" - это временная мера для передвижения приложения, пока что нужно подгонять эти параметры, чтобы окно программы ходило вместе с передвижением мыши, позже с обновлениями эта функция будет убрана и все будет просчитываться автоматически. 'self.expression = ""' - переменная калькулятора</h3>
    <div style="background-color: #1f2024; padding: 10px 20px; border-radius: 10px;">
        <h4><p style="margin-left: 30px;">def main(self):</p>
        <p style="margin-left: 60px;">frame_input = Frame(self.main_frame)</p>
        <p style="margin-left: 60px;">frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")</p>
        <p style="margin-left: 60px;">self.input_field = Entry(frame_input, font='Arial 15 bold', width=24, state="readonly")</p>
        <p style="margin-left: 60px;">self.input_field.pack(fill=BOTH)</p>
        <p style="margin-left: 60px;">buttons = (('7', '8', '9', '/'),</p>
        <p style="margin-left: 150px;">('4', '5', '6', '*'),</p>
        <p style="margin-left: 150px;">('1', '2', '3', '-'),</p>
        <p style="margin-left: 150px;">('0', '.', '=', '+'))</p>
        <p style="margin-left: 60px;">button = Button(self.main_frame, text='C', command=lambda: self.bt_clear())</p>
        <p style="margin-left: 60px;">button.grid(row=1, column=3, sticky="nsew")</p>
        <p style="margin-left: 60px;">for ro in range(4):</p>
        <p style="margin-left: 90px;">for co in range(4):</p>
        <p style="margin-left: 120px;">Button(self.main_frame, width=2, height=3, text=buttons[ro][co], command=lambda row=ro, col=co: self.btn_click(buttons[row][col])).grid(row=ro + 2, column=co, sticky="nsew", padx=1, pady=1)</p>
        <p style="margin-left: 60px;">self.add_menu()</p></h4>
    </div>
    <h3>Здесь нужно обратить внимание на название функции, оно должно быть такое же, какое мы передаем аргументом во время инициализации класса, а также в конце всего кода мы написали "self.add_menu()", эта функция добавляет 2 команды в меню (центрировать и закрыть), в остальном это код калькулятора.</h3>
    <div style="background-color: #1f2024; padding: 10px 20px; border-radius: 10px;">
        <h4><p style="margin-left: 30px;">def bt_clear(self):</p>
        <p style="margin-left: 60px;">self.expression = ""</p>
        <p style="margin-left: 60px;">self.input_field['state'] = "normal"</p>
        <p style="margin-left: 60px;">self.input_field.delete(0, END)</p>
        <p style="margin-left: 60px;">self.input_field['state'] = "readonly"</p></h4>
    </div>
    <h3>И это тоже код калькулятора, не будем входить в подробности, все же не это изучаем.</h3>
    <div style="background-color: #1f2024; padding: 10px 20px; border-radius: 10px;">
        <h4><p style="margin-left: 30px;">def btn_click(self, item):</p>
        <p style="margin-left: 60px;">try:</p>
        <p style="margin-left: 90px;">self.input_field['state'] = "normal"</p>
        <p style="margin-left: 90px;">self.expression += item</p>
        <p style="margin-left: 90px;">self.input_field.insert(END, item)</p>
        <p style="margin-left: 90px;">if item == '=':</p>
        <p style="margin-left: 120px;">result = str(eval(self.expression[:-1]))</p>
        <p style="margin-left: 120px;">self.input_field.delete('0', END)</p>
        <p style="margin-left: 120px;">self.input_field.insert(END, result)</p>
        <p style="margin-left: 120px;">self.expression = ""</p>
        <p style="margin-left: 90px;">self.input_field['state'] = "readonly"</p>
        <p style="margin-left: 60px;">except ZeroDivisionError:</p>
        <p style="margin-left: 90px;">self.input_field.delete(0, END)</p>
        <p style="margin-left: 90px;">self.input_field.insert(0, 'Ошибка (деление на 0)')</p>
        <p style="margin-left: 60px;">except SyntaxError:</p>
        <p style="margin-left: 90px;">self.input_field.delete(0, END)</p>
        <p style="margin-left: 90px;">self.input_field.insert(0, 'Ошибка')</p></h4>
    </div>
    <h3>Наконец-то мы закончили с кодом, полная версия выглядит так:</h3>
    <div style="background-color: #1f2024; padding: 10px 20px; border-radius: 10px;">
        <h4><<p>from tkinter import *</p>
        <p>from modules.app import app</p>
        <p>class App(app):</p>
        <p style="margin-left: 30px;">def __init__(self, win):</p>
        <p style="margin-left: 60px;">super().__init__(win=win, main_func="main", name="Калькулятор")</p>
        <p style="margin-left: 60px;">self.set_size(width=30, height=20.3)</p>
        <p style="margin-left: 60px;">self.expression = ""</p>
        <p style="margin-left: 30px;">def btn_click(self, item):</p>
        <p style="margin-left: 60px;">try:</p>
        <p style="margin-left: 90px;">self.input_field['state'] = "normal"</p>
        <p style="margin-left: 90px;">self.expression += item</p>
        <p style="margin-left: 90px;">self.input_field.insert(END, item)</p>
        <p style="margin-left: 90px;">if item == '=':</p>
        <p style="margin-left: 120px;">result = str(eval(self.expression[:-1]))</p>
        <p style="margin-left: 120px;">self.input_field.delete('0', END)</p>
        <p style="margin-left: 120px;">self.input_field.insert(END, result)</p>
        <p style="margin-left: 120px;">self.expression = ""</p>
        <p style="margin-left: 90px;">self.input_field['state'] = "readonly"</p>
        <p style="margin-left: 60px;">except ZeroDivisionError:</p>
        <p style="margin-left: 90px;">self.input_field.delete(0, END)</p>
        <p style="margin-left: 90px;">self.input_field.insert(0, 'Ошибка (деление на 0)')</p>
        <p style="margin-left: 60px;">except SyntaxError:</p>
        <p style="margin-left: 90px;">self.input_field.delete(0, END)</p>
        <p style="margin-left: 90px;">self.input_field.insert(0, 'Ошибка')</p>
        <p style="margin-left: 30px;">def bt_clear(self):</p>
        <p style="margin-left: 60px;">self.expression = ""</p>
        <p style="margin-left: 60px;">self.input_field['state'] = "normal"</p>
        <p style="margin-left: 60px;">self.input_field.delete(0, END)</p>
        <p style="margin-left: 60px;">self.input_field['state'] = "readonly"</p>
        <p style="margin-left: 30px;">def main(self):</p>
        <p style="margin-left: 60px;">frame_input = Frame(self.main_frame)</p>
        <p style="margin-left: 60px;">frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")</p>
        <p style="margin-left: 60px;">self.input_field = Entry(frame_input, font='Arial 15 bold', width=24, state="readonly")</p>
        <p style="margin-left: 60px;">self.input_field.pack(fill=BOTH)</p>
        <p style="margin-left: 60px;">buttons = (('7', '8', '9', '/'),</p>
        <p style="margin-left: 150px;">('4', '5', '6', '*'),</p>
        <p style="margin-left: 150px;">('1', '2', '3', '-'),</p>
        <p style="margin-left: 150px;">('0', '.', '=', '+'))</p>
        <p style="margin-left: 60px;">button = Button(self.main_frame, text='C', command=lambda: self.bt_clear())</p>
        <p style="margin-left: 60px;">button.grid(row=1, column=3, sticky="nsew")</p>
        <p style="margin-left: 60px;">for ro in range(4):</p>
        <p style="margin-left: 90px;">for co in range(4):</p>
        <p style="margin-left: 120px;">Button(self.main_frame, width=2, height=3, text=buttons[ro][co], command=lambda row=ro, col=co: self.btn_click(buttons[row][col])).grid(row=ro + 2, column=co, sticky="nsew", padx=1, pady=1)</p>
        <p style="margin-left: 60px;">self.add_menu()</p></h4>
    </div>
</div>
<hr>
<h3>Третий шаг: запуск приложения</h3>
<h3>Приложение готово! Давайте зайдем в psevdoOS, откроем терминал и напишем: "sapp my_best_programs.program", приложение откроется на рабочем столе и его название появится на панели задач</h3>
<hr>
<h1>Краткая документация по созданию процессов.</h1>
<h2>Это очень легко!</h2>
<hr>
<h3>Давайте создадим наш первый процесс, который будет запускаться при старте и добавлять наш выше написанный калькулятор в контекстное меню, чтобы нам было удобнее запускать его.</h3>
<h3>Для этого зайдем в директорию проекта "psevdoOS" и найдем папку "startup_processes", заходим в нее и видим файл "start.py", пока что он пустой, так что, почему бы не воспользоваться им? (вы можете просто создать другой файл рядом при желании, все файлы из этой папки автоматически запускаются при старте psevdoOS)</h3>
<h3>Напишем пару строк кода, хотя хватит и одной, но перед началом изменим с этого:</h3>
<div style="background-color: #1f2024; padding: 10px 20px; border-radius: 10px;">
    <h4><p>class Process:</p>
    <p style="margin-left: 30px;">def __init__(self, win):</p>
    <p style="margin-left: 60px;">print("process: start")</p></h4>
</div>
<h3>На это:</h3>
<div style="background-color: #1f2024; padding: 10px 20px; border-radius: 10px;">
    <h4><p>class Process:</p>
    <p style="margin-left: 30px;">def __init__(self, win):</p>
    <p style="margin-left: 60px;">self.win.menu.add_command(label="Мой калькулятор", command=lambda: start_program("my_best_programs.program")</p></h4>
</div>
<h3>Вот и все, мы добавили наш калькулятор в контекстное меню.</h3>
<h2>*Позже появится вики со всеми функциями, классами и тому подобным, так что ждите обновлений, друзья!*</h2>
