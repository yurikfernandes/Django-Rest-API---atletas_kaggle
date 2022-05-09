def valid_name(name):
    return name.isalpha()

def valid_sex(sex):
    return (sex == 'F' or sex == 'M')

def valid_height(height):
    return (height > 0 and height < 250)

def valid_weight(weight):
    return (weight > 0 and len(str(weight)) < 4)

def valid_team(team):
    return team.isalpha()

def valid_noc(noc):
    return noc.isalpha()

def valid_age(age):
    return len(str(age)) < 3
        
def valid_year(year):
    return (year > 0 and year < 2023)

def valid_season(season):
    return (season == 'S' or season == 'W')

def valid_city(city):
    return city.isalpha()
        
def valid_sport(sport):
    return sport.isalpha()

def valid_event(event):
    return not event.isdecimal()