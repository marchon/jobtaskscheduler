# -*- coding: utf-8 -*-
# Copyright (c) 2015, Codrotech Inc. and contributors
# For license information, please see license.txt
from __future__ import unicode_literals

import calendar
import json
import re
from calendar import monthrange, timegm
from datetime import datetime
from time import gmtime, localtime, mktime

import frappe
import rq
import schedule
from frappe import _, _dict
from frappe.model.document import Document
from frappe.utils import get_sites, nowdate
from frappe.utils.background_jobs import get_redis_conn
from rq.queue import get_failed_queue
from rq_scheduler import Scheduler


class JobScheduler(Document):

    def validate(self):
        if self.run == "Hourly":
            check_minutes(self.minute)

        elif self.run == "Daily":
            check_hours(self.hour)
            check_minutes(self.minute)

        elif self.run == "Yearly" or self.run == "Monthly":
            check_day_of_month(self.day_of_month, self.month)
            check_hours(self.hour)
            check_minutes(self.minute)

        elif self.run == "Cron Style":
            check_cron(str(self.cron_style))

        if self.enabled:
            if self.run == "Cron Style":
                cron = str(self.cron_style)
            else:
                cron = get_cron_string(self)

            # cancel_job(get_redis_conn(), self.job_id)
            self.job_id = set_schedule(get_redis_conn(), self, cron)

            frappe.msgprint(self.run + " Job scheduled, id = " + self.job_id)

        elif self.job_id:
            self.job_id = cancel_job(get_redis_conn(), self.job_id)
            frappe.msgprint("Job disabled")

    def on_trash(self):
        cancel_job(get_redis_conn(), self.name)


def check_minutes(minute):
    if not minute or not minute.isdigit() or not 0 <= int(minute) < 60:
        frappe.throw(_("Minute value must be between 0 and 59"))


def check_hours(hour):
    if hour and 0 <= int(hour) < 24:
        pass
    else:
        frappe.throw(_("Hour value must be between 0 and 23"))


def check_day_of_month(day, month):
    m = {v: k for k, v in enumerate(calendar.month_abbr)}
    last = monthrange(datetime.now().year, m.get(str(month).title()))[1]
    if int(day) > last:
        frappe.throw(
            _("Day value for {0} must be between 1 and {1}").format(month, last))


def check_cron(cron):
    validate_crontab_time_format_regex = re.compile(
        "{0}\s+{1}\s+{2}\s+{3}\s+{4}".format(
            "(?P<minute>\*(\/[0-5]?\d)?|[0-5]?\d)", "(?P<hour>\*|[01]?\d|2[0-3])",
            "(?P<day>\*|0?[1-9]|[12]\d|3[01])", "(?P<month>\*|0?[1-9]|1[012])", "(?P<day_of_week>\*|[0-6](\-[0-6])?)")  # end of str.format()
    )  # end of re.compile()

    if validate_crontab_time_format_regex.match(cron) is None:
        frappe.throw(_("Cron string is not a valid format"))


def get_cron_string(task):
    cron = "* * * * *".split()
    cron[0] = task.minute
    cron[1] = None if task.hour is None else str(
        int(task.hour) - get_utc_time_diff())
    cron[2] = task.day_of_month
    cron[3] = task.month
    cron[4] = task.day_of_week

    if task.run == "Hourly":
        cron[1] = cron[2] = cron[3] = cron[4] = "*"

    elif task.run == "Daily":
        cron[2] = cron[3] = cron[4] = "*"

    elif task.run == "Weekly":
        cron[2] = cron[3] = "*"

    elif task.run == "Monthly":
        cron[3] = cron[4] = "*"

    elif task.run == "Yearly":
        cron[4] = "*"

    return " ".join(cron)


def test_job_method(**kwargs):

    print " ********* start jobs execution ".encode("utf-8")
    frappe.init('')
    conn = get_redis_conn()

    print "** empty failed queue"
    q = get_failed_queue(connection=conn)
    e = q.empty()

    print "** get scheduled jobs"
    scheduler = Scheduler(connection=conn)
    print "jobs scheduled : {0}".format(scheduler.get_jobs())

    print "** get kwards args"
    print "kwargs = {0}".format(kwargs)
    print " ********* end jobs execution ".encode("utf-8")


def set_schedule(conn, task, cron_string):

    s = Scheduler(connection=conn)
    kw = json.loads(task.kwargs)

    kw.update({
        "site": frappe.local.site,
        "user": frappe.session.user
    })

    job = s.cron(
        id=task.job_id,
        description=task.title,
        # A cron string (e.g. "0 0 * * 0")
        cron_string=cron_string,
        # Function to be queued
        func=task.method,
        # Arguments passed into function when executed
        # args=[task.args],
        # Keyword arguments passed into function when executed
        kwargs=kw,
        # Repeat this number of times (None means repeat forever)
        repeat=None,
        # In which queue the job should be put in
        queue_name=task.queue
    )
    print " ** scheduled in '" + task.queue + "' queue, with id: " + job.get_id() + " at " + cron_string

    return job.get_id()


def cancel_job(conn, job_id):

    scheduler = Scheduler(connection=conn)

    if job_id in scheduler:
        scheduler.cancel(job_id)
        print " Job: " + job_id + " deleded"

    else:
        print " Job: " + str(job_id) + " not scheduled"

    return None


def get_utc_time_diff():
    t = localtime()
    return (timegm(t) - timegm(gmtime(mktime(t)))) / 3600
