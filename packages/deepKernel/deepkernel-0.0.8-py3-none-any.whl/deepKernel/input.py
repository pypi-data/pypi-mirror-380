from deepKernel import base
import json


#打开料号
def open_job(job:str, path:str)->bool:
    try:
       ret= json.loads(base.open_job(path, job))['paras']['status']
       return ret   
    except Exception as e:
        print(e)
        return False