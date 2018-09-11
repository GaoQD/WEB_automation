# -*- coding: utf-8 -*-
# @Time    : 2018/9/5/005 16:20
# @Author  : Administor
# @File    : page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from config.readConfig import ReadConfig

loc = (By.XPATH, ReadConfig().get_string('xpath', 'username'))
loc1 = (By.XPATH, ReadConfig().get_string('xpath', 'passwd'))
user_name = ReadConfig().get_string('login_state', 'user_name')
passwd = ReadConfig().get_string('login_state', 'passwd')
login_button = (By.XPATH,ReadConfig().get_string('xpath','login'))
login = ReadConfig().get_string('url','login')
h5_url = ReadConfig().get_string('url','h5_url')
pc_url = ReadConfig().get_string('url','pc_url')
app_url = ReadConfig().get_string('url','app_url')

banner_management = (By.XPATH,ReadConfig().get_string('xpath','banner_management'))
banner_channel = (By.XPATH,ReadConfig().get_string('xpath','banner_channel'))
h5_page = (By.XPATH,ReadConfig().get_string('xpath','h5_page'))
pc_page = (By.XPATH,ReadConfig().get_string('xpath','pc_page'))
app_page = (By.XPATH,ReadConfig().get_string('xpath','app_page'))
banner_limit = (By.XPATH,ReadConfig().get_string('xpath','banner_limit'))
query_button = (By.XPATH,ReadConfig().get_string('xpath','query_button'))
reset_search = (By.XPATH,ReadConfig().get_string('xpath','reset_search'))

product_FAQ = (By.XPATH,ReadConfig().get_string('xpath','product_FAQ'))
product_categories = (By.XPATH,ReadConfig().get_string('xpath','product_categories'))
novice_product = (By.XPATH,ReadConfig().get_string('xpath','novice_product'))

product_management = (By.XPATH,ReadConfig().get_string('xpath','product_management'))
rich_product = (By.XPATH,ReadConfig().get_string('xpath','rich_product'))
add_rich_product_button = (By.XPATH,ReadConfig().get_string('xpath','add_rich_product_button'))
product_id = (By.XPATH,ReadConfig().get_string('xpath','product_id'))
id_name = '1382'
product_name = (By.XPATH,ReadConfig().get_string('xpath','product_name'))
pro_name = "UI自动化测试"
risk_level = (By.XPATH,ReadConfig().get_string('xpath','risk_level'))
low_risk_level = (By.XPATH,ReadConfig().get_string('xpath','low_risk_level'))
priority = (By.XPATH,ReadConfig().get_string('xpath','priority'))
priority_value = 1
placement = (By.XPATH,ReadConfig().get_string('xpath','placement'))
home_selection = (By.XPATH,ReadConfig().get_string('xpath','home_selection'))
home_preferred = (By.XPATH,ReadConfig().get_string('xpath','home_preferred'))
floating_rate = (By.XPATH,ReadConfig().get_string('xpath','floating_rate'))
floating_rate_value = "0.5"
rate = (By.XPATH,ReadConfig().get_string('xpath','rate'))
rate_value = "8.2"
release_time = (By.XPATH,ReadConfig().get_string('xpath','release_time'))
cur_time = (By.XPATH,ReadConfig().get_string('xpath','cur_time'))
confirm = (By.XPATH,ReadConfig().get_string('xpath','confirm'))

save_button = (By.XPATH,ReadConfig().get_string('xpath','save_button'))

enter_product_name = (By.XPATH,ReadConfig().get_string('xpath','enter_product_name'))
enter_name = "三只松鼠"
rich_product_url = ReadConfig().get_string('url','rich_product_url')
select_result = (By.XPATH,ReadConfig().get_string('xpath','select_result'))
product_status = (By.XPATH,ReadConfig().get_string('xpath','product_status'))
shelf_button = (By.XPATH,ReadConfig().get_string('xpath','shelf_button'))
limit = (By.XPATH,ReadConfig().get_string('xpath','limit'))
lower_frame = (By.XPATH,ReadConfig().get_string('xpath','lower_frame'))
#市场推广
market_promotion = (By.XPATH,ReadConfig().get_string('xpath','market_promotion'))
channel_management = (By.XPATH,ReadConfig().get_string('xpath','channel_management'))
channel_name = (By.XPATH,ReadConfig().get_string('xpath','channel_name'))
channel_value = "天天爱看"
channel_parameter = (By.XPATH,ReadConfig().get_string('xpath','channel_parameter'))
channel_parameter_value = "pc-channel-ttak"
channel_parameter_text = (By.XPATH,ReadConfig().get_string('xpath','channel_parameter_text'))
add_channel = (By.XPATH,ReadConfig().get_string('xpath','add_channel'))
add_channel_name = (By.XPATH,ReadConfig().get_string('xpath','add_channel_name'))
add_channel_value = "WEBUI自动化测试"
add_channel_param = (By.XPATH,ReadConfig().get_string('xpath','add_channel_param'))
add_param_value = "pc-webUI-test"
next_step = (By.XPATH,ReadConfig().get_string('xpath','next_step'))
add_channel_commit = (By.XPATH,ReadConfig().get_string('xpath','add_channel_commit'))
add_commit_next = (By.XPATH,ReadConfig().get_string('xpath','add_commit_next'))
pane_succ_commit = (By.XPATH,ReadConfig().get_string('xpath','pane_succ_commit'))
pane_fail_commit = (By.XPATH,ReadConfig().get_string('xpath','pane_fail_commit'))
pane_old_commit = (By.XPATH,ReadConfig().get_string('xpath','pane_old_commit'))
delete_channel = (By.XPATH,ReadConfig().get_string('xpath','delete_channel'))
delete_confirm = (By.XPATH,ReadConfig().get_string('xpath','delete_confirm'))
#数据统计
data_statistics = (By.XPATH,ReadConfig().get_string('xpath','data_statistics'))
regist_statistics = (By.XPATH,ReadConfig().get_string('xpath','regist_statistics'))
start_time = (By.XPATH,ReadConfig().get_string('xpath','start_time'))
start_time_value = (By.XPATH,ReadConfig().get_string('xpath','start_time_value'))
end_time = (By.XPATH,ReadConfig().get_string('xpath','end_time'))
end_time_value = (By.XPATH,ReadConfig().get_string('xpath','end_time_value'))
channel = (By.XPATH,ReadConfig().get_string('xpath','channel'))
all_channel = (By.XPATH,ReadConfig().get_string('xpath','all_channel'))
regist_query = (By.XPATH,ReadConfig().get_string('xpath','regist_query'))
obtain_succ_regist = (By.XPATH,ReadConfig().get_string('xpath','obtain_succ_regist'))