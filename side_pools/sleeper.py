from sleeperpy import Leagues
from sorcery import dict_of

# Define league variables
# Ryan's user ID
user_id = '457014438138998784'
season_id = '2022'
league_id = Leagues.get_all_leagues(user_id,'nfl',season_id)[0]['league_id']

def playoff_results(league_id):
    playoffs = Leagues.get_winners_playoff_bracket(league_id)
    league_winner = next((match for match in playoffs if match['r'] == 3 and match['m'] == 6), None)['w']
    league_runnerup = next((match for match in playoffs if match['r'] == 3 and match['m'] == 6), None)['l']
    league_third = next((match for match in playoffs if match['r'] == 3 and match['m'] == 7), None)['w']
    main_pools = dict_of(league_winner,league_runnerup,league_third)
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
            roster_id = list(filter(lambda roster: roster['owner_id'] == user['user_id'], rosters))[0]['roster_id']
        except:
            roster_id = None
        dict = {'username':user['display_name'],'team_name':team_name,'roster_id':roster_id}
        users.append(dict)
    return users

team_count = Leagues.get_league(league_id)["total_rosters"]
side_pool_optout = ['ConePollos']
side_pool_count = team_count - len(side_pool_optout)

print(playoff_results(league_id))
print(team_info(league_id))

