from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag




class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Не указаны теги')

        self.count_is_main_tag = 0

        for form in self.forms:
            if self.count_is_main_tag > 0 and form.cleaned_data.get('is_main'):
                raise ValidationError('Главный может быть только один тег')
            else:
                if form.cleaned_data.get('is_main'):
                    self.count_is_main_tag += 1
                else:
                    continue

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'text',]
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
