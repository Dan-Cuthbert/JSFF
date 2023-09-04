import pools
import pandas
import venmo
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://retool:om9EQK8HsJfh@ep-icy-salad-54868721.us-west-2.retooldb.com/retool?sslmode=require')                

def main():
    pool_list = pools.createPools()
    weekly_winners = pools.calculatePools(pool_list)
    payout_list = pools.payouts(pool_list,weekly_winners)
    
    df = pandas.DataFrame(payout_list)
    print(df)
    confirmation = input("Please confirm that the payouts are accurate (y/n)")
    
    if confirmation == 'y':
        df.to_sql(name='payouts', con=engine, if_exists='append')
        for p in payout_list:
            venmo.payout(p['username'],p['payout'],p['pool']+':week'+str(p['week']))
        print('Hooray')
    else:
        exit()

main()