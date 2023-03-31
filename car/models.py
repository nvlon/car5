from django.db import models

class Car(models.Model):
    CAR_TYPE = (
        ('Для  молодых парней', ' Для молодых парней'),
        ('Для мужчин', 'Для мужчин'),
        ('Для молодых девушек','Для молодых девушек '),
        ('Для женщин', 'Для женщин'),
        ('Для богатых', 'Для богатых')

    )
    title = models.CharField('Название автомобиля', max_length=100)
    description = models.TextField('Обзор на машину')
    image = models.ImageField(upload_to='')
    car_type =models.CharField(max_length=100, choices=CAR_TYPE,null=True)
    created_date = models.DateTimeField()
    cost = models.PositiveIntegerField()
    video = models.URLField()
    type_of_fuel = models.CharField(max_length=100, null=True)
    steering_wheel = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100,null=True)
    transmission_box = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class CommentCar(models.Model):
    RATING=(
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )
    car_choice_comment = models.ForeignKey(Car, on_delete=models.CASCADE,
                                           related_name="comment_object")
    text = models.TextField(null=True)
    rate_stars = models.CharField(max_length=100, choices=RATING, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rate_stars




