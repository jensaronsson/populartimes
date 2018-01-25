from libs.populartimes.populartimes.crawler import get_current_popular_times
import os
import json

k25 = get_current_popular_times(
    "AIzaSyCMlnoa1GquJw61Ybe11uq097YV5mIdMQk", "ChIJizx2Bl2dX0YR_p7fUA7zm1o")

# postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
response.write(str(k25))
response.close()
