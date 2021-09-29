from acamenySchedule import AcademyAssistant

import time

import datetime

def getCourseTime():
    courses = []

    course = ("서양기독교사", [])
    course[1].append((0, datetime.time(hour=12, minute=0), datetime.time(hour=13, minute=15)))
    course[1].append((2, datetime.time(hour=12, minute=0), datetime.time(hour=13, minute=15)))
    courses.append(course)


    course = ("재무관리", [])
    course[1].append((0, datetime.time(hour=14, minute=0), datetime.time(hour=15, minute=15)))
    course[1].append((2, datetime.time(hour=14, minute=0), datetime.time(hour=15, minute=15)))
    courses.append(course)


    course = ("회귀분석", [])
    course[1].append((0, datetime.time(hour=15, minute=30), datetime.time(hour=16, minute=45)))
    course[1].append((2, datetime.time(hour=15, minute=30), datetime.time(hour=16, minute=45)))
    courses.append(course)


    course = ("경제원론2", [])
    course[1].append((0, datetime.time(hour=17, minute=0), datetime.time(hour=18, minute=15)))
    course[1].append((2, datetime.time(hour=17, minute=7), datetime.time(hour=18, minute=15)))
    courses.append(course)


    course = ("확률론입문", [])
    course[1].append((1, datetime.time(hour=9, minute=0), datetime.time(hour=10, minute=15)))
    course[1].append((3, datetime.time(hour=9, minute=0), datetime.time(hour=10, minute=15)))
    courses.append(course)


    course = ("데이터베이스", [])
    course[1].append((1, datetime.time(hour=10, minute=30), datetime.time(hour=11, minute=45)))
    course[1].append((3, datetime.time(hour=10, minute=30), datetime.time(hour=11, minute=45)))
    courses.append(course)

    return courses


def main () :
    courses = getCourseTime()
    day = datetime.datetime.today().weekday()

    bot = AcademyAssistant("학업", 31, '3개월만 버티자')

    while True : 
        now = datetime.datetime.now()
        nowHour = now.hour
        nowMinute = now.minute

        nowAfter = now + datetime.timedelta(minutes=5)
        nowAfterHour = nowAfter.hour
        nowAfterMinute = nowAfter.minute

        for course in courses:
            for courseTime in course[1]:
                if courseTime[0] == day:

                    if courseTime[1].hour == nowHour and courseTime[1].minute == nowMinute:
                        bot.post_message(course[0], True, True)

                    elif courseTime[2].hour == nowHour and courseTime[2].minute == nowMinute:
                        bot.post_message(course[0], False, True)

                    elif courseTime[1].hour == nowAfterHour and courseTime[1].minute == nowAfterMinute:
                        bot.post_message(course[0], True, False)

                    elif courseTime[2].hour == nowAfterHour and courseTime[2].minute == nowAfterMinute:
                        bot.post_message(course[0], False, False)

        time.sleep(60)



if __name__ == "__main__" :
    main()