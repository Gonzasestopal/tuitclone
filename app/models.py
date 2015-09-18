from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.conf import settings
# Create your models here.

class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL) #MyUser
	tweet = models.CharField(max_length=140)

	def __unicode__(self):
		return self.tweet

class MyUserManager(BaseUserManager):
    def _create_user(self, usuario, email, password, is_superuser, is_active, is_staff):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            usuario=usuario,
            email=self.normalize_email(email),
            password=password,
            is_active=is_active,
            is_superuser=is_superuser,
            is_staff=is_staff
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, usuario, email, password=None):
    	return self._create_user(usuario, email, password, False, True, False)

    def create_superuser(self, usuario, email, password):
        return self._create_user(usuario, email, password, True, True, True)

class MyUser(AbstractBaseUser):

    first_name = models.CharField(max_length=200, blank=True, help_text="The first name of the user.")
    last_name = models.CharField(max_length=200, blank=True, help_text="The last name of the user.")
    follow = models.ManyToManyField('self')
    usuario = models.CharField(max_length=40, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        help_text="The email and identifier of the user"
    )
    is_active = models.BooleanField(
        default=True, 
        help_text="Determines whether the user is active or not. ",
        verbose_name="Active"
    )
    is_staff = models.BooleanField(
    	default=True,
    	help_text="Designates where the user will have acces to the admin interface",
    	verbose_name='Staff Status')
    is_superuser = models.BooleanField(
        default=True, 
        help_text="CAUTION - enabling this gives the user full admin access and access to the entire database. Only for ArcCore admins.",
        verbose_name="Superuser"
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['email']


    def get_full_name(self):
        #If the full name is not specified, return email
        if self.first_name == "" and self.last_name == "":
            return self.email
        else:
            return self.first_name + " " + self.last_name
    get_full_name.short_description = 'Name'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True