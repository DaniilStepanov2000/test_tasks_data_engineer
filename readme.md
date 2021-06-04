# Решение домашнего задания на позицию Junior Data Engineer.

## Решение задания на Python.

### Развертывание проекта
1. Перейти в директорию ```/test_tasks```. 
2. Создать виртуальную среду. 
   ```
    python3 -m venv env_name
   ```
3. Активировать виртуальную среду, используя команду:<br>
   _Windows:_
   ``` 
   venv/Scripts/activate
   ```
   _Mac OS / Linux:_
   ``` 
   source mypython/bin/activate
   ```
4. Запустить файл _main.py_, используя команду:
```
python main.py <имя_файла> --em_sue_name=... --em_salary=...
```
Переменные: 
1. ```имя_файла``` - обязательная, __позиционная__ переменная, которая содержит имя файла.
2. ```--em_sue_name``` - не обязательная, __именованная__ переменная, которая содержит имя работника, которого надо добавить.<br>
3. ```--em_salary``` - не обязательная, __именованная__ переменная, которая содержит зарплату работника.

### Пример работы программы:
__Пример__: осуществим чтение файла и добавление в файл нового работника.<br><br>
__Шаг 1:__ Запускаем скрипт main.py, обязательно указывая имя файла. Так же дополнительно добавляем фамилию работника и его зарплату.<br><br>
![image](https://user-images.githubusercontent.com/73431786/120774001-81af9c00-c52a-11eb-9afc-6bf0af758a49.png) <br><br>
__Шаг 2:__ Получаем рассчитанные параметры.<br><br>
![image](https://user-images.githubusercontent.com/73431786/120774502-039fc500-c52b-11eb-93b1-607b8ad3c5a7.png) <br><br>

__Шаг 3:__ Осуществим простое чтение файла и расчет без добавления работника. <br><br>
![image](https://user-images.githubusercontent.com/73431786/120774853-5aa59a00-c52b-11eb-867a-67332e3739af.png) <br><br>

__Шаг 4:__ Получаем результат.<br><br>
![image](https://user-images.githubusercontent.com/73431786/120775012-8032a380-c52b-11eb-92aa-33179119c7f8.png) <br><br>
***
## Решение задания на SQL.
### Описание технической части
Задание выполнялось в СУБД PostgreSQL.<br><br>
Была создана таблица _employees:_ <br><br>
![VS4Z-xZcZQM](https://user-images.githubusercontent.com/73431786/120776597-1915ee80-c52d-11eb-9ba9-cc9335dfd010.jpg) <br><br>
Была создана таблица _actions:_ <br><br>
![ZmdEBApchoU](https://user-images.githubusercontent.com/73431786/120776797-42cf1580-c52d-11eb-9ae0-91731f2af760.jpg) <br>
Структура таблицы _employees:_ <br><br>
![image](https://user-images.githubusercontent.com/73431786/120777752-4adb8500-c52e-11eb-8f3f-7a7603015d99.png) <br><br>
Структура таблицы _actions:_ <br><br>
![image](https://user-images.githubusercontent.com/73431786/120777911-79596000-c52e-11eb-80c6-bd63cbc3c409.png) <br><br>
### Решение
1.1 Запрос, который выводит количество действий за определенный месяц (февраль 2020):<br><br>
![rPv3c5fbst0](https://user-images.githubusercontent.com/73431786/120778312-de14ba80-c52e-11eb-849d-34e94ddc6564.jpg) <br>
```SQL
SELECT COUNT(actions)
FROM actions
WHERE dt >= '2020-02-01 00:00:00'
AND dt < '2020-02-29 23:59:59'
;
```
1.2 Запрос, который выводит количество сотрудников, которые выполняли хоть какие-нибудь действия за указанный период: <br><br>
![vx3s2A_PNZg](https://user-images.githubusercontent.com/73431786/120779056-5aa79900-c52f-11eb-878d-9a5a0ceb24b8.jpg) <br>
```SQL
SELECT COUNT(distinct employee_id)
FROM actions
WHERE dt >= '2020-02-01 00:00:00'
AND dt < '2021-06-02 10:10:10'
;
```
2. Запрос, который выводит логины сотрудников, которые не выполняли никаких действий в феврале 2020: <br><br>
![first](https://user-images.githubusercontent.com/73431786/120779643-eb7e7480-c52f-11eb-9373-af3d38286b0d.jpg) <br>
```SQL
SELECT emp.login
FROM employees emp
LEFT JOIN (SELECT act.employee_id FROM actions act 
WHERE act.dt >= '2020-02-01 00:00:00'
AND act.dt < '2020-02-29 23:59:59') new_table ON new_table.employee_id = emp.id
WHERE new_table.employee_id is NULL
;
```   
3. Запрос, который выводит 5 сотрудников с наибольшим количеством действий за февраль 2020, а также кол-во их действий, отсортированных в порядке убывания: <br><br>
![rLky3h5QQjw](https://user-images.githubusercontent.com/73431786/120780348-b0c90c00-c530-11eb-9fef-da04b3071f0f.jpg) <br>
```SQL
SELECT emp.login, COUNT(emp.login)
FROM employees emp
INNER JOIN actions act ON act.employee_id = emp.id
WHERE act.dt >= '2020-02-01 00:00:00'
AND act.dt < '2020-02-29 23:59:59'
GROUP BY emp.login
ORDER BY COUNT(emp.login) DESC
LIMIT 5
;
```   
   

