import datetime


dob = datetime.datetime(1986,6,5,22,30,00)
now = datetime.datetime.today()

print(now)
print(dob)

age = now - dob

age_in_sec = age.total_seconds()
age_in_days = age_in_sec/(60 * 60 *24)
age_in_years = age/365

print("Age in years : ",age_in_years)
print("Age in seconds : ",age_in_sec)
print("Age in days : ",age_in_days)