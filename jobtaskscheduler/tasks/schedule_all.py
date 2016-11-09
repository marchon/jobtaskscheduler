# -*- coding: utf-8 -*-
# Copyright (c) 2015, Codrotech Inc. and contributors
# For license information, please see license.txt
import time

import frappe
from frappe.model.document import Document
from frappe.utils import get_sites
from frappe.utils.background_jobs import get_redis_conn
from jobtaskscheduler.job_task_scheduler.doctype.job_scheduler.job_scheduler import (get_cron_string,
                                                                                     set_schedule)


def schedule_all_tasks():
    with frappe.init_site():
        sites = get_sites()

    for site in sites:
        get_all_tasks_site(site)

    while True:
        time.sleep(10)


def get_all_tasks_site(site):

    try:
        print "site: {0}".format(site)
        frappe.init(site=site)
        frappe.connect()
        tasks = frappe.get_all("Job Scheduler",
                               filters={"active": "1"},
                               fields=["name", "job_id", "method", "run", "minute", "hour", "day_of_week", "day_of_month", "cron_style", "queue"])

        for task in tasks:
            if (task.run == "Cron Style"):
                print "cron string: {0} ".format(task.cron_style)
            else:
                print get_cron_string(task)

            set_schedule(get_redis_conn(), task, task.cron_style)
    except:
        # it should try to enqueue other sites
        print frappe.get_traceback()

    finally:
        frappe.destroy()
