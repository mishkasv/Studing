import datetime, calendar

today = datetime.date.today()

def get_start_end_statistic_detail(view_statistic_one_car):
    view_years = sorted(list(view_statistic_one_car.keys()))
    start = sorted(view_statistic_one_car[view_years[0]])[0]
    return start, view_years

def get_start_end_statistic_list(view_statistic_many_cars):
    year_set=set()
    for car_view in view_statistic_many_cars:
        year_set.update(set(car_view.keys()))
    year_list = sorted(list(year_set))
    start = today.strftime('%Y-%m-%d')
    for car_view in view_statistic_many_cars:
        if year_list[0] in car_view:
            if start > sorted(car_view[year_list[0]])[0]:
                start = sorted(car_view[year_list[0]])[0]
            if start == f'{year_list[0]}-01-01':
                break
    return start, year_list


def get_calendar(start, year_list, sort):
    calendar_years = []
    for year in year_list:
        calendar_years += calendar.Calendar().yeardatescalendar(int(year))
    weeks = []
    months = []
    days = dict()
    stop = False
    for sq in calendar_years:
        for m in sq:
            if sort == 'months':
                currentmonth = m[2][1].month
                one_month = dict()
            for w in m:
                if w not in weeks:
                    if sort == 'weeks':
                        cw = dict()
                    for d in w:
                        if d >= datetime.datetime.strptime(start, '%Y-%m-%d').date():
                            if sort == 'weeks':
                                cw[d.strftime('%Y-%m-%d')] = 0
                            if sort == 'days':
                                days[d.strftime('%Y-%m-%d')] = 0
                            if sort == 'months':
                                if d.month == currentmonth:
                                    one_month[d.strftime('%Y-%m-%d')] = 0
                            if d == today:
                                stop = True
                                break
                if sort == 'weeks':
                    weeks.append(cw) if cw != {} else None
                if stop:
                    break
            if sort == 'months':
                months.append(one_month) if one_month != {} else None
            if stop:
                break
        if stop:
            break
    if sort == 'months':
        return months
    if sort == 'weeks':
        return weeks
    if sort == 'days':
        return days

def get_list_satistic_from_calendar(car_d,sort,calend):
    for data_car in car_d:
        for y, data in data_car.items():
            if sort == 'months':
                for month in calend:
                    if any(day in data for day, _ in month.items()):
                        for day_v, _ in month.items():
                            if day_v in data:
                                month[day_v] += data[day_v]
            if sort == 'weeks':
                for week in calend:
                    if any(day in data for day, _ in week.items()):
                        for day_v, _ in week.items():
                            if day_v in data:
                                week[day_v] += data[day_v]
            if sort == 'days':
                for d, v in data.items():
                    if d in calend:
                        calend[d] += v
    if sort == 'weeks':
        week_results = []
        for week in calend:
            week_results.append(
                {f'{sorted(list(week.keys()))[0]}-{sorted(list(week.keys()))[-1]}': f'views {sum(week.values())}'})
        return week_results
    if sort == 'months':
        month_results = []
        for month in calend:
            month_results.append({datetime.datetime.strptime(month.popitem()[0], '%Y-%m-%d').strftime(
                '%B-%Y'): f'views {sum(month.values())}'})
        return month_results

    if sort == 'days':
        day_results = []
        for day, views in calend.items():
            day_results.append({day: views})
        return day_results

def get_list_of_statistic_detail(row_dict_statistic, sort):
    start,year_list = get_start_end_statistic_detail(row_dict_statistic)
    result_calendar = get_calendar(start,year_list,sort)
    list_of_statistic = get_list_satistic_from_calendar([row_dict_statistic],sort,result_calendar)
    return list_of_statistic

def get_list_of_statistic_list(row_list_of_dict_statistic, sort):
    start, year_list = get_start_end_statistic_list(row_list_of_dict_statistic)
    result_calendar = get_calendar(start,year_list,sort)
    list_of_statistic = get_list_satistic_from_calendar(row_list_of_dict_statistic,sort,result_calendar)
    return list_of_statistic

