time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
minutes_all = 0

time_parts = time_string.split(',')

for part in time_parts:
    minutes = 0
    units = part.strip().split()
    
    for unit in units:
        if 'h' in unit:
            hours = int(unit.replace('h', ''))
            minutes = (hours * 60) + minutes
        elif 'm' in unit:
            min = int(unit.replace('m', ''))
            minutes = min + minutes
        elif 's' in unit:
            seconds = int(unit.replace('s', ''))
            minutes = (seconds // 60) + minutes  

    minutes_all += minutes

print(f"Общее количество минут: {minutes_all}")