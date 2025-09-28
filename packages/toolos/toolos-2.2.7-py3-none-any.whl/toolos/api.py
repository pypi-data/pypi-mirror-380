    #? ################  SETTINGS API #####################

class SettingsAPI:

    def __init__(self, app, settings_path: str=None):
        self.app = app
        self.SETTINGSPATH = self.app.SDK.SDK_SETTINGS if not settings_path else settings_path
        self.SETTINGS = self.LoadSettings()
        self.VERSION = self.SETTINGS.get("version") if self.SETTINGS.get("version") else None
        self.LANGUAGE = self.SETTINGS.get("language") if self.SETTINGS.get("language") else None
        self.PACKAGEPATH = self.SETTINGS.get("packagepath") if self.SETTINGS.get("packagepath") else None
        self.CACHEPATH = self.SETTINGS.get("cachepath") if self.SETTINGS.get("cachepath") else None
        self.TEMPPATH = self.SETTINGS.get("temppath") if self.SETTINGS.get("temppath") else None
        self.LOGPATH = self.SETTINGS.get("logpath") if self.SETTINGS.get("logpath") else None
        self.APIPATH = self.SETTINGS.get("apipath") if self.SETTINGS.get("apipath") else None
        self.LANGUAGEPATH = self.SETTINGS.get("languagepath") if self.SETTINGS.get("languagepath") else None
        self.MODPATH = self.SETTINGS.get("modpath") if self.SETTINGS.get("modpath") else None
        self.MODS_ENABLED = self.SETTINGS.get("mods_enabled") if self.SETTINGS.get ("mods_enabled") else False

    def LoadSettings(self):
        import json
        with open(self.SETTINGSPATH, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    def Global(self, key):
        return self.SETTINGS.get(key)
    
    def SetUpdate(self):
        self.SETTINGS["update"] = True
        import json
        with open(self.SETTINGSPATH, 'w', encoding='utf-8') as f:
            json.dump(self.SETTINGS, f, indent=4)
            
    def CheckIfUpdate(self):
        return self.SETTINGS.get("update", False)
    
    
    def Update(self):
        import json
        with open(self.SETTINGSPATH, 'r', encoding='utf-8') as f:
            self.SETTINGS = json.load(f)
        self.VERSION = self.SETTINGS.get("version") if self.SETTINGS.get("version") else None
        self.LANGUAGE = self.SETTINGS.get("language") if self.SETTINGS.get("language") else None
        self.PACKAGEPATH = self.SETTINGS.get("packagepath") if self.SETTINGS.get("packagepath") else None
        self.CACHEPATH = self.SETTINGS.get("cachepath") if self.SETTINGS.get("cachepath") else None
        self.TEMPPATH = self.SETTINGS.get("temppath") if self.SETTINGS.get("temppath") else None
        self.LOGPATH = self.SETTINGS.get("logpath") if self.SETTINGS.get("logpath") else None
        self.APIPATH = self.SETTINGS.get("apipath") if self.SETTINGS.get("apipath") else None
        self.LANGUAGEPATH = self.SETTINGS.get("languagepath") if self.SETTINGS.get("languagepath") else None
        self.MODPATH = self.SETTINGS.get("modpath") if self.SETTINGS.get("modpath") else None
        self.MODS_ENABLED = self.SETTINGS.get("mods_enabled") if self.SETTINGS.get ("mods_enabled") else False

    #? ################  StateMachine API #####################
    
class StateMachineAPI:
    STEP_1 = "step_1"
    STEP_2 = "step_2"
    STEP_3 = "step_3"
    STEP_4 = "step_4"
    STEP_5 = "step_5"
    EXIT = "exit"
    MAINMENU = "main_menu"
    FIRST_ENTRY = "first_entry"
    
    
    
    def __init__(self):
        """beginning with first_entry state"""
        self.state = self.FIRST_ENTRY
        
    def SetState(self, new_state):
        self.state = new_state
        
    def GetState(self):
        return self.state
    
    def IsState(self, check_state):
        return self.state == check_state
    

    #? ################  CACHE API #####################

class CacheAPI:
    
    def __init__(self, cache_path):
        self.CACHEPATH = cache_path
        if not self.CacheExists():
            import os
            os.makedirs(cache_path)
        
        
    def WriteCacheFile(self, filename, content):
        with open(f"{self.CACHEPATH}/{filename}", 'w', encoding='utf-8') as f:
            f.write(content)
            
    def ReadCacheFile(self, filename):
        with open(f"{self.CACHEPATH}/{filename}", 'r', encoding='utf-8') as f:
            return f.read()
    
    def AddContent(self, filename, content):
        with open(f"{self.CACHEPATH}/{filename}", 'a', encoding='utf-8') as f:
            f.write(content + "\n")
            
    def RemoveCacheFile(self, filename):
        import os
        os.remove(f"{self.CACHEPATH}/{filename}")
        
    def CacheExists(self, filename=None):
        import os
        if filename:
            return os.path.exists(f"{self.CACHEPATH}/{filename}")
        return os.path.exists(self.CACHEPATH)

    #? ################  TEMP API #####################

class TempAPI:
    
    def __init__(self, temp_path):
        self.TEMPPATH = temp_path
        if not self.TempExists():
            import os
            os.makedirs(temp_path)
        
    def WriteTempFile(self, filename, content):
        with open(f"{self.TEMPPATH}/{filename}", 'w', encoding='utf-8') as f:
            f.write(content)
            
    def ReadTempFile(self, filename):
        with open(f"{self.TEMPPATH}/{filename}", 'r', encoding='utf-8') as f:
            return f.read()
        
    def AddContent(self, filename, content):
        with open(f"{self.TEMPPATH}/{filename}", 'a', encoding='utf-8') as f:
            f.write(content + "\n")
    
    def TempExists(self, filename=None):
        import os
        if filename:
            return os.path.exists(f"{self.TEMPPATH}/{filename}")
        return os.path.exists(self.TEMPPATH)

    def RemoveTempFile(self, filename=None):
        if not filename: # leere Temp ordner
            import os
            for file in os.listdir(self.TEMPPATH):
                file_path = os.path.join(self.TEMPPATH, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception:
                    pass
            return True
        try:
            import os
            os.remove(f"{self.TEMPPATH}/{filename}")
        except Exception:
            return False

    #? ################  PACKAGE API #####################

class PackageAPI:
    
    def __init__(self, package_path):
        self.PACKAGEPATH = package_path
        self.isLoggedIn = False
        self.USERNAME = None
        
    def Login(self, username, password):
        if username == "admin" and password == "password":
            self.isLoggedIn = True
            self.USERNAME = username
            return True
        return False
    
    def Logout(self):
        self.isLoggedIn = False
        self.USERNAME = None
        
    def WritePackageFile(self, filename, content):
        with open(f"{self.PACKAGEPATH}/{filename}", 'w', encoding='utf-8') as f:
            f.write(content)
            
    def ReadPackageFile(self, filename):
        with open(f"{self.PACKAGEPATH}/{filename}", 'r', encoding='utf-8') as f:
            return f.read()
        
    def AddContent(self, filename, content):
        with open(f"{self.PACKAGEPATH}/{filename}", 'a', encoding='utf-8') as f:
            f.write(content + "\n")
    
    def RemovePackageFile(self, filename):
        import os
        os.remove(f"{self.PACKAGEPATH}/{filename}")
        
    #? ################  LOG API #####################
        
class LogAPI:
    
    def __init__(self, log_path):
        self.LOGPATH = log_path
        if not self.LogExists():
            import os
            os.makedirs(log_path)
        
    def WriteLog(self, filename, message):
        import datetime
        timestamp = datetime.datetime.now().isoformat()
        with open(f"{self.LOGPATH}/{filename}", 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")
            
    def ReadLog(self, filename):
        with open(f"{self.LOGPATH}/{filename}", 'r', encoding='utf-8') as f:
            return f.read()
        
    def DeleteLog(self, filename):
        import os
        os.remove(f"{self.LOGPATH}/{filename}")
        
    def ClearLog(self, filename):
        with open(f"{self.LOGPATH}/{filename}", 'w') as f:
            f.write("")
               
    def LogExists(self, filename=None):
        import os
        if filename:
            return os.path.exists(f"{self.LOGPATH}/{filename}")
        return os.path.exists(self.LOGPATH)
            
            

    #? ################  MANAGER API #####################

class ManagerAPI:
    
    def __init__(self):
        pass
        
        
        
    #? ################  GUI API #####################
    
class GuiAPI:
    
    def __init__(self):
        pass
        
    #? ################  HELPER API #####################

class HelperAPI:
    
    def __init__(self, app):
        self.app = app
        self.ui = GuiAPI()
        self.command = CommandAPI(app)

    def GetVersion(self):
        return self.app.Settings.VERSION

    def GetLanguage(self):
        return self.app.Settings.LANGUAGE
    
    

class CommandAPI:

    def __init__(self, app):
        self.app = app
        
    def Execute(self, command):
        import subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode

    #? ################  LANGUAGE API #################

class LanguageAPI:

    def __init__(self, settings, standard_library=True):
        self.Settings = settings
        self.LANGUAGE = settings.LANGUAGE
        self.LANGUAGEPATH = settings.LANGUAGEPATH
        self.PACKAGES = []
        if standard_library:
            import os
            package_dir = os.path.dirname(os.path.abspath(__file__))
            self.LANGUAGEPATH = os.path.join(package_dir, "data", "lang")
        self.language_data = self.LoadLanguageData(self.LANGUAGE)
        
    #? Core Functions

    # Reloading language data (e.g. after changing language in settings or adding new language-packs)
    def Reload(self):
        """Reloading Language-Data and applied Language-Packages"""
        self.LANGUAGE = self.Settings.LANGUAGE
        self.language_data = self.LoadLanguageData(self.LANGUAGE)
        if self.PACKAGES:
            for package in self.PACKAGES:
                if package["language"] == self.LANGUAGE:
                    self.language_data.update(package["data"])

    def SetLanguageData(self, keys: dict=None, prefered_lang_reference=False):
        if prefered_lang_reference:
            # Verwende toolos package data/lang Verzeichnis
            import os
            package_dir = os.path.dirname(os.path.abspath(__file__))
            self.LANGUAGEPATH = os.path.join(package_dir, "data", "lang")
            self.language_data = self.LoadLanguageData(self.LANGUAGE)
        elif keys:
            self.language_data = keys
    
    # Loading Original Language-Data json formats from /assets/manager/lang/{'de', 'en', 'ru',..}.json    
    def LoadLanguageData(self, language):
        """Loading Language-Data by parameter: language"""
        import json
        try:
            with open(f"{self.LANGUAGEPATH}/{language}.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            try:
                with open(f"{self.LANGUAGEPATH}/de.json", 'r', encoding='utf-8') as f:
                    return json.load(f)
            except FileNotFoundError:
                return {}

    #? Interaction Functions
    
    def Translate(self, key):
        """Translating Keyword by key with current language-data"""
        return self.language_data.get(key, key)
    
    def GetAllTranslationKeys(self):
        """Returning all translation keys"""
        return list(self.language_data.keys())
    
    def GetAvailableLanguages(self):
        """Returning all available languages from {self.LANGUAGEPATH}"""
        import os
        files = os.listdir(self.LANGUAGEPATH)
        languages = [f.split('.')[0] for f in files if f.endswith('.json')]
        return languages
    
    def AddLanguagePackage(self, language, datapath):
        import json
        with open(datapath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.PACKAGES.append({"language": language, "data": data})
        
        

    #? ################  TOOL API #####################

class ToolAPI:

    def __init__(self, sdk: dict=None, settings_path: str=None, enable_languages: bool=True):
        """Requires sdk{version, name}. Build for ToolOS"""
        self.SDK = SDK(sdk)
        self.Settings = SettingsAPI(self)
        if self.CheckCompatibility(self.Settings.VERSION, self.SDK.SDK_VERSION):
            self.Cache = CacheAPI(self.Settings.CACHEPATH)
            self.Temp = TempAPI(self.Settings.TEMPPATH)
            self.Package = PackageAPI(self.Settings.PACKAGEPATH)
            self.Log = LogAPI(self.Settings.LOGPATH)
            self.manager = ManagerAPI()
            self.helper = HelperAPI(self)
            self.language = LanguageAPI(self.Settings, standard_library=self.SDK.SDK_LangLib)
            self.state_machine = StateMachineAPI()

    def CheckCompatibility(self, api_version, sdk_version: str):
        major, minor, patch = sdk_version.split(".")
        if major != api_version.split(".")[0]:
            raise ValueError(f"Inkompatible Versionen: API {api_version} != SDK {sdk_version}")
        return True

    #? ################  Global API #####################
    
class Api:
    def __init__(self, sdk: dict=None, settings_path: str=None, enable_languages: bool=True):
        """ToolAPI's API-SDK. made for general use."""
        self.SDK = SDK(sdk)
        if not self.SDK.SDK_AVAILABLE:
            settings_path = settings_path
        self.Settings = SettingsAPI(self, settings_path=settings_path)
        self.Cache = CacheAPI(self.Settings.CACHEPATH)
        self.Temp = TempAPI(self.Settings.TEMPPATH)
        self.Package = PackageAPI(self.Settings.PACKAGEPATH)
        self.Log = LogAPI(self.Settings.LOGPATH)
        self.Manager = ManagerAPI()
        self.Helper = HelperAPI(self)
        self.Language = LanguageAPI(self.Settings, standard_library=self.SDK.SDK_LangLib if not enable_languages else False)
        self.StateMachine = StateMachineAPI()
        
        
class SDK:

    def __init__(self, sdk: dict):
        """ToolAPI's SDK. made for developers."""
        try:
            self.SDK = sdk
            self.SDK_VERSION = sdk.get("version")
            self.SDK_SETTINGS = sdk.get("settings_path")
            self.SDK_NAME = sdk.get("name")
            self.SDK_LangLib = sdk.get("standard_language_library")
            self.SDK_AVAILABLE = True
        except Exception:
                self.SDK_AVAILABLE = False


app = Api(settings_path="data\\assets\\api\\toolos\\toolos\\settings.json")
