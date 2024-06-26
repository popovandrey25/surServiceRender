from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from surApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('show_votings/<int:user_id>/', VotingListByUserAPIView.as_view(), name='voting-list-by-user'),
    path('create/voting/', VotingCreateAPIView.as_view(), name='voting-create'),
    path('update/voting/<int:pk>/', VotingUpdateAPIView.as_view(), name='voting-update'),
    path('delete/voting/<int:pk>/', VotingDeleteAPIView.as_view(), name='voting-delete'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='register'),
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/answer-voting/<int:pk>/', VoteBulkCreateView.as_view(), name='do_response'),
    path('api/response-voting/<int:pk>/', VotingDetailView.as_view(), name='voting-detail'),
    path('api/detail-statistic/<int:pk>/', DetailStatisticAPIView.as_view(), name='detail-statistic'),
    path('api/poll-statistic/<int:poll_id>/', PollDetailAPIView.as_view(), name='poll-statistic'),
    path('api/add_logic/<int:pk>/', VotingUpdateLogicView.as_view(), name='add-logic'),
    path('api/submit/<int:pk>/', VotingUpdateSubmitView.as_view(), name='submit'),
    path('api/token/validate/', ValidateTokenView.as_view(), name='token_validate'),
    path('api/export-votes/<int:voting_id>/', ExportVotesToExcelView.as_view(), name='export-votes'),
    path('api/export-voting-json/<int:voting_id>/', ExportVotingToJsonFileView.as_view(), name='export-voting-json'),
]
