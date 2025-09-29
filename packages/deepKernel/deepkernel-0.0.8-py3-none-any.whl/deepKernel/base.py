from deepKernel import deepline
import json

def _init():
    global _global_dict
    _global_dict={}

def set_config_path(path):
    data = {
        'func': 'SET_CONFIG_PATH',
        'paras': {
                      'path': path
                      }   
    }
    #print(json.dumps(data))
    return deepline.process(json.dumps(data))

#获取当前层feature数
def get_layer_feature_count(jobName, stepName, layerName):
    data = {
        'func': 'GET_LAYER_FEATURE_COUNT',
        'paras': {'jobName': jobName, 
                  'stepName': stepName, 
                  'layerName': layerName}
    }
    return deepline.process(json.dumps(data))

def get_opened_jobs():
    data = {
        'func': 'GET_OPENED_JOBS'
    }
    #print(json.dumps(data))
    return deepline.process(json.dumps(data))

def open_job(path, job):
    data = {
        'func': 'OPEN_JOB',
        'paras': [{'path': path},
                  {'job': job}]
    }
    # print(json.dumps(data))
    ret = deepline.process(json.dumps(data))
    return ret

def get_matrix(job):
    data = {
        'func': 'GET_MATRIX',
        'paras': {'job': job}
    }
    # print(json.dumps(data))
    return deepline.process(json.dumps(data))

def has_profile(job, step):
    data = {
        'func': 'HAS_PROFILE',
        'paras': {
                    'job': job,
                    'step': step
                      }   
    }
    #print(json.dumps(data))
    return deepline.process(json.dumps(data))

def get_profile_box(job, step):
    data = {
            'func': 'PROFILE_BOX',
            'paras': {'job': job, 
                      'step': step}
    }
    js = json.dumps(data)
    #print(js)
    ret = deepline.process(json.dumps(data))
    return ret

#导出
def layer_export(job, step, layer, _type, filename, gdsdbu, resize, angle, scalingX, scalingY, isReverse,
                    mirror, rotate, scale, profiletop, cw, cutprofile, mirrorpointX, mirrorpointY, rotatepointX,
                    rotatepointY, scalepointX, scalepointY, mirrordirection, cut_polygon,numberFormatL=2,numberFormatR=6,
                    zeros=2,unit=0):
    data = {
            'func': 'LAYER_EXPORT',
            'paras': {
                        'job': job,
                        'step': step,
                        'layer': layer,
                        'type': _type,
                        'filename': filename,
                        'gdsdbu': gdsdbu,
                        'resize': resize,
                        'angle': angle,
                        'scalingX': scalingX,
                        'scalingY': scalingY,
                        'isReverse': isReverse,
                        'mirror': mirror,
                        'rotate': rotate,
                        'scale': scale,
                        'profiletop': profiletop,
                        'cw': cw,
                        'cutprofile': cutprofile,
                        'mirrorpointX': mirrorpointX,
                        'mirrorpointY': mirrorpointY,
                        'rotatepointX': rotatepointX,
                        'rotatepointY': rotatepointY,
                        'scalepointX': scalepointX,
                        'scalepointY': scalepointY,
                        'mirrordirection': mirrordirection,
                        'cut_polygon': cut_polygon,
                        'numberFormatL': numberFormatL,
                        'numberFormatR': numberFormatR,
                        'zeros': zeros,
                        'unit': unit
                      }                    
            }   
    js = json.dumps(data)
    print(js)
    return deepline.process(json.dumps(data))

#load layer
def load_layer(jobname, stepname, layername):
    data = {
            'func': 'LOAD_LAYER',
            'paras': {'jobname': jobname,
                      'stepname': stepname,
                      'layername': layername}                   
        }
    js = json.dumps(data)
    #print(js)
    deepline.process(json.dumps(data))

#料号另存为
def save_job_as(job, path):
    data = {
            'func': 'SAVE_JOB_AS',
            'paras': {
                      'job': job,
                      'path': path
                      }             
        }
    js = json.dumps(data)
    #print(js)
    ret = deepline.process(json.dumps(data))
    return ret

def save_png(job,step,layers,xmin,ymin,xmax,ymax,picpath,picname,backcolor,layercolors):
    data = {
        "func": "OUTPUT_FIXED_PICTURE",
        "paras": {
            "job": job,
            "step":step,
            "layers":layers,
            "xmin":xmin,
            "ymin":ymin,
            "xmax": xmax,
            "ymax":ymax,
            "picpath":picpath,
            "picname":picname,
            "backcolor": backcolor,
            "layercolors":layercolors
        }
    }
    return deepline.process(json.dumps(data))

def get_all_feature_info(job, step, layer,featuretype=127):
    data = {
        'func': 'GET_ALL_FEATURE_INFO',
        'paras': {'job': job, 
                  'step': step, 
                  'layer': layer,
                  'featureType':featuretype
        }
    }
    return deepline.process(json.dumps(data))