##### Table of Contents  
* [Настройка окружения](#настройка-окружения)
* [Объект тестирования](#объект-тестирования)
* [Тесты](#тесты)
  * [Введение](#введение)
  * [Запуск](#запуск)

# Настройка окружения

Для работы потребуются:

* Интерпретатор `Python` версии `3.8.2`
* Зависимости из `pip-requirements.txt`

Устанавливаем пакетный менеджер `pip`:
```bash
$ sudo easy_install-3.8 install pip
```
Клонируем репозиторий:
```bash
$ git clone git@github.com:rbudorin/borrower-scoring.git && cd borrower-scoring
```
Устанавливаем зависимости:
```bash
$ pip3.8 install -r pip-requirements.txt
```
# Объект тестирования

Представляет из себя [метод](https://github.com/rbudorin/borrower-scoring/blob/master/borrower_scoring.py#L52) класса `BorrowerScoring`, реализующий алгоритм скоринга заемщика(возвращает сумму годового платежа или `None`, в случае, если сработало одно из условий по которым кредит не выдается). 

Аргументы функции, описанные в задании, передаются в [конструктор](https://github.com/rbudorin/borrower-scoring/blob/master/borrower_scoring.py#L18) класса.

Пример использования и сигнатура вызова конструктора:

```Python
import pytest
from enums import *
from exceptions import *
from borrower_scoring import BorrowerScoring

def main():
    borrower_scoring = BorrowerScoring(
        age=35,
        income_amount=10,
        loan_rating=LoanRating.HIGH,
        loan_amount=3,
        credit_term=10,
        sex=Sex.MALE,
        income_source=IncomeSource.EMPLOYEE,
        purpose=Purpose.MORTGAGE
    )

    result = borrower_scoring.score()
    
    if result is not None:
        print('Year payment is <%s>.' % '{:f}'.format(result))
    else:
        print('Sorry, not today...')

if __name__ == "__main__":
    main()
```

Следующие аргументы реализованы как `Enum`:

* [Кредитный рейтинг](https://github.com/rbudorin/borrower-scoring/blob/master/enums.py#L4)
* [Пол](https://github.com/rbudorin/borrower-scoring/blob/master/enums.py#L45)
* [Источник дохода](https://github.com/rbudorin/borrower-scoring/blob/master/enums.py#L29)
* [Цель](https://github.com/rbudorin/borrower-scoring/blob/master/enums.py#L21)

# Тесты

## Вводная

Тесты расположены в каталоге `tests`, в файле `test_borrower_scoring.py`. Внутри [класс](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L7) с набором тестовых методов и входными параметрами для [объекта тестирования](#объект-тестирования).

## Запуск

Осуществляется из корня каталога `borrower-scoring` командой:

```bash
$ pytest -v
```

Если необходимо сохранить отчет о результатах выполнения тестов, то это можно сделать вот так:

```bash
$ pytest -v --html=report.html --self-contained-html
```

Результаты будут доступны в формате HTML(файл `report.html` в корне проекта).
