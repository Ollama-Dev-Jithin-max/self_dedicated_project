model_name='mistral-nemo'
user_name='Jithin K'
import LLM_ini as l
import polishing_smartly as ps
import logic as lo
ESIR=l.LLM(model_name,user_name)
ps.say('Hello i am ESIR, Even start i rock')
while True:
 command=lo.listen()
 print(command)
 with open('_cache_.txt','a') as file:
   file.write('\n'+command)
   file.close()
 if command=='stop':
   break
 elif command=='launch':
   ps.say('what do you want to open and what do you want to do on it')
   y=lo.listen()
   print(y)
   with open('_cache_.txt','a') as file:
    file.write('\n'+y)
    file.close()
   lo.open(y,match_closest=True)
 else:
  try:
   x=ESIR.chat(command)
   print(x)
   with open('_cache_.txt','a') as file:
    file.write('\n'+x)
    file.close()
   ps.say(x)
  except Exception as e:
     print(e)
