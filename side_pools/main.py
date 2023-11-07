import pools
import pandas
import venmo
import sqlalchemy
import sleeper

engine = sqlalchemy.create_engine('postgresql://retool:om9EQK8HsJfh@ep-icy-salad-54868721.us-west-2.retooldb.com/retool?sslmode=require')                

def main():
    for r in sleeper.rosters:
        print(r['username']+' : '+str(r['roster_id']))
    pool_list = pools.createPools()
    weekly_winners = pools.calculatePools(pool_list)
    payout_list = pools.payouts(pool_list,weekly_winners)
    
    df = pandas.DataFrame(payout_list)
    df['season'] = sleeper.season
    print(df)
    confirmation = input("Please confirm that the payouts are accurate (y/n)")


    if confirmation == 'y':
        for p in payout_list:
            if p['venmo_id'] == 'Ryan-Gillies':
                pass
            else:
                venmo.payout(p['venmo_id'],p['amount'],p['label']+':week'+str(p['week']))
        print('Payments sent!')
        df=df.drop(columns=['label'])
        df['paid'] = True
        df.to_sql(name='payouts', con=engine, if_exists='append', index=False)
    else:
        exit()

main()