from django.conf.urls import patterns, include, url
from dmeventsapp import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register(r'events', views.EventViewSet)

events_router = routers.NestedSimpleRouter(router, r'events', lookup='event')
events_router.register(r'questions', views.QuestionViewSet)
events_router.register(r'participants', views.ParticipantViewSet)
router.register(r'answers', views.AnswerViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ptalessons.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 	url(r'^', include(router.urls)),
 	url(r'^', include(events_router.urls)),
 	url(r'^admin/', include(admin.site.urls)),
 )
