import requests
import random

job_data_id = random.randrange(1,10000)

print(job_data_id)

data = [
  ('project', 'customcrawler'),
  ('spider', 'toscrapespiderax'),
  ('setting', 'CLOSESPIDER_PAGECOUNT=100'),
  ('setting', 'CLOSESPIDER_TIMEOUT=60'),
  ('job_data_id', job_data_id),
  ('url', 'https://lovdata.no/')
]

response = requests.post('http://0.0.0.0:6800/schedule.json', data=data)

print(response.json())
