#!/usr/bin/env python
import logging
import telegram
import requests
import json
import string
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, VIGENERE_ENCRYPT, VIGENERE_DECRYPT, TYPING_CHOICE, CAESAR_DECRYPT, CAESAR_ENCRYPT , RAIL_DECRYPT, RAIL_ENCRYPT= range(8)

reply_keyboard = [['VIGENERE', 'CAESAR', 'RAIL FENCE']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

reply_keyboard2 = [['MENU'],['SELESAI']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)

reply_keyboard3 = [['ENKRIPSI VIGENERE'],['DEKRIPSI VIGENERE']]
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=True)

reply_keyboard4 = [['ENKRIPSI CAESAR'],['DEKRIPSI CAESAR']]
markup4 = ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=True)

reply_keyboard5 = [['ENKRIPSI RAIL FENCE'],['DEKRIPSI RAIL FENCE']]
markup5 = ReplyKeyboardMarkup(reply_keyboard5, one_time_keyboard=True)

def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def start(update, context):
    update.message.reply_text(
        "Halo, selamat datang di *arcrypto_bot*.\n\n"
        "Chat Bot ini menyediakan layanan kriptografi klasik.\n"
        "Silahkan klik /start untuk memulai, kemudian pilih jenis kriptografi yang diinginkan.",
        reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
        
    return CHOOSING

def regular_choice(update, context):
    x = update.message.text.upper()
    context.user_data['choice'] = x
    if x == 'VIGENERE':
        try:
            update.message.reply_text(
                "Anda mau melakukan enkripsi atau dekripsi?.",
            reply_markup=markup3, parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)

    elif x == 'ENKRIPSI VIGENERE':
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau dienkripsi dengan format *PLAINTEXT#KEY* \n"
            "Contoh: kita bertemu di depan gerbang kampus#secret", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return VIGENERE_ENCRYPT

    elif x == 'DEKRIPSI VIGENERE' :
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau didekripsi dengan format *CIPHERTEXT#KEY* \n"
            "Contoh: CMVRFXJXGDYWAHGGEGYITSEGYOCDTNK#secret", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return VIGENERE_DECRYPT

    elif x == 'CAESAR':
        try:
            update.message.reply_text(
                "Anda mau melakukan enkripsi atau dekripsi?.",
            reply_markup=markup4, parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
            
    elif x == 'ENKRIPSI CAESAR':
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau dienkripsi dengan format *PLAINTEXT#SHIFT* \n"
            "Contoh: kita bertemu di depan gerbang kampus#3", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return CAESAR_ENCRYPT

    elif x == 'DEKRIPSI CAESAR' :
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau didekripsi dengan format *CIPHERTEXT#SHIFT* \n"
            "Contoh: nlwd ehuwhpx gl ghsdq jhuedqj ndpsxv#3", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return CAESAR_DECRYPT

    elif x == 'RAIL FENCE':
        try:
            update.message.reply_text(
                "Anda mau melakukan enkripsi atau dekripsi?.",
            reply_markup=markup5, parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
            
    elif x == 'ENKRIPSI RAIL FENCE':
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau dienkripsi dengan format *PLAINTEXT#KEY* \n"
            "Contoh: kita bertemu di depan gerbang kampus#2", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return RAIL_ENCRYPT

    elif x == 'DEKRIPSI RAIL FENCE' :
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau didekripsi dengan format *CIPHERTEXT#KEY* \n"
            "Contoh: KTBREUIEAGRAGAPSIAETMDDPNEBNKMU#2", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return RAIL_DECRYPT
    
    elif x == 'SELESAI':
        update.message.reply_text(
            "Terimakasih, ketik /start untuk memulai kembali.",
        parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        update.message.reply_text(
            "Klik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup. ",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def vigenere_encrypt(update, context):
    text = update.message.text.upper()
    context.user_data['text'] = text
    pm = 1
    text = text.split("#")
    plaintext = text[0].replace(' ', '')
    key = text[1].replace(' ', '')
    keylen = len(key)
    new = ""
    for i in range(len(plaintext)):
        new += chr((ord(plaintext[i]) + pm * ord(key[i % keylen])) % 26 + 65)
    update.message.reply_text(
    "Hasil ciphertext = "+new, reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def vigenere_decrypt(update, context):
    text = update.message.text.upper()
    context.user_data['text'] = text
    pm = -1
    text = text.split("#")
    ciphertext = text[0].replace(' ', '')
    key = text[1].replace(' ', '')
    keylen = len(key)
    new = ""
    for i in range(len(ciphertext)):
        new += chr((ord(ciphertext[i]) + pm * ord(key[i % keylen])) % 26 + 65)
    update.message.reply_text(
    "Hasil plaintext = "+new, reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def caesar_encrypt(update, context):
    text = update.message.text.upper()
    context.user_data['text'] = text
    arr=string.ascii_letters
    text = text.split("#")
    plaintext = text[0]
    key = text[1].replace(' ', '')
    new=""
    for item in plaintext:
        if item.isalpha():
            new+=arr[(arr.index(item)+int(key))%26]
        else :
            new+=item
    update.message.reply_text(
    "Hasil ciphertext = "+new, reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def caesar_decrypt(update, context):
    text = update.message.text.upper()
    context.user_data['text'] = text
    arr=string.ascii_letters
    text = text.split("#")
    ciphertext = text[0]
    key = text[1].replace(' ', '')
    new = ""
    for item in ciphertext:
        if item.isalpha():
            new+=arr[(arr.index(item)-int(key))%26]
        else :
            new+=item
    update.message.reply_text(
    "Hasil plaintext = "+new, reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def rail_encrypt(update, context):
    text = update.message.text.upper()
    context.user_data['text'] = text
    text = text.split("#")
    plaintext = text[0].replace(' ', '')
    key = int(text[1].replace(' ', ''))
    if key > len(plaintext) or key == 1:
        update.message.reply_text("Key tidak boleh lebih besar dari ukuran pesan\n"
        "pilih key yang lebih kecil.", parse_mode=telegram.ParseMode.MARKDOWN)
    new=""
    increment = 1
    row = 0
    col = 0
    rails = [["" for i in range(len(plaintext))] for j in range(key)]
    for x in plaintext:
        if row + increment < 0 or row + increment >= len(rails):
            increment = increment * -1

        rails[row][col] = x

        row += increment
        col += 1

    for rail in rails:
        new += "".join(rail)
    update.message.reply_text(
    "Hasil ciphertext = "+new, reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def rail_decrypt(update, context):
    text = update.message.text.upper()
    context.user_data['text'] = text
    arr=string.ascii_letters
    text = text.split("#")
    ciphertext = text[0].replace(' ', '')
    key = int(text[1].replace(' ', ''))
    new = ""
    indx = 0
    increment = 1

    rails = [["" for i in range(len(ciphertext))] for j in range(key)]

    for selectedRow in range(0, len(rails)):
        row = 0

        for col in range(0, len(rails[row])):
            if row + increment < 0 or row + increment >= len(rails):
                increment = increment * -1

            if row == selectedRow:
                rails[row][col] += ciphertext[indx]
                indx += 1
            row += increment

    rails = transpose(rails)

    for rail in rails:
        new += "".join(rail)
    update.message.reply_text(
    "Hasil plaintext = "+new, reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def transpose(m):

    new = [[0 for y in range(len(m))] for x in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            new[j][i] = m[i][j]

    return new

def done(update, context):
    update.message.reply_text("Terimakasih!")
    context.user_data.clear()
    return ConversationHandler.END

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater("token:nyadisini", use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(Filters.regex('^(VIGENERE|CAESAR|RAIL FENCE|SELESAI|ENKRIPSI VIGENERE|DEKRIPSI VIGENERE|ENKRIPSI CAESAR|DEKRIPSI CAESAR|ENKRIPSI RAIL FENCE|DEKRIPSI RAIL FENCE)$'),
                                      regular_choice),
                       MessageHandler(Filters.text,
                                      start)
                       ],

            TYPING_CHOICE: [MessageHandler(Filters.text,
                                           regular_choice)
                            ],
            
            VIGENERE_ENCRYPT: [MessageHandler(Filters.text,
                                          vigenere_encrypt),
                           ],

            VIGENERE_DECRYPT: [MessageHandler(Filters.text,
                                          vigenere_decrypt),
                           ],

            CAESAR_ENCRYPT: [MessageHandler(Filters.text,
                                          caesar_encrypt),
                           ],

            CAESAR_DECRYPT: [MessageHandler(Filters.text,
                                          caesar_decrypt),
                           ],

            RAIL_ENCRYPT: [MessageHandler(Filters.text,
                                          rail_encrypt),
                           ],

            RAIL_DECRYPT: [MessageHandler(Filters.text,
                                          rail_decrypt),
                           ],
        },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )  
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()