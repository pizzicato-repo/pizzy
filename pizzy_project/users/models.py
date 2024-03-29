from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.conf import settings

from .managers import UserManager

class User(AbstractBaseUser):
    email             = models.EmailField(max_length=255, unique=True, verbose_name='Adresse Email')
    username          = models.CharField(max_length=15, unique=True, verbose_name='Pseudo',)
    first_name        = models.CharField(max_length=30, verbose_name='Prénom')
    last_name         = models.CharField(max_length=50, verbose_name='Nom')
    
    is_active         = models.BooleanField(default=True, verbose_name='Utilisateur actif')
    is_staff          = models.BooleanField(default=False, verbose_name="Staff")
    is_admin          = models.BooleanField(default=False, verbose_name='Admin')
    date_joined       = models.DateTimeField(editable=False, default=timezone.now)
    first_connection  = models.BooleanField(default=True, verbose_name='Premiere connection')

    confirm           = models.BooleanField(default=False)
    confirmation_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "Pizzy Utilisateur"
        verbose_name_plural = "Pizzy Utilisateurs"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()
        
    def get_short_name(self):
        return self.first_name + '#'+ str( self.pk )
    
    def __str__(self):
        return 'User-> '+ self.email

    def has_perm(self, perm, obj=None):
        """ Does the user have a specific permission? """
        return True

    def has_module_perms(self, app_label):
        """ Does the user have permission to view the app 'app_label' """
        return True

class PrivateData(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, related_name='private_data')
    phone_number    = models.CharField(max_length=20)

    def __str__(self):
        return "Données Privées de : " + str(self.user) 

class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    # driver_license  = models.BooleanField(default=False, verbose_name="permis",
    #                                     choices=( (True, "Oui"), (False, "Non")) )
    # trainee         = models.BooleanField(default=False, verbose_name="statut",
    #                                     choices=( (True, "Stagiaire"),(False, "Employé") ))
    # car_owner       = models.BooleanField(default=False, verbose_name="Propriétaire d'un Véhicule",
    #                                     choices=( (True, "Oui"), (False, "Non")) )
    profile_image   = models.ImageField(blank=True, upload_to='avatars/', default='avatar_generique.jpg')
    # smoker          = models.BooleanField(default=False, verbose_name="Fumeur",
    #                                     choices=( (True, "Fumeur"), (False, 'Non Fumeur')))
    # talker          = models.BooleanField(default=False, verbose_name="Bavard",
    #                                     choices=( (True, "Bavard"), (False, 'Peu Bavard')))
    # music           = models.BooleanField(default=False, verbose_name="Musique",
    #                                     choices=( (True, "Oui"), (False, 'Non')))
    gender          = models.CharField(max_length=50, default='None',choices=(
                                        ('None', "Non communiqué"),
                                        ('Woman', "Femme"),
                                        ('Man', "Homme"),),)

    def __str__(self):
        return "Profile de : " + str(self.user)


def create_user_data(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        PrivateData.objects.create(user=instance)

post_save.connect(create_user_data, sender=settings.AUTH_USER_MODEL )
