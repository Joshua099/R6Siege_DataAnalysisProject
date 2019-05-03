import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.raise_for_status())
# print(type(res))
#
# print(res.status_code == requests.codes.ok)
#
# print(len(res.text))
#
# print(res.text[:250])

# ******* Handling nonexisting web pages *******
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

# ******* Opening a txt file and writing it to your file directory ******
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.raise_for_status())

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    print(playFile.write(chunk))

playFile.close()

