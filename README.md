# Lab-6
Лабораторная работа №6

Объектно-ориентированное программирование

**Задание**

* Создать класс с полями, в котором реализовать инициализатор и метод обработки данных.
* Спроектировать иерархию классов от изначально написаного класса, используя наследование. Дописать как минимум одно уникальное поле для каждого класса.
* В классах-наследниках реализовать метод обработки данных.

**Вариант 1**

Класс и его поля: Здание - площадь, стоимость 1 кв. метра, количество проживающих  
Метод 1: Рассчитать общую стоимость  
Иерархия: деревенский дом, многоквартирный городской дом  
Метод 2: Соотношение стоимости к числу проживающих  

**Вариант 2**

Класс и его поля: Станок - производительность (изделий в час), стоимость станка, средняя цена детали  
Метод 1: количество деталей для окупаемости  
Иерархия: фрезерный станок, станок с ЧПУ  
Метод 2: время окупаемости станка при фиксированной цене детали  

**Вариант 3**

Класс и его поля: Автомобиль: ёмкость бака, расход топлива, средняя скорость  
Метод 1: Рассчитать пройденное расстояние до полного опустошения бака  
Иерархия: грузовик, автобус  
Метод 2: Соотношение веса груза / числа пассажиров к количеству топлива на 250 км  

**Вариант 4**

Класс и его поля: Огнестрельное оружие: количество патронов в магазине, скорострельность, дальность стрельбы  
Метод 1: За сколько секунд магазин опустеет  
Иерархия: штурмовая винтовка, снайперская винтовка  
Метод 2: Соотношение скорострельности к дальности стрельбы  

**Вариант 5**

Класс и его поля: Оптический диск - ёмкость, обороты, толщина лазера в нм  
Метод 1: Сколько байт проходит лазер за 20 секунд (считать все дорожки равными длине окружности диска)  
Иерархия: CD, DVD  
Метод 2: среднее время одного оборота каждого вида диска  

**Вариант 6**

Класс и его поля: Фигура - три числа: a, b, c  
Метод 1: Объём V = a * b * c   
Иерархия: Тело с внутренней полостью (все параметры уменьшаются на d), массив из фигур.   
Метод 2: Объём тела за вычетом пустоты (V - (a-d) * (b-d) * (c-d)), суммарный объём нескольких одинаковых фигур  

**Вариант 7**

Класс и его поля: Лампа - мощность излучения в Вт, потребление энергии, срок службы  
Метод 1: через сколько дней лампа перегорит при работе 8 часов в сутки  
Иерархия: лампа дневного освещения, прожектор  
Метод 2: соотношение мощности излучения к энергопотреблению  

**Вариант 8**

Класс и его поля: Книга - количество страниц, время чтения одной страницы, количество картинок  
Метод 1: время чтения книги  
Иерархия: энциклопедия, телефонный справочник  
Метод 2: количество статей/номеров на страницу  

**Вариант 9**

Класс и его поля: Персонаж видеоигры: очки здоровья, очки выносливости, урон  
Метод 1: Рассчитать, сколько ударов наносит персонаж, пока выносливость не кончится  
Иерархия: слабый враг, босс  
Метод 2: Рассчитать, сколько ударов понадобится до смерти врага  

**Вариант 10**

Класс и его поля: Сотрудник: кол-во рабочих часов, ставка, коэффициент премии  
Метод 1: Рассчитать размер премии  
Иерархия: старший сотрудник, директор  
Метод 2: Соотношение зарплаты к рабочим часам  

**Допзадание**
Перегрузите оператор сложения __add__.
