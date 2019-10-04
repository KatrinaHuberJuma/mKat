from django.db import models
# from ..login_app.models import User

# Create your models here.


# Fail
class Fail(models.Model):
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('login_app.User', related_name="points_of_failure", blank=True, null=True)
    # related to Strategy, related_name="strategies"
    # in questions: related to Question related_name="questions"
    def __repr__(self):
        return f"<Fail Object: {self.title}>"
    def __str__(self):
        return 'Fail: {}'.format(self.title)

# Section
class Section(models.Model):
    title = models.CharField(max_length=45)
    # linked to Question by related_name="questions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('login_app.User', related_name="sections", blank=True, null=True)
    def __repr__(self):
        return self.title
    def __str__(self):
        return 'Section: {}'.format(self.title)

# Resource
class Resource(models.Model):
    title = models.CharField(max_length=45)
    # linked to Practice by related name="practice_sessions"
    # todo: further study
    author = models.CharField(max_length=45, null=True, blank=True)
    course = models.CharField(max_length=45, null=True, blank=True)
    url = models.CharField(max_length=45, null=True, blank=True)
    user = models.ForeignKey('login_app.User', related_name="resources", blank=True, null=True)
    level = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Resource Object: {self.title}>"
    def __str__(self):
        return 'Resource: {}'.format(self.title)

# Practice session
class Practice(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    resource = models.ForeignKey(Resource, related_name="practice_sessions", blank=True, null=True)
    # related to Strategy, related_name="strategies")
    # related to Practice, related_name="questions"
    def __repr__(self):
        return f"<Practice Object: {self.date}, {self.resource}>"
    def __str__(self):
        return 'Practice: {}'.format(self.date)

# Topic
class Topic(models.Model):
    title = models.CharField(max_length=45)
    section = models.ForeignKey(Section, related_name="topics", blank=True, null=True)
    # todo: further study 
    # confidence = models.IntegerField()
    # linked to Question by related_name="questions")
    # related to Tag, related name="tags"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Topic Object: {self.title}>"
    def __str__(self):
        return 'Topic: {}'.format(self.title)

# Question
class Question(models.Model):
    title = models.CharField(max_length=45)
    answered_correctly = models.NullBooleanField(null=True)
    # TODO: google "The default form widget for this field is NullBooleanSelect if null=True."
    # related to Tag related_name="tags")
    confidence = models.IntegerField()
    section = models.ForeignKey(Section, related_name="questions", blank=True, null=True)
    practice_session = models.ForeignKey(Practice, related_name="questions", blank=True, null=True)
    topic = models.ForeignKey(Topic, related_name="questions", blank=True, null=True)
    point_of_failure = models.ForeignKey(Fail, related_name="questions", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Question Object: {self.title}>"    
    def __str__(self):
        return 'Question: {}'.format(self.title)


# Tag
class Tag(models.Model):
    title = models.CharField(max_length=45)
    topics = models.ManyToManyField(Topic, related_name="tags")
    questions = models.ManyToManyField(Question, related_name="tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Tag Object: {self.title}>"
    def __str__(self):
        return 'Tag: {}'.format(self.title)

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
    def __str__(self):
        return 'Strategy: {}'.format(self.title)

# notes table
    # date
    # tag fk
class Note(models.Model):
    title = models.CharField(max_length=45, default='(untitled)')
    content = models.TextField()
    point_of_failure = models.ManyToManyField(Fail, related_name="notes")
    tags = models.ManyToManyField(Tag, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Note Object: {self.date}>"
    def __str__(self):
        return 'Note: {}'.format(self.title)