from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Student
#admin.site.register(Choice)
#admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently','question_rate')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None,               {'fields': ['question_rate']}),
    ]
    #inlines = [ChoiceInline]
    list_per_page = 15
    list_filter = ['pub_date']
    search_fields = ['question_text']
    show_full_result_count = False 
    # 增加自定义按钮
    actions = ['custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '当天题目详情'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'primary'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错
    # 设置成链接类型的按钮后，custom_button方法将不会执行。

    custom_button.action_type = 1
    custom_button.action_url = 'http://121.40.138.226:8000/polls/student/'


admin.site.site_title = "开课吧信息管理系统"
admin.site.site_header = "开课吧信息管理系统"
admin.site.index_title = "开课吧信息管理系统"


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Student)

