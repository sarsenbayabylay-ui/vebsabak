from django.db import models


class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ("Төмен", "Төмен"),
        ("Орташа", "Орташа"),
        ("Жоғары", "Жоғары"),
    ]
    STATUS_CHOICES = [
        ("Жаңа", "Жаңа"),
        ("Жұмыста", "Жұмыста"),
        ("Жабылды", "Жабылды"),
    ]

    title = models.CharField(max_length=200, verbose_name="Тақырыбы")
    description = models.TextField(verbose_name="Сипаттамасы")
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="Орташа",
        verbose_name="Басымдығы",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Жаңа",
        verbose_name="Мәртебесі",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"