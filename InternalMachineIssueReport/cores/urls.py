
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from cores.views import RegisterMachine
from cores.views import ReportIssue
from cores.views import ListIssueReports
from cores.views import FilterIssueReports
from cores.views import CountingIssueReports
from cores.views import CountCommonWords
from cores.views import ResolvingandHistory
from cores.views import RetrieveIssueDetail

urlpatterns = [

    path("register_machine/", RegisterMachine.RegisterMachine.as_view(), name="register_machine"),
    path("report_issue/", ReportIssue.ReportIssue.as_view(), name="report_issue"),
    path("retrive_all_issue_reports/", ListIssueReports.ListIssueReports.as_view(), name="retrive_all_issue_reports"),
    path("filter_issue_reports/", FilterIssueReports.FilterIssueReports.as_view(), name="filter_issue_reports"),
    path("counting_issue_reports/", CountingIssueReports.CountingIssueReports.as_view(), name="counting_issue_reports"),
    path("count_common_words/", CountCommonWords.CountCommonWords.as_view(), name="count_common_words"),
    path("resolvingandhistory/<int:issue_id>/", ResolvingandHistory.ResolvingandHistory.as_view(), name="resolvingandhistory"),
    path("retrieveissuedetail/<int:issue_id>/", RetrieveIssueDetail.RetrieveIssueDetail.as_view(), name="resolvingandhistory"),

]
