rsi = int(input("Masukkan besar RSI: "))
if rsi >= 70 : 
    rsi = "sell"
elif rsi <= 30 :
    rsi = "buy"
else :
    rsi = "pak bejo"

macd = input("Masukkan kondisi MACD: ")
if macd == "death-cross":
    macd = "sell"
elif macd == "golden-cross":
    macd = "buy"
else :
    macd = "bu bejo"

if rsi == "sell" and macd == "sell" :
    print ("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya Jual")
elif rsi == "sell" and macd == "buy" :
    print ("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai death-cross")
elif rsi == "buy" and macd == "sell" :
    print ("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD sampai golden-cross")
elif rsi == "buy" and macd == "buy" :
    print ("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya Beli")
else :
    print ("RSI berada di area 30 - 70, Bukan saatnya membeli maupun menjual")