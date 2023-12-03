# DebugApi
Цель: Алгоритм устйочивый к отказам api по самым разным причинам, т.е. максимально эффективный. 

Дано: Сервис по торговле товарами (носки, туфли, одежда) - по факту любой API
Есть сервисы, которые развернули своё API, куда можно "постучаться", забрать список товаров (его характеристики: носки белые, сериые; туфли: черные, замшевые и т.д.) + например цена за 1 позицию.
на нормальных таких API, если все спроектировано отлично то по сути ты делаешь запрос к ним - тебе возвращается ОДНА строка json со списком всего и всех

Проблематика:
Но есть сервисы с ограничениями а самое главное не описанными ограничениями или по просту не продуманными, например:
*если делают API то иногда получается так, что можно забрать данные только по 1 позиции. Т.Е, 1 позиция = 1 запрос к API
*если еще сделали ограничения на запросы. За 1 раз можно использовать 10 запросов. А ТАК ЖЕ если ты авторизован и посылаешь запросы больше 60 минут, то юзера автоматический отрубает от сесии
Есть некий идентификатор сессии (дается при правильном указании логина и пароля от сайта), для задачи можно этот идентификатор генерировать в виде GUID. Нужно загрузить некую выборку позиций товаров с условного сервера (res_api.txt)

Условия: 100 едениц товара, 10 секунд время на один сгенерированный ключь, 2 секунды перерыва между запросами, каждый из 100 элементов записанный последовательно и является уникальным.

