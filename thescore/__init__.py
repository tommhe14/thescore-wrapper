from .api import TheScoreAPIClient
from typing import Dict, Any, Optional, List
from datetime import datetime, date

class TheScore:
    """Main TheScore API wrapper interface"""

    def __init__(self):
        self._api = TheScoreAPIClient()
    
    async def __aenter__(self):
        """Enter async context manager"""
        await self._api._ensure_session()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit async context manager"""
        await self._api.close()

    async def close(self):
        """Close context manager"""
        await self._api.close()

    async def search(self, query: str, page: int = 0, size: int = 20) -> Dict[str, Any]:
        """Search for players, teams, articles, etc."""
        return await self._api._request(f"/search?page={page}&q={query}&size={size}")
    
    async def search_teams(self, query: str, page: int = 0, size: int = 20, include_competition_id: bool = False) -> List[Dict[str, Any]]:
        """Search for teams"""
        data = await self._api._request(f"/search/teams?page={page}&q={query}&size={size}")
        
        if include_competition_id and isinstance(data, list):
            for entry in data:
                if isinstance(entry, dict) and "leagues" in entry:
                    leagues = entry.get("leagues", [])
                    if leagues:
                        entry["competition"] = leagues[0]
        
        return data
    
    async def search_players(self, query: str, page: int = 0, size: int = 20, include_competition_id: bool = False) -> List[Dict[str, Any]]:
        """Search for players"""
        data = await self._api._request(f"/search/players?page={page}&q={query}&size={size}")
        
        if include_competition_id and isinstance(data, list):
            for entry in data:
                if isinstance(entry, dict) and "leagues" in entry:
                    leagues = entry.get("leagues", [])
                    if leagues:
                        entry["competition"] = leagues[0]
        
        return data
    
    async def search_articles(self, query: str, page: int = 0, size: int = 20) -> Dict[str, Any]:
        """Search for news articles"""
        return await self._api._request(f"/search/articles?page={page}&q={query}&size={size}")

    # Player endpoints
    async def get_player(self, competition: str, player_id: int) -> Dict[str, Any]:
        """Get player information"""
        return await self._api._request(f"/{competition}/players/{player_id}")
    
    async def get_player_stats(self, competition: str, player_id: int) -> Dict[str, Any]:
        """Get player statistics"""
        return await self._api._request(f"/{competition}/players/{player_id}/player_records?rpp=1")
    
    async def get_player_summary(self, competition: str, player_id: int) -> Dict[str, Any]:
        """Get player summary"""
        return await self._api._request(f"/{competition}/players/{player_id}/summary?stat_type=multi&rpp=-1")

    async def get_team(self, competition: str, team_id: int) -> Dict[str, Any]:
        """Get team information"""
        return await self._api._request(f"/{competition}/teams/{team_id}")
    
    async def get_team_previous_fixtures(self, competition: str, team_id: int, count: int = 1) -> Dict[str, Any]:
        """Get team's previous fixtures"""
        return await self._api._request(f"/{competition}/teams/{team_id}/events/previous?sideload=away_team,home_team&rpp={count}")
    
    async def get_team_current_fixtures(self, competition: str, team_id: int) -> Dict[str, Any]:
        """Get team's current/live fixtures"""
        return await self._api._request(f"/{competition}/teams/{team_id}/events/current?sideload=away_team,home_team&rpp=-1")
    
    async def get_team_upcoming_fixtures(self, competition: str, team_id: int, count: int = 1) -> Dict[str, Any]:
        """Get team's upcoming fixtures"""
        return await self._api._request(f"/{competition}/teams/{team_id}/events/upcoming?sideload=away_team,home_team&rpp={count}")
    
    async def get_team_full_schedule(self, competition: str, team_id: int) -> Dict[str, Any]:
        """Get team's full schedule"""
        return await self._api._request(f"/{competition}/teams/{team_id}/events/full_schedule?sideload=away_team,home_team&rpp=-1")
    
    async def get_team_profile(self, team_id: int) -> Dict[str, Any]:
        """Get team profile stats"""
        return await self._api._request(f"/soccer/teams/{team_id}/profile")
    
    async def get_team_squad(self, competition: str, team_id: int) -> Dict[str, Any]:
        """Get team squad"""
        return await self._api._request(f"/{competition}/teams/{team_id}/players?sideload=team&rpp=-1")
    
    async def get_team_injuries(self, competition: str, team_id: int) -> Dict[str, Any]:
        """Get team injuries"""
        return await self._api._request(f"/{competition}/teams/{team_id}/injuries")

    async def get_match_timeline(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get match timeline"""
        return await self._api._request(f"/{competition}/events/{event_id}/timeline")
    
    async def get_match_info(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get match information"""
        return await self._api._request(f"/{competition}/events/{event_id}")
    
    async def get_match_lineups(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get match lineups"""
        return await self._api._request(f"/{competition}/events/{event_id}/lineups?sideload=team&rpp=-1")
    
    async def get_goalie_stats(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get goalie statistics"""
        return await self._api._request(f"/{competition}/box_scores/{event_id}/goalie_records?rpp=-1")
    
    async def get_player_match_stats(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get player match statistics"""
        return await self._api._request(f"/{competition}/box_scores/{event_id}/player_records?rpp=-1")
    
    async def get_match_play_by_play(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get match play-by-play records"""
        return await self._api._request(f"/{competition}/events/{event_id}/play_by_play_records?rpp=-1")
    
    async def get_match_betting(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get match betting information"""
        return await self._api._request(f"/{competition}/events/{event_id}/betting")

    async def get_standings(self, competition: str) -> Dict[str, Any]:
        """Get competition standings"""
        return await self._api._request(f"/{competition}/live_standings")
    
    async def get_live_leagues(self) -> Dict[str, Any]:
        """Get live leagues"""
        return await self._api._request("/meta/leagues/live")
    
    async def get_games_by_date(self, game_date: date) -> Dict[str, Any]:
        """Get games by specific date"""
        date_str = game_date.strftime("%Y-%m-%d")
        return await self._api._request(f"/multisport/events?game_date.in={date_str}T00:00:00%2B0100,{date_str}T23:59:59%2B0100")

    async def get_baseball_summary(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get baseball game summary"""
        return await self._api._request(f"/{competition}/box_scores/{event_id}/summaries")
    
    async def get_tennis_match(self, competition: str, match_id: int) -> Dict[str, Any]:
        """Get tennis match information"""
        return await self._api._request(f"/{competition}/matches/{match_id}")
    
    async def get_motorsport_scoreboard(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get motorsport scoreboard"""
        return await self._api._request(f"/{competition}/events/{event_id}/driver_records?rpp=-1")
    
    async def get_motorsport_qualifiers(self, competition: str, event_id: int) -> Dict[str, Any]:
        """Get motorsport qualifiers"""
        return await self._api._request(f"/{competition}/events/{event_id}/event_drivers?rpp=-1")
    
