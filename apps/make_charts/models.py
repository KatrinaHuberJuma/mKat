from django.db import models
# from ..login_app.models import User

# Create your models here.

# Fail
class Fail(models.Model):
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('login_app.User', related_name="points_of_failure", default=1)
    # related to Strategy, related_name="strategies"
    # in questions: related to Question related_name="questions"
    def __repr__(self):
        return f"<Fail Object: {self.title}>"


# Section
class Section(models.Model):
    title = models.CharField(max_length=45)
    # linked to Question by related_name="questions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('login_app.User', related_name="sections", default=1)
    def __repr__(self):
        return f"<Section Object: {self.title}>"

# Resource
class Resource(models.Model):
    title = models.CharField(max_length=45)
    # linked to Practice by related name="practice_sessions"
    # todo: further study
    author = models.CharField(max_length=45, null=True, blank=True)
    course = models.CharField(max_length=45, null=True, blank=True)
    url = models.CharField(max_length=45, null=True, blank=True)
    user = models.ForeignKey('login_app.User', related_name="resources", default=1)
    level = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Resource Object: {self.title}>"


# Practice session
class Practice(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    resource = models.ForeignKey(Resource, related_name="practice_sessions", default=1)
    # related to Strategy, related_name="strategies")
    # related to Practice, related_name="questions"
    def __repr__(self):
        return f"<Practice Object: {self.date}, {self.resource}>"


# Topic
class Topic(models.Model):
    title = models.CharField(max_length=45)
    section = models.ForeignKey(Section, related_name="topics", default=1)
    # todo: further study 
    confidence = models.IntegerField()
    # linked to Question by related_name="questions")
    # related to Tag, related name="tags"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Topic Object: {self.title}>"

# Question
class Question(models.Model):
    title = models.CharField(max_length=45)
    answered_correctly = models.NullBooleanField(null=True)
    # TODO: google "The default form widget for this field is NullBooleanSelect if null=True."
    # related to Tag related_name="tags")
    confidence = models.IntegerField()
    section = models.ForeignKey(Section, related_name="questions", default=1)
    practice_session = models.ForeignKey(Practice, related_name="questions", default=1)
    topic = models.ForeignKey(Topic, related_name="questions", default=1)
    point_of_failure = models.ForeignKey(Fail, related_name="questions", default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Question Object: {self.title}>"    



# Tag
class Tag(models.Model):
    title = models.CharField(max_length=45)
    topics = models.ManyToManyField(Topic, related_name="tags")
    questions = models.ManyToManyField(Question, related_name="tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Tag Object: {self.title}>"

# Strategy
class Strategy(models.Model):
    title = models.CharField(max_length=45)
    # todo: notes
    # todo topics
    practice_sessions = models.ManyToManyField(Practice, related_name="strategies")
    points_of_failure = models.ManyToManyField(Fail, related_name="strategies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Strategy Object: {self.date}>"

