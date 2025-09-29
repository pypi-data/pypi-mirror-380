# lukhed_sports
A collection of sports analysis utility functions and API wrappers

## Installation
```bash
pip install lukhed-sports
```

## Available Wrappers and Classes
- [Sportspage Feeds Wrapper](#sportspage-feeds-wrapper) - For sports schedules and odds from [sportspagefeeds API](https://sportspagefeeds.com/documentation)
- [Draftkings Sports Wrapper](#drafkings-sportsbook-wrapper) - For obtaining live data from [Draftkings sportsbook](https://sportsbook.draftkings.com/)
- [ESPN NFL Stats Wrapper](#espn-nfl-stats-wrapper) - For retrieving NFL team and player statistics from ESPN
- [NFL Next Gen Stats Schedule](#nfl-next-gen-stats-schedule) - For accessing NFL schedule data from Next Gen Stats API

## Drafkings Sportsbook Wrapper
Access live data from Draftkings Sportsbook via their API methods. Quick start information below. Full documentation coming. This class is still a work in progress.

### Table of Contents
- [Instantiation](#instantiation)
- [get_available_leagues(sport)](#get_available_leagues)
- [get_spread_for_team(league, sport)](#get_spread_for_team)
- [get_game_lines_for_league(league)](#get_gamelines_for_league)
- [get_basic_touchdown_scorer_props(league, prop_type_filter=None, game_filter=None)](#get_basic_touchdown_scorer_props)

### Instantiation
```python
from lukhed_sports import DkSportsbook
api = DkSportsbook()
```

### get_available_leagues
Provides valid league inputs for various methods.
```python
leagues = api.get_available_leagues('basketball')
```

```json
[
    "argentina - liga nacional de basquetbol",
    "australia - nbl",
    "brazil - nbb",
    "china - cba",
    "college basketball (m)",
    "college basketball (w)",
    "croatia premier league",
    "germany - bundesliga",
    "greece - basket league",
    "israel - super league (w)",
    "italy - lega 1",
    "korea - basketball league (w)",
    "nba",
    "turkey - bsl",
    "wnba"
]
```


### get_spread_for_team
Provides the current spread and spread odds for the given team.
```python
spread = api.get_spread_for_team('nfl', 'commanders')
```

```json
{
    "spread": 5.5,
    "odds": {
        "american": "-108",
        "decimal": "1.92",
        "fractional": "25/27"
    }
}
```

### get_gamelines_for_league
Provides all the gamelines available for a given league.
```python
gamelines = api.get_gamelines_for_league('nfl')
```
[Full example response](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/gamelinesForLeague.json)


### get_basic_touchdown_scorer_props
Provides all the basic td scoring props available, with various filter options.
```python
td = api.get_basic_touchdown_scorer_props('college football', prop_type_filter='anytime', game_filter='notre dame')
```

```json
[
    {
        "id": "0QA229129141#130806310_13L87637Q1477509025Q20",
        "marketId": "229129141",
        "label": "Jeremiah Smith",
        "displayOdds": {
            "american": "-140",
            "decimal": "1.71",
            "fractional": "5/7"
        },
        "trueOdds": 1.71428572,
        "outcomeType": "Anytime Scorer",
        "participants": [
            {
                "id": "786772",
                "name": "Jeremiah Smith",
                "type": "Player",
                "seoIdentifier": "Jeremiah Smith"
            }
        ],
        "sortOrder": 3001710,
        "tags": [
            "SGP",
            "1stFavorite"
        ],
        "metadata": {}
    },
    {
        "id": "0QA229129141#130806308_13L87637Q1709721529Q20",
        "marketId": "229129141",
        "label": "TreVeyon Henderson",
        "displayOdds": {
            "american": "-140",
            "decimal": "1.71",
            "fractional": "5/7"
        },
        "trueOdds": 1.71428572,
        "outcomeType": "Anytime Scorer",
        "participants": [
            {
                "id": "570977",
                "name": "TreVeyon Henderson",
                "type": "Player",
                "seoIdentifier": "TreVeyon Henderson"
            }
        ],
        "sortOrder": 3001710,
        "tags": [
            "SGP",
            "2ndFavorite"
        ],
        "metadata": {}
    },
    ...
```


## ESPN NFL Stats Wrapper
Access team and player statistics from ESPN for the NFL. This wrapper provides functionality to retrieve team 
statistics, player rosters, player search, and detailed player statistics.

Partial documentation below. See examples.py in the repo for more.

### Table of Contents
- [Instantiation](#instantiation)
- [Team Statistics](#team-statistics)
- [Player Search](#player-search)
- [Player Statistics](#player-statistics)

### Instantiation
```python
from lukhed_sports import EspnNflStats
espn = EspnNflStats()
```

### Team Statistics
Get comprehensive team statistics for the NFL.

```python
# Get all team stats for a specific season
stats = espn.get_all_teams_stats(2023, regular_or_offseason='regular')

# Get offensive stats summary for a team
offense_summary = espn.team_stats_get_ypg_summary('DET', ball_side='offense')
```

### Player Search
Search for players with various filtering options, including fuzzy name matching.

```python
# Basic search
players = espn.player_search('Mahomes')

# Advanced search with fuzzy matching
players = espn.player_search('Mahomes', fuzzy_search=True, fuzzy_threshold=80)
```

### Player Statistics
Access detailed player statistics including career stats, game logs, and splits.

```python
# Get overview stats (page: https://www.espn.com/nfl/player/_/id/3139477/patrick-mahomes)
player_overview = espn.get_player_stat_overview('Patrick Mahomes', team='KC')

# Get player career bio information (page: https://www.espn.com/nfl/player/bio/_/id/3139477/patrick-mahomes)
player_bio = espn.get_player_stat_bio('Patrick Mahomes')

# Get player game log for season (page: https://www.espn.com/nfl/player/gamelog/_/id/3139477/type/nfl/year/2023)
game_log = espn.get_player_stat_gamelog('Patrick Mahomes', season='2023')

# Get player statistical splits (page: https://www.espn.com/nfl/player/splits/_/id/3139477/patrick-mahomes)
splits = espn.get_player_stat_splits('Patrick Mahomes')

# Get college stats for a player (page: https://www.espn.com/nfl/player/gamelog/_/id/3916387/type/college-football)
college_stats = espn.get_player_stat_gamelog('jackson', last_name_search=True, team='bal', position='QB', 
                                             league='college')
```

## Sportspage Feeds Wrapper
This class is a custom wrapper for the [sportspagefeeds API](https://sportspagefeeds.com/documentation). 

It provides:
- Management of api key -> You can store api key locally (by default) or with a private github repo 
    so you can use the api efficiently across different hardware.
- Optionally manage api limits (on by default) 
- Methods to utilize each endpoint from sportspagefeeds
- Optionally validate input (on by default), to ensure you do not waste API calls
- Methods to get valid inputs for each endpoint, as documentation is sparse
- Methods to parse data returned by basic (non-paid) endpoints 

Quick start information below. Full documentation for this class is in development.

### API Key Management Locally
Instatiate without optional parameters and upon first use, the class will take you thru setup (copy and paste your Sportspage key)

```python
api = SportsPage()
```

### API Key Managment with Private Github Repo
Instantiate with option github parameters and Upon first use, class will take you thru setup (github token and Sportspage key). Future instantiation, just reference the github_project.
```python
# 
api = SportsPage(
    config_file_preference='github', 
    github_project='any_project_name'
    )
```

### Games
Get the games occuring today with basic schedule and odds information.
```python
api.get_games('nfl')
```

See full example response [see here.](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/nflGames.json)


### Rankings
Get rankings for the given target.
```python
rankings = api.get_rankings('ncaaf')
```

See full example response [see here.](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/getRankings.json)


### Check API Usage
Free tier of Sportspage is limited. You can check your api usage with this method.
```python
api.check_api_limit()

# print to console
>>>
You have 15 api calls remaining
Your reset time is set for 20241230194114 US/Eastern
Your limit is 20
```

Response
```json
{
    "limit": 20,
    "remaining": 15,
    "resetTime": "20250105194115",
    "lastCall": "20250105121251"
}
```


### All Endpoints
```python
api.get_games           # Get schedule/status of games
api.get_rankings        # Get rankings for various leagues    
api.get_teams           # Get teams in leagues/conferences
api.get_conferences     # Get conferences in leagues
api.get_game_by_id      # Get info about a game by its ID
api.get_odds            # Get odds for a game (requires paid tier)
```

Example responses
- [get_games nfl](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/nflGames.json)
- [get_rankings ncaaf](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/getRankings.json)
- [get_teams ncaaf](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/ncaafTeams.json)
- [get_conferences ncaab](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/ncaabConferences.json)
- [get_game_by_id nfl game id](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/getGameId.json)
- [get_odds error response for non paid](https://github.com/lukhed/lukhed_sports/blob/main/lukhed_sports/example_responses/getOddsById.json)

## NFL Next Gen Stats Schedule
Access NFL schedule data from the Next Gen Stats API. This class provides methods to retrieve schedule information 
and game overviews.

### Table of Contents
- [Instantiation](#ngs-instantiation)
- [Basic Usage](#ngs-basic-usage)
- [Game Data](#ngs-game-data)
- [Team Information](#ngs-team-info)

### Instantiation
```python
from lukhed_sports.nflSchedules import NextGenStatsSchedule
ngs = NextGenStatsSchedule(season='current')  # or specific season like 2023
```

### Basic Usage
Get schedule data and regular season games:

```python
# Get full schedule
schedule = ngs.get_schedule()

# Get regular season games for a specific team
lions_games = ngs.get_regular_season_games('DET')

# Change season
ngs.change_season(2022)
```

### Game Data
Access specific game data and overviews:

```python
# Get data for a specific game given team and week input
game_data = ngs.get_game_data('DET', 1)

# Get detailed game overview with stats given team and week input
game_overview = ngs.get_game_overview_for_team('DET', 1)
```

### Team Information
Get a list of all NFL teams with their nicknames and abbreviations:

```python
# Get all teams with their details
teams = ngs.get_all_teams()

# Example output
[
    {
        "nickname": "Lions",
        "abbreviation": "DET",
        "displayName": "Detroit Lions"
    },
    ...
]
```

Note: Team abbreviations should match those used on the NGS game center page: https://nextgenstats.nfl.com/stats/game-center-index

