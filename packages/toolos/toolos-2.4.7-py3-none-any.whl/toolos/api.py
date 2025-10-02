    #? ################  SETTINGS API #####################

class SettingsAPI:

    def __init__(self, app, settings_path: str=None):
        self.USE_SETTINGS_DICT = False
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
        if self.USE_SETTINGS_DICT:
            return self.DICT_SETTINGS
        try:
            import json
            if own and settings:
                return settings
            with open(self.SETTINGSPATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            raise FileNotFoundError(f"Einstellungsdatei nicht gefunden: {self.SETTINGSPATH}")
        
    def Global(self, key):
        if self.USE_SETTINGS_DICT:
            return self.DICT_SETTINGS.get(key, None)
        return self.SETTINGS.get(key, None)
    
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
        self.USE_SETTINGS_DICT = True
        self.DICT_SETTINGS = settings
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
        
        self.sequenceapi = None
        self.sSTATE = self.FIRST_ENTRY
        self.STATES = []
        
   #? Single State Functions
    
    def sSetState(self, new_state):
        self.sSTATE = new_state

    def sGetState(self):
        return self.sSTATE

    def sIsState(self, check_state):
        return self.sSTATE == check_state

    def sStateIsNot(self, state: str):
        return self.sSTATE != state

   #? Single State Functions with Key (format: 'state:key')

    def sSetStateKey(self, state: str, key: str):
        self.sSTATE = f"{state}:{key}"

    def sGetStateKey(self):
        if ":" in self.sSTATE:
            return self.sSTATE.split(":")[1]
        return None
    
    def sStateKeyIs(self, key: str):
        if ":" in self.sSTATE:
            return self.sSTATE.split(":")[1] == key
        return False
    
    def sIsStateKey(self, state: str, key: str):
        if ":" in self.sSTATE:
            s, k = self.sSTATE.split(":")
            return s == state and k == key
        return False
    
   #? Multi State Functions
   
    def Read(self):
        return self.STATES[-1]["id"], self.STATES[0]["id"]
    
    def mAddState(self, state: str = "name", key: dict = {}):
        self.STATES.append({"id": len(self.STATES) + 1, "state": state,
                            "key": key})
        
    def mGetStates(self):
        return self.STATES
    
    def mGetState(self, id: int):
        for state in self.STATES:
            if state["id"] == id:
                return state
        return None
    
    def mIsState(self, state: str):
        for s in self.STATES:
            if s["state"] == state:
                return True
        return False

    def isKeyInState(self, key: str, get: str):
        for s in self.STATES:
            if s["key"] == key:
                if get in s["key"]:
                    return s["key"][get]
        return None

    def mGetState(self, index: int):
        for state in self.STATES:
            if state["id"] == index:
                return state
            
    def mRemoveState(self, id: int):
        for state in self.STATES:
            if state["id"] == id:
                self.STATES.remove(state)
                return True
        return False
    
    def mGetIdByState(self, state: str):
        for s in self.STATES:
            if s["state"] == state:
                return s["id"]
        return None
    
    def mGetStateByKey(self, key: dict):
        for s in self.STATES:
            if s["key"] == key:
                return s
        return None
    
    def mGetIdByKey(self, key: dict):
        for s in self.STATES:
            if s["key"] == key:
                return s["id"]
        return None
    
    def mListStates(self):
        __all__ = []
        for s in self.STATES:
             __all__.append(s["state"])
        return __all__
    
    def mClearStates(self):
        self.STATES = []
        
   #? ################  Sequence Functions #####################
   
    def Connect(self, sequence):
        self.sequenceapi = sequence
        
    def RunSequenceOn(self, state: str, sequence_name: str, allow_clear: bool=True, enable_header: bool=False, library: str="d"):
        if self.sequenceapi:
            if self.sIsState(state):
                self.sequenceapi.DoSequence(sequence=sequence_name, allow_clear=allow_clear, enable_header=enable_header, library=library)
                return True
            return False
        else:
            raise ValueError("No SequenceAPI connected. Use 'Connect()' to connect a SequenceAPI instance.")
        
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
        
    
    #? ################  Animation API #####################
    
class SequenceAPI:
    
    def __init__(self, helper, force_terminal_print: bool = True, use_rich: bool = True, enable_animation: bool = True):
        import rich
        self.Dynamic = ["r", "-x"]
        self.Static = ["d", "", None]
        self.Sequence = []
        self.rich = rich    
        self.helper = helper
        self.force_terminal_print = force_terminal_print
        self.use_rich = use_rich
        self.enable_animation = enable_animation


    def LoadingSymbol(self, clear_screen: bool=False, can_add_nexto_text: bool = True, show_text: str=False, smooth_loading: bool=True, loading: int=5):
        
        import time
        import sys
        if loading: # Passe 'wait' : '4' -> 4 s in loading
            loading = loading *5
        symbols = ['|', '/', '-', '\\', '|', '/', '-', '\\'] * loading if smooth_loading else loading if loading else ['|', '/', '-', '\\', '|', '/', '-', '\\']
        for symbol in symbols:
            if clear_screen:
                if self.use_rich and not self.force_terminal_print:
                    self.rich.print(f"\r{symbol} {show_text}" if show_text else f"\r{symbol}", end='', flush=True)
                else:
                    print(f"\r{symbol} {show_text}" if show_text else f"\r{symbol}", end='', flush=True)
            else:
                if self.use_rich and not self.force_terminal_print:
                    self.rich.print(f"{symbol} {show_text}" if show_text else f"{symbol}", end='', flush=True)
                else:
                    print(f"{symbol} {show_text}" if show_text else f"{symbol}", end='', flush=True)
            time.sleep(0.1)
                
    def StartUpSequence(self, startup_meta: dict, header: str="Loading...", smooth_loading: bool=True):
        """Create a Startup-Sequence from a dict with the following format:
        ```python
        startup_meta = [
            {"pos": 1, "text": "Loading Modules", "wait": 1},
            {"pos": 2, "text": "Initializing Components", "wait": 2},
            {"pos": 3, "text": "Starting Application", "wait": 1}
        ]
        StartUpSequence(startup_meta)
        ```
        """
        print(header)
        self.header = header
        self.AddSequence({"sequence": "flow", "meta": startup_meta})
        self.ReadSequence("flow")
        self.DoSequence(sequence="flow")

    def AddSequence(self, sequence: dict):
        self.Sequence.append({
            "sequence": sequence.get("sequence"),
            "meta": sequence.get("meta", {})
        })

    def ReadSequence(self, name: str):
        for seq in self.Sequence:
            if seq["sequence"] == name:
                return seq
   #? Global Sequence Running (Connectable with StateMachine)
    def DoSequence(self, sequence: str, allow_clear: bool=True, enable_header: bool=False, library: str="d"):
        """Requires a Sequence in self.Sequence:
        ## Parameters:
        - Sequence: str, name of the sequence to run in self.Sequence
        - allow_clear: bool, if True, clears the screen after each step
        - enable_header: bool, if True, prints the header before each step
        - library: str, "d" for static Sequences (Built-in), "r" for dynamic Sequences (requires own metadata and sdk)
        
        ### Example Static Sequence:
        ```python
        static_sequence = [
            {"sequence": "flow", "meta": {your-sequence}},
            {"sequence": "name", "meta": {your-sequence}}
        ]
        ```
        ```python
        dynamic_sequence = [
            {"sequence": "namexyz", "attributes": "<recognice_attr>", "meta": {your-sequence}},
            {"sequence": "nameabc", "attributes": "<recognice_attr>", "meta": {your-sequence}}
        ]
        ```
        ## Adding Sequences to StateMachine:
        ```python
        self.StateMachine.sequenceapi.Connect(self.Helper.Sequence)
        self.StateMachine.RunSequenceOn()
        ```
        """
        def ReadSequences():
            __all__ = []
            for seq in self.Sequence:
                __all__.append(seq["sequence"])
            return __all__
        
        current = self.ReadSequence(sequence)
        __all__ = ReadSequences()
        if library in self.Static:
            if current == "flow":
                for step in current["meta"]:
                    if enable_header:
                        print(self.header)
                    a = f" {step.get('text')}"
                    if x:= step.get('wait', 0) > 0:
                        self.LoadingSymbol(clear_screen=True, can_add_nexto_text=False, show_text=a, loading=x)
                    if allow_clear:
                        import os
                        os.system('cls' if os.name == 'nt' else 'clear')
                    print(a)
                
        else:
            if library in self.Dynamic:
                if current['attributes'] == f'sdk.{self.helper.SDK.SDK_SOURCETAR}':
                    pass
            else:
                raise ValueError(f"Library '{library}' not found. Available: {__all__}")
                        

                
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
        try:
            self.app = app
            self.ui = GuiAPI()
            self.command = CommandAPI(app)
            self.Sequence = SequenceAPI(helper=app, force_terminal_print=True, use_rich=False, enable_animation=True)
        except Exception as e:
            log = self.app.Settings.Global("log")
            logpath = self.app.Settings.Global("logpath")
            self.app.Log.WriteLog(f"{logpath}/error.log", f"Error initializing HelperAPI: {e}")

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
            self.LANGUAGE = self.Settings.Global("language")
            self.LANGUAGEPATH = self.Settings.Global("LANGUAGEPATH")
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
        self.LANGUAGE = self.Settings.Global("language")
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
        """Requires sdk{version, name}. Build for ToolOS
        
        # OUTDATED - use Api class instead!"""
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
    def __init__(self, sdk: dict=None, settings_path: str=None, enable_languages: bool=True, settings: dict=None, crack_bot: bool=False):
        """
            ![ClayTech](file:///C:/Users/hatte/Downloads/py_claytech_badge.svg)
            ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
            ## ToolAPI's API-SDK. made for general use.
        
            ## Parameters:
            ```python
            sdk: dict = None
            settings_path: str = None
            enable_languages: bool = True
            settings: dict = None
            crack_bot: bool = False
            ```
            
            ## API
            ```python
            self.Settings  # SettingsAPI
            self.Cache  # CacheAPI
            self.Temp  # TempAPI
            self.Package  # PackageAPI
            self.Log  # LogAPI
            self.Manager  # ManagerAPI
            self.Helper  # HelperAPI
            self.Language  # LanguageAPI
            self.StateMachine  # StateMachineAPI
            self.App  # AppAPI
            self.SDK  # SDK
            ```
            # Language Api (Mini Reference)
            
            add language package:
            
            ```python
            self.Language.AddLanguagePackage(language, datapath)
            ```
            
            translate key:
            ```python
            self.Language.Translate("hello_world")
            ```
            
            get all translation keys:
            ```python
            self.Language.GetAllTranslationKeys()
            ```
            
            get available languages:
            ```python
            self.Language.GetAvailableLanguages()
            ```
            
            reload language data:
            ```python
            self.Language.Reload()
            ```
            
            ## StateMachine Api (Mini Reference)
            
            ### Single State Functions:
            ```python
            self.StateMachine.sSetState()
            self.StateMachine.sGetState()
            ```
            
            ### Single State Functions with Key ('state:key')
            
            ```python
            self.StateMachine.sSetStateKey()
            self.StateMachine.sGetStateKey()
            ```
            
            ### Multi State Functions:
            
            ```python
            self.StateMachine.mAddState(state="state_name", key={"key1": "value1"})
            self.StateMachine.mGetStates()
            ```
            # Details
            Last Updated: 01.10.25
            Version: v2.4.7
            Api-Reference: https://pypi.org/project/toolos/
            Author: Lilias Hatterscheidt
            Copyright © 2025 ClayTechnologie. All rights reserved.
            
            
            """
        self.OwnSettings = settings
        
        self.CACHEPATH = None
        self.TEMPPATH = None
        self.PACKAGEPATH = None
        self.LOGPATH = None
        
        
        self.SDK = SDK(sdk)
        self.Settings = SettingsAPI(self, settings_path=settings_path if settings_path else None)
        if not self.SDK.SDK_AVAILABLE:
            settings_path = settings_path
        if self.OwnSettings:
            self.Settings.SetSettings(settings=self.OwnSettings)
            if not self.Settings.USE_SETTINGS_DICT:
                self.CACHEPATH = None
                self.TEMPPATH = None
                self.PACKAGEPATH = None
                self.LOGPATH = None
            
            self.CACHEPATH = self.Settings.Global("CACHEPATH")
            self.TEMPPATH = self.Settings.Global("TEMPPATH")
            self.PACKAGEPATH = self.Settings.Global("PACKAGEPATH")
            self.LOGPATH = self.Settings.Global("LOGPATH")
        
        self.Cache = CacheAPI(self.CACHEPATH)
        self.Temp = TempAPI(self.TEMPPATH)
        self.Package = PackageAPI(self.PACKAGEPATH)
        self.Log = LogAPI(self.LOGPATH)
        self.Manager = ManagerAPI()
        self.Helper = HelperAPI(self)
        self.Language = LanguageAPI(self.Settings, standard_library=self.SDK.SDK_LangLib if not enable_languages else False)
        self.StateMachine = StateMachineAPI()
        self.App = AppAPI(self)
        if crack_bot:
            self.Bot = BotDriver(self, self.Settings, settings_path if settings_path else None)
        
    #? ################  SDK #####################
   
class SDK:

    def __init__(self, sdk: dict):
        """ToolAPI's SDK. made for developers."""
        try:
            self.SDK = sdk
            self.SDK_VERSION = sdk.get("version", "2.4.7")
            self.SDK_SETTINGS = sdk.get("settings_path")
            self.SDK_NAME = sdk.get("name")
            self.SDK_LangLib = sdk.get("standard_language_library")
            self.SDK_AVAILABLE = True
            self.SDK_SOURCETAR = self.GetSDKSuperManifest()
        except Exception:
                self.SDK_AVAILABLE = False
                
    def GetSDKSuperManifest(self):
        import secrets
        import hashlib
        token = secrets.token_hex(len(self.SDK_VERSION))
        return hashlib.sha256(token.encode()).hexdigest()


class BotDriver:

    def __init__(self, settings: dict, config_path: str, metadata: list[dict, dict, dict]=None, app = None):
        """Provides a full Discord-Bot Development Environment with several helper functions and Api-based Working
        The settings dict must contain at least the following keys: BOT_APIKEY, GUILD_ID
        # Use built-ins!:
         
        - self.discord
        - self.commands
        - self.tasks
        - self.app_commands
        - self.asyncio
        - self.os
        # Use Settings: 
        - self.Settings
        - self.Config
        - self.BotMetadata
        - self.ApiKey
        - self.GuildId"""
        import discord
        import discord.ext.commands as commands
        import discord.ext.tasks as tasks
        import discord.app_commands as app_commands
        import asyncio
        import os
        self.BotMetadata = metadata if metadata else None
        self.Settings = settings
        self.Config = config_path
        self.discord = discord
        self.commands = commands
        self.tasks = tasks
        self.app_commands = app_commands
        self.asyncio = asyncio
        self.os = os
        self.app = app
        try:
            self.Settings.SetSettings(settings=self.Settings)
            self.Settings.update()
            self.ApiKey = self.Settings.Global("BOT_APIKEY")
            self.GuildId = self.Settings.Global("GUILD_ID")
            
        except Exception:
            self.SETTINGS_LOADED = None
        finally:
            self.SETTINGS_LOADED = True
            self.Config = config_path
            
            
    def GetApiKey(self):
        return self.ApiKey
    
    def GetGuildId(self):
        return self.GuildId
    
    def GetConfigPath(self):
        return self.Config
    
    
    def RunBot(self, key: str = None):
        self.bot = self.commands.Bot(command_prefix="!", intents=self.discord.Intents.all())
        self.bot.run(key if not None else self.ApiKey)
        
        
haha = Api()
