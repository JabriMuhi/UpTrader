# UpTrader MenuApp

Пример реализации древовидного меню: 
- Меню 1
  - Меню 1.1
    - Меню 1.1.1
    - Меню 1.1.2
  - Меню 1.2
- Меню 2
  - Меню 2.1
    - Меню 2.1.1
      - Меню 2.1.1.1
      - Меню 2.1.1.2
    - Меню 2.1.2
  - Меню 2.2

Все пункты меню являются ссылками, при переходе по ссылке меню заголовком выводится название меню, на которое перешли (родитель) и его дети (подпункты меню).
Также реализовано добавление пунктов меню через админ панель Django, в параметрах есть возможность указать родителей. 

Я не стал редиректить стартовый url на url ../menu/, потому что мне кажется, что раз я писал приложение меню, то оно не должно быть основой сайта.
В таком случае, готовая ссылка для перехода в меню выглядит так: http://127.0.0.1:8000/menu/

Данные от админ панели Django:<br>
login: jabrimuhi <br>
pass: a6d3fdd4
