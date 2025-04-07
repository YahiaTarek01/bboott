import telebot
from rapidfuzz import fuzz
API_TOKEN = '7698088733:AAFa_kPXw844d4sknOftr3X-M04b0AJeuB0'

bot = telebot.TeleBot(API_TOKEN)

qa_pairs = {
    "السلام عليكم": "وعليكم السلام كيف يمكنني أن أساعدك؟",
    "انا اشتريت تليفون هواوي 7 2018 وبعد لما فتحته بجرب الكاميرا لقيتها مش شغالة": "آسف أنك واجهت المشكلة دي، يُرجى التحقق من إعدادات الكاميرا وعمل سينسار للجهاز وإذا استمرت المشكلة بنصحك بزيارة أقرب فرع.",
    "طب انا اللي هروح الفرع ولا في مندوب هيجي ياخد الموبايل": "بصراحة يا فندم الموبايل مش من الحالات اللي بيبعت فيها مندوب بس تقدر تروح أقرب فرع.",
    "طب لو ما فيش فرع قريب مني أعمل ايه": "تمام عشان ترجع المنتج هتخش على اللينك ده وهتملا البيانات: https://btech-logic-production.up.railway.app/",
    "تمام": "تحتاج الى المساعدة مرة أخرى؟",
    "عفوا": "تحتاج الى المساعدة مرة أخرى؟"
}

def get_best_match(user_input):
    best_score = 0
    best_response = "معذرة، لم أفهم سؤالك. حاول مرة أخرى."
    for question, answer in qa_pairs.items():
        score = fuzz.ratio(user_input, question)
        if score > best_score and score > 70:
            best_score = score
            best_response = answer
    return best_response

@bot.message_handler(func=lambda message: True)
def respond_to_question(message):
    text = message.text.strip()
    response = get_best_match(text)
    bot.reply_to(message, response)

bot.polling()
