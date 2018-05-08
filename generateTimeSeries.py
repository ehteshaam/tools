from datetime import datetime, timedelta

# Make a date object with today's date
abhi = datetime.today()

# Adjust it to have expected date
abhi = abhi.replace(year=2018, day=30, month=04, hour=06,minute=24,second=04, microsecond=000000)

# Confirm you got your date set correctly
print(abhi)

# Define a list for saving dates
finalTimes = list()

# Add your starting date to list
finalTimes.append(abhi)

# Subtract time periods from date for making a series
for i in range(1,261):
    abhi = abhi - timedelta(seconds=30)
    finalTimes.append(abhi)

# Reverse the generated time series
finalTimes.reverse()

print ("Going in reverse to correct order")

# Print time series
for item in finalTimes:
    print (item)
