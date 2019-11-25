from chicken_dinner.pubgapi import PUBG
import pandas as pd

#solo, duo, squad 평균값 추출 함수
def getAvgVal(dic):
    resultList = []
    result = 0
    count = 0
    games = 0
    modes = ['solo', 'duo', 'squad']
    valuenames = ['walk_distance', 'weapons_acquired', 'longest_kill', \
                  'heals', 'boosts', 'damage_dealt']
    for value in valuenames:
        for mode in modes:
            games = dic[mode]['wins'] + dic[mode]['losses']
            if dic[mode][value] != 0:
                if value == 'longest_kill':
                    result = result + dic[mode][value]
                    count = count + 1
                else:
                    result = result + (dic[mode][value] / games)
                    count = count + 1
        if count == 0:
            resultList.append(0)
        else:
            resultList.append(result/count)
            
        result = 0
        count = 0
                
    return resultList

#유저데이터 추출 및 입력형식 변환 변수
def player_data_collect(username, server):
	api_key = "" # input your api key
	pubg = PUBG(api_key, server)
	player_data = pubg.players_from_names(username)[0]
	player_season_data = player_data.get_current_season()
	player_season_data_stats = player_season_data.game_mode_stats()

	dataList = getAvgVal(player_season_data_stats)
	input = {'walkDistance':[dataList[0]], 'weaponsAcquired':[dataList[1]], 'longestKill':[dataList[2]], \
         'heals':[dataList[3]], 'boosts':[dataList[4]], 'damageDealt':[dataList[5]]}
	predictData = pd.DataFrame(input)

	return dataList, predictData