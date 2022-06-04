# VkPostSenderBot

_Бот-рассылка новых постов в группе VK по беседам сообщества._

## Описание
Рассылает новые постые в указанной группе с помощью просмотра стены, отслеживания [VkBotEventType.WALL_POST_NEW](https://vk-api.readthedocs.io/en/latest/_modules/vk_api/bot_longpoll.html) и [longpoll.listen()](https://vk-api.readthedocs.io/en/latest/longpoll.html#vk_api.longpoll.VkLongPoll.listen). 
Для отправки поста используется метод [messages.send](https://dev.vk.com/method/messages.send) с полем attachment, значением которого является ссылка на новый пост.

## Работа с ботом
В файле _config_ необходимо указать следующие значения:
| Переменная | Значение |
| ------ | ------ |
| group_token | Токен группы из раздела "Работа с API". |
| login | Логин страницы пользователя.  |
| password | Пароль страницы пользователя. |
| group_id | ID группы (числовое). |
| chat_list | Список из ID бесед относительно сообщества. |
