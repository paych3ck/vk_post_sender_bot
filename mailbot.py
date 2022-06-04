import vk_api
import time
import requests

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import group_token, phone_number, password, chat_list, group_id


def handler_function():
    code = input("Код: ")
    auth = True
    return code, auth

vk = vk_api.VkApi(token=group_token)
longpoll = VkBotLongPoll(vk, group_id)

vk_session = vk_api.VkApi(phone_number, password, auth_handler=handler_function)
vk_session.auth()
vk_phone = vk_session.get_api()

print("Авторизация пройдена.")

try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.WALL_POST_NEW:
            new_post = vk_phone.wall.get(owner_id=-group_id, count=1)
            new_post_id = new_post["items"][0].get("id")
            attachment_formed = f"wall-{str(group_id}_{str(new_post_id)}"

            for chat_id in chat_list:
                vk.method("messages.send", {"chat_id": chat_id, "attachment": attachment_formed, "random_id": 0})

except requests.exceptions.ReadTimeout:
    time.sleep(5)
