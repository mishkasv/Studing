import datetime,calendar
today = datetime.date.today()
cal_year = calendar.Calendar().yeardatescalendar(2020)+calendar.Calendar().yeardatescalendar(2021)
weeks = []
months=[]
days = dict()
stop=False
for sq in cal_year:
    for m in sq:
        currentmonth=m[2][1].month
        one_month = dict()
        for w in m:
            if w not in weeks:
                cw=dict()
                for d in w:
                    if d>datetime.date(2020,8,3):
                        cw[d.strftime('%Y-%m-%d')]=0
                        days[d.strftime('%Y-%m-%d')]=0
                        if d.month==currentmonth:
                            one_month[d.strftime('%Y-%m-%d')]=0
                        if d==today:
                            stop=True
                            break
            weeks.append(cw) if cw!={} else None
            if stop:
                break
        months.append(one_month) if one_month!={} else None
        if stop:
            break
    if stop:
        break
key='weeks'
test_dict = {"2022":{},"2021":{"2021-08-29":3,"2021-08-22":1,"2021-08-24":2,"2021-08-26":6},"2020":{"2020-08-29":3,"2020-08-22":1,"2020-08-24":2,"2020-08-26":6}}
test_dict2 = {'2021':{'2021-08-21':3,'2021-08-22':1,'2021-08-24':2,'2021-08-26':6}}
test_dict3={'2023':{}}
test_dict4 = {'2020':{'2020-10-21':3,'2020-11-22':1,'2020-12-24':2,'2020-09-26':6}}
list_car = [test_dict,test_dict2,test_dict4,test_dict3]
car_d= dict()
car_d['car1']=test_dict
car_d['car2']=test_dict2
car_d['car3']=test_dict3
car_d['car4']=test_dict4

for car,data_car in car_d.items():
    for y,data in data_car.items():
        if key=='months':
            for month in months:
                if any(day in data for day,_ in month.items()):
                    for day_v,_ in month.items():
                        if day_v in data:
                            month[day_v]+=data[day_v]
        if key=='weeks':
            for week in weeks:
                if any(day in data for day,_ in week.items()):
                    for day_v,_ in week.items():
                        if day_v in data:
                            week[day_v]+=data[day_v]
        if key == 'days':
            for d,v in data.items():
                if d in days:
                    days[d]+=v
if key=='weeks':
    week_results =[]
    for week in weeks:
        week_results.append({f'{sorted(list(week.keys()))[0]}-{sorted(list(week.keys()))[-1]}':f'views {sum(week.values())}'})

if key=='months':
    month_results =[]
    for month in months:
        month_results.append({datetime.datetime.strptime(month.popitem()[0],'%Y-%m-%d').strftime('%B-%Y'):f'views {sum(month.values())}'})

if key=='days':
    day_results=[]
    for day,views in days.items():
        day_results.append({day:views})

a =sorted(list(test_dict.keys()))
start = sorted(test_dict[a[0]])
end = sorted(test_dict[a[-1]])
print(a)
r = set()
for car_view in list_car:
    r.update(set(car_view.keys()))
r = sorted(list(r))
start = today.strftime('%Y-%m-%d')
for car_view in list_car:
    if r[0] in car_view:
        if start > sorted(car_view[r[0]])[0]:
            start = sorted(car_view[r[0]])[0]
        if start==f'{r[0]}-01-01':
            break

print(start)

# print([sum(x.values()) for x in weeks])
# print(days.values())
# print([sum(x.values()) for x in months])