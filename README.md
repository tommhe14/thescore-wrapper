# TheScore API Wrapper

A comprehensive asynchronous Python wrapper for TheScore sports API, providing easy access to sports data including players, teams, matches, competitions, and more.

[![PyPI Downloads](https://static.pepy.tech/badge/thescore-wrapper)](https://pepy.tech/projects/thescore-wrapper)

## Features

- **Full API Coverage:** Access to all TheScore API endpoints

- **Async/Await Support:** Built on aiohttp for high performance

- **Type Annotations:** Full type hint support for better development experience

- **Error Handling:** Robust error handling and connection management

- **Flexible Search:** Advanced search capabilities with competition ID inclusion

## Installation

```bash
pip install thescore-wrapper
```

## Example usage

```py
import asyncio
from thescore import TheScore

async def main():
    async with TheScore() as ts:
        # Search for players
        players = await ts.search_players("LeBron", include_competition_id=True)
        print(f"Found {len(players)} players")
        
        # Get team information
        team = await ts.get_team("nba", 13)  # Miami Heat
        print(team.get("full_name"))
        
        # Get today's games
        from datetime import date
        games = await ts.get_games_by_date(date.today())
        print(f"Games today: {len(games)}")

asyncio.run(main())
```

## Complete API Reference

### Search Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `search(query, page, size)` | General search | `search("Lakers")` |
| `search_teams(query, page, size, include_competition_id)` | Team search | `search_teams("Heat", include_competition_id=True)` |
| `search_players(query, page, size, include_competition_id)` | Player search | `search_players("James", include_competition_id=True)` |
| `search_articles(query, page, size)` | News search | `search_articles("NBA finals")` |

### Club Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_team(competition, team_id)` | Team info | `get_team("nba", 13)` |
| `get_team_previous_fixtures(competition, team_id, count)` | Previous games| `get_team_previous_fixtures("nba", 13, 5)` |
| `get_team_current_fixtures(competition, team_id)` | Live games | `get_team_current_fixtures("nba", 13)` |
| `get_team_upcoming_fixtures(competition, team_id, count)` | Upcoming games | `get_team_upcoming_fixtures("nba", 13, 3)` |
| `get_team_full_schedule(competition, team_id)` | Full schedule | `get_team_full_schedule("nba", 13)` |
| `get_team_profile(team_id)` | Team profile | `get_team_profile(13)` |
| `get_team_squad(competition, team_id)` | Team roster | `get_team_squad("nba", 13)` |
| `get_team_injuries(competition, team_id)` | Team injuries | `get_team_injuries("nba", 13)` |


### Player Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_player(competition, player_id)` | Player info | `get_player("nba", 106844)` |
| `get_player_stats(competition, player_id)` | Player stats | `get_player_stats("nba", 106844)` |
| `get_player_summary(competition, player_id)` | Get participating clubs | `get_live_leagues()` |
| `get_games_by_date(game_date)` | 	Player summary | `get_player_summary("nba", 106844)` |


### Competition Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_standings(competition)` | Standings | `get_standings("nba")` |
| `get_live_leagues()` | Live leagues | `get_competition_transfers("GB1")` |
| `get_competition_clubs(competitionId: str)` | Get participating clubs | `get_live_leagues()` |
| `get_games_by_date(game_date)` | 	Games by date | `get_games_by_date(date.today())` |


### Match Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_match_timeline(competition, event_id)` | Match timeline | `get_match_timeline("nba", 89094)` |
| `get_match_info(competition, event_id)` | Match info | `get_match_info("nba", 89094)` |
| `get_match_lineups(competition, event_id)` | Lineups | `get_match_lineups("nba", 89094)` |
| `get_goalie_stats(competition, event_id)` | Goalie stats | `get_goalie_stats("nhl", 72229)` |
| `get_player_match_stats(competition, event_id)` | Player stats | `get_player_match_stats("nba", 72229)` |
| `get_match_play_by_play(competition, event_id)` | Play-by-play | `get_match_play_by_play("nba", 89094)` |
| `gget_match_betting(competition, event_id)` | Betting info | `get_match_betting("nba", 89094)` |


### Sport-Specific Endpoints

| Method | Description | Example |
|--------|-------------|---------|
| `get_baseball_summary(competition, event_id)` | Baseball summary | `get_baseball_summary("mlb", 64015)` |
| `get_tennis_match(competition, match_id)` | Tennis match | `get_tennis_match("wta", 162108)` |
| `get_motorsport_scoreboard(competition, event_id)` | Motorsport scores | `get_motorsport_scoreboard("nascar", 1556)` |
| `get_motorsport_qualifiers(competition, event_id)` | Motorsport qualifiers | `get_motorsport_qualifiers("nascar", 1556)` |
