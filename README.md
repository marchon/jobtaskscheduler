## Job Task Scheduler

A very simple frappe scheduler for job tasks based on rq-scheduler


#### 1. It use **rq-scheduler**, it has been added in requirements; in case it will not be installed, should be added manually using:

`$ pip install rq-scheduler`

and

`$ cd frappe-bench/`

`$ source env/bin/activate`

`$ pip install rq-scheduler`


#### 2. Add it to `Procfile` in `frappe-bench` folder:

It is needed to connect to the Redis queue:

`rqscheduler: rqscheduler -H [host] --port [redis_port]`

you can find info for [host] and [port] in `frappe-bench/config/redis_queue.conf`

#### 3. It is needed to run a script on `bench start` in order to pull all jobs from database and add to `rqscheduler`, so add the following to `Procfile`

`startup: bench execute jobtaskscheduler.tasks.schedule_all.schedule_all_tasks`

#### License

GPL

## This app is not needed anymore as frappe now have the ability to schedule cron jobs, see: 

https://github.com/frappe//frappe/docs/user/en/tutorial/task-runner.md
