import urllib2
import urllib
import re
from bs4 import BeautifulSoup

day_names = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ]

def get_timetable_html(id):
    data = urllib.urlencode({ "T1": id })
    request = urllib2.Request("http://www.timetable.ul.ie/tt2.asp", data)
    response = urllib2.urlopen(request)
    return response.read()

def get_schedule(days):
    global day_names
    schedule = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": []
    }

    for idx in xrange(len(days)):
        day = days[idx]
        day_name = day_names[idx]
        classes = []
        for c in day.findAll("p"):
            if c.text.rstrip():
                c = re.sub('\r', '', c.text.rstrip())
                c = re.sub('\n', '', c)
                c = re.sub('\xa0', '', c)
                c = re.sub(' +', ' ', c)
                c = re.sub(' - ', '-', c)
                c = re.sub('LEC-', 'LEC ', c)
                classes.append(c)

        for _class in classes:
            info = _class.split()
            if len(info) == 4:
                module = info[1].split("-")
                type = module[1]
                type = type if type == "LEC" else type + "-" + module[2]
                schedule[day_name].append({
                    "time": info[0],
                    "module": module[0],
                    "type": type,
                    "location": info[2],
                    "duration": info[3]
                })

    return schedule

def get_student_timetable_json(id):
    try:
        html = get_timetable_html(id)
        soup = BeautifulSoup(html, "lxml")
        table = soup.find("table").findAll("tr")[1]
        days = table.findAll("td")
        data = {
            "status": "success",
            "data": get_schedule(days)
        }
        return data
    except:
        return {
          "status": "failed",
          "error": "Could not find user ID"
        }
