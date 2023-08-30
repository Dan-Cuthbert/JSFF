import sleeper
import statistics
import pandas

# Set global variables
buy_in = 100.00
side_buy_in = 100.00
total_pot = buy_in*sleeper.team_count
total_side_pot = side_buy_in*sleeper.side_pool_count
pool_winners = []


# Define weeks
regular_season = list(range(1, 15))
opening_week = regular_season[0]
rivalry_week = statistics.median(regular_season)
last_week = regular_season[-1]
playoffs = list(range(15,18))
championship_week = playoffs[-1]

class Pool:
    _pool_types = set(['standard', 'side'])

    def __init__(self, pool, payout, pool_type, week, no_winners):
        self.pool = pool
        self.payout = payout
        self.pool_type = pool_type
        self.week = week
        self.no_winners = no_winners
        self.pool_type = pool_type
        self.label = pool.replace('_',' ').title()

# Define properties of all pools
def createPools():
    # Define pools
    pool_list = []

    # main_pools
    pool_list.append(Pool('league_winner', total_pot*8/12, 'main', 16, 1).__dict__)
    pool_list.append(Pool('league_runnerup', total_pot*3/12, 'main', 16, 1).__dict__)
    pool_list.append(Pool('league_third', total_pot*1/12, 'main', 16, 1).__dict__)

    # Full Regular Season
    pool_list.append(Pool('regular_season_first_place', 0 , 'side', 13, 1).__dict__)
    pool_list.append(Pool('regular_season_most_points', round(total_side_pot*.07,0), 'side', 13, 1).__dict__)
    pool_list.append(
        Pool('regular_season_highest_scoring_player', round(total_side_pot*.07,0), 'side', 13, 1).__dict__)

    # One-Week Highs
    pool_list.append(Pool('one-week_highest_score', round(total_side_pot*.04,0), 'side', 13, 1).__dict__)
    pool_list.append(Pool('one-week_highest_score_against', round(total_side_pot*.04,0), 'side', 13, 1).__dict__)
    pool_list.append(Pool('one-week_highest_scoring_player_(non-qb)', round(total_side_pot*.04,0), 'side', 13, 1).__dict__)
    pool_list.append(Pool('one-week_highest_scoring_kicker', round(total_side_pot*.04,0), 'side', 13, 1).__dict__)

    # Special Weeks
    pool_list.append(Pool('each_winner_of_opening_week', round(total_side_pot*.10/round(sleeper.side_pool_count/2,0),0),
                'side', opening_week, round(sleeper.side_pool_count/2,0)).__dict__)
    pool_list.append(Pool('each_winner_of_rivalry_week', round(total_side_pot*.10/round(sleeper.side_pool_count/2,0),0),
                'side', rivalry_week, round(sleeper.side_pool_count/2,0)).__dict__)
    pool_list.append(Pool('each_winner_of_last_week', round(total_side_pot*.10/round(sleeper.side_pool_count/2,0),0),
                'side', last_week, round(sleeper.side_pool_count/2,0)).__dict__)

    # Weekly
    for week in regular_season:
        pool_list.append(Pool('highest_score_of_the_week',round(total_side_pot*.0077,0),'side',week,1).__dict__)
        pool_list.append(Pool('highest_scoring_margin_of_the_week',round(total_side_pot*.0077,0),'side',week,1).__dict__)

    # Props
    pool_list.append(Pool('most_reacted_to_post_in_league_chat',round(total_side_pot*.02,0),'side',13,1).__dict__)
    pool_list.append(Pool('best_team_name',round(total_side_pot*.02,0),'side',13,1).__dict__)
    pool_list.append(Pool('Most_rejected_received_trade_offers',round(total_side_pot*.02),'side',13,1).__dict__)
    pool_list.append(Pool('TBD',round(total_side_pot*.02,0),'side',13,1).__dict__)
    pool_list.append(Pool('TBD',round(total_side_pot*.02,0),'side',13,1).__dict__)

    sum = 0
    for p in pool_list:
        if p['pool_type'] == 'side':
            sum += (p['payout']*p['no_winners'])
    
    plug = [x for x in pool_list if x['pool'] == 'regular_season_first_place'][0]
    plug['payout'] = total_side_pot-sum
    sum += plug['payout']

    return pool_list

def calculatePools(pool_list):
    weekly_winners = {}

    # Weekly Pools
    matchups = sleeper.Leagues.get_matchups(sleeper.league_id, sleeper.week)
    matchup_list = [1,2,3,4,5,6]
    matchup_winners = []
    weekly_high_score = max(matchups, key=lambda x:x['points'])['roster_id']
    for l in matchup_list:
        matchup = [x for x in matchups if x['matchup_id'] == l]
        matchup_winner = max(matchup, key=lambda x:x['points'])
        matchup_loser =  min(matchup, key=lambda x:x['points'])
        matchup_margin = matchup_winner['points'] - matchup_loser['points']
        matchup_dict = {}
        matchup_dict['matchup_id'] = l
        matchup_dict['matchup_winner'] = matchup_winner['roster_id']
        matchup_dict['matchup_loser'] = matchup_loser['roster_id']
        matchup_dict['matchup_margin'] = matchup_margin
        matchup_winners.append(matchup_dict)
    weekly_winners['highest_score_of_the_week'] = weekly_high_score
    weekly_winners['highest_scoring_margin_of_the_week'] = max(matchup_winners, key=lambda x:x['matchup_margin'])['matchup_winner']

    # Special Weeks
    if sleeper.week == opening_week:
        ls = []
        for w in matchup_winners:
            ls.append(w['matchup_winner'])
        weekly_winners['each_winner_of_opening_week'] = ls
    elif sleeper.week == rivalry_week:
        ls = []
        for w in matchup_winners:
            ls.append(w['matchup_winner'])
        weekly_winners['each_winner_of_rivalry_week'] = ls
    elif sleeper.week == last_week:
        ls = []
        for w in matchup_winners:
            ls.append(w['matchup_winner'])
        weekly_winners['each_winner_of_last_week'] = ls
    else:
        pass

    if sleeper.week == last_week:
        pass
        # Full Regular Season
        ## weekly_winners['regular_season_first_place'] =  
        ## weekly_winners['regular_season_most_points'] = 
        ## weekly_winners[regular_season_highest_scoring_player'] = 
        ## weekly_winners[regular_season_highest_scoring_player'] = 

        # One-Week Highs
        ## weekly_winners['one-week_highest_score'] = 
        ## weekly_winners['one-week_highest_score_against'] = 
        ## weekly_winners['one-week_highest_scoring_player_(non-qb)'] =
        ## weekly_winners['one-week_highest_scoring_kicker'] = 

        # # Props
        # pool_list.append(Pool('most_reacted_to_post_in_league_chat',round(total_side_pot*.02),'side',13,1).__dict__)
        # pool_list.append(Pool('best_team_name',round(total_side_pot*.02),'side',13,1).__dict__)
        # pool_list.append(Pool('Most_rejected_received_trade_offers',round(total_side_pot*.02),'side',13,1).__dict__)
        # pool_list.append(Pool('TBD',round(total_side_pot*.02),'side',13,1).__dict__)
        # pool_list.append(Pool('TBD',round(total_side_pot*.02),'side',13,1).__dict__)

    # Main pools
    if sleeper.week == championship_week:
        weekly_winners['league_winner'] = sleeper.get_playoff_results(sleeper.league_id)['league_winner']
        weekly_winners['league_runnerup'] = sleeper.get_playoff_results(sleeper.league_id)['league_runnerup']
        weekly_winners['league_third'] = sleeper.get_playoff_results(sleeper.league_id)['league_third']

    pool_winners.append(weekly_winners)

    return pool_winners

pool_list = createPools()
pool_df = pandas.DataFrame(pool_list)
print(pool_df['payout'])

weekly_winners = calculatePools(pool_list)
print(weekly_winners)

