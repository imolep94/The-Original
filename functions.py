class main:
    def __init__(self, api_id, api_hash, api_session, CW_ids:dict={}):
        import logging
        log = logging.getLogger()
        
        self.api_id = api_id
        self.api_hash = api_hash
        self.api_session = api_session

        from pyrogram import Client, MessageHandler, Filters
        from pyrogram.api import functions
        from numpy.random import randint
        
        import re
        import time
        from datetime import datetime
        import os
        import random
        from pyrogram.errors import AuthKeyUnregistered, MessageIdInvalid, AuthKeyDuplicated

        app = Client(api_session, api_id, api_hash)
        try:
            app.start()
        except AuthKeyUnregistered:
            log.warning("Han desactivado este HASH: "+api_session)
            return
        except AuthKeyDuplicated:
            raise Exception("ERROR!! HASH DUPLICADO" + api_session)
        ids = {}

       
        me=app.get_me()
        me.username = me.username if me.username else me.first_name

        """
        CW CODE
        """

        ids["CW"] = 408101137 #game
        # ids["CastleOrders"] = -1001155831076 #Lupus
        ids["Auction"] = -1001209424945 #Auctions
        # ids["Grup"] = -1001386769293 #Coffee Break Guild Chat
        # ids["Canal"] = -1001194163201 #Coffee Break Guild Channel
        # ids["Caza"] = 807376493 #Botdecaza
        ids["helper"] = 1967904059#1242346205#1137518285 #Bot de ayuda dreadwitch
        # ids["RangerSquad"] = -1001227862489
        # ids["spam_CB"] = -423693600
        # ids["grup_mm"] = -1001274004593
        try:
            ids.update(CW_ids)
        except:
            log.warning("CW_ids not found or is an incorrect dict")

        GC = True if (me.id == 645258806) else False
        GCmm = True if (me.id == 883822191) else False
        auto_quest=False
        caza=False
        quest="⛰️Valley" if ((me.id == 645258806) or (me.id == 740687108)) else ("🌲Forest" if  (me.id == 645258856) else "🍄Swamp")
        level=30
        ff=True
        collector = True if ((me.id == 802156685) or (me.id == 740687108) or (me.id == 955268100)or (me.id == 953357637)or (me.id == 925069789)) else False 
        ambush =False
        Blacksmith =True if (me.id == 645258806) else False
        en_quest=False
        gast_stmn=True
        sentinela = True if ((me.id == 609697213) or (me.id == 705724375) or (me.id == 434324721)) else False
        tactics = "/tactics_eagles"
        cod_trader = "09" if (me.id == 873541475) else ("55" if (me.id == 434324721) else "41")
        trader = True if ((me.id == 609697213) or (me.id == 705724375) or (me.id == 434324721)) else False
        ofertas = True if ((me.id == 774368292) or (me.id == 716287267)) else False
        knight = True if ((me.id == 835010542) or (me.id == 953357637)) else False
        ranger = True if ((me.id == 774368292) or (me.id == 609697213) or (me.id == 434324721) or (me.id == 705724375)) else False
        ordenes = False if ranger else True 
        tregua = True
        rango_max = 6
        dice = False
        general = True if me.id == 835010162 else False
        general2 = True if me.id == 609697213 else False
        orden_adelantada = False
        #defensores = True if ((me.id == 983997362) or (me.id == 913237756) or (me.id == 883822191) or (me.id == 896337255)) else False  
        defensores = False  
        apuntar = False
        pet = True if me.id == 774368292 else False 
        gopher = False 
        warra = True if me.id == 645258806 else False
        pasapasa = False
        vago = True if me.id == 774368292 else False
        envio_rep = True if vago else False
        

        import time
        # def cazar(mensaje):
        #     nonlocal level, ids, rango_max
        #     has_link = False
        #     if mensaje.edit_date: return None
        #     if re.search("lvl\.([0-9]+)", mensaje.text):
        #         mob_info = int(re.findall("lvl\.([0-9]+)", mensaje.text)[0])
        #         log.info (mob_info)
        #     else:
        #         mob_info = 999
        #         log.info ('No level encontrado en caza')
            
        #     if mensaje.reply_markup:
        #         if mensaje.reply_markup.inline_keyboard:
        #             if re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url):
        #                 has_link=re.search("(\/fight_[A-z0-9]+)",mensaje.reply_markup.inline_keyboard[0][0].url).group()
            
        #     if int(level-10)< mob_info < int(level+rango_max):
        #         if re.search("an ambush\!", mensaje.text):
        #             if GC or int(level)>mob_info:
        #                 if has_link:
        #                     app.send_message(ids["CW"], str(has_link))
        #                 else:
        #                     mensaje.forward(ids["CW"])
        #             else:
        #                 time.sleep(abs(int(level)-mob_info))
        #                 if has_link:
        #                     app.send_message(ids["CW"], str(has_link))
        #                 else:
        #                     mensaje.forward(ids["CW"])
        #         else:
        #             if has_link:
        #                 app.send_message(ids["CW"], str(has_link))
        #             else:
        #                 mensaje.forward(ids["CW"])

        # def programar_ataque(mensaje, timer:int=randint(3, 7)):
        #     nonlocal app, ids
        #     try:
        #         orden_list=re.search("(⚔Attack) ([^\w\d\s]+)(\w+)",mensaje)
        #         if orden_list:
        #             orden_list=orden_list.groups()
        #             time.sleep(timer-2)
        #             app.send_message(ids["Canal"], "#atk_"+orden_list[2].lower())
        #             time.sleep(timer-2)
        #             app.send_message(ids["CW"], orden_list[0])
        #             time.sleep(timer-2)
        #             app.send_message(ids["CW"], orden_list[1])
        #         else:
        #             log.warning("No detecto el formato de ataque"+mensaje)
        #     except:
        #         log.warning("Alerta: El ataque no ha sido programado.")

        # def orden_adelant(mensaje, timer:int=randint(3, 7)):
        #     nonlocal app, ids
        #     try:
        #         orden_list=re.search("(⚔Attack) ([^\w\d\s]+)(\w+)",mensaje)   
        #         if orden_list:
        #             orden_list=orden_list.groups()
        #             time.sleep(timer-2)
        #             app.send_message(ids["Canal"], "#atkad_"+orden_list[2].lower())
        #             time.sleep(timer-2)
        #             app.send_message(ids["CW"], orden_list[0])
        #             time.sleep(timer-2)
        #             app.send_message(ids["CW"], orden_list[1])
        #         else:
        #             log.warning("No detecto el formato de ataque"+mensaje)
        #     except:
        #         log.warning("Alerta: El ataque no ha sido programado.")

       
        def reporte():
            nonlocal ids, app, ordenes, auto_quest, caza, level, GC, GCmm, quest, ff, ambush, Blacksmith, en_quest, gast_stmn, sentinela, tactics, cod_trader, trader, ofertas, dice, apuntar, pet, gopher, log
            app.send_message(ids["helper"], "Hola, las funciones de ayuda al CW están activadas"+"\n"+
                 ("El autoquest a "+str(quest)+" está activado" if auto_quest else "El autoquest está desactivado")+"\n"+
                 ("Las órdenes automáticas están activadas" if ordenes else "Las órdenes automáticas están desactivadas")+"\n"+
                 ("Captarás las órdenes adelantadas de Ranger" if apuntar else "No captarás las órdenes adelantadas de Ranger")+"\n"+
                 ("La caza de mobs está activada" if caza else "La caza de mobs se encuentra desactivada")+"\n"+
                 "El level medio para la caza y ayuda en ambush fijado es: "+str(level)+"\n"+
                 ("La autoarena está activada" if ff else "La autoarena está desactivada")+"\n"+
                 ("La ayuda a las ambush está activada" if ambush else "La ayuda a las ambush está desactivada")+"\n"+
                 ("Se activará el loop de quest cuando se llene la stamina" if ordenes else "No se activará el loop de quest cuando se llene la stamina")+"\n"+
                 ("Las tactics fijadas son: "+tactics if sentinela else "Métele al /mem para que seas sentí con tactics 😜")+"\n"+
                 ("Las ofertas del auction se encuentran activadas" if ofertas else "Las ofertas del auction se encuentran desactivadas")+"\n"+ 
                 ("Deja el invento que tú no eres sentinela /mem 🌚 no vas a vender "+cod_trader if not sentinela else ("El trader se encuentra activado con el recurso: "+cod_trader if trader else "El trader se encuentra desactivado"))+"\n"+
                 ("El loop de los dados se encuentra activado" if dice else "El loop de los dados se encuentra desactivado")+"\n"+
                 ("La diversión y el baño de tu mascota está en mis manos 😘"+"\n" if pet else "")+
                 ("Las funciones del GC se encuentran activadas" if GC else "Las funciones del GC se encuentran desactivadas"))


        # def mascota():
        #     nonlocal ids, app, pet, log
        #     timer = randint(1, 60) 
        #     while pet:
        #         app.send_message(ids["CW"], "/pet")
        #         time.sleep(2)
        #         app.send_message(ids["CW"], "⚽Play")
        #         time.sleep(2)
        #         app.send_message(ids["CW"], "🛁Clean")
        #         time.sleep(7200+timer)
                
        def selector_CW(message):
            nonlocal ids, app, ordenes, auto_quest, caza, level, GC, GCmm, quest, ff, ambush, Blacksmith, en_quest, gast_stmn, sentinela, tactics, cod_trader, trader,ofertas, knight, collector, ranger, tregua, rango_max, dice, general, general2, orden_adelantada, defensores, apuntar, pet, warra, pasapasa, envio_rep, gopher, vago, log
            
            mensaje = message
            timer = randint(3, 7)
            tiempo = randint(7, 60)
            open_shop = randint(240,500)
            tiempo_or = randint(5,600)
            timer_aq = randint(1, 60) 
            timer_rep = randint (1, 700)

            if (mensaje.chat.id==ids["CW"]) and (mensaje.from_user.id==ids["CW"]): #Game
                if "Congratulations! You are still alive." in mensaje.text: #Para que cuando llegue de un ambush diga con /f_report cómo fue la batalla y con /whois quién ayudo 
                    app.send_message(ids["CW"], '/f_report')
                    time.sleep(timer)  
                    mensaje.reply('/whois')
                elif ('You were strolling around on your horse' in mensaje.text): # El más importante para que cuando llegue un foray de alguien más responda /go
                    auto_quest=False
                    time.sleep(tiempo)
                    mensaje.click(0)
                elif '/pledge' in mensaje.text: # Para que cuando llegue un pledge a un knight lo coja
                    mensaje.reply('/pledge')
                elif 'Leaderboard of fighters' in mensaje.text and ff: # Loop para ir a la arena cuando da resultado de arena
                    time.sleep(timer)  
                    mensaje.reply('▶️Fast fight')
                elif 'You didn’t find an opponent. Return later.' in mensaje.text and ff:
                    time.sleep(timer)
                    mensaje.reply('▶️Fast fight')
                # elif re.search("an ambush\!", mensaje.text):
                #     mensaje.forward(ids["spam_CB"])
                # elif 'You met some hostile creatures.' in mensaje.text:
                #     mensaje.forward(ids["spam_CB"])
                #     time.sleep(10+timer)
                #     mensaje.forward(ids["Caza"])

                ###################################################################                    
                # elif "Class info: /class" in mensaje.text:
                #     if (re.search(".+?🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹.+?Class info: /class", mensaje.text)) or (re.search("🏹+Class info: /class", mensaje.text)):
                #         ranger = True
                #     else:
                #         ranger = False

                #     if (re.search(".+?⚔️.+?Class info: /class", mensaje.text)) or (re.search("⚔️.+?Class info: /class", mensaje.text)) or (re.search("⚔️+Class info: /class", mensaje.text)):
                #         knight = True  
                #     else:
                #         knight = False                

                #     if (re.search(".+?🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡.+?Class info: /class", mensaje.text)) or (re.search("🛡+Class info: /class", mensaje.text)):
                #         sentinela = True
                #     else:
                #         sentinela = False
                    
                #     if (re.search(".+?⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️.+?Class info: /class", mensaje.text)) or (re.search("⚗️+Class info: /class", mensaje.text)):
                #         alch = True
                #     else:
                #         alch = False
                    
                #     if (re.search(".+?📦.+?Class info: /class", mensaje.text)) or (re.search("📦.+?Class info: /class", mensaje.text)) or (re.search("📦+Class info: /class", mensaje.text)):
                #         collector = True
                #     else:
                #         collector = False
                    
                #     if (re.search(".+?⚒.+?Class info: /class", mensaje.text)) or (re.search("⚒.+?Class info: /class", mensaje.text)) or (re.search("⚒+Class info: /class", mensaje.text)):
                #         Blacksmith = True
                #     else:
                #         Blacksmith = False
                    
                #     time.sleep(timer)
                #     app.send_message(ids["helper"], "Clase/es registrada: "+"\n"+("-Ranger"+"\n" if ranger else "")+("-Knight"+"\n" if knight else "")+("-Sentinel"+"\n" if sentinela else "")+("-Alchemist"+"\n" if alch else "")+("-Collector"+"\n" if collector else "")+("-Blacksmith"+"\n" if Blacksmith else ""))
                #############################################################################

                # elif 'Invite has been sent.' in mensaje.text and GC:
                #     time.sleep(timer)
                #     app.send_message(ids["Grup"], 'Tómate un cafecito anda ☕️')
                # elif '[invalid action]' in mensaje.text and GC:
                #     time.sleep(timer)
                #     app.send_message(ids["Grup"], 'No hay café pa ti ☕️')
                    
                # elif 'Invite has been sent.' in mensaje.text and GCmm:
                #     time.sleep(timer)
                #     app.send_message(ids["grup_mm"], 'Tómate un cafecito anda ☕️')
                # elif '[invalid action]' in mensaje.text and GCmm:
                #     time.sleep(timer)
                #     app.send_message(ids["grup_mm"], 'No hay café pa ti ☕️')
                elif 'be back in' in mensaje.text:
                    en_quest=True
                    time_enquest = int(re.findall("be back in (\d+)", mensaje.text)[0])
                    time.sleep(15+time_enquest*60)
                    en_quest=False
                    time.sleep(timer)
                    mensaje.reply('🗺Quests')
               
                elif 'Many things can happen in the forest.' in mensaje.text and auto_quest:
                        time.sleep(timer)
                        mensaje.click(quest)
                elif 'Stamina restored. You are ready for more adventures!' in mensaje.text and gast_stmn:
                    auto_quest=True
                    time.sleep(timer)
                    app.send_message(ids["CW"], '🗺Quests')
                elif (re.search("🏅Level: ([0-9]+)", mensaje.text)) and ('Battle of the seven castles in' in mensaje.text):
                    level = int(re.findall("🏅Level: ([0-9]+)", mensaje.text)[0])
                    hp = int(re.findall("Hp\:.([0-9]+)", mensaje.text)[0])
                    #time.sleep(timer)
                    #mensaje.forward(ids["expbot"]) 
                    #if vago:
                        #if hp < 500:
                            #caza = False
                            #time.sleep(1800+timer_aq)
                            #app.send_message(ids["CW"], "🏅Me")
                        #else:
                            #caza = True
                elif re.search("Back in ([0-9]+)", mensaje.text):
                    quest_time = int(re.findall("Back in ([0-9]+)", mensaje.text)[0])
                elif re.search("carry ([0-9]+)", mensaje.text.lower()) and trader:
                    carry = int(re.findall("carry ([0-9]+)", mensaje.text.lower())[0])
                    app.send_message(ids["CW"], "/sc "+str(cod_trader)+" "+str(carry))
                # elif ('⚜️Forbidden Champion') and ('Your attacks:') in mensaje.text:
                #     time.sleep(timer)
                #     mensaje.forward(ids["spam_CB"])

                elif 'won! - he takes' in mensaje.text and dice:
                    app.send_message(ids["CW"], '🎲Play some dice')

                # elif 'Recipient shall send to bot:' in mensaje.text and warra and pasapasa:
                #     mensaje.forward(ids["spam_CB"])
                #     pasapasa = False
                # elif 'Recipient shall send to bot:' in mensaje.text and GCmm and pasapasa:
                #     mensaje.forward(ids["grup_mm"])
                #     pasapasa = False

                # elif 'Your result on the battlefield:' in mensaje.text and envio_rep and vago:
                #     envio_rep = False
                #     time.sleep(timer_rep)
                #     mensaje.forward(ids["RangerSquad"])
              
              
            # elif (mensaje.chat.id==ids["Auction"]) and ofertas:
            #     if "Mystery" in mensaje.text: 
            #         time.sleep(timer)
            #         mensaje.forward(ids["CW"])
             #   elif "stone" in mensaje.text: 
               #     time.sleep(timer)
                #    mensaje.forward(ids["CW"])

                          
                  
            # elif (mensaje.chat.id==ids["CastleOrders"]):
            #     if general:
            #         if '🛡Defenders defend the castle wall' in mensaje.text:
            #             time.sleep(timer-1)
            #             app.send_message(ids["Canal"], '#def_castillo')
            #             time.sleep(timer-1)
            #             app.send_message(ids["CW"], '🛡Defend')

            #         #elif ('⚔Attack' in mensaje.text) or ('⚔Attack' in mensaje.text):
            #             #programar_ataque(mensaje.text, timer)

            #         elif ('⚔BATTLE SOON!⚔' in mensaje.text):
            #             time.sleep(timer+2)
            #             app.send_message(ids["CW"], '⚽Play')
                   

            # elif (mensaje.chat.id==ids["RangerSquad"]) and (general2):
            #     #if ('⚔Attack' in mensaje.text):
            #         #if orden_adelantada:
            #             #orden_adelant(mensaje.text, timer)
            #             #orden_adelantada = False
   

            #     if ('🛡Defenders defend the castle wall' in mensaje.text):
            #         if orden_adelantada:
            #             time.sleep(timer-1)
            #             app.send_message(ids["Canal"], '#defad_castillo')
            #             time.sleep(7200)
            #             app.send_message(ids["CW"], '🛡Defend')
            #             orden_adelantada = False
                  

                
            # elif caza and mensaje.chat.id==ids["CastleOrders"] and ("Be careful" in  mensaje.text):
            #     if vago:
            #         rango_max = 30
            #         cazar(mensaje)
            #     else:
            #         rango_max = 6
            #         cazar(mensaje)


            # elif mensaje.chat.id==ids["spam_CB"]:
            #     if re.search("an ambush\!", mensaje.text):
            #         if ambush:
            #             if level < 36:
            #                 rango_max = 11
            #                 cazar(mensaje)
            #             else:
            #                 if vago:
            #                     rango_max = 30
            #                     cazar(mensaje)
            #                 else:
            #                     rango_max = 9
            #                     cazar(mensaje)

            #     elif (caza) and ("Be careful" in  mensaje.text):
            #         if vago:
            #             rango_max = 30
            #             cazar(mensaje)
            #         else:
            #             rango_max = 6
            #             cazar(mensaje)

            #     elif ("/g_withdraw" in mensaje.text) and warra: 
            #         mensaje.forward(ids["CW"])
            #         pasapasa = True
                    
            # elif mensaje.chat.id==ids["Grup"]:
            #     if re.search("an ambush\!", mensaje.text):
            #         if ambush:
            #             if level < 36:
            #                 rango_max = 11
            #                 cazar(mensaje)
            #             else:
            #                 if vago:
            #                     rango_max = 30
            #                     cazar(mensaje)
            #                 else:
            #                     rango_max = 9
            #                     cazar(mensaje)
 
                    
              
            #     elif ("/g_invite" in mensaje.text) and GC: 
            #         time.sleep(timer)
            #         mensaje.forward(ids["CW"])
                    
                    
            # elif mensaje.chat.id==ids["grup_mm"]:

                    
              
                # if ("/g_invite" in mensaje.text) and GCmm: 
                #     time.sleep(timer)
                #     mensaje.forward(ids["CW"])
                
                # elif ("/g_withdraw" in mensaje.text) and GCmm: 
                #     mensaje.forward(ids["CW"])
                #     pasapasa = True

                # elif ("#oa_on"==mensaje.text.lower()) and general2:
                #     orden_adelantada = True 
                #     app.send_message(ids["Grup"], "El envío de órdenes de ranger está activado" if orden_adelantada else "El envío de órdenes de ranger está desactivado")

                # elif ("#oa_off"==mensaje.text.lower()) and general2:
                #     orden_adelantada = False
                #     app.send_message(ids["Grup"], "El envío de órdenes de ranger está activado" if orden_adelantada else "El envío de órdenes de ranger está desactivado")
               
                # elif ("#open_shop" in mensaje.text) and Blacksmith:
                #     time.sleep(timer)
                #     app.send_message(ids["CW"], '/myshop_open')
                # elif ("⛳️Battle results:" in mensaje.text):
                #     orden_adelantada = True
                #     envio_rep = True
                #     time.sleep(timer+420)
                #     app.send_message(ids["CW"], '/report')
                #     if Blacksmith:
                #         time.sleep(open_shop)
                #         app.send_message(ids["CW"], '/myshop_open')
                #     #elif sentinela:
                #         #time.sleep(open_shop)
                #         #app.send_message(ids["CW"], '/use_tnt')
                #     #elif knight:
                #         #time.sleep(open_shop)
                #         #app.send_message(ids["CW"], '/use_cry')
                #     #elif collector:
                #         #time.sleep(open_shop)
                #         #app.send_message(ids["CW"], '/use_crl')  
                #    #if general:
                #         #time.sleep(timer+450)
                #         #app.send_message(ids["CW"], '⚽Play')  

        
                # elif (caza) and ("Be careful" in  mensaje.text):
                #     if vago:
                #         rango_max = 30
                #         cazar(mensaje)
                #     else:
                #         rango_max = 6
                #         cazar(mensaje)
       

            # elif mensaje.chat.id==ids["Canal"]:

            #     #if sentinela or defensores:
            #     if defensores:
            #         if ordenes:
            #             if '#def_guild' == mensaje.text:
            #                 if defensores:
            #                     if sentinela:
            #                         app.send_message(ids["CW"], '🛡Defend')
            #                         time.sleep(timer+1)
            #                         app.send_message(ids["CW"], tactics)
            #                     else:
            #                         time.sleep(timer+1)
            #                         app.send_message(ids["CW"], '🛡Defend')
            #                         time.sleep(timer_aq+900)
            #                         auto_quest=True
            #                         app.send_message(ids["CW"], '🗺Quests')         
            #                 else:
            #                     time.sleep(timer+1)
            #                     app.send_message(ids["CW"], '/g_def') 
            #                     time.sleep(timer+1)
            #                     app.send_message(ids["CW"], tactics) 


            #     #elif not (sentinela) and not (defensores):
            #     elif not (defensores):
                

            #         if ordenes:

            #             if '#atk_dragons' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🐉')
            #             elif '#atk_sharks' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🦈')
            #             elif '#atk_eagles' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🦅')
            #             elif '#atk_deers' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🦌')
            #             elif '#atk_potato' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🥔')
            #             elif '#atk_moon' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🌑')
            #             elif '#def_castillo' == mensaje.text:
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🛡Defend')
            #             elif '#def_guild' == mensaje.text and tregua:
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '/g_def')                   
            #             elif '#def_total' == mensaje.text:
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '/g_def')
            #             elif re.search("ga_atk ([A-z0-9]+)", mensaje.text):
            #                 cod_atk = re.findall("ga_atk ([A-z0-9]+)", mensaje.text)[0]
            #                 app.send_message(ids["CW"], "/ga_atk "+cod_atk)  
            #             elif re.search("ga_def ([A-z0-9]+)", mensaje.text):
            #                 cod_def = re.findall("ga_def ([A-z0-9]+)", mensaje.text)[0]
            #                 app.send_message(ids["CW"], "/ga_def "+cod_def)
                        
            #         if apuntar:
            #             if '#atkad_dragons' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🐉')
            #                 if GC and orden_adelantada:
            #                     orden_adelantada = False     
              
            #             elif '#atkad_sharks' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🦈')
            #                 if GC and orden_adelantada:
            #                     orden_adelantada = False      
              
            #             elif '#atkad_eagles' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🦅')
            #                 if GC and orden_adelantada:
            #                     orden_adelantada = False 
              
            #             elif '#atkad_deers' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🦌')
            #                 if GC and orden_adelantada:
            #                     orden_adelantada = False    
              
            #             elif '#atkad_potato' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🥔')
            #                 if GC and orden_adelantada:
            #                     orden_adelantada = False         
              
            #             elif '#atkad_moon' == mensaje.text:
            #                 app.send_message(ids["CW"], '⚔Attack')
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🌑')
            #                 if GC and orden_adelantada:
            #                     orden_adelantada = False      
              
            #             elif '#defad_castillo' == mensaje.text:
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '🛡Defend')
            #                 if GC and orden_adelantada:
            #                     orden_adelantada = False  
              
            #             elif '#defad_guild' == mensaje.text and tregua:
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '/g_def')                   
            #             elif '#defad_total' == mensaje.text:
            #                 time.sleep(timer+1)
            #                 app.send_message(ids["CW"], '/g_def C')
            #             elif re.search("ga_atkad ([A-z0-9]+)", mensaje.text):
            #                 cod_atk = re.findall("ga_atkad ([A-z0-9]+)", mensaje.text)[0]
            #                 app.send_message(ids["CW"], "/ga_atk "+cod_atk)  
            #             elif re.search("ga_defad ([A-z0-9]+)", mensaje.text):
            #                 cod_def = re.findall("ga_defad ([A-z0-9]+)", mensaje.text)[0]
            #                 app.send_message(ids["CW"], "/ga_def "+cod_def) 
   

                
            # elif caza and mensaje.chat.id==ids["Caza"] and ("Prepare yourself to fight:" in  mensaje.text):
            #     if vago:
            #         rango_max = 30
            #         cazar(mensaje)
            #     else:
            #         rango_max = 6
            #         cazar(mensaje)
    
            elif mensaje.chat.id==ids["helper"]:
                if re.search("level ([0-9]+)", mensaje.text.lower()):
                    level = int(re.findall("level ([0-9]+)", mensaje.text.lower())[0])
                    app.send_message(ids["helper"], "Level para caza registrado: "+str(level))
                elif re.search("sc ([0-9]+)", mensaje.text.lower()):
                    cod_trader = re.findall("sc ([0-9]+)", mensaje.text.lower())[0]
                    app.send_message(ids["helper"], "Recurso a vender al trader  registrado: "+cod_trader)
                elif "/trader"==mensaje.text.lower():
                    if (sentinela) or (me.id == 705724375):
                        trader = not trader
                        app.send_message(ids["helper"], "Trader activado" if trader else "Trader desactivado")
                    else:
                        app.send_message(ids["helper"], "Deja el invento que tú no eres sentinela /mem 🌚")
                elif "/aq"==mensaje.text.lower():
                    auto_quest = not auto_quest
                    app.send_message(ids["helper"], "Autoquest activado" if auto_quest else "Autoquest desactivado")
                elif 'swamp'==mensaje.text.lower():
                    quest='🍄Swamp'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                elif 'forest'==mensaje.text.lower():
                    quest='🌲Forest'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)
                elif 'valley'==mensaje.text.lower():
                    quest='⛰️Valley'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Información de quest actualizada: "+quest)


                elif ("/gc"==mensaje.text.lower()):
                    GC = not GC
                    app.send_message(ids["helper"], "Las funciones del GC se encuentran activadas" if GC else "Las funciones del GC se encuentran desactivadas")
                elif ("/general"==mensaje.text.lower()):
                    general = not general
                    app.send_message(ids["helper"], "El envío de órdenes automáticas está activado" if general else "El envío de órdenes automáticas está desactivado")
                elif ("/captain"==mensaje.text.lower()):
                    general2 = not general2
                    app.send_message(ids["helper"], "El envío de órdenes automáticas está activado" if general2 else "El envío de órdenes automáticas está desactivado")
            
                elif "/caza"==mensaje.text.lower():
                    caza = not caza
                    app.send_message(ids["helper"], "La caza de mobs se encuentra activada" if caza else "La caza de mobs se encuentra desactivada")
                elif "/ff"==mensaje.text.lower():
                    ff = not ff
                    app.send_message(ids["helper"], "La autoarena está activada" if ff else "La autoarena está desactivada")
                elif "/ambush"==mensaje.text.lower():
                    ambush = not ambush
                    app.send_message(ids["helper"], "La ayuda a las ambush está activada" if ambush else "La ayuda a las ambush está desactivada")
                elif "/ordenes"==mensaje.text.lower():
                    ordenes = not ordenes
                    app.send_message(ids["helper"], "Las órdenes automáticas están activadas" if ordenes else "Las órdenes automáticas están desactivadas") 
                elif "/apuntar"==mensaje.text.lower():
                    apuntar = not apuntar
                    app.send_message(ids["helper"], "Las órdenes adelantadas están activadas" if apuntar else "Las órdenes adelantadas están desactivadas")        
                elif 'moon'==mensaje.text.lower():
                    tactics='/tactics_moonlight'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)  
                elif 'potato'==mensaje.text.lower():
                    tactics='/tactics_potato'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'eagle'==mensaje.text.lower():
                    tactics='/tactics_highnest'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)  
                elif 'deer'==mensaje.text.lower():
                    tactics='/tactics_deerhorn'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'shark'==mensaje.text.lower():
                    tactics='/tactics_sharkteeth'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif 'dragon'==mensaje.text.lower():
                    tactics='/tactics_dragonscale'
                    time.sleep(2)
                    app.send_message(ids["helper"], "Tactics actualizadas: "+tactics)
                elif "/stamina"==mensaje.text.lower():
                    gast_stmn = not gast_stmn
                    app.send_message(ids["helper"], "Se activará el loop de quest cuando se llene la stamina" if ordenes else "No se activará el loop de quest cuando se llene la stamina")
                elif "/oferta"==mensaje.text.lower():
                    ofertas = not ofertas
                    app.send_message(ids["helper"], "Las ofertas del auction se encuentran activadas" if ofertas else "Las ofertas del auction se encuentran desactivadas") 
                elif "/dice"==mensaje.text.lower():
                    dice = not dice
                    app.send_message(ids["helper"], "El loop de los dados se encuentra activado" if dice else "El loop de los dados se encuentra desactivado") 

                elif "/taberna"==mensaje.text.lower():
                    taberna = not taberna
                    app.send_message(ids["helper"], "El loop de taberna está activado" if taberna else "El loop de taberna se encuentra desactivado")
                elif "/mascota"==mensaje.text.lower():
                    pet = not pet
                    app.send_message(ids["helper"], "You are now the proud owner of a cute pet" if pet else "You just kill your pet I hope you feel great about it")
                    if pet:
                        mascota()
                elif "/gopher"==mensaje.text.lower():
                    gopher = not gopher
                    app.send_message(ids["helper"], "You are now the proud owner of a cute gopher" if gopher else "You just kill your gopher I hope you feel great about it")
                    #if gopher:
                        #gopher()
                
                elif "/sa"==mensaje.text.lower():
                    stamina_alt = not stamina_alt
                    app.send_message(ids["helper"], "True stamina_alt" if stamina_alt else "False stamina_alt")
                    

                elif "/report"==mensaje.text.lower():
                    reporte()
                elif "/on"==mensaje.text.lower():
                    (caza,ff,ambush,auto_quest,ordenes)=(True,True,True,True,True)
                    reporte()
                elif "/off"==mensaje.text.lower():
                    (caza,ff,ambush,auto_quest,ordenes)=(False,False,False,False,False)
                    reporte()
                # elif (GC) or (general):
                #     if '🛡Defenders defend the castle wall' in mensaje.text:
                #         time.sleep(timer-2)
                #         app.send_message(ids["Canal"], '#def_castillo')
                #         time.sleep(timer-2)
                #         app.send_message(ids["CW"], '🛡Defend')
                #     #elif ('⚔Attack' in mensaje.text) or ('⚔Attack' in mensaje.text):
                #         #programar_ataque(mensaje.text, timer)
                # elif general2:     
                #     if '🛡Defenders defend the castle wall' in mensaje.text:
                #         time.sleep(timer-1)
                #         app.send_message(ids["Canal"], '#def_castillo')
                #         time.sleep(timer-1)
                #         app.send_message(ids["CW"], '🛡Defend')
                #     #elif (('⚔Attack' in mensaje.text) or ('⚔Attack' in mensaje.text)) and (orden_adelantada):
                #         #orden_adelant(mensaje.text, timer)
                #         orden_adelantada = False
                #     elif '⚔BATTLE IS OVER⚔' in mensaje.text:
                #         orden_adelantada = True
                elif (re.search("🏅Level: ([0-9]+)", mensaje.text)) and ('Battle of the seven castles in' in mensaje.text):
                    level = int(re.findall("🏅Level: ([0-9]+)", mensaje.text)[0])
                    hp = int(re.findall("Hp\:.([0-9]+)", mensaje.text)[0])
                    if vago:
                        if hp < 500:
                            caza = False
                            time.sleep(1800+timer_aq)
                            app.send_message(ids["CW"], "🏅Me")
                        else:
                            caza = True
                            
                            
                           

        
        """

        nonlocal FUNCTION

        """
        Basura_id = 1190610473 #1217879961
      #Borrar aquellos que ids que no son utiles. 
        def chat_on():
            nonlocal ids, Basura_id 
            dialogs = [i.chat.id for i in app.iter_dialogs()]
            faltan = False
            for k, v in ids.items():
                if  v not in dialogs:
                    ids[k]=Basura_id
                    faltan = True
            if -1001386769293 in dialogs: #🔲 Alianza DRK EKE & no #🔰DRKyEKE alianza
                #Allies = Allies_cuadrado
                if faltan:
                    try:
                        #app.send_message("@shitandtrash_bot", "/start")
                        app.send_message("@MugiwarasTrash_bot", "/start")
                        app.send_message(Basura_id,"mandaré aquí lo que deberia mandar a otros chats pero no pude."+
                                         "puedes moverlo a archivados, pero no lo borres por favor...")
                    except:
                        log.warning("No se ha podido unir al bot de Basuramia_bot")
           # if BS:
                #No_Allies = ["🌶"] + [ally for ally in Allies if ally not in ("🛹", "💍","🔍")]

     
        
        chat_on()
        if ids["CW"] != Basura_id: #No está en la basura..
               app.send_message(ids["CW"],"🏅Me")
               time.sleep(8)
               app.send_message(ids["CW"],"/hero")
        if ids["helper"] != Basura_id: #No está en la basura...
               app.send_message(ids["helper"],"Bot reiniciado...!!! 😜😘")                
               reporte()
             #  mascota()
        

        #else:
            #def selector_CW(message): #borrar modulo CW
                #pass
        
        @app.on_message(Filters.chat(list(ids.values())) & Filters.text & ~Filters.scheduled)
        def cliente(client, message):
            nonlocal api_session, Basura_id
            if message.chat.id!=Basura_id: #no es de Basuramia_bot
                #try:
                    #if BS: selector_BS(message)
               # except Exception as e:
                   # log.warning(str(me.username)+" ha sufrido un error:", exc_info=True)
                try:
                    selector_CW(message)
                except Exception as e:
                    log.warning(str(me.username)+" ha sufrido un error:", exc_info=True)
            elif message.text == "ids":
                app.send_message(Basura_id,str(ids))
            elif message.text == "users":
                usuarios = app.get_chat_members(-1001386769293) #🔰DRKyEKE alianza
                #usuarios += app.get_chat_members(-1001455157282) #🔲 Alianza DRK EKE
                app.send_message(Basura_id,str([[member.user.first_name, member.user.id] for member in usuarios]))
            elif message.text == "hash":
                app.send_message(Basura_id,str(api_session[0:20]))
                app.send_message(Basura_id,str(api_session[-21:]))

    def stop(self):
        app.stop()
 

        
        
