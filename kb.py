from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from bot import questions

# названия кнопок
button_main = '🏠 Главное меню'
button_back = 'Назад'
button_que = '✏️ Задать вопрос'
button_faq = '📝 Часто задаваемые вопросы'
button_again = '🔄 Задать вопрос снова'

# создание клавиатур
faq = VkKeyboard(inline=True)
faq1 = VkKeyboard(inline=True)
main = VkKeyboard(one_time=True)
again_main = VkKeyboard(one_time=True)
menu = VkKeyboard(one_time=True)
back = VkKeyboard(one_time=True)

# добавление инлайн кнопок 1 часть
faq.add_button(f'{questions[0]}', VkKeyboardColor.SECONDARY, {'question': 0})
faq.add_line()
faq.add_button(f'{questions[1]}', VkKeyboardColor.SECONDARY, {'question': 1})
faq.add_line()
faq.add_button(f'{questions[2]}', VkKeyboardColor.SECONDARY, {'question': 2})
faq.add_line()
faq.add_button(f'{questions[3]}', VkKeyboardColor.SECONDARY, {'question': 3})
faq.add_line()
faq.add_button(f'{questions[4]}', VkKeyboardColor.SECONDARY, {'question': 4})

# добавление инлайн кнопок 2 часть
faq1.add_button(f'{questions[5]}', VkKeyboardColor.SECONDARY, {'question': 5})
faq1.add_line()
faq1.add_button(f'{questions[6]}', VkKeyboardColor.SECONDARY, {'question': 6})
faq1.add_line()
faq1.add_button(f'{questions[7]}', VkKeyboardColor.SECONDARY, {'question': 7})
faq1.add_line()
faq1.add_button(f'{questions[8]}', VkKeyboardColor.SECONDARY, {'question': 8})

# добавление кнопок
main.add_button(button_main, VkKeyboardColor.SECONDARY)

again_main.add_button(button_again, VkKeyboardColor.SECONDARY)
again_main.add_line()
again_main.add_button(button_main, VkKeyboardColor.SECONDARY)

menu.add_button(button_que, VkKeyboardColor.SECONDARY)
menu.add_line()
menu.add_button(button_faq, VkKeyboardColor.SECONDARY)

back.add_button(button_back, VkKeyboardColor.NEGATIVE)
