from MyPackage.iRequest import iRequest


if __name__ == '__main__':
  url = 'http://25.17.1.55:8080/GameSupport/game/queryGameCoin.do'
  gameId = '4482'
  userId = ['9871','9873','9875','9901']

for n in range(100):
  for i in userId:
      data = {'data':'{body:{gameId:'+gameId+',userId:'+i+'}}'}
      a =  iRequest.post(url,data)
      print(a)
