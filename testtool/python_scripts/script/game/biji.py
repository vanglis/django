#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
Created on 2016-01-13
Author: xiaohanfei
TODO: 校验game_biji_info表中的牌型和得分数据是否正确
'''
from tools.db.dbmodule import conn
from tools.log import w_log
import json

def poker_type(pokers):
    #pokers = ['D9','A9','C9']
    #牌面大小
    c1 = pokers[0][1:]
    c2 = pokers[1][1:]
    c3 = pokers[2][1:]
    #牌面图案
    d1 = pokers[0][0]
    d2 = pokers[1][0]
    d3 = pokers[2][0]
    p_sort = sorted(pokers,key=lambda x:int(x[1::]),reverse=True)
    tuAnScore = {
            'A' : 4,
            'B' : 3,
            'C' : 2,
            'D' : 1,
    }
    if c1 == c2 == c3 :
       print('三条')
       score = 6000000000
       c1_1 = int(c1)*10000000
       c2_2 = int(c2)*100000
       c3_3 = int(c3)*1000
       st_sort = sorted(pokers)
       print(st_sort)
       score = score+c1_1+c2_2+c3_3+tuAnScore[st_sort[0][0]]*100+tuAnScore[st_sort[1][0]]*10+tuAnScore[st_sort[2][0]]
    elif d1 == d2 == d3 and int(p_sort[0][1:]) - int(p_sort[1][1:]) == int(p_sort[1][1:]) - int(p_sort[2][1:]) == 1:
       print('同花顺')
       score = 5000000000
       c1_1 = int(p_sort[0][1:])*10000000
       c2_2 = int(p_sort[1][1:])*100000
       c3_3 = int(p_sort[2][1:])*1000
       score = score+c1_1+c2_2+c3_3+tuAnScore[d1]*100+tuAnScore[d2]*10+tuAnScore[d3]
    elif d1 == d2 == d3:
       print('同花')
       score = 4000000000
       c1_1 = int(p_sort[0][1:])*10000000
       c2_2 = int(p_sort[1][1:])*100000
       c3_3 = int(p_sort[2][1:])*1000
       score = score+c1_1+c2_2+c3_3+tuAnScore[d1]*100+tuAnScore[d2]*10+tuAnScore[d3]
    elif int(p_sort[0][1:]) - int(p_sort[1][1:]) == int(p_sort[1][1:]) - int(p_sort[2][1:]) == 1:
       print('顺子')
       score = 3000000000
       c1_1 = int(p_sort[0][1:])*10000000
       c2_2 = int(p_sort[1][1:])*100000
       c3_3 = int(p_sort[2][1:])*1000
       score = score+c1_1+c2_2+c3_3+tuAnScore[p_sort[0][0]]*100+tuAnScore[p_sort[1][0]]*10+tuAnScore[p_sort[2][0]]
    elif int(c1) == int(c2) or int(c1) == int(c3) or int(c2) == int(c3):
       print('对子')
       score = 2000000000
       if int(c1) == int(c2):
          #对子花色大小比较
          if tuAnScore[d1] > tuAnScore[d2]:
             p_sort2 = [d1+c1,d2+c2,d3+c3]
             c1_1 = int(p_sort2[0][1:])*10000000
             c2_2 = int(p_sort2[1][1:])*100000
             c3_3 = int(p_sort2[2][1:])*1000
             score = score+c1_1+c2_2+c3_3+tuAnScore[d1]*100+tuAnScore[d2]*10+tuAnScore[d3]
          else:
             p_sort2 = [d2+c1,d1+c2,d3+c3]
             c1_1 = int(p_sort2[0][1:])*10000000
             c2_2 = int(p_sort2[1][1:])*100000
             c3_3 = int(p_sort2[2][1:])*1000
             score = score+c1_1+c2_2+c3_3+tuAnScore[d2]*100+tuAnScore[d1]*10+tuAnScore[d3]
       elif int(c1) == int(c3):
          if tuAnScore[d1] > tuAnScore[d3]:
             p_sort2 = [d1+c1,d3+c3,d2+c2]
             c1_1 = int(p_sort2[0][1:])*10000000
             c2_2 = int(p_sort2[1][1:])*100000
             c3_3 = int(p_sort2[2][1:])*1000
             score = score+c1_1+c2_2+c3_3+tuAnScore[d1]*100+tuAnScore[d3]*10+tuAnScore[d2]
          else:
             p_sort2 = [d3+c1,d1+c3,d2+c2]
             c1_1 = int(p_sort2[0][1:])*10000000
             c2_2 = int(p_sort2[1][1:])*100000
             c3_3 = int(p_sort2[2][1:])*1000
             score = score+c1_1+c2_2+c3_3+tuAnScore[d3]*100+tuAnScore[d1]*10+tuAnScore[d2]
       else:
          if tuAnScore[d2] > tuAnScore[d3]:
             p_sort2 = [d2+c2,d3+c3,d1+c1]
             c1_1 = int(p_sort2[0][1:])*10000000
             c2_2 = int(p_sort2[1][1:])*100000
             c3_3 = int(p_sort2[2][1:])*1000
             score = score+c1_1+c2_2+c3_3+tuAnScore[d2]*100+tuAnScore[d3]*10+tuAnScore[d1]
          else:
             p_sort2 = [d3+c2,d2+c3,d1+c1]
             c1_1 = int(p_sort2[0][1:])*10000000
             c2_2 = int(p_sort2[1][1:])*100000
             c3_3 = int(p_sort2[2][1:])*1000
             score = score+c1_1+c2_2+c3_3+tuAnScore[d3]*100+tuAnScore[d2]*10+tuAnScore[d1]
    else:
       print('单张')
       score = 1000000000
       c1_1 = int(p_sort[0][1:])*10000000
       c2_2 = int(p_sort[1][1:])*100000
       c3_3 = int(p_sort[2][1:])*1000
       score = score+c1_1+c2_2+c3_3+tuAnScore[p_sort[0][0]]*100+tuAnScore[p_sort[1][0]]*10+tuAnScore[p_sort[2][0]]
    return score

def player(re):
    player_td_poker = re['player']['td']['poker']
    player_td_score = re['player']['td']['score']
    player_zd_poker = re['player']['zd']['poker']
    player_zd_score = re['player']['zd']['score']
    player_wd_poker = re['player']['wd']['poker']
    player_wd_score = re['player']['wd']['score']
    player_pokers_score = {
                     'player_td_poker':player_td_poker,
                     'player_td_score':player_td_score,
                     'player_zd_poker':player_zd_poker,
                     'player_zd_score':player_zd_score,
                     'player_wd_poker':player_wd_poker,
                     'player_wd_score':player_wd_score,
                     }
    return player_pokers_score

def robot1(re):
    robot1_td_poker = re['robot1']['td']['poker']
    robot1_td_score = re['robot1']['td']['score']
    robot1_zd_poker = re['robot1']['zd']['poker']
    robot1_zd_score = re['robot1']['zd']['score']
    robot1_wd_poker = re['robot1']['wd']['poker']
    robot1_wd_score = re['robot1']['wd']['score']
    robot1_pokers_score = {
                     'robot1_td_poker':robot1_td_poker,
                     'robot1_td_score':robot1_td_score,
                     'robot1_zd_poker':robot1_zd_poker,
                     'robot1_zd_score':robot1_zd_score,
                     'robot1_wd_poker':robot1_wd_poker,
                     'robot1_wd_score':robot1_wd_score,
                     }
    return robot1_pokers_score

def robot2(re):
    robot2_td_poker = re['robot2']['td']['poker']
    robot2_td_score = re['robot2']['td']['score']
    robot2_zd_poker = re['robot2']['zd']['poker']
    robot2_zd_score = re['robot2']['zd']['score']
    robot2_wd_poker = re['robot2']['wd']['poker']
    robot2_wd_score = re['robot2']['wd']['score']
    robot2_pokers_score = {
                     'robot2_td_poker':robot2_td_poker,
                     'robot2_td_score':robot2_td_score,
                     'robot2_zd_poker':robot2_zd_poker,
                     'robot2_zd_score':robot2_zd_score,
                     'robot2_wd_poker':robot2_wd_poker,
                     'robot2_wd_score':robot2_wd_score,
                     }
    return robot2_pokers_score

if __name__ == "__main__":
  try:
   id = 8124467
   sql = 'SELECT `poker` FROM game_biji_info where id ='+str(id)
   #count = conn('db_game_yace','SELECT `id` FROM game_biji_info  ORDER BY id DESC LIMIT 1;')
   for i in range(8680195,9124467,2):
      sql = 'SELECT `poker` FROM game_biji_info where id ='+str(i)
      r = conn('db_game_yace',sql)
      print(i)
      i+=2
      s = r[0]
      poker = s['poker']
      re = json.loads(poker)
      player_pokers_score = player(re)
      robot1_pokers_score = robot1(re)
      robot2_pokers_score = robot2(re)
      for m in ['td','zd','wd']:
          player_td_poker_score = poker_type(player_pokers_score['player_'+m+'_poker'])
          if player_td_poker_score == player_pokers_score['player_'+m+'_score']:
             output = 'player验证通过=>'+str(player_pokers_score['player_'+m+'_poker'])+str(player_td_poker_score)
             w_log.w_log('biji',output)
             print(output)
          else:
             output = 'player验证失败|头墩牌型：'+str(player_pokers_score['player_'+m+'_poker'])+'--预期分数:'+str(player_td_poker_score)+'实际分数：'+str(player_pokers_score['player_'+m+'_score'])
             w_log.w_log('biji',output)  
          robot1_td_poker_score = poker_type(robot1_pokers_score['robot1_'+m+'_poker'])
          if robot1_td_poker_score == robot1_pokers_score['robot1_'+m+'_score']:
             output = 'robot1验证通过=>'+str(robot1_pokers_score['robot1_'+m+'_poker'])+str(robot1_td_poker_score)
             w_log.w_log('biji',output)
             print(output)
          else:
             output = 'robot1验证失败|头墩牌型：'+str(robot1_pokers_score['robot1_'+m+'_poker'])+'--预期分数:'+str(robot1_td_poker_score)+'实际分数：'+str(robot1_pokers_score['robot1_'+m+'_score'])
             w_log.w_log('biji',output)
          robot2_td_poker_score = poker_type(robot2_pokers_score['robot2_'+m+'_poker']) 
          if robot2_td_poker_score == robot2_pokers_score['robot2_'+m+'_score']:
             output = 'robot2验证通过=>'+str(robot2_pokers_score['robot2_'+m+'_poker'])+str(robot2_td_poker_score)
             w_log.w_log('biji',output)
             print(output)
          else:
             output = 'robot2验证失败|头墩牌型：'+str(robot2_pokers_score['robot2_'+m+'_poker'])+'--预期分数:'+str(robot2_td_poker_score)+'实际分数：'+str(robot2_pokers_score['robot2_'+m+'_score'])
             w_log.w_log('biji',output)
  except Exception as e:
    w_log.w_log('biji',e)
