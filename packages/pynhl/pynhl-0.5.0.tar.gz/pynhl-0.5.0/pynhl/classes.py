"""
Python wrapper for the Undocumented NHL API by jayblackedout
"""

from datetime import datetime as dt
import requests

BASE = "https://api-web.nhle.com/v1/"


class Player:
    """
    Representation of the NHL API Player dataset

    ...

    Attributes
    ----------
    player_id : str
        The 7 digit player ID of the defined player

    Methods
    -------
    player_info()
        Parses the json data and returns a dict of game info
    """

    def __init__(self, player_id: str) -> None:
        endpoint = f"player/{player_id}/landing"
        url = BASE + endpoint
        try:
            self.response = requests.get(url, timeout=5)
            self.data = self.response.json()
        except requests.Timeout:
            pass

    def player_info(self) -> dict:
        """Parses the json data and returns a dict of game info"""
        response = self.response
        data = self.data
        if response.ok:
            try:
                player_id = data["playerId"]
                current_team_id = data["currentTeamId"]
                current_team_abbrev = data["currentTeamAbbrev"]
                current_team_name = data["fullTeamName"]
                player_first = data["firstName"]
                player_last = data["lastName"]
                player_name = " ".join([player_first, player_last])
                player_number = data["sweaterNumber"]
                player_position = data["position"]
                headshot = data["headshot"]
                stats = data["featuredStats"]["regularSeason"]["subSeason"]
                season_games_played = stats["gamesPlayed"]
                season_goals = stats["goals"]
                season_assists = stats["assists"]
                season_points = stats["points"]
                output = {
                    "player_id": player_id,
                    "current_team_id": current_team_id,
                    "current_team_abbrev": current_team_abbrev,
                    "current_team_name": current_team_name,
                    "player_first": player_first,
                    "player_last": player_last,
                    "player_name": player_name,
                    "player_number": player_number,
                    "player_position": player_position,
                    "headshot": headshot,
                    "season_games_played": season_games_played,
                    "season_goals": season_goals,
                    "season_assists": season_assists,
                    "season_points": season_points,
                }
            except KeyError:
                output = {"player_id": "Not Found"}
            return output


class Team:
    """
    Representation of the NHL API Team dataset

    ...

    Attributes
    ----------
    team_id : str
        The 3 letter abbreviation (AKA tricode) of the defined team

    Methods
    -------
    team_info()
        Parses the json data and returns a dict of game info
    """

    def __init__(self, team_id: str) -> None:
        url = "https://api.nhle.com/stats/rest/en/team"
        self.team_id = team_id
        try:
            self.response = requests.get(url, timeout=5)
            self.data = self.response.json()
        except requests.Timeout:
            pass

    def team_info(self) -> dict:
        """Parses the json data and returns a dict of game info"""
        response = self.response
        data = self.data
        if response.ok:
            try:
                info = data["data"]
                for i in range(0,len(info)):
                    if info[i]["triCode"] == self.team_id.upper():
                        team_name = info[i]["fullName"]
                        team_id = info[i]["id"]
                        team_franchise_id = info[i]["franchiseId"]
                        team_abbrev = info[i]["triCode"]
                        output = {
                            "team_name": team_name,
                            "team_id": team_id,
                            "team_franchise_id": team_franchise_id,
                            "team_abbrev": team_abbrev,
                            "team_logo": f"https://assets.nhle.com/logos/nhl/svg/{team_abbrev}_light.svg"
                        }
                        return output
            except KeyError:
                pass


class Schedule:
    """
    Representation of the NHL API Schedule dataset

    ...

    Attributes
    ----------
    team_id : str
        The 3 letter abbreviation (AKA tricode) of the defined team

    Methods
    -------
    game_index()
        Parses the json data and returns the index of the current or next game
    game_info()
        Parses the json data and returns a dict of game info
    datetime_info()
        Parses the json data and returns a dict of UTC date and time info
    broadcast_info()
        Parses the json data and returns a dict of broadcast info
    """

    def __init__(self, team_id: str) -> None:
        """Returns the json data of the defined team's next scheduled game"""
        endpoint = f"scoreboard/{team_id}/now"
        url = BASE + endpoint
        try:
            self.response = requests.get(url, timeout=5)
            self.data = self.response.json()
        except requests.Timeout:
            pass

    def game_index(self) -> int:
        """Parses the json data and returns the index of the current or next game"""
        response = self.response
        data = self.data
        if response.ok:
            try:
                date_count = data["focusedDateCount"]
                for i in range(0, date_count-1):
                    try_date = dt.strptime(data["gamesByDate"][i]["games"][0]["startTimeUTC"],
                                           "%Y-%m-%dT%H:%M:%SZ")
                    # will return the index of the most current game for 10 hours
                    if ((try_date - dt.utcnow()).total_seconds())/3600 >= -10:
                        output = i
                        break
                    else:
                        output = -1
            except KeyError:
                output = -1
            return output

    def game_info(self) -> dict:
        """Parses the json data and returns a dict of game info"""
        response = self.response
        data = self.data
        if response.ok:
            try:
                games = data["gamesByDate"][self.game_index()]["games"][0]
                game_id = games["id"]
                live_feed = games["gameCenterLink"]
                game_state = games["gameState"]
                away_id = games["awayTeam"]["id"]
                home_id = games["homeTeam"]["id"]
                away_name = games["awayTeam"]["name"]
                home_name = games["homeTeam"]["name"]
                away_logo = games["awayTeam"]["logo"]
                home_logo = games["homeTeam"]["logo"]
                output = {
                    "game_id": game_id,
                    "live_feed": f"https://www.nhl.com{live_feed}",
                    "game_state": game_state,
                    "away_id": away_id,
                    "home_id": home_id,
                    "away_name": away_name.get("default"),
                    "home_name": home_name.get("default"),
                    "away_logo": away_logo,
                    "home_logo": home_logo,
                }
            except KeyError:
                output = {"game_state": "No Game Scheduled"}
            return output

    def datetime_info(self) -> dict:
        """Parses the json data and returns a dict of date and UTC time info"""
        response = self.response
        data = self.data
        if response.ok:
            try:
                games = data["gamesByDate"][self.game_index()]["games"][0]
                game_date = games["startTimeUTC"]
                next_game_date = \
                    dt.strptime(game_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y")
                next_game_time = \
                    dt.strptime(game_date, "%Y-%m-%dT%H:%M:%SZ").strftime("%H:%M")
                output = {
                    "next_game_date": next_game_date,
                    "next_game_time": next_game_time,
                    "next_game_datetime": game_date,
                }
            except KeyError:
                output = {"next_game_datetime": "None"}
            return output

    def broadcast_info(self) -> dict:
        """Parses the json data and returns a dict of broadcast info"""
        response = self.response
        data = self.data
        if response.ok:
            try:
                games = data["gamesByDate"][self.game_index()]["games"][0]
                info = games["tvBroadcasts"]
                nat = [i["network"] for i in info if i["market"] == "N"]
                away = [i["network"] for i in info if i["market"] == "A"]
                home = [i["network"] for i in info if i["market"] == "H"]
                output = {
                    "national_broadcasts": nat,
                    "away_broadcasts": away,
                    "home_broadcasts": home,
                }
            except KeyError:
                output = None
            return output


class Plays:
    """
    Representation of the NHL API Plays dataset

    ...

    Attributes
    ----------
    game_id : str
        The 10 digit game id representing the desired game

    Methods
    -------
    scoring_info()
        Parses the json data and returns a dict of scoring info
    linescore_info()
        Parses the json data and returns a dict of linescore info
    """

    def __init__(self, game_id: str) -> None:
        """Returns the json data of the defined team's last/current game"""
        endpoint = f"gamecenter/{game_id}/play-by-play"
        url = BASE + endpoint
        try:
            self.response = requests.get(url, timeout=5)
            self.data = self.response.json()
        except requests.Timeout:
            pass

    def scoring_info(self) -> dict:
        """Parses the json data and returns a dict of scoring info"""
        response = self.response
        data = self.data
        if response.ok:
            away_id = data["awayTeam"]["id"]
            home_id = data["homeTeam"]["id"] # currently unused but may be useful for last_goal
            away_team = data["awayTeam"]["commonName"]["default"]
            home_team = data["homeTeam"]["commonName"]["default"]
            away_place = data["awayTeam"]["placeName"]["default"]
            home_place = data["homeTeam"]["placeName"]["default"]
            away_name = f'{away_place} {away_team}'
            home_name = f'{home_place} {home_team}'
            away_abbrev = data["awayTeam"]["abbrev"]
            home_abbrev = data["homeTeam"]["abbrev"]
            away_score = data["awayTeam"]["score"]
            home_score = data["homeTeam"]["score"]
            plays = data["plays"]
            if plays != []:
                for i in range(-1, -15, -1):
                    event_type = plays[i]["typeDescKey"]
                    goal_event_id = plays[i]["eventId"]
                    if event_type == "goal":
                        goal_situation = plays[i]["situationCode"]
                        goal_away_str = int(goal_situation[1])
                        goal_home_str = int(goal_situation[2])
                        goal_team_id = plays[i]["details"]["eventOwnerTeamId"]
                        goal_team_str = goal_away_str if away_id == goal_team_id else goal_home_str
                        other_team_str = goal_home_str if away_id == goal_team_id else goal_away_str
                        if goal_team_str > other_team_str:
                            goal_type = "PPG"
                        elif goal_team_str < other_team_str:
                            goal_type = "SHG"
                        else:
                            goal_type = "EVEN"
                        goal_team_name = away_name if away_id == goal_team_id else home_name
                        goal_team_abbrev = away_abbrev if away_id == goal_team_id else home_abbrev
                        scoring_player_id = plays[i]["details"]["scoringPlayerId"]
                        scoring_player_total = plays[i]["details"]["scoringPlayerTotal"]
                        assist1_player_id = plays[i]["details"]["assist1PlayerId"]
                        assist1_player_total = plays[i]["details"]["assist1PlayerTotal"]
                        assist2_player_id = plays[i]["details"]["assist2PlayerId"]
                        assist2_player_total = plays[i]["details"]["assist2PlayerTotal"]
                        output = {
                            "goal_type": goal_type,
                            "goal_team_id": goal_team_id,
                            "goal_event_id": goal_event_id,
                            "goal_team_name": goal_team_name,
                            "goal_team_abbrev": goal_team_abbrev,
                            "away_score": away_score,
                            "home_score": home_score,
                            "scoring_player_id": scoring_player_id,
                            "scoring_player_total": scoring_player_total,
                            "assist1_player_id": assist1_player_id,
                            "assist1_player_total": assist1_player_total,
                            "assist2_player_id": assist2_player_id,
                            "assist2_player_total": assist2_player_total,
                        }
                        return output
                    else:
                        output = {
                            "away_score": away_score,
                            "home_score": home_score,
                        }
                else:
                    output = {
                        "away_score": away_score,
                        "home_score": home_score,
                    }
                    return output

    def linescore_info(self):
        """Parses the json data and returns a dict of linescore info"""
        response = self.response
        data = self.data
        if response.ok:
            try:
                time_remaining = data["clock"]["timeRemaining"]
                is_intermission = data["clock"]["inIntermission"]
                current_period = data["periodDescriptor"]["number"]
                away_sog = data["awayTeam"]["sog"]
                home_sog = data["homeTeam"]["sog"]
                output = {
                    "time_remaining": time_remaining,
                    "is_intermission": is_intermission,
                    "current_period": current_period,
                    "away_sog": away_sog,
                    "home_sog": home_sog,
                }
            except KeyError:
                output = None
            return output
