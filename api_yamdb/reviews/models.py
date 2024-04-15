from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

User = get_user_model()
MX_CHARS = 256


class Category(models.Model):
    name = models.CharField(
        max_length=MX_CHARS,
        verbose_name='Название',
        unique=True,
        blank=False
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=False,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы '
                  'латиницы, цифры, дефис и подчёркивание.',
        validators=[
            RegexValidator(
                regex=r'^[-a-zA-Z0-9_]+$',
                message='Идентификатор страницы должен содержать только '
                        'латинские символы, цифры, дефис и подчёркивание.',
                code='invalid_slug'
            )
        ]
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=MX_CHARS,
        verbose_name='Название',
        unique=True,
        blank=False
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=False,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы '
                  'латиницы, цифры, дефис и подчёркивание.',
        validators=[
            RegexValidator(
                regex=r'^[-a-zA-Z0-9_]+$',
                message='Идентификатор страницы должен содержать только '
                        'латинские символы, цифры, дефис и подчёркивание.',
                code='invalid_slug'
            )
        ]
    )

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=MX_CHARS,
        verbose_name='Название',
        blank=False
    )
    year = models.IntegerField(
        verbose_name='Год выхода',
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    genre = models.ManyToManyField(
        Genre,
        on_delete=models.SET_NULL,
        blank=False,
        verbose_name='Жанр',
        related_name='titles'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=False,
        verbose_name='Категория',
        related_name='titles'
    )

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='ID_Произведения'
    )
    text = models.TextField(
        verbose_name='Текст обзора',
        blank=False
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='reviews'
    )
    score = models.IntegerField(
        verbose_name='Оценка'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'обзор'
        verbose_name_plural = 'Обзоры'

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='commentaries',
        verbose_name='ID_Комментария'
    )
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Создан')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор',
                               related_name='commentaries')

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text