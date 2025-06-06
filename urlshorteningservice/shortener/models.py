from django.db import models
import secrets
import string

# Create your models here.
class URL(models.Model):
    url = models.URLField()
    shortCode = models.CharField(unique=True, max_length=12, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    accessCount = models.IntegerField(default=0)
    # expiration_date =
    # user_assocaition = 
    def __str__(self):
        return self.shortCode
    

    def generate_shortcode(self):
        alphabet = string.ascii_letters + string.digits
        length = self._meta.get_field('shortCode').max_length
        while True:
            code = ''.join(secrets.choice(alphabet) for _ in range(length))
            if not URL.objects.filter(shortCode=code).exists():
                return code
    
    def save(self, *args, **kwargs):
        if not self.shortCode:
            self.shortCode = self.generate_shortcode()
        super().save(*args, **kwargs)


        