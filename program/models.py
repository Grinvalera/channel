from django.db import models


Category = [
    ('Новини', 'Новини'),
    ('Серіали', 'Серіали'),
    ('Фільми', 'Фільми'),
    ('Мультфільми', 'Мультфільмы'),
    ('Телешоу', 'Телешоу'),
    ('Нічная музика', 'Нічная музика')
]

Week = [
    ('Monday', 'Понедельник'),
    ('Tuesday', 'Вторник'),
    ('Wednesday', 'Среда'),
    ('Thursday', 'Четверг'),
    ('Friday', 'Пятница'),
    ('Saturday', 'Суббота'),
    ('Sunday', 'Воскресенье')
]


class Channel(models.Model):

    program_type = models.CharField(max_length=128,
                                    choices=Category,
                                    verbose_name='Тип программы',
                                    blank=False
                                    )
    name_program = models.CharField(max_length=256,
                                    verbose_name='Имя телепрограммы',
                                    blank=False
                                    )
    time_program = models.CharField(max_length=128,
                                    verbose_name='Время программы',
                                    blank=False
                                    )
    day_program = models.CharField(max_length=256,
                                   choices=Week,
                                   verbose_name='Дни недели',
                                   blank=False
                                   )

    class Meta:
        verbose_name = 'Телеканал'

    def __str__(self):
        return "{} - '{}' - '{}'".format(self.day_program, self.name_program, self.time_program)
