from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bot import ID, Bot, vk_session, answers
from kb import faq, faq1, main, again_main, menu, back

# замена типа сообщения
new_message = VkBotEventType.MESSAGE_NEW

# подставление сессии
vk_session = vk_session

# подключение longpoll
longpoll = VkBotLongPoll(vk_session, ID)


# главная функция
def message_handler():
    for event in longpoll.listen():
        if event.type == new_message:
            message = event.obj
            id = message.from_id

            ''' Обработки callback запросов '''
            if message.payload == '{"command":"start"}':
                name = Bot.user_check(id)
                Bot.send_message(
                    id,
                    f'👋 Привет, {name}!'
                    '\nЯ — HR-бот аэропорта Шереметьево. Помогаю адаптироваться новым сотрудникам. '
                    'Начать пользоваться сервисом, перейди в Главное меню, нажав на кнопку',
                    main.get_keyboard()
                )

            elif message.payload == '{"question":0}':
                Bot.send_message(
                    id,
                    answers[0] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            elif message.payload == '{"question":1}':
                Bot.send_message(
                    id,
                    answers[1] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            elif message.payload == '{"question":2}':
                Bot.send_message(
                    id,
                    answers[2] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            elif message.payload == '{"question":3}':
                Bot.send_message(
                    id,
                    answers[3] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            elif message.payload == '{"question":4}':
                Bot.send_message(
                    id,
                    answers[4] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            elif message.payload == '{"question":5}':
                Bot.send_message(
                    id,
                    answers[5] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            elif message.payload == '{"question":6}':
                Bot.send_message(
                    id,
                    answers[6] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            elif message.payload == '{"question":7}':
                Bot.send_message(
                    id,
                    answers[7] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            elif message.payload == '{"question":8}':
                Bot.send_message(
                    id,
                    answers[8] + '\n\nМожешь еще раз задать вопрос или вернуться в Главное меню',
                    again_main.get_keyboard()
                )

            else:

                ''' Обработки text запросов '''
                if message.text.lower() == 'привет':
                    name = Bot.user_check(id)
                    Bot.send_message(
                        id,
                        f'👋 Привет, {name}!'
                        '\nЯ — HR-бот аэропорта Шереметьево. Помогаю адаптироваться новым сотрудникам. '
                        'Начать пользоваться сервисом, перейди в Главное меню, нажав на кнопку',
                        main.get_keyboard()
                    )

                elif message.text == '🏠 Главное меню':
                    Bot.send_message(
                        id,
                        'Ты в Главном меню, выбери что ты хочешь',
                        menu.get_keyboard()
                    )

                elif message.text == '✏️ Задать вопрос':
                    Bot.send_message(
                        id,
                        'Введи мне свой вопрос, хочешь вернуться назад, нажми на кнопку',
                        back.get_keyboard()
                    )

                elif message.text == '📝 Часто задаваемые вопросы':
                    Bot.send_message(
                        id,
                        'Чтобы получить ответ, выбери тему интересующей информации:',
                        faq.get_keyboard()
                    )
                    Bot.send_message(
                        id,
                        '&#12;',
                        faq1.get_keyboard()
                    )
                    Bot.send_message(
                        id,
                        'Хочешь вернуться назад, нажми на кнопку',
                        back.get_keyboard()
                    )

                elif message.text == 'Назад':
                    Bot.send_message(
                        id,
                        'Ты в Главном меню, выбери что ты хочешь',
                        menu.get_keyboard()
                    )

                elif message.text == '🔄 Задать вопрос снова':
                    Bot.send_message(
                        id,
                        'Ты в Главном меню, выбери что ты хочешь',
                        menu.get_keyboard()
                    )

                else:
                    Bot.send_message(
                        id,
                        'Я тебя не понимаю 🙃'
                    )


# запуск функции
if __name__ == '__main__':
    message_handler()
