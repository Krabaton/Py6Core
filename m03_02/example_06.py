def to_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):
    # 60s -> 1m, 60m - 1h, 24h - 1d, 7d - 1w
    number_seconds_in_minute = 60
    number_seconds_in_hour = 60 * number_seconds_in_minute
    number_seconds_in_day = 24 * number_seconds_in_hour
    number_seconds_in_week = 7 * number_seconds_in_day

    result = seconds + minutes * number_seconds_in_minute + \
        hours * number_seconds_in_hour + \
        days * number_seconds_in_day + \
        weeks * number_seconds_in_week

    return result


print(to_seconds(minutes=5, days=1))
print(to_seconds(minutes=10, days=1, weeks=12))
