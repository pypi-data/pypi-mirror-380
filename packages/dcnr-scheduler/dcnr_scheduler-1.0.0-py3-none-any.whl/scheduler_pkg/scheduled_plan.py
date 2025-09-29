
from datetime import datetime, timedelta
from typing import List
import time


class ScheduledPlanError(RuntimeError):
    pass


class EventPatterns:
    APPLY_INCLUDE = 1
    APPLY_EXCLUDE = 2

    def __init__(self):
        self.apply_type = EventPatterns.APPLY_INCLUDE
        self.hours = []
        self.days = []

    def contains_data(self):
        if len(self.hours)==0 and len(self.days)==0:
            return False
        if len(self.hours)==0:
            self.hours = [a for a in range(24)]
        if len(self.days)==0:
            self.days = [a for a in range(7)]
        return True


class ScheduledPlan():
    WEEKDAYS = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
    g_last_runs = {}
    g_period = 60  # seconds

    @staticmethod
    def to_int(p, default):
        try:
            hr = int(p)
            return hr
        except Exception:
            return default
        
    @staticmethod
    def set_period(seconds:int):
        periond = ScheduledPlan.to_int(seconds, 60)
        if periond < 10:
            periond = 10
        if period > 3600:
            period = 3600
        ScheduledPlan.g_period = periond
            
    def __init__(self, name):
        self.name = name
        self.clear_map()
        # minimum number of seconds from last run
        self.maxtime_from_last = 3600
        self.no_hours = True
        self.last_run = 0

    def clear_map(self):
        self._map = [[False]*24 for _ in range(7)]
        self.no_hours = True

    def produce_array_range(self, start, end, modulo):
        counter = 0
        arr = []
        start = start % modulo
        end = end % modulo
        while counter < modulo:
            arr.append(start)
            if start == end:
                break
            start = (start + 1) % modulo
            counter += 1
        return arr

    def find_weekday(self, p):
        def find_by_name(name):
            for idx,wd in enumerate(ScheduledPlan.WEEKDAYS):
                if name.startswith(wd):
                    return idx
            return None
        if p in ['*', 'everyday']:
            return [a for a in range(7)]
        if '-' in p:
            range_days = p.split('-')
            if len(range_days) != 2:
                raise ScheduledPlanError('Range in weekdays has to contain only two values joined by dash char.')
            idx1 = find_by_name(range_days[0])
            idx2 = find_by_name(range_days[1])
            if idx1 is not None and idx2 is not None:
                return self.produce_array_range(idx1, idx2, 7)
            else:
                raise ScheduledPlanError(f'Cannot be interpreted as weeday range: {p}')

        idx = find_by_name(p)
        if idx is not None:
            return [idx]
        return []

    def find_hour(self, p):
        if p in ['*', 'every']:
            return [a for a in range(24)]
        if '-' in p:
            range_hours = p.split('-')
            if len(range_hours) != 2:
                raise ScheduledPlanError('Range in hours has to contain only two values joined by dash char.')
            idx1 = ScheduledPlan.to_int(range_hours[0], 0)
            idx2 = ScheduledPlan.to_int(range_hours[1], 23)
            return self.produce_array_range(idx1, idx2, 24)
        hr = ScheduledPlan.to_int(p, None)
        if hr is not None:
            return [hr]
        return []

    def _copy_to_map(self, inc:EventPatterns):
        value = (inc.apply_type == EventPatterns.APPLY_INCLUDE)
        for d in inc.days:
            for h in inc.hours:
                self.no_hours = False
                self._map[d][h] = value

    def _get_scripts(self, text) -> List[EventPatterns]:
        data = []
        mode = 0
        paths = text.lower().split(',')
        for path in paths:
            print(f'Parsing path: "{path}"')
            curr = EventPatterns()
            data.append(curr)
            for p in [a for a in path.split(' ') if len(a)>0]:
                if p.startswith('excl'):
                    curr.apply_type = EventPatterns.APPLY_EXCLUDE
                elif p.startswith('incl'):
                    curr.apply_type = EventPatterns.APPLY_INCLUDE
                elif p == 'on':
                    mode = 1
                elif p == 'at':
                    mode = 2
                elif p == 'freq':
                    mode = 3
                elif mode == 3:
                    mode = 0
                    self.set_frequency(p)
                elif mode == 1:
                    wd = self.find_weekday(p)
                    curr.days.extend(wd)
                elif mode == 2:
                    hr = self.find_hour(p)
                    curr.hours.extend(hr)
        return data

    def set_frequency(self, text):
        lengths = {
            'hour': 60*60,
            'day': 24*60*60,
            'week': 7*24*60*60
        }
        if text is None or not isinstance(text,str):
            raise ScheduledPlanError(f'Input for set_frequency has to be string')
        format_error = 'Argument for frequency has to be <number>/<interval>, where "number" is integer value and "interval" is from "hour", "day", "week".'
        p = text.split('/')
        if len(p)!=2:
            raise ScheduledPlanError(format_error)
        number = ScheduledPlan.to_int(p[0],-1)
        interval = p[1].lower()
        if interval not in ['day', 'hour', 'week']:
            raise ScheduledPlanError(format_error)
        if number < 1 or number > lengths[interval]:
            raise ScheduledPlanError(f'Number has to be from range <1,{lengths[interval]}) for interval "{interval}".')
        self.maxtime_from_last = int(lengths[interval]/number)
        


    def analyze(self, text):
        self.clear_map()
        data = self._get_scripts(text)
        for inc in data:
            if not inc.contains_data():
                continue
            self._copy_to_map(inc)

    def can_run(self, current:datetime):
        weekday = current.weekday()
        hour = current.hour

        if self.no_hours:
            hour_is_suitable = (self.maxtime_from_last is not None)
        else:
            hour_is_suitable = self._map[weekday][hour]

        if not hour_is_suitable:
            return False

        # if we are interested in frequency and have all info available
        if self.maxtime_from_last is not None and self.last_run is not None:
            # if last run was less than allowed time frame, do not allow
            from_last = current.timestamp() - self.last_run
            if from_last < self.maxtime_from_last:
                return False

        self.last_run = current.timestamp()
        return True
        

    def format_map(self):
        s = ''
        for day in self._map:
            for h in day:
                if h:
                    s += 'x'
                else:
                    s += '-'
            s += '\n'
        return s

if __name__=='__main__':
    tp = ScheduledPlan('plan1')
    tp.analyze('at 3 4 5 on mon tue fri sun, at 6 7 on tue, exclude at 4 on tue')
    print(tp.format_map())

    tp.analyze('on mon tu we fr th')
    print(tp.format_map())

    tp.analyze('at 9 10 on mon-fr, at 11 on sa su')
    print(tp.format_map())