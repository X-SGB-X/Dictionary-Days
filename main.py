meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya karşılık verilen cevap, gerçek hayatta gülmek",
    "SHEESH": "Onaylamamak, şaşırmak veya hafif bir hayret ifadesi",
    "CREEPY": "Korkutucu, ürkütücü bir şey",
    "AGGRO": "Sinirlenmek, agresifleşmek",
    "NOOB": "Yeni başlayan, acemi kişi",
    "GG": "Good Game - iyi oyundu, genelde oyun sonunda söylenir",
    "AFK": "Klavyeden uzakta - şuan bilgisayar başında değilim",
    "BRB": "Hemen dönüyorum - kısa bir ara için",
}

word = input("Anlamadığınız bir kelime yazın (hepsini BÜYÜK HARFLE yazın!): ").upper()

if word in meme_dict.keys():
    print("\n{} kelimesinin anlamı: {}".format(word, meme_dict[word]))
else:
    print("\nÜzgünüz, '{}' kelimesinin anlamını bilmiyoruz. Sözlüğümüzü güncelleyeceğiz! 😊".format(word))
