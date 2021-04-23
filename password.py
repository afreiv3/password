password = 'a123456'

num = 3 #剩餘機會
i = 1 #測試次數
while num > 0:
	input_password = input('輸入密碼:')

	if input_password == password:
		print('登入成功')
		break
	else:
		num = num - 1
		print('密碼錯誤!還有',num,'次機會')


	