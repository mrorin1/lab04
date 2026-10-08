import sys

def parse_record(line: str) -> dict:
    city, temp_str, date = line.split(";")
    test_line = line.split(";")
    if len(test_line) != 3:
        raise ValueError(f"Введите 3 аргумента,вы ввели {len(test_line)}")
    if not city:
        raise ValueError(f"Введите город,вы ввели {city}")
    if not date:
        raise ValueError(f"Введите дату,вы ввели {date}")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура не число флоат ")
    return {"city": city, "temperature": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    rec = []
    for ln in lines:
        if not ln.strip():
            continue
        try:
            rec.append(parse_record(ln))
        except ValueError:
            continue
    return rec
def _mean_by_city(records: list[dict]) -> dict:
    total: dict[str, float] = {}
    count: dict[str, int] = {}
    for r in records:
        total[r["city"]] = total.get(r["city"], 0.0) + r["temperature"]
        count[r["city"]] = count.get(r["city"], 0) + 1
    return {city: total[city] / count[city] for city in total}

def average_by_city(records: list[dict]) -> dict:
    return {city: round(avg, 1) for city, avg in _mean_by_city(records).items()}


def warmest_city(records: list[dict]) -> str:
    means = _mean_by_city(records)
    if not means:
        raise ValueError("Нет записей")
    return min(means, key=lambda city: (-means[city], city))
