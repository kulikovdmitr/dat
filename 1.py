from datetime import timedelta, datetime

now = datetime.now()
print("--------------------------------------------")
print("Сегодня :|", now)
print("--------------------------------------------")

days61 = timedelta(61)
in_days61 = now + days61
print("За 61 день до окончания :|", in_days61)
create61 = timedelta(365)
in_create61 = in_days61 - create61
print ("Дата создания данного сертификата(61)|:", in_create61)

print("--------------------------------------------")

days60 = timedelta(60)
in_days60 = now + days60
print("За 60 дней до окончания :|", in_days60)
create = timedelta(365)
in_create = in_days60 - create
print ("Дата создания данного сертификата(60)|:", in_create)

print("--------------------------------------------")

days30 = timedelta(30)
in_days30 = now + days30
print("За 30 дней до окончания :|", in_days30)
create30 = timedelta(365)
in_create30 = in_days30 - create30
print ("Дата создания данного сертификата(30)|:", in_create30)

print("--------------------------------------------")

dayspr15 = timedelta(15)
in_daysp15 = now - dayspr15
print("Просрочка 15 дней :|", in_daysp15)
createp15 = timedelta(365)
in_createp15 = in_daysp15 - createp15
print ("Дата создания данного сертификата(просрочка 15)|:", in_createp15)

print("--------------------------------------------")

dayspr30 = timedelta(30)
in_daysp30 = now - dayspr30
print("Просрочка 30 дней :|", in_daysp30)
createp30 = timedelta(365)
in_createp30 = in_daysp30 - createp30
print ("Дата создания данного сертификата(просрочка 30)|:", in_createp30)

print("--------------------------------------------")

dayspr31 = timedelta(31)
in_daysp31 = now - dayspr31
print("Просрочка 31 день :|", in_daysp31)
createp31 = timedelta(365)
in_createp31 = in_daysp31 - createp31
print ("Дата создания данного сертификата(просрочка 30)|:", in_createp31)

print("--------------------------------------------")

dayspr60 = timedelta(60)
in_daysp60 = now - dayspr60
print("Просрочка 60 дней :|", in_daysp60)
createp60 = timedelta(365)
in_createp60 = in_daysp60 - createp60
print ("Дата создания данного сертификата(просрочка 60)|:", in_createp60)

print("--------------------------------------------")
