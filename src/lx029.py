import os,sys,re
 
rootDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'webapp','web','routers')
print('rootDir:{}'.format(rootDir))
for dirName, subdirList, fileList in os.walk(rootDir):
    # print('Folder: {}'.format(dirName))
    sys.path.append(dirName)
    for fname in fileList:

        fileName = os.path.join(dirName,fname)
        print(fileName)
        if re.match(r'[_,a-z,A-Z]+.py$', fname):
            mod_name = fname.split('.')[0]
            mod = __import__(mod_name, globals(), locals())
            for attr in dir(mod):
                
                if attr.startswith('_'):
                    continue
                fn = getattr(mod, attr)
                
                if callable(fn):
                    print(attr)
                    method = getattr(fn, '__method__', None)
                    path = getattr(fn, '__route__', None)
                    if method and path:
                        pass
    
    if len(subdirList) > 0:
        subdirList = subdirList[1:]