####################################################################################
# Bluetooth: bluetooth_adapter_winrt.cc:1074 Getting Default Adapter failed.
# : 셀레니움 최신화, 파이썬, 크롬 드라이버랑 크롬 최신화 진행해서 해결됨
####################################################################################
# stale element reference: element is not attached to the page document
# : 뭔가를 해야하는데 페이지가 나와있지 않을 때 나오는 오류

# for item in items:
#   if item.text == '루나':
#     item.click()
#     time.sleep(2)
#     break

# 여기서 클릭 후 items가 남아있는데 클릭으로 인해 페이지가 바뀌어 남은 반복문을 더 진행하지 못해 오류가 생겼다.
# 클릭 후 break를 추가했더니 오류가 해결됨
####################################################################################
# no such element: Unable to locate element: {"method":"css selector","selector":".member-grade-header"}
# : 그 태그가 없는곳에서 정보를 찾으려고 해서 생긴 문제

# if i == biggrade[0]:
#     grade = item.find_element(By.CSS_SELECTOR, '.member-grade-header').text
# elif i == biggrade[1]: 
#     grade = '길드원'