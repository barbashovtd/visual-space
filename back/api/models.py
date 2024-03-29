from django.db import models


class Appeal(models.Model):
    date_created = models.DateTimeField("Дата обращения", auto_now_add=True, editable=False)
    comment = models.TextField("Комментарий к обращению")
    date_updated = models.DateTimeField("Дата последнего обновления", auto_now=True, editable=False)
    phone = models.CharField("Телефон заказчика", max_length=15)  # я погуглил, максимальная длина номера 15 символов
    name = models.CharField("Имя заказчика", max_length=128, blank=False)
    notes = models.TextField("Заметки по заказу")

    def __str__(self):
        return f"{self.name} ({self.date_created})"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class MainPageContent(models.Model):
    title = models.CharField(max_length=64, blank=False, default="Web Studio \n helping startup's")
    suptitle = models.CharField(max_length=64, blank=False, default="Команда, понимающая ваши проблемы")
    box_tl = models.TextField(default="Молодая \n креативная \n студия")
    box_tr = models.TextField(
        default="Мы - участники программы ФСИ, понимаем ваши потребности и помогаем с их закрытием"
    )
    box_bl = models.TextField(default="Разрабатываем сайты, понимая ваши проблемы и решая их доступным способом")
    box_br = models.TextField(default="Развиваем вас и ваш бренд")
    advantages = models.CharField(max_length=32, default="Преимущества")
    adv_1_title = models.CharField(max_length=32, default="Индивидуальный подход")
    adv_2_title = models.CharField(max_length=32, default="Сэкономленное время")
    adv_3_title = models.CharField(max_length=32, default="Качество исполнения")
    adv_4_title = models.CharField(max_length=32, default="Технологичность")
    adv_1_text = models.TextField(
        default="Стремимся к тому, чтобы наше сотрудничество точно отражало ваши индивидуальные требования и предпочтения, обговариваемые в процессе онлайн встречи"
    )
    adv_2_text = models.TextField(
        default="Сотрудничество с нами позволяет заказчику сосредоточиться на своем бизнесе не тратя время на создание и поддержку веб-сайта"
    )
    adv_3_text = models.TextField(
        default="Предлагаем лучшее соотношение цены и качества. Создаем продукт, доступный для стартапов на разных этапах развития"
    )
    adv_4_text = models.TextField(
        default="Используем современные технологии для создания интерактивных и масштабируемых сайтов, сосредоточенных на адаптацию под ваши потребности"
    )
    services_title = models.CharField(max_length=16, default="Услуги")
    services_landing_title = models.CharField(max_length=20, default="Landing page")
    services_landing_suptitle = models.CharField(
        max_length=80, default="Сайт-визитка, который помогает компании рассказать о себе в одной странице"
    )
    services_landing_o1_title = models.CharField(max_length=20, default="О1. Брифинг")
    services_landing_o2_title = models.CharField(max_length=20, default="О2. Исследования")
    services_landing_o3_title = models.CharField(max_length=20, default="О3. Дизайн")
    services_landing_o4_title = models.CharField(max_length=20, default="О4. Разработка")
    services_landing_o1_text = models.TextField(
        default="Перед началом работы мы проводим с Вами брифинг, чтобы уточнить все нюансы и особенности проекта, не упустить важные детали. Это позволяет нам эффективно использовать время клиентов и сразу переходить к исследованиям."
    )
    services_landing_o2_text = models.TextField(
        default="Получив от Вас необходимую информацию по проекту, мы анализируем конкурентов, удобство пользования сайтом, качество дизайна и потребности Ваших клиентов, чтобы найти оптимальные решения."
    )
    services_landing_o3_text = models.TextField(
        default="на этом этапе мы разрабатываем функциональный прототип сайта, отображающий структуру контента и функционал. После утверждения этого прототипа, начинается работа над визуальным оформлением сайта, согласование с Вами его общего вида."
    )
    services_landing_o4_text = models.TextField(
        default="Наша команда разработчиков преобразует веб-дизайн и утвержденный функционал в интерактивный веб-сайт с применением передовых web-технологий, таких как Vue.js, Python с Django + REST API, контейнеризация с Docker. Наш подход сосредоточен на адаптации каждого элемента к Вашим уникальным потребностям, чтобы гарантировать высокое качество и уникальный пользовательский опыт."
    )
    services_landing_note_title = models.CharField(max_length=16, default="Примечание:")
    services_landing_note_text = models.CharField(
        max_length=100, default="Итоговые сроки могут быть значительно меньше, это обговаривается с клиентом"
    )
    services_business_title = models.CharField(max_length=32, default="Корпоративный сайт")
    services_business_suptitle = models.CharField(
        max_length=100, default="Многостраничный сайт для бизнеса, помогает рассказать о продукте"
    )
