# import json
import datetime as dt
import time
import threading
import logging
import signal
import sys

from .run_mode import is_test_mode
from .scheduled_plan import ScheduledPlan


logger = logging.getLogger(__name__)

# Global shutdown flag for graceful termination
_shutdown_requested = False
_shutdown_lock = threading.Lock()

def _signal_handler(signum, frame):
    """Handle termination signals by setting shutdown flag."""
    global _shutdown_requested
    with _shutdown_lock:
        _shutdown_requested = True
    logger.info(f"Received signal {signum}, initiating graceful shutdown...")

def _setup_signal_handlers():
    """Setup signal handlers for graceful shutdown."""
    # Handle common termination signals
    if hasattr(signal, 'SIGTERM'):
        signal.signal(signal.SIGTERM, _signal_handler)
    if hasattr(signal, 'SIGINT'):  # Ctrl+C
        signal.signal(signal.SIGINT, _signal_handler)
    # On Windows, handle SIGBREAK (Ctrl+Break)
    if sys.platform == 'win32' and hasattr(signal, 'SIGBREAK'):
        signal.signal(signal.SIGBREAK, _signal_handler)

def _is_shutdown_requested():
    """Check if shutdown has been requested."""
    with _shutdown_lock:
        return _shutdown_requested

def request_shutdown():
    """Manually request shutdown of all scheduler loops."""
    global _shutdown_requested
    with _shutdown_lock:
        _shutdown_requested = True
    logger.info("Manual shutdown requested for scheduler...")

# Initialize signal handlers
_setup_signal_handlers()

#
# safe conversion to integer from string
#
def to_int(text):
    try:
        val = int(text)
        return val, True
    except ValueError:
        return None, False


#
# count of days in year before given month
# 0 - January, 11 - December
#
yeardaycount = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


#
# range of values for event
# used only internally
#
class MomentRange:
    def __init__(self, text=None):
        self.set_range_text(text)
        self.range_from = 0
        self.range_to = 3000

    def dictionary(self):
        return {'from': self.range_from, 'to': self.range_to}

    def is_active(self, a):
        return a >= self.range_from and a <= self.range_to

    def set_range_text(self, text):
        va = vb = False
        if '-' in text:
            parts = text.split('-')
            if len(parts) != 2:
                logger.info(f'Too many parts of range in string {text}')
            self.range_from, va = to_int(parts[0])
            if not va:
                logger.info(f'Value "{parts[0]}" is not number')
                self.range_from = 0
            self.range_to, vb = to_int(parts[1])
            if not vb:
                logger.info(f'Value "{parts[1]}" is not number')
                self.range_to = 3000
        elif text == '*':
            self.range_from = 0
            self.range_to = 3000
        else:
            self.range_from, va = to_int(text)
            if not va:
                logger.info(f'Invalid number "{text}"')
                self.range_from = 0
                self.range_from = 3000
            else:
                self.range_to = self.range_from


#
# Period for scheduling event
# Used only internally
#
class MomentPeriod:
    def __init__(self, text):
        self.base = None
        self.period = 1
        if '/' in text:
            a = text.split('/')
            self.base = MomentRange(a[0])
            self.set_period_text(a[1])
        else:
            self.base = MomentRange(text)

    def dictionary(self):
        return {
            'range': self.base.dictionary(),
            'period': self.period
        }

    def is_active(self, num):
        return self.base.is_active(num) and \
               (num - self.base.range_from) % self.period == 0

    def set_period_text(self, text):
        self.period, va = to_int(text)
        if not va:
            self.period = 1
            logger.info(f'Invalid period {text}')


#
# List of values for scheduling event
# used only internally
#
class MomentList:
    def __init__(self, text):
        self.moments = []
        if ',' in text:
            parts = text.split(',')
            for p in parts:
                self.append_text(p)
        else:
            self.append_text(text)

    def dictionary(self):
        return [a.dictionary() for a in self.moments]

    def append_text(self, text):
        if '/' in text:
            self.moments.append(MomentPeriod(text))
        else:
            self.moments.append(MomentRange(text))

    def is_active(self, text):
        n, na = to_int(text)
        if not na:
            return False
        for m in self.moments:
            if m.is_active(n):
                return True
        return False


#
# Main class for scheduler
#
class SchedulerConfig:
    def __init__(self, minute=None, hour=None, weekday=None, day=None,
                 month=None, year=None, yearday=None):
        self.minute = self.text_to_numbers(minute or '*')
        self.hour = self.text_to_numbers(hour or '*')
        self.weekday = self.text_to_numbers(weekday or '*')
        self.day = self.text_to_numbers(day or '*')
        self.month = self.text_to_numbers(month or '*')
        self.year = self.text_to_numbers(year or '*')
        self.yearday = self.text_to_numbers(yearday or '*')

    def dictionary(self):
        value = {}
        if self.minute is not None:
            value['minute'] = self.minute.dictionary()
        if self.hour is not None:
            value['hour'] = self.hour.dictionary()
        if self.weekday is not None:
            value['weekday'] = self.weekday.dictionary()
        if self.day is not None:
            value['day'] = self.day.dictionary()
        if self.month is not None:
            value['month'] = self.month.dictionary()
        if self.year is not None:
            value['year'] = self.year.dictionary()
        if self.yearday is not None:
            value['yearday'] = self.yearday.dictionary()
        return value

    def text_to_numbers(self, text):
        if text is None or text == '*':
            return None
        if ',' in text:
            return MomentList(text)
        elif '/' in text:
            return MomentPeriod(text)
        else:
            return MomentRange(text)

    def next_datetime(self):
        d = dt.datetime.now()
        for a in range(0, 2):
            at = self.active_on_day(d)
            if at:
                return at
            d = dt.datetime(d.year, d.month, d.day, 0, 0) \
                + dt.timedelta(days=1)
        return None

    def day_of_year(self, d):
        leap = 0
        if d.year % 4 == 0 and (d.year % 100 != 0
           or d.year % 400 == 0) and d.month > 2:
            leap = 1
        return yeardaycount[d.month - 1] + (d.day - 1) + leap

    #
    # Internal function - to check if there will be event triggered
    # in current day (parameter d) and if yes, then returns only future events
    def active_on_day(self, d, target=None, limit=None):
        if self.year is not None and not self.year.is_active(d.year):
            return None
        if self.month is not None and not self.month.is_active(d.month):
            return None
        if self.day is not None and not self.day.is_active(d.day):
            return None
        if self.weekday is not None \
           and not self.weekday.is_active(d.isoweekday() % 7):
            return None
        if self.yearday is not None \
           and not self.yearday.is_active(self.day_of_year(d)):
            return None
        for hc in range(d.hour, 23):
            if self.hour is None or self.hour.is_active(hc):
                sm = d.minute if hc == d.hour else 0
                for hm in range(sm, 59):
                    if self.minute is None or self.minute.is_active(hm):
                        if target is None:
                            return dt.datetime(d.year, d.month, d.day, hc, hm)
                        else:
                            if limit is None or len(target) + 1 <= limit:
                                target.append(dt.datetime(d.year, d.month,
                                                          d.day, hc, hm))
                            else:
                                return None
        return None

    # Retrieve next events from NOW till specified days in future
    # or till we reach maximum number of entries (whichever comes first)
    def next_events(self, daysInFuture=7, maxEntries=10):
        entries = []
        d = dt.datetime.now()
        for a in range(0, daysInFuture):
            self.active_on_day(d, target=entries, limit=maxEntries)
            if len(entries) >= maxEntries:
                return entries
            # we are interested only in events
            # in range of (current_hour_min, 23:59) for today
            # and in range (00:00, 23:59) for all other days
            d = dt.datetime(d.year, d.month, d.day, 0, 0) \
                + dt.timedelta(days=1)
        return entries

    # only for debug purposes
    def log_status(self, daysInFuture=7, maxEntries=10):
        print('==========next events=============')
        for e in self.next_events(daysInFuture=daysInFuture,
                                 maxEntries=maxEntries):
            print(f'          {e}')

    # run scheduler in non-blocking mode (in background thread)
    def run_async(self, func):
        if is_test_mode():
            print('Subprocess mode detected, scheduler will not be started.')
            return
        
        t = threading.Thread(target=self.run, args=(func,))
        t.daemon = True  # Make thread daemon so it exits when main exits
        t.start()

    # run scheduler in blocking mode
    def run(self, func):
        if is_test_mode():
            print('Subprocess mode detected, scheduler will not be started.')
            return
        
        lastfire = 0
        self.log_status()
        # schedule forever (until shutdown is requested)
        while not _is_shutdown_requested():
            n = self.next_datetime()
            if n is None:  # no future events in near future, wait 1 day
                logger.debug('Wait for 1 day')
                # Sleep in smaller chunks to check shutdown flag more frequently
                for _ in range(864):  # 864 * 100 = 86400 seconds (1 day)
                    if _is_shutdown_requested():
                        break
                    time.sleep(100)
            else:  # some event in near future, wait for required time
                d = dt.datetime.now()
                diff = (n - d).total_seconds()
                if diff <= 0:
                    # no events should be triggered twice, so if there was
                    # trigger in last 60 seconds, then wait some time
                    if time.time() - lastfire < 60:
                        logger.debug('Wait for 1 minute')
                        # Sleep in smaller chunks to check shutdown flag
                        for _ in range(60):
                            if _is_shutdown_requested():
                                break
                            time.sleep(1)
                    else:
                        lastfire = time.time()
                        logger.debug(f'Trigger event at: {n}')
                        t = threading.Thread(target=func, args=(self, d,))
                        t.daemon = True  # Make thread daemon so it exits when main exits
                        t.start()
                else:
                    waittime = max(min(86400, diff), 1)
                    logger.debug(f'Wait for {waittime} seconds, diff={diff}')
                    # Sleep in smaller chunks to check shutdown flag more frequently
                    sleep_chunks = max(1, int(waittime))
                    sleep_per_chunk = waittime / sleep_chunks
                    for _ in range(sleep_chunks):
                        if _is_shutdown_requested():
                            break
                        time.sleep(sleep_per_chunk)
        
        logger.info('Scheduler shutdown completed gracefully.')

class ScheduledPlanPool:
    PLANS = []
    PLANS_LOCK = threading.Lock()
    PLANS_THREAD = None
    PLANS_THREAD_RUNNING = False

    @staticmethod
    def len():
        with ScheduledPlanPool.PLANS_LOCK:
            return len(ScheduledPlanPool.PLANS)


    @staticmethod
    def get(idx:int):
        with ScheduledPlanPool.PLANS_LOCK:
            if idx < 0 or idx >= len(ScheduledPlanPool.PLANS):
                return (None, None)
            return ScheduledPlanPool.PLANS[idx]

    @staticmethod
    def check_thread():
        with ScheduledPlanPool.PLANS_LOCK:
            if not ScheduledPlanPool.PLANS_THREAD_RUNNING:
                ScheduledPlanPool.PLANS_THREAD_RUNNING = True
                ScheduledPlanPool.PLANS_THREAD = threading.Thread(target=ScheduledPlanPool.runner)
                ScheduledPlanPool.PLANS_THREAD.daemon = True  # Make thread daemon so it exits when main exits
                ScheduledPlanPool.PLANS_THREAD.start()

    @staticmethod
    def runner():
        while not _is_shutdown_requested():
            d = dt.datetime.now()
            for idx in range(ScheduledPlanPool.len()):
                plan, func = ScheduledPlanPool.get(idx)
                if plan is not None and plan.can_run(d):
                    logger.debug(f'Trigger event at: {d}')
                    t = threading.Thread(target=func, args=(plan, d,))
                    t.daemon = True  # Make thread daemon so it exits when main exits
                    t.start()
            time.sleep(ScheduledPlan.g_period)
        
        # Mark thread as not running when exiting
        with ScheduledPlanPool.PLANS_LOCK:
            ScheduledPlanPool.PLANS_THREAD_RUNNING = False
        logger.info('ScheduledPlanPool runner shutdown completed gracefully.')

def run_async_plan(plan: ScheduledPlan, func:callable):
    if is_test_mode():
        print('Subprocess mode detected, scheduler will not be started.')
        return

    ScheduledPlanPool.check_thread()

    with ScheduledPlanPool.PLANS_LOCK:
        ScheduledPlanPool.PLANS.append((plan, func))


#
# Creating decorator for function, that is called in scheduled times
# Automatically starts scheduler in the background
#
def ScheduledRun(script=None, minute=None, hour=None, day=None, month=None,
                 year=None, weekday=None, yearday=None):
    def decorator(func):
        def wrapper(scheduler, current_time):
            return func(scheduler, current_time)
        if not is_test_mode():
            if script is not None:
                plan = ScheduledPlan("plan")
                plan.analyze(script)
                run_async_plan(plan, func)
            else:
                s = SchedulerConfig(minute=minute, hour=hour,
                                    weekday=weekday, yearday=yearday,
                                    day=day, month=month, year=year)
                s.run_async(func)
            time.sleep(1)
        return wrapper
    return decorator

def is_shutdown_requested():
    """
    Public function to check if shutdown has been requested.
    
    Returns:
        bool: True if shutdown has been requested, False otherwise.
    """
    return _is_shutdown_requested()

