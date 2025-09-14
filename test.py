import asyncio
from thescore import TheScore

import json
from datetime import date

async def main(player_query: str):
    async with TheScore() as ts:
        # Search for players
        players = await ts.search_players(player_query, include_competition_id=True)
        if players:
            print("Player Search Results:")
            for player in players:
                print(f"{player.get('full_name')} {player.get('id')} {player.get('competition')}")

            print("---------")
        
        chosen_player = players[0]
        if chosen_player:
            player_comp = chosen_player.get("competition")
            player_team = chosen_player.get("team").get("id")

            team = await ts.get_team(player_comp, player_team)  
            print(team.get("full_name"), chosen_player.get('full_name'))

            next_fixture = await ts.get_team_upcoming_fixtures(player_comp, player_team)
            print(f"{next_fixture.get('home_teams')[0].get('full_name')} v {next_fixture.get('away_teams')[0].get('full_name')} {next_fixture.get('events')[0].get('game_date')}")
        
        # Get today's games
        games = await ts.get_games_by_date(date.today())
        print(f"Games today: {len(games)}")

asyncio.run(main("saka"))