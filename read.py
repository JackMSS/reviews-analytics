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

print('檔案讀取完了, 總共有', len(data), '筆資料')



# 如果想要知道這1,000,000筆留言的平均長度是多少該怎麼做？
# 也就是說每筆字串都有長度， 例如'筆資料'長度就是3

sum_len = 0 
#4 我有所有留言的長度了那我要怎麼知道他的平均？=>sum 加總, 剛開始先給他0
for d in data: 
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))
	#5把每一筆留言的長度len(d)跟目前的總數sum_len加在一起, 
	#然後存回目前的總數sum_len, 所以sum_len就會一直累積每一筆留言的長度, 因此這個最前面的sum_len 會越來越大
#1每一筆的資料叫做d，data裡面裝著一百萬筆的字串, 每一筆字串就是一個留言
#2而字串可以求長度, 字串可以當成清單一樣, 我們可以用len去求他的長度
    #len(d) #3 代表所有留言的長度
    
    #6 print(sum_len)每一次加上去我就把它印出來, 因為我們把每一筆留言的長度都加起來所以數字會非常的大(一共3.6億個字)
    #7 所以從步驟1-6我們可以知道這樣做能夠把留言的長度加總, 那我們要怎麼知道平均？ 也就是每一筆留言的平均長度是多少？
    #7 所以平均就是把總長sum_len除以 你有幾筆留言len(data),len(data)就是ㄧ百萬筆！ 這一百萬筆資料裡面有3.6億個字




