import json
import codecs

def readJSON():
    f = codecs.open('./data/members.json', 'r', 'utf-8')
    data = json.load(f)
    f.close()
    return data

def getGuildName(data):
    return data['Guild']['name']


if __name__ == '__main__':
    data = readJSON()
    print(getGuildName(data))