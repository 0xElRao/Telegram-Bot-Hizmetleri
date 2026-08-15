import telebot
import time

# Telegram @BotFather'dan aldığın bot tokenini buraya yazarsın
TOKEN = "BURAYA_BOT_TOKEN_YAZ"
bot = telebot.TeleBot(TOKEN)

# Mesaj atılacak kanal veya grup kullanıcı adı
CHAT_ID = "@kanal_adi_buraya" 
MESAJ = "Merhaba! Bu mesaj otomatik bot tarafından gönderilmiştir."

print("Bot çalışıyor...")

while True:
    try:
        bot.send_message(CHAT_ID, MESAJ)
        print("Mesaj başarıyla gönderildi!")
        time.sleep(3600)  # 3600 saniye = 1 saatte bir mesaj atar
    except Exception as e:
        print("Hata oluştu:", e)
        time.sleep(10)
      
