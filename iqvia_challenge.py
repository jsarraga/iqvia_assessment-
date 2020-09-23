import feedparser
import time
import calendar
from datetime import datetime, timedelta 
from pprint import pprint

"""
Task: Given a tuple of Disease and RSS feeds, determine which disease had no
activity for a given number of days. 

I assumed the given input is a list of tuples (disease, rss feed).
I then made a function to see if the feed had activity within the last 2 days.
If the feed had recent activity, I returned True, else, returned False.
If the feed had no activity in the last two days, I returned the corresponding tuple.
"""

# given rss feed urls
url1 = "https://clinicaltrials.gov/ct2/results/rss.xml?cond=Wolman+Disease&amp;sfpd_s=09%2F09%2F2020&amp;sfpd_d=14&amp;count=1000&amp;sel_rss=new14"
url2 = "https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d=14&lup_d=&sel_rss=new14&cond=Alzheimer+Disease&count=10000"

my_tuples = [('Wolman', url1), ('Alzheimer', url2)]

def recent_activity(url):
    data = feedparser.parse(url)    
    to_send = []
    # iterate through rss feeds entries
    for i in data.entries:
        time_struct_now = time.localtime()
        # convert to the current time to seconds
        time_now_in_seconds = calendar.timegm(time_struct_now)
        # find the time of published entry in seconds
        published_entries_in_seconds = calendar.timegm(i.published_parsed)
        # if entry is within the last 2 days, append to to_send
        if time_now_in_seconds - published_entries_in_seconds < (86400 * 2):
            to_send.append(i)
        
    if len(to_send) != 0:
        return True
    else:
        return False

def no_activity(alist):
    output = []
    # get to each url within tuple
    for i in my_tuples:
        if recent_activity(i[1]) == False:
            output.append(i)
    return output


activity(my_tuples)