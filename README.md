# Построение распределенных систем и облачные вычисления

### Achievement 2

Выполнила Екатерина Еременко, МИВ231.

1. Диаграмма компонентов расположена в директории UML (`diag_comp.png`)
1. Диаграмма последовательностей расположена в директории UML (`diag_seq.png`)
2. Для запуска демо:
```bash
pip install -r requirements.txt
python local_start.py
```
Лог-файл: `app.log`.

#### Требования:
Python 3.8 и выше.

#### Инициализация базы данных
```bash
flask db init
flask db upgrade
```

#### Примеры тестирования

```bash
# Ошибка: такое число уже есть
curl --location '127.0.0.1:5000/api/send-number' \                                                                                                                           ✔ 
--header 'Content-Type: application/json' \
--data '{
        "value": "4"
}'
{
  "error": "Number 4 already processed"
}

# Ошибка: есть число на 1 больше
curl --location '127.0.0.1:5000/api/send-number' \                                                                                                                           ✔ 
--header 'Content-Type: application/json' \
--data '{
        "value": "3"
}'
{
  "error": "Number 3 number is one less than the processed one"
}

# Успешная отправка
curl --location '127.0.0.1:5000/api/send-number' \                                                                                                                           ✔ 
--header 'Content-Type: application/json' \
--data '{
        "value": "0"
}'
{
  "1"
}
```

