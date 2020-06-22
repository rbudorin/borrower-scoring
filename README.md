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

Представляет из себя [метод](blob/master/borrower_scoring.py#L55) класса `BorrowerScoring`, реализующий алгоритм скоринга заемщика.

# Тесты

## Вводная

Тесты расположены в каталоге `tests`, в файле [tests/test_borrower_scoring.py](test_borrower_scoring.py). Внутри класс с набором тестовых методов и входными параметрами для [объекта тестирования](#объект-тестирования).

## Запуск

Осуществляется из корня каталога `borrower-scoring` командой:

```bash
$ pytest -v
```
