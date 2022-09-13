from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Choice, Question, Student, Task 
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pathlib import Path
from datetime import date, datetime
import mysql.connector
import json
from django.template import loader
from django.template.loader import render_to_string
import pymysql
import ast
from django.forms import model_to_dict
import decimal
from decimal import Decimal, getcontext
import time
import polls.Conn as Conn
#import visualization2
# Create your views here.
# 数据库部分
#mycursor = 0;
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj,decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class DecimalEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,decimal.Decimal):
            return float(o)
        super(DecimalEncoder,self).default(o)

#def content_mysql():
#     mydb = mysql.connector.connect(
#     host="xue.kaikeba.com",       # 数据库主机地址
#     user="lys",    # 数据库用户名
#     passwd="wLQ2uFbMiZEeh7qS",   # 数据库密码
##     database="suanke"
#    )
    #mydb = mysql.connector.connect(
    #host="121.40.138.226",       # 数据库主机地址
    #user="root",    # 数据库用户名
    #passwd="root",   # 数据库密码
    #database="database2"
    #)

#    mycursor = mydb.cursor()
#    return mycursor



def get_information(sql, foo):

#    foo = Conn.Conn()
    mycursor = foo.conn.cursor()
    mycursor.execute(sql)
    fields = mycursor.description
    result = mycursor.fetchall()
    column_list=[]
    jsondata = []
    for i in fields:
        column_list.append(i[0])
    for row in result:
        data = {}
        for i in range(len(column_list)):
            data[column_list[i]] = row[i]
            
        jsondata.append(json.dumps(data, cls=ComplexEncoder, ensure_ascii=False))
    value = jsondata
    i = 0
    for question in value:
        question = json.loads(question)
        value[i] = question
        i = i + 1;
    return value

def get_information1(sql):
    mydb = mysql.connector.connect(
        host="xue.kaikeba.com",       # 数据库主机地址
        user="lys",    # 数据库用户名
        passwd="wLQ2uFbMiZEeh7qS",   # 数据库密码
        database="suanke"
    )
    #mydb = mysql.connector.connect(
    #host="121.40.138.226",       # 数据库主机地址
    #user="root",    # 数据库用户名
    #passwd="root",   # 数据库密码
    #database="database2"
    #)

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    fields = mycursor.description
    result = mycursor.fetchall()
    column_list=[]
    jsondata = []
    for i in fields:
        column_list.append(i[0])
    for row in result:
        data = {}
        for i in range(len(column_list)):
            data[column_list[i]] = row[i]
            
        jsondata.append(json.dumps(data, cls=ComplexEncoder, ensure_ascii=False))
    value = jsondata
    i = 0
    for question in value:
        question = json.loads(question)
        value[i] = question
        i = i + 1;
    return value


def detail3(question_id, mycursor):
#    print("question_id")
#    print(question_id)
    sql = "select content, choice_analysis, true_answer  FROM suanke_choice_questions WHERE id =" + str(question_id)
#    t1 = time.time()
    question_list = get_information(sql, mycursor)
#    t2 = time.time()
#    print("time = ",t2 - t1)
    question03 = []
    for question0 in question_list:
        question03 = question0
    sql2 = "select count(*) FROM suanke_choice_question_user_answer_data where  is_true_answer = 1 and choice_question_id = " + str(question_id)
    question1_list = get_information(sql2, mycursor)
    question3 = []
    for question2 in question1_list:
        question3 = question2 
    sql3 = "SELECT count(*) FROM suanke_choice_question_user_answer_data where  is_true_answer = 0 and choice_question_id = " + str(question_id)
    question3_list = get_information(sql3, mycursor)
    question5 = []
    for question4 in question3_list:
        question5 = question4
    

    sql4 = "select choice_question_id,choice_option, choice_content from suanke_choice_question_options where choice_question_id = " + str(question_id)

    question4_list = get_information(sql4, mycursor)
    question6 = []
    for question7 in question4_list:
        question6 = question7
    question = []
    for question1 in question_list:
        question = question1
    
    sqla1 = "SELECT count(*) FROM suanke_choice_question_submit_detail_log WHERE submit_context = 'A' and choice_question_id =" + str(question_id)
    questiona_list = get_information(sqla1, mycursor)
    questiona = []
    for questiona1 in questiona_list:
        questiona = questiona1
    question["questiona"] = questiona["count(*)"]
    sqlb1 = "SELECT count(*) FROM suanke_choice_question_submit_detail_log WHERE submit_context = 'B' and choice_question_id =" + str(question_id) 
    questionb_list = get_information(sqlb1, mycursor)
    questionb = []
    for questionb1 in questionb_list:
        questionb = questionb1
    question["questionb"] = questionb["count(*)"]
    sqlc1 = "SELECT count(*) FROM suanke_choice_question_submit_detail_log WHERE submit_context = 'C' and choice_question_id =" + str(question_id)
    questionc_list = get_information(sqlc1, mycursor)
    questionc = []
    for questionc1 in questionc_list:
        questionc = questionc1
    question["questionc"] = questionc["count(*)"]
    sqld1 = "SELECT count(*) FROM suanke_choice_question_submit_detail_log WHERE submit_context = 'D' and choice_question_id =" + str(question_id)
    questiond_list = get_information(sqld1, mycursor)
    questiond = []
    for questiond1 in questiond_list:
        questiond = questiond1
    question["questiond"] = questiond["count(*)"]

    question["is_true_answer"] = question3["count(*)"]
    question["is_false_answer"] = question5["count(*)"]
    question["choice_option_content"] = question4_list
    question["true_answer"] = question03["true_answer"]
#    print("questiona\n",question["questiona"]);
#    print("questionb\n", question["questionb"]);
#    print("questionc\n", question["questionc"]);
#    print("questiond\n", question["questiond"]);

#    print("这里 ~true_answer/n", question["is_true_answer"]);
    #detail_sql2_pag3(question_id)
    sql_student_class = "SELECT * from (SELECT suanke_student_class.name,sum(is_true_answer),sum(is_true_answer)/count(is_true_answer), is_true_answer,count(is_true_answer),suanke_choice_question_user_answer_data.choice_question_id FROM suanke_student INNER JOIN suanke_student_student_class on suanke_student.id = suanke_student_student_class.student_id INNER JOIN suanke_student_class  on suanke_student_student_class.studentclass_id = suanke_student_class.id INNER JOIN suanke_choice_question_user_answer_data on suanke_student.user_id = suanke_choice_question_user_answer_data.user_id GROUP BY suanke_choice_question_user_answer_data.choice_question_id,suanke_student_class.name ORDER BY suanke_choice_question_user_answer_data.choice_question_id,(sum(is_true_answer)/count(is_true_answer)) DESC,sum(is_true_answer) DESC,suanke_student_class.name) AS A where A.choice_question_id =" + str(question_id)
    question_class_list = get_information(sql_student_class, mycursor)
    question_class = []
    question_answer_name  = []
    question_answer_rate = []
    question_answer_right = []
    question_answer_all = []
    i = 1
#    print("question_class_list")
#    print(question_class_list)
    for question_class1 in question_class_list:
        question_class  = question_class1
        #print("question_class")
        #print(question_class)
        if(i == 6):
            break
        #print("question_class[name]")
        #print(question_class['name'])
        question_answer_name.append(question_class['name'])
        question_answer_rate.append(question_class['sum(is_true_answer)/count(is_true_answer)'])
        question_answer_right.append(question_class['sum(is_true_answer)'])
        question_answer_all.append(question_class['count(is_true_answer)'] - question_class['sum(is_true_answer)'])
        i = i + 1
    question_answer_name.reverse()
    question_answer_rate.reverse()
    question_answer_right.reverse()
    question_answer_all.reverse()
    i = 1

#    print("就是这里\n");
    question["question_answer_name"] = question_answer_name
#    print("question_answer_name", question_answer_name)
    question["question_answer_rate"] = question_answer_rate
#    print("question_answer_rate", question_answer_rate)
    question["question_answer_right"] = question_answer_right
#    print("question_answer_right", question_answer_right)
    question["question_answer_all"] = question_answer_all
#    print("question_answer_all", question_answer_all)


    #print("question_answer")
    #print(question_class_list)
    #return render(request, 'polls/index.html', {'question': question})
    return question





def index(request):
    mycursor = Conn.Conn()
    #mycursor = foo.conn.cursor()

    sql = "select id, title, updated_at FROM suanke_choice_questions order by updated_at  desc"
    sql_last_quesiton = "SELECT * FROM suanke_choice_questions ORDER BY id DeSC LIMIT 1"
    sql_last_quesiton_value = get_information(sql_last_quesiton, mycursor)
    question_last = []
    for question_last1 in sql_last_quesiton_value:
        question_last = question_last1
#    print("question_last1", question_last)
    question_last_id = question_last['id']
    value = get_information(sql, mycursor)
    set1 = set()
    for question in value:
        question = str(question['updated_at']).split(" ")
        set1.add(question[0])
    list1 = list(set1)
    list1.sort(reverse=True)

    template = loader.get_template('polls/index.html')
    question_updated_content_list = {}
    
    name = request.POST.get('name', '')
    age = int(request.POST.get('age', '0'))
    question_id1 = int(request.POST.get('question_id', '1'))
#    print("question_id1--->", question_id1)
    if request.is_ajax():
        # 直接获取所有的post请求数据
        data = request.POST
#        print("data")
#        print(data)
        # 获取其中的某个键的值
        host = request.POST.get("name")
        if name != '': 
        #host1 = request.POST.gets("question_id")
        #print("host")
        #print(host)
        #print("host1")
        #print(host1)
        #if not name:
            sql_index = "select title,id from suanke_choice_questions where to_days(updated_at) = to_days('" + str(host) + " 00:00:00')"
            sql_index = get_information(sql_index, mycursor)
            question_updated_content_list[host] = sql_index
            data = question_updated_content_list[host],
            host = data
            response = JsonResponse({"name":host})
            return response
        else :
        # 将前端传来的数据再次传回前端，只是为了测试
            host1 = request.POST.get("question_id")
#            print('host1--->', host1)
        #if host1 is None:
            #detail(host1)
            question_id1 = detail3(host1, mycursor)
            #detail(host1)
#            print("question_id1-->", question_id1)
            response = JsonResponse({"detail2_question_all":detail3(host1, mycursor)})
            return response
            # return render(request, 'polls/index.html', {"quesiton":question_id1})
            # html = render_to_string('polls/temp.html', {'detail2_question_all': detail3(host1)})
            # return JsonResponse({"htm":html})

#    print("name age")
#    print(name)
#    print(age)
    detail2_question_all = detail3(question_last_id, mycursor)
    context = {
        'latest_question_list': value,
        'question_updated_list': list1,
        'first_quesiton': question_last,
        'detail2_question_all': detail2_question_all,
        'question_updated_content_list': question_updated_content_list,
    }
#    print("detail2_question_all-->", detail2_question_all)
    return HttpResponse(template.render(context, request))

def question_content(request, question):
    sql_index = "select title from suanke_choice_questions where to_days(updated_at) = to_days('" + str(question) + " 00:00:00');"
    sql_index = get_information(sql_index)
    question_updated_content_list[question] = sql_index
    context = {
        'question_updated_content_list': question_updated_content_list,
    }
    return render(template.render(content, request))

def detail_sql_pag3(question_id):
    sql_student_class = "SELECT distinct studentclass_id FROM suanke_student_student_class" #得到班级的id
    question_class_list = get_information(sql_student_class)
    question_answer = {}
    for question0 in question_class_list:
        sql_class_name = "select name from suanke_student_class where id =" + str(question0['studentclass_id']); 
        question_class_name_list = get_information(sql_class_name)#班级名字
        sql_right = "SELECT student_id  from suanke_student_student_class where studentclass_id =" + str(question0['studentclass_id'])
        question_right_list = get_information(sql_right)#每个班级的人数
        question_id_to_user_id = []
        question_id_to_user_id_ans = {}
        for question_right_id in question_right_list:#把学生的id转换为user_id
            sql_id_to_user_id = "SELECT user_id from suanke_student where id =" + str(question_right_id['student_id'])
            question_id_to_user_id = get_information(sql_id_to_user_id)
            question_to_l = []
            for question_l in question_id_to_user_id:
                question_to_l = question_l
                question_id_to_user_id_ans[question_right_id['student_id']] = question_to_l['user_id']
        sum1 = 0
        sum2 = 0
        sum_question = 0
        for question01 in question_right_list:
            sql_right_answer_ans = []
            sql_right_answer = "select count(id) from suanke_choice_question_user_answer_data where is_true_answer = 1 and choice_question_id = " + str(question_id) +" and user_id = " + str(question_id_to_user_id_ans[question01['student_id']])
            sql_right_answer_ans = get_information(sql_right_answer)
            for question_ans in sql_right_answer_ans:
                sum_question = question_ans['count(id)']
                if (sum_question > 0):
                    sum1 = sum1 + sum_question
                else : 
                    sum2 = sum2 + 1

def detail_sql2_pag3(question_id):
#    print("question_id")
#    print(question_id)
    sql_student_class = "SELECT * from (SELECT suanke_student_class.name,sum(is_true_answer)/count(is_true_answer),suanke_choice_question_user_answer_data.choice_question_id FROM suanke_student INNER JOIN suanke_student_student_class on suanke_student.id = suanke_student_student_class.student_id INNER JOIN suanke_student_class  on suanke_student_student_class.studentclass_id = suanke_student_class.id INNER JOIN suanke_choice_question_user_answer_data on suanke_student.user_id = suanke_choice_question_user_answer_data.user_id GROUP BY suanke_choice_question_user_answer_data.choice_question_id,suanke_student_class.name ORDER BY suanke_choice_question_user_answer_data.choice_question_id,(sum(is_true_answer)/count(is_true_answer)) DESC,suanke_student_class.name) AS A where A.choice_question_id = 1"
    question_class_list = get_information(sql_student_class)
    question_answer = {}
#    print("question_answer")
#    print(question_class_list)

    

def detail(request, question_id):
#    print("question_id")
#    print(question_id)
    sql = "select content, choice_analysis, true_answer  FROM suanke_choice_questions WHERE id =" + str(question_id) 
    question_list = get_information(sql)
    question03 = []
    for question0 in question_list:
        question03 = question0
    sql2 = "select count(*) FROM suanke_choice_question_user_answer_data where  is_true_answer = 1 and choice_question_id = " + str(question_id)
    question1_list = get_information(sql2)
    question3 = []
    for question2 in question1_list:
        question3 = question2 
    sql3 = "SELECT count(*) FROM suanke_choice_question_user_answer_data where  is_true_answer = 0 and choice_question_id = " + str(question_id)
    question3_list = get_information(sql3)
    question5 = []
    for question4 in question3_list:
        question5 = question4
    

    sql4 = "select choice_question_id,choice_option, choice_content from suanke_choice_question_options where choice_question_id = " + str(question_id)

    question4_list = get_information(sql4)
    question6 = []
    for question7 in question4_list:
        question6 = question7
    question = []
    for question1 in question_list:
        question = question1
    
    sqla1 = "SELECT count(*) FROM suanke_choice_question_submit_detail_log WHERE submit_context = 'A' and choice_question_id =" + str(question_id)
    questiona_list = get_information(sqla1)
    questiona = []
    for questiona1 in questiona_list:
        questiona = questiona1
    question["questiona"] = questiona["count(*)"]
    sqlb1 = "SELECT count(*) FROM suanke_choice_question_submit_detail_log WHERE submit_context = 'B' and choice_question_id =" + str(question_id) 
    questionb_list = get_information(sqlb1)
    questionb = []
    for questionb1 in questionb_list:
        questionb = questionb1
    question["questionb"] = questionb["count(*)"]
    sqlc1 = "SELECT count(*) FROM suanke_choice_question_submit_detail_log WHERE submit_context = 'C' and choice_question_id =" + str(question_id)
    questionc_list = get_information(sqlc1)
    questionc = []
    for questionc1 in questionc_list:
        questionc = questionc1
    question["questionc"] = questionc["count(*)"]
    sqld1 = "SELECT count(*) FROM suanke_choice_question_submit_detail_log WHERE submit_context = 'D' and choice_question_id =" + str(question_id)
    questiond_list = get_information(sqld1)
    questiond = []
    for questiond1 in questiond_list:
        questiond = questiond1
    question["questiond"] = questiond["count(*)"]

    question["is_true_answer"] = question3["count(*)"]
    question["is_false_answer"] = question5["count(*)"]
    question["choice_option_content"] = question4_list
    question["true_answer"] = question03["true_answer"]
    #detail_sql2_pag3(question_id)
    sql_student_class = "SELECT * from (SELECT suanke_student_class.name,sum(is_true_answer),sum(is_true_answer)/count(is_true_answer), is_true_answer,count(is_true_answer),suanke_choice_question_user_answer_data.choice_question_id FROM suanke_student INNER JOIN suanke_student_student_class on suanke_student.id = suanke_student_student_class.student_id INNER JOIN suanke_student_class  on suanke_student_student_class.studentclass_id = suanke_student_class.id INNER JOIN suanke_choice_question_user_answer_data on suanke_student.user_id = suanke_choice_question_user_answer_data.user_id GROUP BY suanke_choice_question_user_answer_data.choice_question_id,suanke_student_class.name ORDER BY suanke_choice_question_user_answer_data.choice_question_id,(sum(is_true_answer)/count(is_true_answer)) DESC,suanke_student_class.name) AS A where A.choice_question_id =" + str(question_id)
    question_class_list = get_information(sql_student_class)
    question_class = []
    question_answer_name  = []
    question_answer_rate = []
    question_answer_right = []
    question_answer_all = []
    i = 1
    for question_class1 in question_class_list:
        question_class  = question_class1
        #print("question_class")
        #print(question_class)
        if(i == 6):
            break
        #print("question_class[name]")
        #print(question_class['name'])
        question_answer_name.append(question_class['name'])
        question_answer_rate.append(question_class['sum(is_true_answer)/count(is_true_answer)'])
        question_answer_right.append(question_class['sum(is_true_answer)'])
        question_answer_all.append(question_class['count(is_true_answer)'] - question_class['sum(is_true_answer)'])
        i = i + 1
        question_answer_name.reverse()
        question_answer_rate.reverse()
        question_answer_right.reverse()
        question_answer_all.reverse()
    i = 1

    question["question_answer_name"] = question_answer_name
#    print("question_answer_name", question_answer_name)
    question["question_answer_rate"] = question_answer_rate
#    print("question_answer_rate", question_answer_rate)
    question["question_answer_right"] = question_answer_right
#    print("question_answer_right", question_answer_right)
    question["question_answer_all"] = question_answer_all
#    print("question_answer_all", question_answer_all)


    #print("question_answer")
    #print(question_class_list)
    return render(request, 'polls/index.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    return render(request, 'polls/student.html', {'question_number': question_id})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def student(request, question_id):
    #question_number = model.Student.objects.get(pk=1)
    question_number = 1
    return render(request, 'polls/student.html', {'question_number': question_id})

def pyecharts(request):
    choose = ["用户量","答对人数","其他人数"]
    values = [visualization2.x1,visualization2.x2,visualization2.x3]
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(choose,values)],
            center=["35%", "50%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-调整位置"),
            legend_opts=opts.LegendOpts(pos_left="15%"),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
        .render("polls/sector.html")
)
   # question_number = 1
    #return render(request, 'polls/sector.html', {'question_number':question_number})
