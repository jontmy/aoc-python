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

    if not os.path.isfile(filename):
        req = requests.get(url, cookies={'session': token}, headers={
            'User-Agent': "https://github.com/jontmy/aoc-python/blob/master/utils/input.py by jontmy"})
        text = req.text.strip()
        with open(filename, 'w') as f:
            f.write(text)
        return text

    with open(filename) as f:
        return f.read().strip()
