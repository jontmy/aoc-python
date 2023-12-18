import os
import requests
from dotenv import load_dotenv


def aoc(year, day):
    load_dotenv()
    token = os.getenv('SESSION_TOKEN')
    filename = f'{year}/{day:02d}.in'
    url = f'https://adventofcode.com/{year}/day/{day}/input'

    if not token and not os.path.isfile(filename):
        raise Exception(f'SESSION_TOKEN not found in .env file and manual input in {filename} not found.')

    curr = ""
    if os.path.isfile(filename):
        with open(filename) as f:
            curr = f.read().strip()

    if curr and not curr.startswith("Please don't repeatedly request this endpoint before it unlocks!"):
        return curr

    req = requests.get(url, cookies={'session': token}, headers={
        'User-Agent': "https://github.com/jontmy/aoc-python/blob/master/utils/input.py by jontmy"})
    curr = req.text.strip()
    with open(filename, 'w') as f:
        f.write(curr)
    return curr
