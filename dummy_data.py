from apps.make_charts.models import *
from apps.login_app.models import *
from datetime import datetime, timedelta
import random

N = 0

date_N_days_ago = datetime.now() - timedelta(days=N)

print(datetime.now())
print(date_N_days_ago)


# --------------------

user = User.objects.first()
re = Resource.objects.first()
sec = Section.objects.first()

practice = Practice.objects.create(resource=re)
practice.date = date_N_days_ago
practice.save()
def make_questions(num, win_fail_lst, fail_source, tag_list, topic_lst):
    
    for i in range(num):
        answered_correctly = random.choice(win_fail_lst)
        print(answered_correctly)
        if answered_correctly:
            fail_source = [Fail.objects.get(title="N/A")]
        q = Question.objects.create(title=i, 
                                    answered_correctly=answered_correctly, 
                                    point_of_failure=random.choice(fail_source), 
                                    section=sec, confidence=random.choice([1,2,3,4,5,6]), 
                                    practice_session=practice, 
                                    topic=random.choice(topic_lst))
        print(q)
        q.tags.add(random.choice(tag_list))
        q.save()




win_fail_lst = [True, True, True, True, True,True,True, True,True,True,True,True,True,True, True,True,True,True,True,True,True,True, False, False, False, False, False]
fail_source = Fail.objects.exclude(id=7)
tag_list = Tag.objects.all()
topic_lst = Topic.objects.all()


make_questions(15, win_fail_lst, fail_source, tag_list, topic_lst)






# --------------------

questions = Question.objects.all()

def make_tags(tag_titles, q_dict):
    q_lst = list(q_dict)
    for i in range(len(tag_titles)):
        tag = Tag.objects.create(title=tag_titles[i])
        questions_to_tag = random.sample(q_lst, 20)
        for question in questions_to_tag:
            tag.questions.add(question)
    
        
            



make_tags(["curries", "guesses", "beets"], questions)



questions = Question.objects.all()
for i in range(len(questions)):
    if i % 2 == 0:
        questions[i].answered_correctly = False