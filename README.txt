mKat: an application for tracking learning goals

SHELLTIME!

from apps.make_charts.models import *
from apps.login_app.models import *

use = User.objects.create(first_name="kat", last_name="J")

first_fail = Fail.objects.create(title="Point of failure test")
re = Resource.objects.create(title="my resource re")
sec = Section.objects.create(title="my section", user=use)
topic = Topic.objects.create(title="my topic", section=sec, confidence=4)

practice = Practice.objects.create(resource=re)


q = Question.objects.create(title="First Test Q", answered_correctly=True, point_of_failure=first_fail, section=sec, confidence=3, practice_session=practice, topic=topic)

q.practice_session.date
q.point_of_failure.title
q.section.title
q.topic.title
q.section.user.first_name
q.tags.add(Tag.objects.create(title="my tag"))
q.tags.add(Tag.objects.create(title="my other tag"))

tg = Tag.objects.first()
tg.topics.add(Topic.objects.first())
tg.topics.first()
a_topic = tg.topics.first()
a_topic.tags.first()



all_questions = Question.objects.all()
for question in all_questions:
    print(question.id)
    print(question.title)





all_fails = Fail.objects.all()
for fail in all_fails:
    print(fail.id)
    print(fail.title)
                    3
                    Vocab
                    4
                    Time Pressure
                    5
                    Misread the question
                    6
                    Sloppiness
                    7
                    N/A



all_tags = Tag.objects.all()
for tag in all_tags:
    print(tag.id)
                    Syntax
                    4
                    Explaining my thoughts
                    5


all_sections = Section.objects.all()
for section in all_sections:
    print(section.id)
    print(section.title)
                    136
                    Algos



all_topics = Topic.objects.all()
for topic in all_topics:
    print(topic.id)
    print(topic.title)
                    28
                    Data Structures
                    29
                    Big O
                    30
                    Space complexity
                    31
                    Recursion

res = Resource.objects.all() 



# can make loops to create practice sessions with semi-random data




