from requesters import Requester
from helpers import SimpleFormatter


requester_latest = Requester(
    'https://api.spacexdata.com/v3/launches/latest'
)

requester_next = Requester(
    'https://api.spacexdata.com/v3/launches/next'
)

requester_upcoming = Requester(
    'https://api.spacexdata.com/v3/launches/upcoming'
)


requester_past = Requester(
    'https://api.spacexdata.com/v3/launches/past'
)
