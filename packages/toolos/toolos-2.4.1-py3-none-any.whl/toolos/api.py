    #? ################  SETTINGS API #####################

class SettingsAPI:

    def __init__(self, app, settings_path: str=None):
        try:
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
        except Exception:
            pass

    def LoadSettings(self, own=False, settings: dict=None):
        try:
            import json
            if own and settings:
                return settings
            with open(self.SETTINGSPATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            raise FileNotFoundError(f"Einstellungsdatei nicht gefunden: {self.SETTINGSPATH}")
        
    def Global(self, key):
        return self.SETTINGS.get(key)
    
    def SetUpdate(self):
        try:
            self.SETTINGS["update"] = True
            import json
            with open(self.SETTINGSPATH, 'w', encoding='utf-8') as f:
                json.dump(self.SETTINGS, f, indent=4)
        except Exception:
            return False
            
    def CheckIfUpdate(self):
        return self.SETTINGS.get("update", False)
    
    def SetSettingsPath(self, path):
        self.SETTINGSPATH = path
        self.Update()
        
    def SetSettings(self, settings: dict):
        if not isinstance(settings, dict):
            return False
        self.LoadSettings(own=True, settings=settings)
    
    
    def Update(self):
        try:
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
        except Exception:
            return False

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
    LOGIN = "login"
    VERIFIED = "verified"
    
    
    
    def __init__(self):
        """beginning with first_entry state"""
        self.state = self.FIRST_ENTRY
        
    def SetState(self, new_state):
        self.state = new_state
        
    def GetState(self):
        return self.state
    
    def IsState(self, check_state):
        return self.state == check_state
    
    def StateIsNot(self, state: str):
        return self.state != state
    
    def SetStateKey(self, state: str, key: str):
        self.state = f"{state}:{key}"
        
    def GetStateKey(self):
        if ":" in self.state:
            return self.state.split(":")[1]
        return None
    
    def StateKeyIs(self, key: str):
        if ":" in self.state:
            return self.state.split(":")[1] == key
        return False
    
    def IsStateKey(self, state: str, key: str):
        if ":" in self.state:
            s, k = self.state.split(":")
            return s == state and k == key
        return False

    #? ################  CACHE API #####################

class CacheAPI:
    
    def __init__(self, cache_path=None):
        try:
            self.CACHEPATH = cache_path
            if not self.CacheExists():
                import os
                os.makedirs(cache_path)
        except Exception:
            pass
    
    def SetCachePath(self, path):
        self.CACHEPATH = path
        if not self.CacheExists():
            import os
            os.makedirs(path)
        
        
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
        try:
            import os
            if filename:
                return os.path.exists(f"{self.CACHEPATH}/{filename}")
            return os.path.exists(self.CACHEPATH)
        except Exception:
            return False

    #? ################  TEMP API #####################

class TempAPI:
    
    def __init__(self, temp_path=None):
        try:
            self.TEMPPATH = temp_path
            if not self.TempExists():
                import os
                os.makedirs(temp_path)
        except Exception:
            pass
        
    def SetTempPath(self, path):
        self.TEMPPATH = path
        if not self.TempExists():
            import os
            os.makedirs(path)
        
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
        try:
            import os
            if filename:
                return os.path.exists(f"{self.TEMPPATH}/{filename}")
            return os.path.exists(self.TEMPPATH)
        except Exception:
            return False

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
    
    def __init__(self, package_path=None):
        self.PACKAGEPATH = package_path
        self.isLoggedIn = False
        self.USERNAME = None
        
    def SetPackagePath(self, path):
        self.PACKAGEPATH = path
        if not self.PackageExists():
            import os
            os.makedirs(path)
        
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
    
    def __init__(self, log_path=None):
        try:
            self.LOGPATH = log_path
            if not self.LogExists():
                import os
                os.makedirs(log_path)
        except Exception:
            pass
            
    def SetLogPath(self, path):
        self.LOGPATH = path
        if not self.LogExists():
            import os
            os.makedirs(path)
        
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
        try:
            import os
            if filename:
                return os.path.exists(f"{self.LOGPATH}/{filename}")
            return os.path.exists(self.LOGPATH)
        except Exception:
            return False
            
            

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
        try:
            self.app = app
            self.ui = GuiAPI()
            self.command = CommandAPI(app)
        except Exception:
            pass

    def GetVersion(self):
        return self.app.Settings.VERSION

    def GetLanguage(self):
        return self.app.Settings.LANGUAGE
    
    

class CommandAPI:

    def __init__(self, app):
        try:
            self.app = app
        except Exception:
            pass

    def Execute(self, command):
        import subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    
    #? ####################  AI API #####################
    
class AiAPI:
    def __init__(self, api_key=None, model="gpt-4", temperature=0.7):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        
    def SetApiKey(self, api_key):
        self.api_key = api_key
        
    def GenerateText(self, prompt):
        if not self.api_key:
            raise ValueError("API key is not set.")
        import openai
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    #? ################  LANGUAGE API #################

class LanguageAPI:

    def __init__(self, settings, standard_library=True, enable_ai_translation=False):
        try:
            self.Settings = settings
            self.LANGUAGE = settings.LANGUAGE
            self.LANGUAGEPATH = settings.LANGUAGEPATH
            self.PACKAGES = []
            self.ENABLE_AI_TRANSLATION = enable_ai_translation
            if self.ENABLE_AI_TRANSLATION:
                self.AI = AiAPI()
                
            if standard_library:
                import os
                package_dir = os.path.dirname(os.path.abspath(__file__))
                self.LANGUAGEPATH = os.path.join(package_dir, "data", "lang")
            self.language_data = self.LoadLanguageData(self.LANGUAGE)
        except Exception:
            pass
        
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
        if self.ENABLE_AI_TRANSLATION:
            x = self.AI.GenerateText(f"Translate the following key to {self.LANGUAGE}: {key}")
            return x
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
        
    
    #? ################  APP API #####################
    
class AppAPI:
    
    def __init__(self, app):
        self.app = app
        self.MENU = []
        self.IMENU = []
        
    
    def BuildMenu(self, menus: list=None, start=0):
        if not menus:
            menu = self.MENU if not None else []
        else:
            menu = menus
        for i, key in enumerate(menu, start=start):
            self.InteractiveMenu = {
                "index": i,
                "name": key,
                "lambda": None
            }
            self.IMENU.append(self.InteractiveMenu)
            
    def AddLambdaToMenu(self, index, func):
        for item in self.IMENU:
            if item["index"] == index:
                item["lambda"] = func
                return True
        return False
    
    def ClearMenu(self):
        self.MENU = []
        self.IMENU = []
            
    def ShowMenu(self, menus: list=None):
        if menus:
            for i, key in enumerate(menus):
                print(f"{i}: {key}")
        else:
            for item in self.IMENU:
                print(f"{item['index']}: {item['name']}")

    def SelectMenuLambda(self, index):
        for item in self.IMENU:
            if item["index"] == index and item["lambda"]:
                return item["lambda"]
                    
                
    def SelectMenu(self, index, use_imenu: bool=False):
        if use_imenu:
            for item in self.IMENU:
                if item["index"] == index:
                    return item["name"]
        else:
            if index < len(self.MENU):
                return self.MENU[index]
        return None
    
    def GetIndexAndKey(self, index):
        for item in self.IMENU:
            if item["index"] == index:
                return item["name"], item["lambda"] if item["lambda"] else None
        return None, None
    
    def AskInput(self, input_style=None):
        if input_style == "terminal":
            return input("$ ")
        return input("> ")
            
        
        

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
            self.app = AppAPI(self)

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
        self.Settings = SettingsAPI(self, settings_path=settings_path if settings_path else None)
        self.Cache = CacheAPI(self.Settings.CACHEPATH if self.Settings.CACHEPATH else None)
        self.Temp = TempAPI(self.Settings.TEMPPATH if self.Settings.TEMPPATH else None)
        self.Package = PackageAPI(self.Settings.PACKAGEPATH if self.Settings.PACKAGEPATH else None)
        self.Log = LogAPI(self.Settings.LOGPATH if self.Settings.LOGPATH else None)
        self.Manager = ManagerAPI()
        self.Helper = HelperAPI(self)
        self.Language = LanguageAPI(self.Settings, standard_library=self.SDK.SDK_LangLib if not enable_languages else False)
        self.StateMachine = StateMachineAPI()
        self.App = AppAPI(self)
        
    #? ################  SDK #####################
   
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
                
            
