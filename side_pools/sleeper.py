from sleeperpy import Leagues
from sorcery import dict_of
import main_pools
import pandas as pd

# Define league variables
# Ryan's user ID
user_id = '457014438138998784'
season_id = '2022'
league_id = Leagues.get_all_leagues(user_id, 'nfl', season_id)[0]['league_id']


def playoff_results(league_id):
    playoffs = Leagues.get_winners_playoff_bracket(league_id)
    league_winner = next(
        (match for match in playoffs if match['r'] == 3 and match['m'] == 6), None)['w']
    league_runnerup = next(
        (match for match in playoffs if match['r'] == 3 and match['m'] == 6), None)['l']
    league_third = next(
        (match for match in playoffs if match['r'] == 3 and match['m'] == 7), None)['w']
    main_pools = dict_of(league_winner, league_runnerup, league_third)
    return main_pools


def team_info(league_id):
    user_data = Leagues.get_users(league_id)
    rosters = Leagues.get_rosters(league_id)
    users = []
    for user in user_data:
        try:
            team_name = user['metadata']['team_name']
        except:
            team_name = None
        try:
            roster = list(
                filter(lambda roster: roster['owner_id'] == user['user_id'], rosters))[0]
            roster_id = roster['roster_id']
        except:
            roster_id = None
        if roster_id != None:
            total_wins = roster['settings']['wins']
            total_losses = roster['settings']['losses']
            total_ties = roster['settings']['ties']
            total_points_for = roster['settings']['fpts'] + \
                (roster['settings']['fpts_decimal']/100)
            total_points_against = roster['settings']['fpts_against'] + \
                (roster['settings']['fpts_against_decimal']/100)
            dict = {'username': user['display_name'], 'team_name': team_name,
                    'roster_id': roster_id, 'total_wins': total_wins, 'total_losses': total_losses,
                    'total_ties': total_ties, 'total_points_for': total_points_for, 'total_points_against': total_points_against}
        users.append(dict)
    return users


team_count = Leagues.get_league(league_id)["total_rosters"]
side_pool_optout = ['ConePollos']
side_pool_count = team_count - len(side_pool_optout)

print(team_info(league_id))
