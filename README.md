# Visual Space

(๑òᗜó) **Коммиты только в dev-ветку** o,..,o
---

## Back
В корне проекта бэкенда лежит файл *pyproject.toml*. Установка всего необходимого для разработки (в предварительно созданное виртуальное окружение, само собой) делается простым
```sh
pip install .[all]
```
В системе должен наличествовать [Hatch](https://hatch.pypa.io/latest/). Рекомендую ставить через [pipx](https://pipx.pypa.io/stable/)
```sh
pipx install --include-deps hatch
```
Вообще, всячески pipx рекомендую -- избавляет от кучи проблем с изоляцией нужных инструментов.
Сайд-эффект такого подхода -- бессмысленная (в нашем случае) установка самого проекта как приложения в venv, но это ни на что не влияет.
В *pyproject'е* же -- настройки основных нужных инструментов. Они должны подхватываться IDE автоматически (в VSCode проверено).
Почитайте про pyproject, ну:
* [What is pyproject.toml file for?](https://stackoverflow.com/a/66472800)
* [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/#pyproject-toml)
* [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-your-pyproject-toml)
Также есть рабочее окружение (.code-workspace) для VSCode, рекомендуется установить рекомендуемые расширения ( ͡° ͜ʖ ͡°).
Кто устанет от бесконечных python manage.py -- попробуйте [just](https://github.com/casey/just). К проекту также приложен, базовый функционал в виде маграций и запуска в наличии.
