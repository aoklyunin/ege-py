# Java решения заданий ЕГЭ

Объяснения лежат [здесь](https://ege.buran.rest)

Задания взяты с [сайта Константина Полякова](https://kpolyakov.spb.ru/school/ege.htm).

[Java Исходники решений](https://github.com/aoklyunin/ege-java)

[С++ Исходники решений](https://github.com/aoklyunin/ege-cpp) 

## Задание 1

### Пример 1

(№ 4145) (Е. Джобс) На рисунке справа схема дорог Н-ского района изображена в виде графа, в
таблице содержатся сведения о длинах этих дорог (в километрах).
Так как таблицу и схему рисовали независимо друг от друга, то нумерация населённых пунктов
в таблице никак не связана с буквенными обозначениями на графе. В таблице в левом столбце
указаны номера пунктов, откуда совершается движение, в первой строке – куда. Определите
длину дороги между пунктами А и Б, если известно, что длина дороги между Г и Д меньше длины
дороги между Г и Е. Передвигаться можно только по указанным дорогам.

![Задание 1](problems/problem1/task1.png)

Ответ: 10

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example1.py)

### Пример 2

Р-09. На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице
содержатся сведения о длинах этих дорог (в километрах). Так как таблицу и схему рисовали 
независимо друг от друга, то нумерация населённых пунктов в таблице никак не связана с
буквенными обозначениями на графе. Известно, что длина кратчайшего пути из пункта А в
пункт Ж не больше 15. Определите, какова длина кратчайшего пути из пункта Д в пункт В. 
В ответе запишите целое число – так, как оно указано в таблице.

![Задание 2](problems/problem1/task2.png)

Ответ: 19

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example2.py)

### Пример 3


Р-10 (демо-2021). На рисунке справа схема дорог Н-ского района изображена в виде
графа, в таблице содержатся сведения о длинах этих дорог (в километрах).
Так как таблицу и схему рисовали независимо друг от друга, то нумерация населённых
пунктов в таблице никак не связана с буквенными обозначениями на графе. Определите,
какова протяжённость дороги из пункта Г в пункт Ж. В ответе запишите целое число –
так, как оно указано в таблице.


![Задание 3](problems/problem1/task3.png)

Ответ: 9

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example3.py)


### Пример 4

На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице содержатся 
сведения о длинах этих дорог (в километрах). Так как таблицу и схему рисовали независимо 
друг от друга, то нумерация населённых пунктов в таблице никак не связана с буквенными 
обозначениями на графе. Определите, какова длина дороги из пункта В в пункт Е. 
В ответе запишите целое число – так, как оно указано в таблице.

![Задание 4](problems/problem1/task4.png)

Ответ: 20

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example4.py)


### Пример 5

На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице содержатся
сведения о длинах этих дорог (в километрах). Так как таблицу и схему рисовали независимо друг
от друга, то нумерация населённых пунктов в таблице никак не связана с буквенными
обозначениями на графе. Определите, какова длина дороги из пункта А в пункт Д. В ответе
запишите целое число – так, как оно указано в таблице.

![Задание 5](problems/problem1/task5.png)

Ответ: 46

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example5.py)


### Пример 6

Между населёнными пунктами A, B, C, D, E, F построены дороги, протяжённость которых приведена
в таблице. (Отсутствие числа в таблице означает, что прямой дороги между пунктами нет.)
Определите длину кратчайшего пути между пунктами A и F, проходящего через пункт E и не 
проходящего через пункт B. Передвигаться можно только по указанным дорогам.


![Задание 6](problems/problem1/task6.png)

Ответ: 17

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example6.py)


### Пример 7

Между населёнными пунктами A, B, C, D, E, F, Z построены дороги с односторонним движением. 
В таблице указана протяжённость каждой дороги. Отсутствие числа в таблице означает, 
что прямой дороги между пунктами нет. Например, из A в B есть дорога длиной 4 км, а из
B в A дороги нет.

Сколько существует таких маршрутов из A в Z, которые проходят через 6 и более населен-ных
пунктов? Пункты A и Z при подсчете учитывать. Два раза проходить через один пункт нельзя.


![Задание 7](problems/problem1/task7.png)

Ответ: 6

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example7.py)


### Пример 8

Р-04. Между населёнными пунктами A, B, C, D, E, F, G построены дороги, протяжённость 
которых приведена в таблице. (Отсутствие числа в таблице означает, что прямой дороги между
пунктами нет.)

Определите длину кратчайшего пути между пунктами A и G (при условии, что
передвигаться можно только по построенным дорогам).


![Задание 8](problems/problem1/task8.png)

Ответ: 23

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example8.py)


### Пример 9

Р-03. Между населёнными пунктами A, B, C, D, E, F построены дороги, протяжённость которых
приведена в таблице. (Отсутствие числа в таблице означает, что прямой дороги между
пунктами нет.)

Определите длину кратчайшего пути между пунктами A и F (при условии, что передвигаться 
можно только по построенным дорогам).



![Задание 9](problems/problem1/task9.png)

Ответ: 9

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem1/example9.py)


[Задания для самостоятельного выполнения](problems/problem1/exercises.pdf)



## Задание 2

### Пример 1

Логическая функция F задаётся выражением

![Задание 2](problems/problem2/task1.png)

На рисунке
приведён фрагмент таблицы истинности функции F, содержащий все наборы аргументов,
при которых функция F ложна. Определите, какому столбцу таблицы истинности функции
F соответствует каждая из переменных x, y, z, w.

В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им
столбцы. Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.

<table>
    <tbody>
    <tr>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>F</td>
    </tr>
    <tr>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
    </tr>
    </tbody>
</table>

**Ответ:** x y z w

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem2/example1.py)

### Пример 2


Логическая функция F задаётся выражением

![Задание 2](problems/problem2/task2.png)

На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий
неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F соответствует
каждая из переменных x, y, z, w.

<table>
    <tbody>
    <tr>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>F</td>
    </tr>
    <tr>
        <td>1</td>
        <td></td>
        <td>1</td>
        <td></td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td></td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td></td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
    </tr>
    </tbody>
</table>

В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы.
Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.

**Ответ:** z y x w

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem2/example2.py)

### Пример 3


Логическая функция F задаётся выражением

![Задание 3](problems/problem2/task3.png)

На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий
неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F соответствует
каждая из переменных x, y, z, w.

<table>
    <tbody>
    <tr>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>F</td>
    </tr>
    <tr>
        <td></td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td></td>
        <td></td>
        <td>1</td>
        <td>1</td>
    </tr>
    </tbody>
</table>

В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы.
Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.

**Ответ:** z y w x

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem2/example3.py)

### Пример 4


Логическая функция F задаётся выражением

![Задание 4](problems/problem2/task4.png)

На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий
неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F соответствует
каждая из переменных x, y, z, w.

<table>
    <tbody>
    <tr>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>F</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td></td>
        <td>1</td>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td></td>
        <td>1</td>
    </tr>
    </tbody>
</table>

В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы.
Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.


**Ответ:** x w z y

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem2/example4.py)

### Пример 5


Логическая функция F задаётся выражением

![Задание 5](problems/problem2/task5.png)

На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий
неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции F соответствует
каждая из переменных x, y, z, w.

<table>
    <tbody>
    <tr>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>?</td>
        <td>F</td>
    </tr>
    <tr>
        <td>1</td>
        <td></td>
        <td></td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>1</td>
        <td></td>
        <td>1</td>
        <td></td>
        <td>1</td>
    </tr>
    </tbody>
</table>

В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы.
Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.

**Ответ:** y x z w

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem2/example5.py)

[Задания для самостоятельного выполнения](problems/problem2/exercises.pdf)



## Задание 5

### Пример 1
Автомат обрабатывает натуральное число N по следующему алгоритму:
1. Строится двоичная запись числа N.
2. Удаляются первая слева единица и все следующие непосредственно за
   ней нули. Если после этого в числе не остаётся цифр, результат этого
   действия считается равным нулю.
3. Полученное число переводится в десятичную запись.
4. Новое число вычитается из исходного, полученная разность выводится на экран.


Пример: дано число N = 11. Алгоритм работает следующим образом:
1. Двоичная запись числа N: 1011.
2. Удаляется первая единица и следующий за ней ноль: 11.
3. Десятичное значение полученного числа 3.
4. На экран выводится число 11 – 3 = 8.

Сколько разных значений будет показано на экране автомата при последовательном вводе
всех натуральных чисел от 500 до 5000?

**Ответ: 256, 512, 1024, 2048, 4096**

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem5/example4.py)

### Пример 2

Учитель предлагает детям три цифры. Ученики должны сначала найти сумму
первой и второй цифр, потом – сумму второй и третьей цифр.
Затем полученные числа записываются друг за другом в порядке невозрастания
(правое число меньше или равно левому).

Пример. Исходные цифры: 6, 3, 9. Суммы: 6 + 3 = 9; 3 + 9 = 12.

Результат: 129.
Укажите, какая из следующих последовательностей символов может быть получена в результате.

1) 1915

2) 1815

3) 188

4) 1518

**Ответ: 2**

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem5/example5.py)

### Пример 3

Автомат получает на вход четырёхзначное натуральное число и строит новое число по следующему алгоритму:

1) вычисляются суммы первой и второй, второй и третьей и третьей и четвёртой цифр;

2) из полученных сумм отбрасывается наименьшая;

3) остальные записываются в порядке неубывания.

Пример: исходное число: $1284$. Суммы: 1 + 2 = 3; 2 + 8 = 10; 8 + 4 = 12. Отбрасывается
наименьшая сумма 3. Результат: 1012. Укажите наименьшее и наибольшее число, при вводе
которого автомат выдаёт значение 511.


**Ответ: максимальное число равно 9232, минимальное - 1056*

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem5/example6.py)

### Пример 4


Автомат получает на вход два двузначных шестнадцатеричных числа. В этих
числах все цифры не превосходят цифру 6 (если в числе есть цифра больше 6, автомат отказывается работать). По этим числам строится новое
шестнадцатеричное число по следующим правилам.
1. Вычисляются два шестнадцатеричных числа – сумма старших разрядов полученных чисел и сумма младших разрядов этих чисел.
2. Полученные два шестнадцатеричных числа записываются друг за другом в порядке возрастания (без разделителей).

Пример. Исходные числа: 66, 43. Поразрядные суммы: A, 9. Результат: 9A.

Определите, какое из следующих чисел может быть результатом работы автомата.

1) 9F

2) 911

3) 42

4) 7A

[Исходник](https://github.com/aoklyunin/ege-py/blob/master/problem5/example7.py)


[Задания для самостоятельного выполнения](problems/problem5/exercises.pdf)
