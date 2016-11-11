## Job Task Scheduler

A very simple frappe scheduler for job tasks


#### 1. It use **rq-scheduler**, it has been added in requirements; in case it will not be installed, should be added manually using:

`$ pip install rq-schedule`

and 

`$ cd frappe-bench/`

`$ source env/bin/activate`

`$ pip install rq-schedule`


#### 2. Add it to `Procfile` in `frappe-bench` folder:

`# This runs a scheduler process using the default Redis connection`
`rqscheduler: rqscheduler`

`# If you want to use a different Redis server you could also do:`
`rqscheduler: rqscheduler -H [host] --port [redis_port]`


#### 3. It is needed to run a script on `bench start` in order to pull all jobs from database and add to `rqscheduler`, so add the following to `Procfile`

`startup: bench execute jobtaskscheduler.tasks.schedule_all.schedule_all_tasks`

#### License

GPL
