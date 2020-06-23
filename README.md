# Содержание  

* [Объект тестирования](#объект-тестирования)
* [Модель тестирования](#модель-тестирования)
  * [Алгоритм](#алгоритм)
  * [Данные](#данные)
  * [Группы пользовательских сценариев](#группы-пользовательски-сценариев)
    * [Исключение на этапе валидации входных данных](#исключение-на-этапе-валидации-входных-данных)
    * [Отказ на этапе проверки первичной платежеспособности](#отказ-на-этапе-проверки-первичной-платежеспособности)
    * [Отказ на этапе сравнения доступной и желаемой суммы займа](#отказ-на-этапе-сравнения-доступной-и-запрошенной-суммы-займа)
    * [Отказ на этапе проверки платежеспособности на основе годового платежа](#отказ-на-этапе-проверки-платежеспособности-на-основе-годового-платежа)
    * [Получение кредита](#получение-кредита)
* [Настройка окружения](#настройка-окружения)
* [Unit-тесты](#unit-тесты)
  * [Запуск](#запуск)

# Объект тестирования

Представляет из себя [метод](https://github.com/rbudorin/borrower-scoring/blob/master/borrower_scoring.py#L52) класса `BorrowerScoring`, реализующий алгоритм скоринга заемщика(возвращает сумму годового платежа или `None`, в случае, если сработало одно из условий по которым кредит не выдается). 

Аргументы функции, описанные в задании, передаются в [конструктор](https://github.com/rbudorin/borrower-scoring/blob/master/borrower_scoring.py#L18) класса:

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

# Модель тестирования

## Алгоритм

Согласно требованиям алгоритм оценки заемщика состоит из нескольких последовательных этапов:

* Валидация входных параметров
* Первичная оценка платежеспособности
* Определение доступной суммы займа
* Сравнение доступной и желаемой суммы займа
* Расчет базовой ставки
* Калькуляция годового платежа
* Оценка платежеспособности на основе годового платежа
* Возврат значения годового платежа

Каждый последующий этап базируется на результатах вычислений предыдущего или не выполняется в принципе, в случае, если заемщик на прошел по условиям скоринга.

## Данные

Значения аргументов функции могут напрямую или косвенно влиять как на факт отказа в получении кредита, так и на финальное значение годового платежа.

## Группы пользовательских сценариев

На основе описания алгоритма и данных можно сформировать следующие группы пользовательских сценарииев:

| ID | Описание группы сценариев |  
|------------------|---------------|
| 1 | Исключение на этапе валидации входных данных |
| 2 | Отказ на этапе проверки первичной платежеспособности |
| 3 | Отказ на этапе сравнения доступной и запрошенной суммы займа |
| 4 | Отказ на этапе проверки платежеспособности на основе годового платежа |
| 5 | Получение кредита |

### Исключение на этапе валидации входных данных

Пользовательские сценарии для проверки исключений:

| ID | Сценарий передачи невалидного значения аргумента |  
|------------------|---------------|
| [1.1](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L770) | Возраст |
| [1.2](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L857) | Пол |
| [1.3](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L895) | Источник дохода |
| [1.4](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L838) | Доход за последний год |
| [1.5](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L672) | Кредитный рейтинг |
| [1.6](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L799) | Запрошенная сумма |
| [1.7](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L731) | Срок погашения |
| [1.8](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L876) | Цель |

### Отказ на этапе проверки первичной платежеспособности

Возможные причины отказа в займе:

| ID | Сценарий |  
|------------------|---------------|
| [2.1](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L614) | Превышение пенсионного возраста на момент последнего платежа |
| [2.2](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L634) | Годовой платеж превышает треть дохода |
| [2.3](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L570) | Низкий кредитный рейтинг |
| [2.4](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L530) | Безработный |

### Отказ на этапе сравнения доступной и запрошенной суммы займа

На доступную для займа сумму влияют источник дохода и кредитный рейтинг:

| ID | Сценарий |  
|------------------|---------------|
| [3.1](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L312) | Зависимость запрошенной суммы и источника дохода |
| [3.2](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L388) | Зависимость запрошенной суммы и кредитного рейтинга |
| [3.3](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L476) | Выбор наименьшей суммы доступной для займа |

### Отказ на этапе проверки платежеспособности на основе годового платежа

После вычисления годового платежа проиходит проверка на то, что он не превышает половину дохода:

| ID | Сценарий |  
|------------------|---------------|
| [4.1](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L550) | Годовой платеж с процентами превышает половину дохода |

### Получение кредита

Сценарии успешного получения кредита исходя из аргументов(параметров заемщика):

| ID | Сценарий |  
|------------------|---------------|
| [5.1](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L116) | Изменение ставки в зависимости от суммы кредита |
| [5.2](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L72) | Изменение ставки в зависимости от кредитного рейтинга, цели и дохода |
| [5.3](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L172) | Изменение ставки в зависимости от цели займа |
| [5.4](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L216) | Возраст заемщика |
| [5.5](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L248) | Получение суммы от 0.1 до 10 млн включительно |
| [5.6](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L280) | Получение кредита на срок от 1 до 10 лет включительно |
| [5.7](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L356) | Получение суммы равной ограничению по источнику дохода |
| [5.8](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L444) | Получение суммы равной ограничению по кредитному рейтингу |
| [5.9](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L509) | Получение суммы равной минимальной из ограничений по кредитному рейтингу и источнику дохода |
| [5.10](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L654) | Получение суммы, годовой платеж по которой(без процентов) равен трети готового дохода |

# Настройка окружения

Для работы потребуются:

* Интерпретатор `Python` версии `3.8.2`
* Пакетный менеджер `pip`
* Зависимости из `pip-requirements.txt`

Клонируем репозиторий:
```bash
$ git clone git@github.com:rbudorin/borrower-scoring.git && cd borrower-scoring
```

Устанавливаем зависимости:
```bash
$ pip install -r pip-requirements.txt
```

# Unit-тесты

Расположены в каталоге `tests`, в файле `test_borrower_scoring.py`. Внутри [класс](https://github.com/rbudorin/borrower-scoring/blob/master/test/test_borrower_scoring.py#L7) с набором тестовых методов и входными параметрами для [объекта тестирования](#объект-тестирования). Каждый метод имеет комментарий с идентификатором пользовательского сценария, который он покрывает.

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
