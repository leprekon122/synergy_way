from django.db import models

# Create your models here.

"""model for group page"""


class CreatedGroup(models.Model):
    group = models.CharField(max_length=25)

    def __str__(self):
        return self.group

    def get_absolute_url(self):
        return f"/Second_page"

    class Meta:
        verbose_name = 'CreatedGroup'
        verbose_name_plural = "CreatedGroup's"


"""model for user page"""


class CreatedUsers(models.Model):
    username = models.CharField(max_length=55)
    created_date = models.DateField(auto_now_add=True)
    groups = models.ForeignKey(CreatedGroup, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.username}, {self.created_date}"

    def get_absolute_url(self):
        return f"/"

    class Meta:
        verbose_name = "CreatedUsers"
        verbose_name_plural = "CreatedUsers"
