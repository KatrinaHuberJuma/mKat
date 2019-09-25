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


