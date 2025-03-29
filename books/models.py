from django.db import models
# from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    data_create = models.DateField(auto_now= True)
    url = models.TextField(default="/")
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    data_create = models.DateField(auto_now= True)
    url = models.TextField(default="/")
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255, null=False)
    # title_page = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="books", null=True)
    # url_base = ''
    # image = ''
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name="books", blank=False, null= False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books", null=False, blank=False)
    inventory = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # class Meta:
        # db_table = 'Publication'
        # verbose_name = _("کتاب")
        # verbose_name_plural = _("کتاب ها")
    

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


