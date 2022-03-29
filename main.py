import csv
import snscrape.modules.twitter as sntwitter

from datetime import datetime, timedelta
dateFrom = datetime.now()
dateFrom = dateFrom.strftime('%Y-%m-%d')
dateTo = datetime.now() + timedelta(days = 1)
dateTo = dateTo.strftime('%Y-%m-%d')

print("-------------------Welcome to NTP Twitter Scraper-------------------")
keyword = input("Please enter keyword for search query: ")
maxTweets = int(input("Scrape how many tweets?: "))
isCustomDate = input("Custom Date? (y for yes, n for no): ");

if isCustomDate == "y":
    # formatting dateFrom
    dateString1 = input("Please enter starting date (\"YYYY/MM/DD\"):")
    dateFrom = datetime.strptime(dateString1,"%Y/%m/%d").date()
    dateFrom = dateFrom.strftime('%Y-%m-%d')
    # formatting dateTo
    dateString2 = input("Please enter ending date (\"YYYY/MM/DD\"):")
    dateTo = datetime.strptime(dateString2, "%Y/%m/%d").date()
    dateTo = dateTo.strftime('%Y-%m-%d')

elif isCustomDate =="n":
    dateTo = dateTo
    dateFrom = dateFrom

else:
    print("Invalid entry, closing program")
    quit()

#Open/create a file to append data to
mainFileResponse = input("Enter into main log?")
isMainFile = False
if mainFileResponse == "y":
    isMainFile = True
    csvFile = open('Logs\mainLog.csv', 'a', newline='', encoding='utf8')
    csvFile.truncate()
else:
    isMainFile = False
    csvFile = open('Logs\\' + keyword + dateFrom + '.csv', 'a', newline='', encoding='utf8')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Tweet ID", "Date", "Tweet", "User Location", "Media Link",])
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:en since:' +  dateFrom + ' until:' + dateTo).get_items()):
    if i > maxTweets:
        break
    csvWriter.writerow([tweet.id, tweet.date, tweet.content, tweet.user.location,])
csvFile.close()


