import vk_api

from vk_api.utils import get_random_id


FAQ_list = {
	"Парковочные места": "Для получения карты на парковку необходимо:\n"
	"• Обратиться лично с пропуском и документами на автомобиль.\n\n"
	"• Оформление парковочной карты осуществляется в отделе по работе с парковочными картами:\n"
	"1) Здание Администрации парковки P17 «Лобненское шоссе»\n"
	"2) Здание Многоуровневого паркинга Терминала D при выезде из паркинга.\n\n"
	"Время работы отделов:\n"
	"Понедельник – четверг 08:00 - 17:00, пятница 08:00 - 15:45. Суббота, воскресенье - выходной.\n"
	"Дополнительную информацию можно уточнить по телефону: +7(800)707-96-72 (доб.5) круглосуточно.\n\n"
	"У меня есть ещё информация по данному вопросу, чтобы получить её, нажми «Ещё»",
	"Телефоны срочных служб": "Сменный начальник аэропорта:\n"
	"+7(495)578-45-41; +7(925)500-65-21\n\n"
	"Сменный начальник транспортной безопасности:\n"
	"+7(495)578-74-52; +7(925)500-41-25\n\n"
	"Дежурный ЛУ МВД в аэропорту:\n"
	"+7(795)578-27-21; +7(495)578-14-25\n\n"
	"Дежурный ФСБ в аэропорту:\n"
	"+7(495)578-23-14",
	"Скидки для сотрудников в аэропорту": "<b>Рестораны</b>: Coffeeshop Company, Заведения компании «Аэропит-Сервис», "
	"Пельмени&Pelmeni, Кафе-Бар «Урожай», Кафе «Шоколадница»\n\n"
	"<b>Магазины</b>: Imperial Dudy Free, Магазин «Глобус Гурме Экспресс», Минимаркет «Мандарин»\n\n"
	"<b>Услуги</b>: City Business School, Wall Street English",
	"Узнать о наставнике и связаться с ним": "Максимов Максим Максимович, mm.maximov@svo.aero, +7(999)999-99-99",
	"Маршруты корпоративного транспорта": "Для того, чтобы пользоваться корпоративный транспортом, "
	"необходимо приобрести месячный абонемент и всегда иметь с собой пропуск.\n\n"
	"Нажми на кнопку «Ещё», чтобы увидеть расписание движения корпоративного транспорта",
	"Прохождение обучения по охране труда": "Семинар по охране труда проводится каждый вторник и четверг в 9:15 в "
	"здании «Трансаэро», каб. 319. Семинар проводит ведущий специалист по охране труда – Чучвара Александр Игоревич, "
	"контактный номер: +7(926)244-63-59. С собой необходимо иметь паспорт или пропуск.",
	"Важные события на испытательном сроке": "Можете сами придумать какое-то событие, например ежедневная утренняя "
	"планерка работников, для демонстрации этой функции.",
	"Оформить пропуск на территорию аэропорта": "Шаг 1. Заполнить заявку на пропуск и заявку СКУД\n\n"
	"Шаг 2. Подписать данные заявки у непосредственного руководителя\n\n"
	"Шаг 3. С подписанными заявлениями, оригиналом паспорта, а также с 3 копии всех документов необходимо "
	"прийти в здание КИВЦ, эт. 2, каб. 17.\n\n"
	"Шаг 4. Отслеживать статус заявки на пропуск, по готовности прийти в КИВЦ за готовым пропуском.",
	"Получение карты медицинского страхования": "Для получения полиса ДМС необходимо обратиться в Поликлинику "
	"аэропорта, к. 316. Выдача производится - с понедельника по четверг с 8 до 16 часов, в пятницу с 8 до 14 часов."
}

# извлекаем вопросы
questions = ('$'.join(FAQ_list.keys())).split('$')

# извлекаем ответы
answers = ('$'.join(FAQ_list.values())).split('$')

# token group
TOKEN = ''

# подключение к vk
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

# id group
ID = int


# обработка отправлений
class Bot():

	def user_check(id: int) -> str:
		name = vk.users.get(user_ids=id)[0]['first_name']
		return name

	def send_message(id: int, message: str, keyboard=None) -> None:
		vk.messages.send(user_id=id, message=message, random_id=get_random_id(), keyboard=keyboard)
