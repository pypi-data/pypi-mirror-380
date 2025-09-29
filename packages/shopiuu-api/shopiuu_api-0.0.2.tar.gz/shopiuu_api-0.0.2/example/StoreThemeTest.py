from shopiuu_api.ShopiuuClient import ShopiuuClient
from shopiuu_api.Core.ShopiuuException import ShopiuuException

accessToken = 'shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
endpoint = 'http://xxxxx.example.com/'
apiClient = ShopiuuClient(accessToken, endpoint)
try:
    
    themes_res = apiClient.getStoreThemes()
    #print(themes_res)
    #print(themes_res.getData())
    #print(themes.parseDataFromResponse())
    #print(themes.getStatus())
    #themesSettingsFiles = apiClient.getThemeFiles(['theme_id'=>3])
    #print(themesSettingsFiles)
    #print(themesSettingsFiles.getData())

    themes = themes_res.parseDataFromResponse()
    #print(themes)
    #print(type(themes['data']))
    
    accessToken_2 = 'shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx2'
    endpoint_2 = 'http://xxxx2.example.com/'
    apiClient2 = ShopiuuClient(accessToken_2, endpoint_2)
    for index, theme in enumerate(themes['data']):
        themesSettingsFiles = apiClient.getThemeFiles({'theme_id':theme['id']})
        themefiles = themesSettingsFiles.parseDataFromResponse()
        data = {}
        data['name'] = theme['name']
        data['system_theme_id'] = theme['system_theme_id']
        data['system_theme_name'] = theme['system_theme_name']
        data['is_default'] = theme['is_default']
        data['theme_files'] = themefiles['data']
        #print(data)
        result = apiClient2.createTheme(data)
        #print(result.getRawResponse())
        print(result.getData())
        print(result.getStatus())
    
except ShopiuuException as e:
    print("ShopiuuException异常")
    print(e)
except Exception as e:
    print("异常")
    print(e)
