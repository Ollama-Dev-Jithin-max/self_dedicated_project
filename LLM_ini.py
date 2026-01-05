import ollama as ol
class LLM:
 def __init__ (self,model_name,user_name):
  self.model=model_name
  self.user_name=user_name
 def chat(self,command):
    with open('_cache_.txt','r') as file:
     _cache_=file.read()
     print(_cache_)
     file.close()
    response=ol.chat(
            model=self.model,
            messages=[ 
            {"role":"system","content":_cache_},
            {"role":"user","content":command}
            ]
            )
    return response["message"]["content"]