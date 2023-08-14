import sleeper

buy_in = 100
side_buy_in = 50
total_pot = buy_in*sleeper.team_count
total_side_pot = side_buy_in*sleeper.side_pool_count
weeks = list(range(1, 14))

class Pool:
    _pool_types = set(["standard", "side"])

    def __init__(self, pool, payout, pool_type, week, no_winners, label):
        self.pool = pool
        self.payout = payout
        self.pool_type = pool_type
        self.week = week
        self.no_winners = no_winners
        self.pool_type = pool_type
        self.label = pool.replace('_',' ').title()

# Define pools
pools = []

# Championships
pools.append(Pool("league_winner", total_pot*8/12, "main", 16, 1))
def league_winner_payout(pool):
    league_winner = sleeper.playoff_results(sleeper.league_id)

    return league_w


pools.append(Pool("league_runnerup", total_pot*3/12, "main", 16, 1))
pools.append(Pool("league_third", total_pot*1/12, "main", 16, 1))

# Full Regular Season
pools.append(Pool("Regular Season 1st Place", round(total_side_pot*.08,2), "side", 13, 1))
pools.append(Pool("Regular Season Most Points", round(total_side_pot*.08,2), "side", 13, 1))
pools.append(
    Pool("Regular Season Highest Scoring Player", round(total_side_pot*.08,2), "side", 13, 1))

# One-Week Highs
pools.append(Pool("One-Week Highest Score", round(total_side_pot*.04,2), "side", 13, 1))
pools.append(Pool("One-Week Highest Score Against", round(total_side_pot*.04,2), "side", 13, 1))
pools.append(Pool("One-Week Highest Scoring Player (Non-QB)", round(total_side_pot*.04,2), "side", 13, 1))
pools.append(Pool("One-Week Highest Scoring Kicker", round(total_side_pot*.04,2), "side", 13, 1))

# Special Weeks
pools.append(Pool("Each Winner of Opening Week", round(total_side_pot*.10,2),
             "side", 1, round(sleeper.side_pool_count/2,0)))
pools.append(Pool("Each Winner of Rivalry Week", round(total_side_pot*.10,2),
             "side", 8, round(sleeper.side_pool_count/2,0)))
pools.append(Pool("Each Winner of Last Week", round(total_side_pot*.10,2),
             "side", 13, round(sleeper.side_pool_count/2,0)))

# Weekly
for week in weeks:
    pools.append(Pool("Highest Score of the Week",round(total_side_pot*.0077,2),"side",week,1))
    pools.append(Pool("Highest Scoring Margin of the Week",round(total_side_pot*.0077,2),"side",week,1))

# Props
pools.append(Pool("Most Reacted to Post in League Chat",round(total_side_pot*.02),"side",13,1))
pools.append(Pool("Best Team Name",round(total_side_pot*.02),"side",13,1))
pools.append(Pool("Most Rejected Received Trade Offers",round(total_side_pot*.02),"side",13,1))
pools.append(Pool("TBD",round(total_side_pot*.02),"side",13,1))
pools.append(Pool("TBD",round(total_side_pot*.02),"side",13,1))


sum = 0
for p in pools:
    if p.pool_type == 'side':
        sum = sum + p.payout

if round(sum,0) !=  round(total_side_pot,0):
    print("ERROR: Total payouts do not equal total pot")
