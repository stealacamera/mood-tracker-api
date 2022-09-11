# Mood tracker API
> REST API built with django and django rest framework.

## Installation
1. **Clone the repo**
```
git clone https://github.com/stealacamera/mood-tracker-api.git
```
2. **Create and activate a virtual environment**
```
virtualenv <venv name>
<venv name>/Scripts/activate
```
3. **Install the dependencies**
```
pip install -r requirements.txt
```
4. **Run migrations and server**
```
python manage.py migrate
python manage.py runserver
```

## API endpoints
- **POST** Register: `http://localhost:5000/account/register`  
*Registers a user.*  
```
HEADER
{
    "username": "Example",
    "email": "example@test.com",
    "password": "examplepass",
    "password2": "examplepass"
}

OUTPUT
{
    "username": "Example",
    "tokens": {
        "refresh": <refresh token>,
        "access": <access token>
    }
}
```

- **POST** Login: `http://localhost:5000/account/login/`  
*Logs in a user.*  
```
HEADER
{
    "username": "Example",
    "password": "examplepass"
}

OUTPUT
{
    "refresh": <refresh token>,
    "access": <access token>
}
```

- **POST** Login refresh: `http://localhost:5000/account/login/refresh/`  
*Returns a new access token for the logged in user.*  
```
{
    "refresh": <refresh token>,
    "access": <access token>
}
```

- **GET** Profile: `http://localhost:5000/account/profile/`  
*Returns user's profile.*
```
{
    "id": <user id>,
    "username": "Example",
    "email": "example@test.com",
    "profile": {
        "current_streak": <user's current streak>,
        "best_streak": <user's best streak>
    }
}
```

- **GET** User profiles: `http://localhost:5000/account/user-profiles/` `http://localhost:5000/account/user-profiles/<id>`  
*Returns all/specified registered users' profiles.  
Only accessable by admins.*

- **GET** Mood entry: `http://localhost:5000/`  
*Returns all entries made by user.*

- **POST** Mood entry: `http://localhost:5000/`  
*Submits a new entry.*  
```
{
    "mood": <PositiveIntegerField 1-5 required>,
    "reason": <TextField>,
    "social_situation": <CharField choices>,
    "activity": <Charfield choices>,
    "date": <DateField (default: today's date)>
}
```
`social_situation choices`[^1]  
`activity choices`[^2]

- **GET PUT PATCH DELETE** Mood entry: `http://localhost:5000/<id>`  

- **GET** Entry summaries: `http://localhost:5000/summary/annual`  
*Returns a summary report of each year.*
```
[
    {
        "year": <year>,
        "num_of_entries": <total no. of entries>,
        "avg_mood": <average mood of that year>
    }
]
```

[^1]: 'By myself' (default), 'With acquaintances', 'With friends', 'With family', 'With partner'
[^2]: 'Sports', 'Exercise', 'Movies', 'Reading', 'Gaming', 'Drawing', 'Other' (default)
