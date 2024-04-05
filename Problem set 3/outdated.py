months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

while True:
    date = input('Date: ')

    if '/' in date:
        month1, date1, year1 = date.split('/')
        if month1.isdigit() and date1.isdigit() and year1.isdigit():
            month = int(month1)
            date = int(date1)
            year = int(year1)
            if 1 <= month <= 12 and 1 <= date <= 31:
                print(f'{year}-{month:02}-{date:02}')
                break

            else:
                continue

        else:
            continue


    elif ',' in date:
        month2, date2, year2 = date.replace(',','').split(' ')
        if date2.isdigit() and month2.isalpha():
            bulan = month2.title()
            day = int(date2)
            tahun = int(year2)
            if bulan in months and 1 <= day <= 31:
                real_bulan = months[bulan]
                print(f'{tahun}-{real_bulan:02}-{day:02}')
                break

            else:
                continue

        else:
            continue
