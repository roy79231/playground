import random
y=int(input('一天聊幾句?'))
while True :
    if y == 0:
        print('她媽連聊都不會聊告三小白')
        print('請認真作答喔:)')
    elif y == 1:
        print('偏少欸，你確定真的要?')
        break
    elif y >= 10 :
        print('這邊大中計,高機率會成功喔!')
        break
    else :
        print('有點機會喔!')
        break
z=int(input('多久聊一次(天):'))
while True :    
    if z == 0 :
    	print('講啥洨話喔，他媽認真填拉')
    if z == 1 :
    	print('這邊信我，一定中的拉')
    	break
    if z >=2 and y == 1:
    	print('你該懷疑人家是不是不想屌你欸')
    	break
    else:
        print('如果一次聊很多，那就還有機會拉')
        break


r=input('關係如何?')
if r == '曖昧':
	print('她媽曖昧都不衝，你是要等他給別人喔?')
if r == '陌生人':
    print('這邊一定衝，中了拿男朋友，沒中別人會說當朋友，期望至>0')
if r == '朋友':
    print('衝拉，賭一把，反正失敗還是能繼續當朋友一起玩')


x = random.randint(1,100)
j=0
if y == 1 and z >= 2 and r == '陌生人':
    print('告白成功的機率為50%')
    print('賭一把拉，單車變摩托，失敗還賺一個朋友')
if y >= 10 and z == 1 and r == '曖昧' :
    print('告白成功的機率為100%')
    print('這都不衝的話,你懶蛋八成被閹割了')
if x >= 75 : 
    print('告白成功的機率為',x,'%')
    print('這機率都有75%，你就沒道理失敗喔')
else :
    print('告白成功的機率為',x,'%')
    print('其實太低也沒關係，數據僅供參考')       

print('重點是相信你會成功，你才能成功')
while True :
		    print('你一定成功，衝衝衝衝衝')
		    j= j+1
		    if j>=10 :
			    break