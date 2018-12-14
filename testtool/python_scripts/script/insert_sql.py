#!/usr/bin/env python3
#-*-coding:utf-8-*-

from tools.db.dbmodule import conn
import random

for x in range(1,2011):
 userid = random.randint(10000000,90000000)
 flowid = random.randint(10000000,90000000)
 sql = "INSERT INTO `db_wlt_gameplatform`.`game_inpour_order` (`flowid`, `userid`, `channelid`, `pay_no`, `bank_code`, `order_amount`, `amount`, `status`, `inpour_rate`, `delete_flag`, `raw_add_time`, `raw_update_time`, `pay_code`, `remark`, `channel_fee`, `convert_flowid`, `convert_orderid`) VALUES ('%s', '%s', '88', '', '', '1.0000', '1.0000', '2', '500.0000', '0', NOW(), NOW(), '', '', '0.0000', '0', '0');" % (flowid,userid)
 r = conn('db_wlt_gameplatform',sql)
