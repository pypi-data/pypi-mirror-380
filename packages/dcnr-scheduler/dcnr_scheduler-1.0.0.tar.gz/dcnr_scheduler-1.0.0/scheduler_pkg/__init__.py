"""Scheduler API offers the possibility to schedule running of tasks within current application. 
It may serve as main entry point for application, as well as side support for application run.

It offers similar functionality to `crontab` utility in Linux, however implementation of this 
functionality is completely custom.


### Example

Write a decorator for your custom function and run.

```python
from tma_common import ScheduledRun

# custom function with decorator
@ScheduledRun(minute='13',hour='*/2',weekday='1-5')
def func1(scheduler,current_time):
    scheduler.logStatus()
```

Custom function `func1` takes two parameters. First `scheduler` is scheduler object. Usually we
do not need this object, but for debug purposes it may be useful. Second parameter `currentTime`
is `datetime` object native to Python.

Parameters for function decorator are described in section **Scheduler Parameters**.

**Very important**: custom function is executed asynchronously in separate thread, 
that means if you schedule events for every minute of day, and your task takes 10 minutes for example,
then execution time does not interfere with triggering of events. As a result, your application may at the 
times be executing simultaneously around 10 tasks, each one started a minute after another.


### Scheduler Parameters

Parameters for function decorator are completely equivalent to parameters of SchedulerConfig class constructor.
They are based on format of `crontab` utility values.

Scheduler offers scheduling events with various granularity, where all granularities has to be satisfied in order to fire event.

Following table shows what parameters are available for Scheduler.

Parameter | Description
--------- | ------------------------------------------------
minute    | minute of hour (0, 1, ...59). For example value '5' matches times 08:05, 09:05, 10:05, ....
hour      | hour of day (0, 1, ... 23)
day       | day of month (1, 2, ...., 31)
month     | month of year (1-January, 2-February, ....12-December)
year      | year
weekday   | day of week, values: 0-Sunday, 1-Monday, ..., 6-Saturday
yearday   | day of year, values: 0, 1, ...365. value 0 is Jan 1, value 50 is February 20, value 120 is May 1 in non-leap year but is also Apr 30 in leap year

These parameters, if defined for scheduler, has to be satisfied simultaneously in order to fire event. Default value is, than all values of given parameter are valid for firing the event.

Values for each parameter can be defined in multiple ways. Scheduler support not only scalars, but also list of scalars, intervals and periods.

Format | Meaning
------- | -------------------
'*'     |  all values of given parameter are acceptable, that means every minute, every hour, every day ... depending on parameter itself
'*/5'   | all fifths, every 5 minute, every 5 hours, etc
'2-7'   | values in range of 2 to 7. From 2nd to 7th minute, from 2nd to 7th day, ...
'10-50/10' | every 10th in the range from 10 to 50, namely it means 10, 20, 30, 40, 50. Every x-th is taken from start of interval, not from absolute value. That means '13-55/7' is expanded to values 13, 20, 27, 34, 41, 48, 55
'1,2,5,6' | list of explicit values. In context of weekdays these values mean Monday, Tuesday, Friday, Saturday.

**@ScheduledRun(minute='13',hour='*/2',weekday='1-5')**

This makes an event every working day (Monday to Friday) every two hours exactly on 13th minute. So for monday it will be scheduled for these times:

```
00:13
02:13
04:13
06:13
...
22:13
```

**@ScheduledRun(day='*/5')**

This makes and event every minute during whole day on every fifth day in the month. That means 1440 events during day (1 day = 1440 minutes). This is because minute and hour parameters are not set here, and default value is '*' what means 'each and every'.

Please not, that 'fifth' is derived from the beginning of month, that means the series of days may look like: Jan 5, Jan 10, Jan 15 ... Jan 30, Feb 5, Feb 10, Feb 15, Feb 20, Feb 25, Mar 5, ....

You may notice that between Jan 30 and Feb 5 are 6 days, and between Feb 25 and Mar 5 are 8 or 9 days depending on leap/no-leap year. If you need to run exactly every 5th day, you may use parameter `yearday` exemplified in next example.

**@ScheduledRun(yearday='*/13', minute='0',hour='12')**

This creates event every 13th day in the year at noon (once a day). That means series of dates may look like: Jan 12, Jan 25, Feb 7, Feb 20, Mar 5, Mar 18, Mar 31, Apr 13, ...

## Advanced

If you need even more precise control over firing events, just remember that you may place any logic between scheduler-event and execution of your task. Your logic may filter-out any unwanted times. In the most extreme case, you may just scheduler for triggering event every minute, and do you own filtering of times completely.

```python

@ScheduledRun()
def my_own_func(scheduler,currentDateTime):
    if currentDateTime.day==3 and currentDateTime.month==4:
        # do my task in the background
        pass
```

"""

__all__ = [
    "set_test_mode",
    "is_test_mode",
    "scheduled",
    "request_shutdown",
    "is_shutdown_requested",
    "ScheduledPlan",
    "SchedulerConfig"
]
from .scheduler import ScheduledRun, request_shutdown, SchedulerConfig, is_shutdown_requested
from .scheduled_plan import ScheduledPlan
from .run_mode import set_test_mode, is_test_mode

scheduled = ScheduledRun  # alias for convenience