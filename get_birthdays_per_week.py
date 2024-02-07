import datetime


def get_birthdays_per_week(users):
    list_name = []
    today = datetime.datetime.today().date()

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_name = birthday_this_year.strftime("%A")
            if day_name in ['Saturday', 'Sunday']:
                day_name = 'Monday'
            for dictionary in list_name:
                if day_name in dictionary:
                    dictionary[day_name] += name
                else:
                    dictionary[day_name] = name
    print(list_name)