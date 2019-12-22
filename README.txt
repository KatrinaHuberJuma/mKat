# mKat
> an application for tracking learning goals


To run project locally:
1. `source mKat_venv/bin/activate`
1. `cd mkat_project`
1. `python manage.py runserver`

___

## Objects:

**Fail** 
Short for "point of failure"
+ fields: 
    - title
    - user (fk, user id)
    - created_at, updated_at

**Section** 
An area of study, a grouping of topics
+ fields:
    - title
    - user (fk, user id)
    - created_at, updated_at

**Resource** 
For keeping track of where questions come from, and where good explanations can be found
+ fields:
    - title
    - author
    - course
    - url
    - level
    - user (fk, user id)
    - created_at, updated_at

**Practice** 
Once session of practice, to group questions by date
+ fields:
    - date
    - resource (fk, resource id)

**Topic** 
A middle level of sorting, between section and tag
+ fields:
    - title
    - section (fk, section id)
    - created_at, updated_at
        * confidence

**Question** 
A question (such as from a practice test or quiz)
+ fields:
    - title
    - answered_correctly
    - confidence
    - section
    - practice_session
    - topics
    - point_of_failure
    - user (fk, user id)
    - created_at, updated_at

**Tag** 
Smallest unit of grouping, might be a single keyword or concept
+ fields:
    - title
    - topics
    - questions
    - created_at, updated_at

**Strategy** 
A plan of attack, addressing a point(s) of failure, or solidifying a concept (tag/topic)
+ fields:
    - title
    - practice_sessions
    - points_of_failure
    - created_at, updated_at

**Note** 
A place for misc refelections
+ fields:
    - title
    - content
    - point_of_failure
    - tags
    - created_at, updated_at
        * consider adding "practice session"?
