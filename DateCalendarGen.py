def set(): #1
	month = int(input("Month: ")) #ask the user what their date is
	day = int(input("Day: "))
	year = int(input("Year: "))
	set_year(month, day, year)
def set_year(month, day, year): #2
	yearo = year
	if year >= 1400 and year < 1500:         # figures out the year in order to set a century code needed for calculations
		century = 5
		year = year - 1400                     #set year to just last two digits
		get_index(month, day, year, century, yearo)
	elif year >= 1500 and year < 1600:
		century = 3
		year = year - 1500
		get_index(month, day, year, century, yearo)

	elif year >= 1600 and year < 1700:
		century = 2
		year = year - 1600
		get_index(month, day, year, century, yearo)

	elif year >= 1700 and year < 1800:
		century = 0
		year = year - 1700
		get_index(month, day, year, century, yearo)

	elif year >= 1800 and year < 1900:
		century = 5
		year = year - 1800
		get_index(month, day, year, century, yearo)

	elif year >= 1900 and year < 2000:
		century = 3
		year = year - 1900
		get_index(month, day, year, century, yearo)

	elif year >= 2000 and year < 2100:
		century = 2
		year = year - 2000
		get_index(month, day, year, century, yearo)

	elif year >= 2100 and year < 2200:
		century = 0
		year = year - 2100
		get_index(month, day, year, century, yearo)

	elif year >= 2200 and year < 2300:
		century = 5
		year = year - 2200
		get_index(month, day, year, century, yearo)

	elif year >= 2300 and year < 2400:
		century = 3
		year = year - 2300
		get_index(month, day, year, century, yearo)

	elif year >= 2400 and year < 2500:
		century = 2
		year = year - 2400
		get_index(month, day, year, century, yearo)

	elif year >= 2500 and year < 2600:
		century = 0
		year = year - 2500
		get_index(month, day, year, century, yearo)

	elif year >= 2600 and year < 2700:
		century = 5
		year = year - 2600
		get_index(month, day, year, century, yearo)
	else:
		print("Error!")
		print("Try Again") # if year is invalid
		set()
def get_index(month, day, year, century, yearo): #3
	year_temp = year
	index = 0
	while year_temp >= 12: #how many times the year goes into 12
		year_temp -= 12
		index += 1
	middle = 0
	middle = year - (index * 12)
	ring = 0
	middle_temp = middle
	while middle_temp >= 4:
		middle_temp -= 4
		ring += 1
	doomsweekday = (century + index + middle + ring) % 7
	get_month(month, day, year, century, index, middle, ring, doomsweekday,
	          yearo)
def get_month(month, day, year, century, index, middle, ring, doomsweekday,yearo): #7
	if (month == 1 and day <= 31):
		if yearo % 4 == 0:
			doomsday = 4
		else:
			doomsday = 3
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 2 and day <= 29:
		if yearo % 4 == 0:
			doomsday = 29
			calc_weekday(month, day, yearo, doomsweekday, doomsday)
		else:
			if day <= 28:
				doomsday = 28
				calc_weekday(month, day, yearo, doomsweekday, doomsday)
			else:
				set()
	elif month == 3 and day <= 31:
		doomsday = 14
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 4 and day <= 30:
		doomsday = 4
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 5 and day <= 31:
		doomsday = 9
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 6 and day <= 30:
		doomsday = 6
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 7 and day <= 31:
		doomsday = 11
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 8 and day <= 31:
		doomsday = 8
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 9 and day <= 30:
		doomsday = 5
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 10 and day <= 31:
		doomsday = 10
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 11 and day <= 30:
		doomsday = 7
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	elif month == 12 and day <= 31:
		doomsday = 12
		calc_weekday(month, day, yearo, doomsweekday, doomsday)
	else:
		print("Error!")
		print("Try Again")
		set()
def calc_weekday(month, day, yearo, doomsweekday, doomsday): #7
	if day >= doomsday:
	  weekday = ((day - doomsday) +doomsweekday) %7
	else:
	  weekday = (doomsweekday - (doomsday - day)) %7
	print(month, "/", day, "/", yearo, "is a ")
	if weekday == 0:
		print("\033[1;32;40mSunday  \n")
	elif weekday == 1:
		print("\033[1;31;40mMonday  \n")
	elif weekday == 2:
		print("\033[1;34;40mTuesday  \n")
	elif weekday == 3:
		print("\033[1;35;40mWednesday  \n")
	elif weekday == 4:
		print("\033[1;36;40mThursday  \n")
	elif weekday == 5:
		print("\033[1;33;50mFriday  \n")
	elif weekday == 6:
		print("\033[1;37;40mSaturday  \n")
	if month == 1:
		legnth = 31     # identify the legnth of the month in order to create a calender of the correct legnth
	elif month == 2:
		if yearo % 4 == 0:
			legnth = 29
		else:
			legnth = 28
	elif month == 3:
		legnth = 31
	elif month == 4:
		legnth = 3
	elif month == 5:
		legnth = 31
	elif month == 6:
		legnth = 30
	elif month == 7:
		legnth = 31
	elif month == 8:
		legnth = 31
	elif month == 9:
		legnth = 30
	elif month == 10:
		legnth = 31
	elif month == 11:
		legnth = 30
	elif month == 12:
		legnth = 31
	firstday = (doomsweekday - (doomsday - 1)) %7       # get day of week for first day of month in order to have a basis to choose the correct calender
	df=pd.read_csv("Calender.csv")                      #read an excel file in order to recieve data about the calender
	monthw = ""
	if month == 1:
		monthw = "JAN"
	elif month == 2:
		monthw = "FEB"
	elif month == 3:            # label the month on the calender
		monthw =  "MAR"
	elif month == 4:
		monthw = "APR"
	elif month == 5:
		monthw = "MAY"
	elif month == 6:
		monthw = "JUN"
	elif month == 7:
		monthw = "JUL"
	elif month == 8:
		monthw = "AUG"
	elif month == 9:
		monthw = "SEPT"
	elif month == 10:
		monthw = "OCT"
	elif month == 11:
		monthw = "NOV"
	elif month == 12:
		monthw = " DEC"
	df.rename(columns={'MONTH': monthw, 'YEAR': yearo}, inplace=True) #replace month and year on calender
	print("    ______________________________________")
	if firstday == 0:
		if legnth == 31:
			print(df.iloc[[0, 1, 2, 3, 4, 5]]) # choose the correct set of values to create a calender that is equal in legnth to the month and also starts on the correct day
		elif legnth == 30:
			print(df.iloc[[0, 1, 2, 3, 4, 38]])
		elif legnth == 28:
			print(df.iloc[[0, 1, 2, 3, 4]])
		else:
			print(df.iloc[[0, 1, 2, 3, 4, 39]])
	elif firstday == 1:
		if legnth == 31:
			print(df.iloc[[0, 6, 7, 8, 9, 10]])
		elif legnth == 30:
			print(df.iloc[[0, 6, 7, 8, 9, 40]])
		elif legnth == 28:
			print(df.iloc[[0, 6, 7, 8, 9, 41]])
		else:
		  print(df.iloc[[0,6,7,8,9,42]])
	elif firstday == 2:
		if legnth == 31:
			print(df.iloc[[0, 11, 12, 13, 14, 15]])
		elif legnth == 30:
			print(df.iloc[[0, 11, 12, 13, 14, 43]])
		elif legnth == 28:
			print(df.iloc[[0, 11, 12, 13, 14, 44]])
		else:
			print(df.iloc[[0, 11, 12, 13, 14, 45]])
	elif firstday == 3:
		if legnth == 31:
			print(df.iloc[[0, 16, 17, 18, 19, 20]])
		elif legnth == 30:
			print(df.iloc[[0, 16, 17, 18, 19, 46]])
		elif legnth == 28:
			print(df.iloc[[0, 16, 17, 18, 19, 47]])
		else:
			print(df.iloc[[0, 16, 17, 18, 19, 48]])
	elif firstday == 4:
		if legnth == 31:
			print(df.iloc[[0, 21, 22, 23, 24, 25]])
		elif legnth == 30:
			print(df.iloc[[0, 21, 22, 23, 24, 49]])
		elif legnth == 28:
			print(df.iloc[[0, 21, 22, 23, 24, 50]])
		else:
			print(df.iloc[[0, 21, 22, 23, 24, 51]])
	elif firstday == 5:
		if legnth == 31:
			print(df.iloc[[0, 26, 27, 28, 29, 30, 31]])
		elif legnth == 30:
			print(df.iloc[[0, 26, 27, 28, 29, 30]])
		elif legnth == 28:
			print(df.iloc[[0, 26, 27, 28, 29, 52]])
		else:
			print(df.iloc[[0, 26, 27, 28, 29, 53]])
	elif firstday == 6:
		if legnth == 31:
			print(df.iloc[[0, 32, 33, 34, 35, 36, 37]])
		elif legnth == 30:
			print(df.iloc[[0, 32, 33, 34, 35, 36, 54]])
		elif legnth == 28:
			print(df.iloc[[0, 32, 33, 34, 35, 55]])
		else:
			print(df.iloc[[0, 32, 33, 34, 35, 56]])
	print("   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
import pandas as pd
while True:
  set()
