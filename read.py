data=[]

# 在做完列印出1,000,000筆資料跟了解資料總共
#有幾筆然後打出第一個留言跟第二個留言之後, 
#如果我想要每次讀取1000筆就印出一次怎麼做？ 
count = 0 # 這邊寫一個計數器count來計數,剛開始為0代表一筆都還沒讀

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1 # 每讀一筆就+1(or count+=1)
		if count % 1000 == 0: #如果count跟1000的餘數是0 
		#才會把你print出來，這個意思就是每一千筆列出一次的意思
		# 在數學上就是如果count是1000的倍數就會把你印出來
		# % 餘數：1002%1000:2   7%3:1  
		    print(len(data)) #這樣他每次讀一行就把長度列給你看

print(len(data))
print(data[0])
print('---------')
print(data[1])

