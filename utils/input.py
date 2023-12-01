def aoc(year, day):
    with open(f'{year}/{day:02d}.in') as f:
        return f.read().strip()
