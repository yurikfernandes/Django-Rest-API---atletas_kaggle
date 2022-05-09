def check_only_letters(field):
    return all([letter.isalpha() for letter in field if letter.strip() != ''])
    
def valid_name(name):
    return check_only_letters(name)

def valid_sex(sex):
    return (sex == 'F' or sex == 'M')

def valid_height(height):
    return (height > 0 and height < 250)

def valid_weight(weight):
    return (weight > 0 and len(str(weight)) < 4)

def valid_team(team):
    return check_only_letters(team)

def valid_noc(noc):
    return check_only_letters(noc)

def valid_age(age):
    return len(str(age)) < 3
        
def valid_year(year):
    return (year > 0 and year < 2023)

def valid_season(season):
    return (season == 'S' or season == 'W')

def valid_city(city):
    return check_only_letters(city)
        
def valid_sport(sport):
    return check_only_letters(sport)

def valid_event(event):
    return not event.isdecimal()