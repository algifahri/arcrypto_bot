#!/usr/bin/env python
#!/usr/bin/env python
import logging
import telegram
import requests
import json
import string
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from Crypto.Cipher import DES
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
import Crypto.Random
import Crypto.Random.random
from Crypto.PublicKey import ElGamal
import base64

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, VIGENERE_ENCRYPT, VIGENERE_DECRYPT, TYPING_CHOICE, CAESAR_DECRYPT, CAESAR_ENCRYPT , RAIL_DECRYPT, RAIL_ENCRYPT, DES_ENCRYPT, DES_DECRYPT, DES3_ENCRYPT, DES3_DECRYPT, AES_ENCRYPT, AES_DECRYPT, RSA_KEY, RSA_ENCRYPT, RSA_DECRYPT, ELGAMAL_KEY = range(18)

reply_keyboard = [['VIGENERE', 'CAESAR', 'RAIL FENCE'],['DES','AES','DES3'],['RSA','ELGAMAL']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

reply_keyboard2 = [['MENU'],['SELESAI']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)

reply_keyboard3 = [['ENKRIPSI VIGENERE'],['DEKRIPSI VIGENERE']]
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=True)

reply_keyboard4 = [['ENKRIPSI CAESAR'],['DEKRIPSI CAESAR']]
markup4 = ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=True)

reply_keyboard5 = [['ENKRIPSI RAIL FENCE'],['DEKRIPSI RAIL FENCE']]
markup5 = ReplyKeyboardMarkup(reply_keyboard5, one_time_keyboard=True)

reply_keyboard6 = [['ENKRIPSI DES'],['DEKRIPSI DES']]
markup6 = ReplyKeyboardMarkup(reply_keyboard6, one_time_keyboard=True)

reply_keyboard7 = [['ENKRIPSI AES'],['DEKRIPSI AES']]
markup7 = ReplyKeyboardMarkup(reply_keyboard7, one_time_keyboard=True)

reply_keyboard8 = [['ENKRIPSI DES3'],['DEKRIPSI DES3']]
markup8 = ReplyKeyboardMarkup(reply_keyboard8, one_time_keyboard=True)

reply_keyboard9 = [['GENERATE KEY RSA'],['ENKRIPSI RSA'],['DEKRIPSI RSA']]
markup9 = ReplyKeyboardMarkup(reply_keyboard9, one_time_keyboard=True)

def start(update, context):
    update.message.reply_text(
        "Halo, selamat datang di *arcrypto_bot*.\n\n"
        "Chat Bot ini menyediakan layanan kriptografi.\n"
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
    
    elif x == 'DES':
        try:
            update.message.reply_text(
                "Anda mau melakukan enkripsi atau dekripsi?.",
            reply_markup=markup6, parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
            
    elif x == 'ENKRIPSI DES':
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau dienkripsi dengan format *PLAINTEXT#KEY* \n"
            "KEY *minimal* 1 *maximal* 8 karakter \n"
            "Contoh: *kita bertemu di depan gerbang kampus#password*\n"
            "Note: Hasil enkripsi diubah menjadi bentuk base64", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return DES_ENCRYPT

    elif x == 'DEKRIPSI DES' :
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau didekripsi dengan format *CIPHERTEXT#KEY* \n"
            "KEY *minimal* 1 *maximal* 8 karakter \n"
            "Contoh: 3nU7Sr4mMQU4OnYmUhxXTpijNH9+NRigCJz+uvm/rUSAx6bdin40ew==#password", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return DES_DECRYPT
        
    elif x == 'AES':
        try:
            update.message.reply_text(
                "Anda mau melakukan enkripsi atau dekripsi?.",
            reply_markup=markup7, parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
            
    elif x == 'ENKRIPSI AES':
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau dienkripsi dengan format *PLAINTEXT#KEY* \n"
            "KEY *minimal* 9 *maximal* 32 karakter \n"
            "Contoh: *kita bertemu di depan gerbang kampus#password12345678*\n"
            "Note: Hasil enkripsi diubah menjadi bentuk base64", parse_mode=telegram.ParseMode.MARKDOWN)
            
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return AES_ENCRYPT

    elif x == 'DEKRIPSI AES' :
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau didekripsi dengan format *CIPHERTEXT#KEY* \n"
            "KEY *minimal* 9 *maximal* 32 karakter \n"
            "Contoh: TC1zAKDQoYxY5iBzLXTYPF7rYJ/zcZvHRunqrg4TqLnvbmMy5rIr9ZTP1QgQpvNu==#password12345678", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return AES_DECRYPT
    
    elif x == 'DES3':
        try:
            update.message.reply_text(
                "Anda mau melakukan enkripsi atau dekripsi?.",
            reply_markup=markup8, parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)

    elif x == 'ENKRIPSI DES3':
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau dienkripsi dengan format *PLAINTEXT#KEY* \n"
            "KEY *minimal* 9 *maximal* 24 karakter \n"
            "Contoh: *kita bertemu di depan gerbang kampus#password12345678*\n"
            "Note: Hasil enkripsi diubah menjadi bentuk base64", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return DES3_ENCRYPT

    elif x == 'DEKRIPSI DES3' :
        try:
            update.message.reply_text(
            "Ketikkan kata yang mau didekripsi dengan format *CIPHERTEXT#KEY* \n"
            "KEY *minimal* 9 *maximal* 24 karakter \n"
            "Contoh: Ovqw+n1mc87eiCLN7yr0DvjRohAk0q94iXpoMhaND9+gNAamfKUIRA==#password12345678", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return DES3_DECRYPT
    
    elif x == 'RSA':
        try:
            update.message.reply_text(
                "Anda harus memiliki Public Key dan Private Key terlebih dahulu\n"
                "Untuk itu, anda perlu melakukan *GENERATE KEY*\n (lewati langkah ini jika sudah memiliki Public Key dan Private Key)\n\n"
                "Public Key digunakan untuk proses Enkripsi dan Private Key digunakan untuk proses Dekripsi\n",
                reply_markup=markup9, parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)

    elif x == 'GENERATE KEY RSA':
        try:
            update.message.reply_text(
                "Anda harus *GENERATE KEY* terlebih dahulu\n"
                "Ketikkan panjang key dengan format *KEY_SIZE*\n"
                "Contoh: *1024*\n\n"
                "Key Size harus *kelipatan* 256, *minimal* 1024, dan *maximal* 4096"
            ,parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return RSA_KEY

    elif x == 'ENKRIPSI RSA':
        try:
            update.message.reply_text(
                "Ketikkan kata yang mau dienkripsi dengan format *PLAINTEXT#PUBLIC_KEY*\n"
                "Public Key termasuk -----BEGIN PUBLIC KEY----- dan -----END PUBLIC KEY-----\n\n"
                "Note: Hasil enkripsi diubah menjadi bentuk base64", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return RSA_ENCRYPT

    elif x == 'DEKRIPSI RSA' :
        try:
            update.message.reply_text(
                "Ketikkan kata yang mau didekripsi dengan format *CIPHERTEXT#PRIVATE_KEY*\n"
                "Private Key termasuk -----BEGIN RSA PRIVATE KEY----- dan -----END RSA PRIVATE KEY-----\n\n", parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return RSA_DECRYPT

    elif x == 'ELGAMAL':
        try:
            update.message.reply_text(
                "*Ayo bermain simulasi ElGamal..!!*\n"
                "Masukkan pesan berupa angka dan panjang key elgamal dengan format *PESAN#PANJANG_KUNCI*\n\n"
                "Contoh: 20172021#128"
                ,parse_mode=telegram.ParseMode.MARKDOWN)
        except:
            update.message.reply_text(
                "Klik *MENU* untuk kembali ke menu awal, atau klik *SELESAI* jika sudah cukup.",
            reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
        return ELGAMAL_KEY

    elif x == 'SELESAI':
        update.message.reply_text(
            "Terimakasih, ketik /start untuk memulai kembali.",
        parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        update.message.reply_text(
            "Klik *MENU* untuk mendapatkan informasi lainnya, atau klik *SELESAI* jika sudah cukup. ",reply_markup=markup2,parse_mode=telegram.ParseMode.MARKDOWN)
    return CHOOSING

def vigenere_encrypt(update, context):
    try:
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
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup3, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def vigenere_decrypt(update, context):
    try:
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
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup3, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def caesar_encrypt(update, context):
    try:
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
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup4, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def caesar_decrypt(update, context):
    try:
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
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup4, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def rail_encrypt(update, context):
    try:
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
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup5, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def rail_decrypt(update, context):
    try:
        text = update.message.text.upper()
        context.user_data['text'] = text
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
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup5, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def transpose(m):

    new = [[0 for y in range(len(m))] for x in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            new[j][i] = m[i][j]

    return new

def des_encrypt(update, context):
    try:
        BS = DES.block_size
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        text = update.message.text
        context.user_data['text'] = text
        text = text.split("#")
        plaintext = pad(text[0])
        key = text[1]
        if len(key) > 8:
            update.message.reply_text(
            "KEY *minimal* 1 *maximal* 8 karakter", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
        else:
            while len(key) % 8 != 0:
                key += ' '
            des = DES.new(key, DES.MODE_ECB)
            new=base64.b64encode(des.encrypt(plaintext))
            enc=new.decode('utf-8')
            update.message.reply_text(
                "Hasil ciphertext = *" + enc +"*", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup6, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def des_decrypt(update, context):
    try:
        BS = DES.block_size
        text = update.message.text
        context.user_data['text'] = text
        text = text.split("#")
        ciphertext = text[0]
        key = text[1]
        if len(key) > 8:
            update.message.reply_text(
                "KEY *minimal* 1 *maximal* 8 karakter", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
        else:
            while len(key) % 8 != 0:
                key += ' '
            des = DES.new(key, DES.MODE_ECB)
            new=des.decrypt(base64.b64decode(ciphertext))
            dec=new.decode('utf-8')
            update.message.reply_text(
                "Hasil plaintext = *" + dec +"*", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup6, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def aes_encrypt(update, context):
    try:
        BS = AES.block_size
        PADDING = ' '
        pad = lambda s: s + (BS - len(s) % BS) * PADDING
        text = update.message.text
        context.user_data['text'] = text
        text = text.split("#")
        plaintext = pad(text[0])
        key = text[1]
        if len(key) < 9 or len(key) > 32:
            update.message.reply_text(
                "KEY *minimal* 9 *maximal* 32 karakter", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
        else:
            while len(key) % 8 != 0:
                key += ' '
            aes = AES.new(key, AES.MODE_ECB)
            new=base64.b64encode(aes.encrypt(plaintext))
            enc=new.decode('utf-8')
            update.message.reply_text(
                "Hasil ciphertext = *" + enc +"*", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup7, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING        

def aes_decrypt(update, context):
    try:
        BS = AES.block_size
        text = update.message.text
        context.user_data['text'] = text
        text = text.split("#")
        ciphertext = text[0]
        key = text[1]
        if len(key) < 9 or len(key) > 32:
            update.message.reply_text(
                "KEY *minimal* 9 *maximal* 32 karakter", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
        else:
            while len(key) % 8 != 0:
                key += ' '
            aes = AES.new(key, AES.MODE_ECB)
            new=aes.decrypt(base64.b64decode(ciphertext))
            dec=new.decode('utf-8')
            update.message.reply_text(
                "Hasil plaintext = *" + dec +"*", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup7, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def des3_encrypt(update, context):
    try:
        BS = DES3.block_size
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        text = update.message.text
        context.user_data['text'] = text
        text = text.split("#")
        plaintext = pad(text[0])
        key = text[1]
        if len(key) < 9 or len(key) > 24:
            update.message.reply_text(
            "KEY *minimal* 9 *maximal* 24 karakter \n", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
        else:
            while len(key) % 8 != 0:
                key += ' '
            des = DES3.new(key, DES3.MODE_ECB)
            new=base64.b64encode(des.encrypt(plaintext))
            enc=new.decode('utf-8')
            update.message.reply_text(
                "Hasil ciphertext = *" + enc +"*", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup8, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def des3_decrypt(update, context):
    try:
        BS = DES3.block_size
        text = update.message.text
        context.user_data['text'] = text
        text = text.split("#")
        ciphertext = text[0]
        key = text[1]
        if len(key) < 9 or len(key) > 24:
            update.message.reply_text(
            "KEY *minimal* 9 *maximal* 24 karakter \n", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
        else:
            while len(key) % 8 != 0:
                key += ' '
            des = DES3.new(key, DES3.MODE_ECB)
            new=des.decrypt(base64.b64decode(ciphertext))
            dec=new.decode('utf-8')
            update.message.reply_text(
                "Hasil plaintext = *" + dec +"*", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup8, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def rsa_key(update, context):
    try:
        text = update.message.text
        if (int(text)%8 != 0) and (int(text)<1024) and (int(text)>4096):
            update.message.reply_text(
                "Key Size harus *kelipatan* 256, *minimal* 1024, dan *maximal* 4096", reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
        else:
            key = RSA.generate(int(text), e=65537)
            private_key = key.exportKey("PEM").decode("utf-8")
            public_key = key.publickey().exportKey("PEM").decode("utf-8")
            update.message.reply_text(
                "*" + public_key +"*\n\n"
                "*" + private_key + "*\n\n"
                "NB: Simpan Public Key dan Private Key diatas.\n"
                "Public Key digunakan untuk proses Enkripsi dan Private Key digunakan untuk proses Dekripsi"
                ,reply_markup=markup9, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup9, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def rsa_encrypt(update, context):
    try:
        text = update.message.text
        context.user_data['text'] = text
        text = text.split("#")
        plaintext = text[0].encode("utf-8")
        public_key = text[1].replace(' ', '').encode("utf-8")
        key = RSA.importKey(public_key)
        cipher = PKCS1_v1_5.new(key)
        enc = base64.b64encode(cipher.encrypt(plaintext)).decode("utf-8")
        update.message.reply_text(
            "Hasil ciphertext = *" + enc +"*"
            ,reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup9, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def rsa_decrypt(update, context):
    try:
        text = update.message.text
        context.user_data['text'] = text
        text = text.split("#")
        ciphertext = base64.b64decode(text[0].encode("utf-8"))
        private_key = text[1].replace(' ', '').encode("utf-8")
        key = RSA.importKey(private_key)
        cipher = PKCS1_v1_5.new(key)
        dec = cipher.decrypt(ciphertext,"decryption error").decode("utf-8")
        update.message.reply_text(
            "Hasil plaintext = *" + dec +"*"
            ,reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup9, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def elgamal_key(update, context):
    try:
        text = update.message.text
        name = update.message.chat.first_name
        context.user_data['text'] = text
        text = text.split("#")
        plaintext = int(text[0])
        key = int(text[1])
        
        if(key<4):
            update.message.reply_text(
                "Panjang kunci anda terlalu kecil"
            ,reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
            return CHOOSING
        else:
            private_key = ElGamal.generate(int(key), Random.new().read)
            public_key = private_key.publickey()
            
            p = ('p')
            p_out = "\n".join(["{} = {}".format(comp, getattr(private_key, comp)) for comp in p])
            gx = ('g','x')
            gx_out = "\n".join(["{} = {}".format(comp, getattr(private_key, comp)) for comp in gx])
            y = ('y')
            y_out = "\n".join(["{} = {}".format(comp, getattr(private_key, comp)) for comp in y])

            p_if = int(p_out.replace('p = ', ''))
            if (plaintext<1) or (plaintext>p_if-1):
                update.message.reply_text(
                    "Pesan tidak boleh lebih kecil dari 1 atau lebih besar dari P \n"
                    "Kurangin angka pesan anda atau naikkan nilai panjang kunci"
                ,reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
                return CHOOSING
            else:
                update.message.reply_text(
                    "Pertama, "+name+" memilih angka prima (p)\n"+p_out,parse_mode=telegram.ParseMode.MARKDOWN)
                update.message.reply_text(
                    "Kemudian, "+name+" memilih dua buah bilangan acak (g) dan (x) dengan syarat g < p dan x diantara 1 sampai p-2\n"
                    +gx_out+"\n*x adalah private key*, bersifat rahasia dan digunakan untuk proses dekripsi"
                ,parse_mode=telegram.ParseMode.MARKDOWN)
                update.message.reply_text(
                    "Kemudian, "+name+" menghitung nilai y dengan rumus y=g^x mod p\n"
                    +y_out+"\n*y adalah public key*, boleh di bagikan dan digunakan untuk proses enkripsi"
                ,parse_mode=telegram.ParseMode.MARKDOWN)
                    
                update.message.reply_text(
                    ""+name+" ingin mengirim pesan kepada Alice berupa angka "+text[0]
                ,parse_mode=telegram.ParseMode.MARKDOWN)
                    
                k = Crypto.Random.random.StrongRandom().randint(1,public_key.p-1)
                enc = public_key.encrypt(plaintext,k)
                dec = private_key.decrypt(enc)

                update.message.reply_text("Kemudian "+name+" melakukan enkripsi menggunakan public key (y) dengan hasil enkripsi seperti dibawah ini",parse_mode=telegram.ParseMode.MARKDOWN)
                update.message.reply_text(str(enc),parse_mode=telegram.ParseMode.MARKDOWN)
                
                update.message.reply_text("Hasil enkripsi tersebut dikirimkan kepada Alice.\n"
                "Kemudian, Alice melakukan dekripsi menggunakan private key (x) dengan hasil dibawah ini",parse_mode=telegram.ParseMode.MARKDOWN)
                update.message.reply_text(str(dec),reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)

                return CHOOSING
    except:
        update.message.reply_text(
            "Perintah yang anda masukkan salah"
            ,reply_markup=markup, parse_mode=telegram.ParseMode.MARKDOWN)
        return CHOOSING

def done(update, context):
    update.message.reply_text("Terimakasih!")
    context.user_data.clear()
    return ConversationHandler.END

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater("1344373576:AAF3EKRHrKLzuINVKMTCqPr9fzNSgqESLRI", use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(Filters.regex('^(VIGENERE|CAESAR|RAIL FENCE|DES|AES|DES3|RSA|ELGAMAL|SELESAI|ENKRIPSI VIGENERE|DEKRIPSI VIGENERE|ENKRIPSI CAESAR|DEKRIPSI CAESAR|ENKRIPSI RAIL FENCE|DEKRIPSI RAIL FENCE|ENKRIPSI DES|DEKRIPSI DES|ENKRIPSI AES|DEKRIPSI AES|ENKRIPSI DES3|DEKRIPSI DES3|GENERATE KEY RSA|ENKRIPSI RSA|DEKRIPSI RSA|)$'),
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

            DES_ENCRYPT: [MessageHandler(Filters.text,
                                          des_encrypt),
                           ],

            DES_DECRYPT: [MessageHandler(Filters.text,
                                          des_decrypt),
                           ],
            
            DES3_ENCRYPT: [MessageHandler(Filters.text,
                                          des3_encrypt),
                           ],

            DES3_DECRYPT: [MessageHandler(Filters.text,
                                          des3_decrypt),
                           ],

            AES_ENCRYPT: [MessageHandler(Filters.text,
                                          aes_encrypt),
                           ],

            AES_DECRYPT: [MessageHandler(Filters.text,
                                          aes_decrypt),
                           ],    

            RSA_KEY: [MessageHandler(Filters.text,
                                          rsa_key),
                           ],

            RSA_ENCRYPT: [MessageHandler(Filters.text,
                                          rsa_encrypt),
                           ],

            RSA_DECRYPT: [MessageHandler(Filters.text,
                                          rsa_decrypt),
                           ],

            ELGAMAL_KEY: [MessageHandler(Filters.text,
                                          elgamal_key),
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
