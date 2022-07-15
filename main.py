import telebot
from telebot import types,TeleBot

#token

token = input ('   ارسل توكن بوتك\n')
sudo= int(input('   ارسل ايدي المطور\n'))

#bot

bot = telebot.TeleBot(token)

#methouds

@bot.message_handler(content_types=['text'])
def MSG(message):
	commands = message.text
	if commands == '/start':
			if message.from_user.id == sudo:
				a = types.InlineKeyboardMarkup(row_width=2)
				b = types.InlineKeyboardButton(text='y', callback_data='api')
				l = types.InlineKeyboardButton(text='u' , callback_data='api1')
				c = types.InlineKeyboardButton(text='u' , callback_data='api2')
				d = types.InlineKeyboardButton(text='f' , callback_data='api3')
				g = types.InlineKeyboardButton(text='p' , callback_data='api4')
				f = types.InlineKeyboardButton(text='b' , callback_data='api5')
				a.add(b,l,c,d,g,f)
				bot.send_message(message.chat.id , text='مرحبا حبيبي المبرمج 🌚\n\n اؤمرنى حبيبي المبرمج وانا هنفذ كل شيئ 😊😊' , reply_markup= a)
			else:
				text6 = message.from_user.username
				photo = 'https://telegra.ph/file/9040a729ae5c29922372d.jpg'
				bot.send_photo(message.chat.id  ,photo , ''''🚸| مرحبا بك عزيرى « @{} »\n\n🚸| هذا البوت مخصص للحصول علي جميع الكتب للمرحله الثانويه \n\n🚸| لكتب الثانويه العامه ارسل « /edu » \n\n🚸| للحصول علي كتب ثانويه ازهريه ارسل « /eda » \n\n🚸| لطلب اي كتاب غير متوفر يرجي التواصل مع مبرمج البوت \n\n🚸|للتواصل مع المبرمج ارسل « المبرمج » او « /help »'''.format(text6))
				#/edu
				#/eda
				#/help
				#المبرمج
#commands				
	if commands =='/eda'or commands == 'ثانوى ازهرى':
		ky = types.InlineKeyboardMarkup(row_width=2)
		bu = types.InlineKeyboardButton(text='👨‍🔬 الصف الاول ', callback_data='awal')
		bu1 = types.InlineKeyboardButton(text='👨‍🔬 الصف الثاني', callback_data='tanya')
		bu2 = types.InlineKeyboardButton(text='👨‍🔬 الصف الثالث', callback_data='talta')
		u = types.InlineKeyboardButton(text='👑 Developer', url='t.me/UG_U4')
		ky.add(bu , bu1 , bu2,u)
		usr = message.from_user.id
		gg = message.from_user.first_name
		bot.reply_to(message , '🙋 مرحبا بك عزيزى « {} 🇪🇬»\n\n 👈 اختر ما تريد من الازرار.' .format(gg), reply_markup= ky)
	if commands =='/edu'or commands == 'ثانوى عام':
		typ = types.InlineKeyboardMarkup(row_width=2)
		j = types.InlineKeyboardButton(text='👨‍🔬 الصف الاول', callback_data='اول عام')
		k = types.InlineKeyboardButton(text='👨‍🔬 الصف الثاني', callback_data='ثان عام')
		p = types.InlineKeyboardButton(text='👨‍🔬 الصف الثالث', callback_data='ثالث عام')
		u = types.InlineKeyboardButton(text='👑 Developer', url='t.me/UG_U4')
		typ.add(j , k , p , u)
		gg = message.from_user.first_name
		bot.reply_to(message , '🙋 مرحبا بك عزيزى « {} 🇪🇬 »\n\n👈 اختر من الازرار .'.format(gg), reply_markup= typ)
	if commands == '/help' or commands =='المبرمج':
		mobarmeg = types.InlineKeyboardMarkup(row_width=1)
		mob = types.InlineKeyboardButton(text='📲 ¦ المبرمج ¦ 📲', url='https://t.me/UG_U4')
		mobarmeg.add(mob)
		bot.reply_to(message , 'مرحبا بيك يا اخويا / اختي \n\n انا عبد الرحمن عبد الجليل \n\nعندى 17 سنه داخل تانيه ثانوى \n\nحلمي اكون مبرمج كبير وبدات في الطريق ومشيت فيه كويس الحمد لله \n\nالبوت دا هديه لكل اخواتي من كل مكان ولوجه الله ولو محتاج حاجه متترددش اضغط عالزر وشكرا ❤🙂🇪🇬', reply_markup= mobarmeg)
		
#callback_data
#callback_/eda
@bot.callback_query_handler(func= lambda call:True)
def call_data(call):
	if call.message:
		if call.data == 'awal':
			lol = types.InlineKeyboardMarkup(row_width=2)
			lol1 = types.InlineKeyboardButton(text='🖇 ¦ الترم الاول ', callback_data='term1')
			lol2 = types.InlineKeyboardButton(text='🖇 ¦ الترم الثاني', callback_data='term2')
			lol3 = types.InlineKeyboardButton(text='🚶‍♂𝘽𝙖𝙘𝙠', callback_data='ex')
			lol.add(lol1,lol2,lol3)
			user_name = call.from_user.first_name
			bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id , text='🙋 ¦ مرحبا بك عزيزى « {} 🇪🇬» \n\n🚸| اليك عزيزى الاقسام الخاصه بالصف الاول الثانوى الازهرى .'.format(user_name), reply_markup= lol)
#callback_/eda/scond
		elif call.data == 'tanya':
			lp = types.InlineKeyboardMarkup(row_width=2)
			lp1 = types.InlineKeyboardButton(text='🖇 ¦ الترم الاول', callback_data='term11')
			lp2 = types.InlineKeyboardButton(text='🖇 ¦ الترم الثاني', callback_data='term22')
			lp3 = types.InlineKeyboardButton(text='🚶‍♂𝘽𝙖𝙘𝙠', callback_data='ex')
			lp.add(lp1 , lp2 , lp3)
			user_name = call.from_user.first_name
			bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id , text='🙋 ¦ مرحبا بك عزيزى « {} 🇪🇬» \n\n🚸| اليك عزيزى الاقسام الخاصه بالصف الثاني الثانوى الازهرى .'.format(user_name), reply_markup= lp)
#callback_/eda/talta
		elif call.data == 'talta':
			ll = types.InlineKeyboardMarkup(row_width=2)
			ll1 = types.InlineKeyboardButton(text='🖇 ¦ الترم الاول', callback_data='ter1')
			ll2 = types.InlineKeyboardButton(text='🖇 ¦ الترم الثاني', callback_data='ter2')
			ll3 = types.InlineKeyboardButton(text='🚶‍♂𝘽𝙖𝙘𝙠', callback_data='ex')
			ll.add(ll1,ll2,ll3)
			user_name = call.from_user.first_name
			bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id , text='🙋 ¦ مرحبا بك عزيزى « {} 🇪🇬» \n\n🚸| اليك عزيزى الاقسام الخاصه بالصف الثالث الثانوى الازهرى .'.format(user_name), reply_markup= ll)
#callback_/eda/ex
		elif call.data == 'ex':
			ky = types.InlineKeyboardMarkup(row_width=2)
			bu = types.InlineKeyboardButton(text='👨‍🔬 الصف الاول ', callback_data='awal')
			bu1 = types.InlineKeyboardButton(text='👨‍🔬 الصف الثاني', callback_data='tanya')
			bu2 = types.InlineKeyboardButton(text='👨‍🔬 الصف الثالث', callback_data='talta')
			ky.add(bu , bu1 , bu2)
			user_name = call.from_user.first_name
			bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id , text= '🌚 ¦ مرحبا {} بعودتك مجددا..... \n\n👈اختر ما تريد من الاسفل .'.format(user_name), reply_markup=ky)
#callback_/edu/اول عام
		elif call.data == 'اول عام':
			lpg = types.InlineKeyboardMarkup(row_width=2)
			lpg1 = types.InlineKeyboardButton(text='🖇 ¦ الترم الاول', callback_data='trm11')
			lpg2 = types.InlineKeyboardButton(text='🖇 ¦ الترم الثاني', callback_data='trm22')
			lpg3 = types.InlineKeyboardButton(text='🚶‍♂𝘽𝙖𝙘𝙠',
			 callback_data='eee')
			lpg.add(lpg1 , lpg2 , lpg3)
			user_name = call.from_user.first_name
			bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id , text='🙋 ¦ مرحبا بك عزيزى « {} 🇪🇬» \n\n🚸| اليك عزيزى الاقسام الخاصه بالصف الاول الثانوى العام ..'.format(user_name), reply_markup= lpg)
#callback_/edu/ثان عام
		elif call.data =='ثان عام':
			e = types.InlineKeyboardMarkup(row_width=2)
			ee = types.InlineKeyboardButton(text='🖇 ¦ الترم الاول', callback_data='e')
			e2 = types.InlineKeyboardButton(text='🖇 ¦الترم الثاني' , callback_data='ee')
			e3 = types.InlineKeyboardButton(text='🚶‍𝘽𝙖𝙘𝙠', callback_data='eee')
			e.add(ee , e2 , e3)
			user_name = call.from_user.first_name
			bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id , text='🙋 ¦ مرحبا بك عزيزى « {} 🇪🇬» \n\n🚸| اليك عزيزى الاقسام الخاصه بالصف الثاني الثانوى العام ..'.format(user_name), reply_markup= e)
#callback_/edu/ثالث عام
		elif call.data =='ثالث عام':
			x = types.InlineKeyboardMarkup(row_width=2)
			xx = types.InlineKeyboardButton(text='🖇 ¦ الترم الاول', callback_data= 'drop')
			xxx = types.InlineKeyboardButton(text='🖇 ¦ الترم الثاني', callback_data='drop1')
			x3x = types.InlineKeyboardButton(text='🚶‍♂𝘽𝙖𝙘𝙠',callback_data='eee')
			x.add(xx , xxx , x3x)
			user_name = call.from_user.first_name
			bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id , text='🙋 ¦ مرحبا بك عزيزى « {} 🇪🇬» \n\n🚸| اليك عزيزى الاقسام الخاصه بالصف الثالث الثانوى العام ..'.format(user_name), reply_markup= x)
		elif call.data == 'eee':
			typ = types.InlineKeyboardMarkup(row_width=2)
			j = types.InlineKeyboardButton(text='👨‍🔬 الصف الاول', callback_data='اول عام')
			k = types.InlineKeyboardButton(text='👨‍🔬الصف  الثاني', callback_data='ثان عام')
			p = types.InlineKeyboardButton(text='👨‍🔬 الصف الثالث', callback_data='ثالث عام')
			typ.add(j , k ,p )
			user_name = call.from_user.first_name
			bot.edit_message_text(chat_id=call.message.chat.id , message_id=call.message.message_id , text= '🌚 ¦ مرحبا {} بعودتك مجددا..... \n\n👈اختر ما تريد من الاسفل .'.format(user_name), reply_markup=typ)
			
bot.infinity_polling()