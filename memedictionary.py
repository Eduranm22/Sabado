meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LMAO": "Otra respuesta común a algo gracioso",
            "RIZZ": "La capacidad de atraer a una pareja romántica o sexual",
            "CREEPY": "Aterrador, siniestro",
            "SHEESH": "Ligera desaprobacion",
            "AGGRO": "ponerse agresivo/enojado"
            }
 
for i in range(5):           
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Esta palabra no esta en el diccionario!')
