from django.db import models

# Create your models here.
class EventModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва події')
    description = models.TextField(verbose_name='Опис події')
    date = models.DateField(verbose_name='Дата події')
    start_time = models.TimeField(verbose_name='Час початку')
    end_time = models.TimeField(verbose_name='Час закінчення')
    location = models.CharField(max_length=200, verbose_name='Місце проведення')
    people_count = models.PositiveIntegerField(verbose_name='Кількість людей')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def __str__(self):
        return f"{self.title} - {self.date} - {self.start_time} to {self.end_time}"
    
    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'Події'
        ordering = ['-created_at']
    
    
class TicketModel(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE, related_name='tickets', verbose_name='Подія')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна квитка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def __str__(self):
        return f"{self.event.title} - {self.price}"
    
    class Meta:
        verbose_name = 'Квиток'
        verbose_name_plural = 'Квитки'
        ordering = ['-created_at']
    

class BookingModel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В процесі'),
        ('confirmed', 'Підтверджено'),
        ('done', 'Виконано'),
        ('cancelled', 'Скасовано'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус бронювання')

    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE, related_name='bookings', verbose_name='Квиток')
    user_first_name = models.CharField(max_length=100, verbose_name='Ім\'я користувача')
    user_last_name = models.CharField(max_length=100, verbose_name='Прізвище користувача')
    user_email = models.EmailField(verbose_name='Електронна пошта користувача')
    quantity = models.PositiveIntegerField(verbose_name='Кількість заброньованих квитків')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name} - {self.ticket.event.title} - {self.quantity}"
    

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ['-created_at']