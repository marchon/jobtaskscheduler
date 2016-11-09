"""
Configuration for docs
"""

source_link = "https://github.com/giovanni-codrotech/jobtaskscheduler"
docs_base_url = "https://giovanni-codrotech.github.io/jobtaskscheduler"
headline = "Job Task Scheduler"
sub_heading = "A very simple scheulder for frappe using rq-schedule"


def get_context(context):
    context.brand_html = "Job Task Scheduler"
