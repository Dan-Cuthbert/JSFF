import sleeper

buy_in = 100
side_buy_in = 50
total_pot = buy_in*sleeper.team_count
total_side_pot = side_buy_in*sleeper.side_pool_count
weeks = list(range(1, 14))

class Pool:
    _pool_types = set(["standard", "side"])

    def __init__(self, pool, payout, pool_type, week, no_winners):
        self.pool = pool
        self.payout = payout
        self.pool_type = pool_type
        self.week = week
        self.no_winners = no_winners
        self.pool_type = pool_type
        self.label = pool.replace('_',' ').title()

# Define pools
pools = []

# main_pools
pools.append(Pool("league_winner", total_pot*8/12, "main", 16, 1))
pools.append(Pool("league_runnerup", total_pot*3/12, "main", 16, 1))
pools.append(Pool("league_third", total_pot*1/12, "main", 16, 1))

# Full Regular Season
pools.append(Pool("regular_season_first_place", round(total_side_pot*.08,2), "side", 13, 1))
pools.append(Pool("regular_season_most_points", round(total_side_pot*.08,2), "side", 13, 1))
pools.append(
    Pool("regular_season_highest_scoring_player", round(total_side_pot*.08,2), "side", 13, 1))

# One-Week Highs
pools.append(Pool("one-week_highest_score", round(total_side_pot*.04,2), "side", 13, 1))
pools.append(Pool("one-week_highest_score_against", round(total_side_pot*.04,2), "side", 13, 1))
pools.append(Pool("one-week_highest_scoring_player_(non-qb)", round(total_side_pot*.04,2), "side", 13, 1))
pools.append(Pool("one-week_highest_scoring_kicker", round(total_side_pot*.04,2), "side", 13, 1))

# Special Weeks
pools.append(Pool("each_winner_of_opening_week", round(total_side_pot*.10,2),
             "side", 1, round(sleeper.side_pool_count/2,0)))
pools.append(Pool("each_winner_of_rivalry_week", round(total_side_pot*.10,2),
             "side", 8, round(sleeper.side_pool_count/2,0)))
pools.append(Pool("each_winner_of_last_week", round(total_side_pot*.10,2),
             "side", 13, round(sleeper.side_pool_count/2,0)))

# Weekly
for week in weeks:
    pools.append(Pool("highest_score_of_the_week",round(total_side_pot*.0077,2),"side",week,1))
    pools.append(Pool("highest_scoring_margin_of_the_week",round(total_side_pot*.0077,2),"side",week,1))

# Props
pools.append(Pool("most_reacted_to_post_in_league_chat",round(total_side_pot*.02),"side",13,1))
pools.append(Pool("best_team_name",round(total_side_pot*.02),"side",13,1))
pools.append(Pool("Most_rejected_received_trade_offers",round(total_side_pot*.02),"side",13,1))
pools.append(Pool("TBD",round(total_side_pot*.02),"side",13,1))
pools.append(Pool("TBD",round(total_side_pot*.02),"side",13,1))

sum = 0
for p in pools:
    if p.pool_type == 'side':
        sum = sum + p.payout
        print(p.label)

if round(sum,0) !=  round(total_side_pot,0):
    print("ERROR: Total payouts do not equal total pot")
