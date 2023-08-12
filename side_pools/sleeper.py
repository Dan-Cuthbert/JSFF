from sleeperpy import Leagues

def owner_info(league_id):
    user_data = Leagues.get_users(league_id)
    users = []
    for user in user_data:
        try:
            team_name = user['metadata']['team_name']
        except:
            team_name = None
        dict = {'username':user['display_name'],'team_name':team_name}
        users.append(dict)
    return users

# Define league variables
league_id = 978439391255322624
team_count = Leagues.get_league(league_id)["total_rosters"]
side_pool_optout = ['ConePollos']
side_pool_count = team_count - len(side_pool_optout)

