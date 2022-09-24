# Mood tracker API
> REST API to store and keep track of mood records, yearly summaries (total no. of entries, average mood), and user recording streaks.

## API endpoints
<sub>*Methods in bold are only accessable by admins.*</sub>

### User endpoints
`http://localhost:5000/account/`
| Endpoint | HTTP methods | Description |
| --- | --- | --- |
| `register/` | `POST` | 
| `login/` | `POST` |
| `login/refresh/` | `POST` |
| `profile/` | `GET` | Gets profile of logged in user |
| `user-profiles/` | **`GET`** | Get all existing profiles |
| `user-profiles/<int:pk>/` | **`GET`** |

### Mood tracker endpoints
`http://localhost:5000/`
| Endpoint | HTTP methods | Description |
| --- | --- | --- |
| ` ` | `GET` `POST` | Create a mood entry |
| `<int:pk>/` | `GET` `PUT` `PATCH` `DELETE` |
| `summary/annual/` | `GET` | Gets a summary report of each year for logged in user |

## Usage examples
- `POST` `http://localhost:5000/account/register`  
```
HEADER
{
    "username": "Example",
    "email": "example@test.com",
    "password": "examplepass",
    "password2": "examplepass"
}
```
```
OUTPUT
{
    "username": "Example",
    "tokens": {
        "refresh": <refresh token>,
        "access": <access token>
    }
}
```

- `POST` `http://localhost:5000/account/login/`
```
HEADER
{
    "username": "Example",
    "password": "examplepass"
}
```
```
OUTPUT
{
    "refresh": <refresh token>,
    "access": <access token>
}
```

- `GET` `http://localhost:5000/account/profile/`
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

- `POST` `http://localhost:5000/`
```
{
    "mood": <PositiveIntegerField 1-5 required>,
    "reason": <TextField>,
    "social_situation": <CharField choices>,
    "activity": <Charfield choices>,
    "date": <DateField (default: today's date)>
}
```
<sub>`social_situation choices`</sub>[^1]  
<sub>`activity choices`</sub>[^2] 

- `GET` `http://localhost:5000/summary/annual`
```
[
    {
        "year": <year>,
        "num_of_entries": <total no. of entries>,
        "avg_mood": <average mood of that year>
    }
]
```

## Installation
1. **Clone the repo**
```
git clone https://github.com/stealacamera/mood-tracker-api.git
```
2. **Create and activate a virtual environment**
```
virtualenv <venv name>
<venv name>\Scripts\activate
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

[^1]: 'By myself' (default), 'With acquaintances', 'With friends', 'With family', 'With partner'
[^2]: 'Sports', 'Exercise', 'Movies', 'Reading', 'Gaming', 'Drawing', 'Other' (default)
