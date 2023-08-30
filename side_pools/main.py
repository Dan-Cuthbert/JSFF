from pools import createPools
import sleeper

def main():
    pool_list = createPools()
    for pool in pool_list:
        if pool['week'] == sleeper.week : 
            ## Calculate winner
            print(pool)
        else:
            pass

main()
