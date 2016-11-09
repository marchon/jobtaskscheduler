## Job Task Scheduler

A very simple frappe scheduler for job tasks

#### 1. It use **rq-scheduler**, it has been added in requirements; in case it will not be installed, should be added manually using:

`$ cd frappe-bench/`

`$ source env/bin/activate`

`$ pip install rq-schedule`

#### 2. Add it to `Procfile` in `frappe-bench` folder:

`rqscheduler: rqscheduler -H localhost -p 11000 -v`

#### 3. It is needed to run a script on `bench start` in order to pull all jobs from database and add to `rqscheduler`, so add the following to `Procfile`

`startup: bench execute jobtaskscheduler.tasks.schedule_all.schedule_all_tasks`

#### License

GPL
