# Internal-Machine-Issue-Report-System-Mini-Project

HOST : https://heartnxz.pythonanywhere.com/




API register_machine
POST : {host}/api/register_machine/
Body : {
    "name":"<name_machin>"
}




API report_issue
POST : {host}/api/report_issue/
Body : {
    "machine_id":"<machine_id>",
    "issue": "<issue>",
    "description": "<description>"
}




API retrive_all_issue_reports
GET : {host}/api/retrive_all_issue_reports/?page=<page>




API filter_issue_reports
GET :  {host}/api/filter_issue_reports/?machine_id=<machine_id>&title=<title>&description=<description>&start_timestamp=<start_timestamp>&end_timestamp=<start_timestamp>&status=<status>




API counting_issue_reports
GET : {host}/api/counting_issue_reports/?page=<page>




API count_common_words
GET : {host}/api/count_common_words/?top_k=<top_k>




API count_common_words
POST : {host}/api/resolvingandhistory/<issue_id>/
Body : {
    "status":"<status>",
    "comment": "<comment>",
}




API count_common_words
GET : {host}/api/retrieveissuedetail/<issue_id>/



