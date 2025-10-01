# ToolOS SDK

A lightweight Python app framework with inheritance-based architecture, multi-language support, and modular design.

## 📚 Documentation

**🌐 Complete Documentation:** https://claytechnologie.github.io/ToolSDK/


### Quick Links for more information:
- 🚀 [Getting Started](https://claytechnologie.github.io/ToolSDK/getting-started/)
- 📋 [API Reference](https://claytechnologie.github.io/ToolSDK/api-reference/)
- 🎮 [Modding SDK](https://claytechnologie.github.io/ToolSDK/modding-sdk/)

## Installation

```bash
pip install toolos
```

# Getting Started

This guide will help you get started with ToolOS SDK and build your first application.



## Your First ToolOS Application

### 1. Create a Settings File and SDK

First, create a `settings.json` file to configure your application:

```json
{
  "version": "1.0.0",
  "language": "en",
  "cachepath": "data/cache",
  "temppath": "data/temp",
  "logpath": "data/logs",
  "languagepath": "data/lang"
}
```

Then, initialize the SDK in your application:
as a JSON file:
```json
{
  "version": "1.0.0",
  "name": "MyAppSDK",
  "settings_path": "settings.json",
  "standard_language_library": true
}
```
or as a dictionary in your code:
```python
sdk = {
  "version": "1.0.0",
  "name": "MyAppSDK",
  "settings_path": "path/to/settings.json",
  "standard_language_library": True
app = MyApp(**sdk)
...
```

### 2. Application Usages

Create your main application file:


```python
# app.py
import toolos as engine

class MyApp(engine.Api):
    
    def __init__(self, sdk**):

        super().__init__(sdk=sdk)

        self.Helper # Helper Class Function
        self.Log # Log Class Function
        self.Cache # Cache Class Function
        self.Temp # Temp Class Function
        self.Settings # Settings Class Function
        self.StateMachine # StateMachine Class Function
        self.Language # Language Class Function
        self.Utils # Utils Class Function
```

## 3. Short API Usage

ToolOS SDK includes several built-in functionalities for smooth and efficient app development.

Language Management:
```python
import toolos as api

class YourApp(api.Api):

    def __init__(self, sdk**):
        # standard_language_library = True Enables loading built-in language files (en, de, fr, ru, ...)
        super().__init__(sdk=sdk)

        self.Language # Language Class Function
        
        # Reading Language Files
        self.Language.GetAvailableLanguages()
        
        # Reading Language UsageKeys for a specific language
        self.Language.GetAllTranslationKeys(lang="de")
        # Returns: list: ['key1', 'key2', ...] for language "de"
        
        # Reading Language UsageKeys for current language
        self.Language.GetAllTranslationKeys()
        # Returns: list: ['key1', 'key2', ...] for current language
        
        # Translate Texts
        print(self.Language.Translate("settings")) # Dynamic Translates to current language (settings.json)
        # Prints "Einstellungen" if current language is "de" or "Settings" if current language is "en"
        
        # Adding a own translationpackage
        
        # Add a specific language package
        de_lang = "/data/lang/de_extras.json"
        fr_lang = "/data/lang/fr_extras.json"
        en_lang = "/data/lang/en_extras.json"
        
        # Adding language packages
        self.Language.AddLanguagePackage("de", de_lang)
        self.Language.AddLanguagePackage("fr", fr_lang)
        self.Language.AddLanguagePackage("en", en_lang)
        
        # Reaload Language Instance
        self.Language.Reload()
        
        # Now the new keys are available
        print(self.Language.Translate("new_key")) # Dynamic Translates to current language (new_key from de_extras.json)
        # Prints "Neuer Schlüssel" if current language is "de" or "New Key
```

Example language package (de/fr/... .json)

Example de.json:
```json
{
  "new_key": "Neuer Schlüssel",
  "another_key": "Ein weiterer Schlüssel",
  "header": "Überschrift"
}
```
Or ru.json:
```json
{
  "new_key": "Новый ключ",
  "another_key": "Еще один ключ",
  "header": "Заголовок"
}
```


### 4. State Management

Use the state machine to control application flow:

```python
import toolos as engine

class YourApp(engine.Api):
    
    def __init__(self, sdk**):
        super().__init__(sdk=sdk)
        self.StateMachine.AddKeyState("mods", False)  # Adding a key state "mods" with default value False # Use this together with Settings.Global("mods_enabled", False) like:
        mods = self.Settings.Global("mods_enabled", False)
        self.StateMachine.SetKeyState("mods", mods)

        # The StateMachine automatically starts with "FIRST_ENTRY" state
        while self.StateMachine.IsRunning: # IsRunning is always True unless you stop it

            if self.StateMachine.IsState(self.StateMachine.FIRST_ENTRY):
                # Your logic for FIRST_ENTRY state

                # Transition to MAINMENU state
                self.StateMachine.SetState(self.StateMachine.MAINMENU)
                
            elif self.StateMachine.IsState(self.StateMachine.MAINMENU):
                # Your logic for MAINMENU state

                # Transition to STEP_1 state
                self.StateMachine.SetState(self.StateMachine.STEP_1)
                
            elif self.StateMachine.IsState(self.StateMachine.ERROR):
                # Your logic for ERROR state
                self.StateMachine.SetState(self.StateMachine.EXIT)  # Transition to EXIT state
                
            elif self.StateMachine.IsState(self.StateMachine.EXIT):
                # Your logic for EXIT state
                self.StateMachine.Stop()  # Stop the state machine loop

            elif self.StateMachine.KeyStateIs("mods", key=True):
                # Your logic when "mods" key state is True. If mods doesnt exist or is False, it will always return False
                pass

```
### 5. Settings Management

Handle application settings dynamically:
```python
import toolos as engine

class YourApp(engine.Api):

    def __init__(self, sdk):
        super().__init__(sdk=sdk)

        yourneed = self.Settings.Global("yourneed", "default_value")
        # Returning "default_value" if "yourneed" is not set in settings.json
        # else returns the value of your key "yourneed"
        
        # Practical Example:
        if mods_enabled := self.Settings.Global("mods_enabled", False):
            self.StateMachine.SetKeyState("mods", mods_enabled)
        else:
            self.StateMachine.SetKeyState("mods", mods_enabled)
            
        # Check if settings were updated and reload if necessary
        if self.Settings.CheckIfUpdate():
            self.Settings.Update()
```

### Caching System

Efficiently manage temporary data:

```python

class YourApp(engine.Api):

    def __init__(self, sdk):
        super().__init__(sdk=sdk)

        import json
        
        preferences = {
            "theme": "dark",
            "font_size": 14,
            "show_tips": True
        }
        cachepath = self.Settings.Global("cachepath", "/")
        cachename = self.Settings.Global("cachename", "example.cache")
        # Write a cache file
        self.Cache.WriteCacheFile(f"{cachepath}{cachename}", json.dumps(preferences))

# Read cache file
if self.Cache.CacheExists(f"{cachepath}{cachename}"):
    data = self.Cache.ReadCacheFile(f"{cachepath}{cachename}")
    preferences = json.loads(data)
```
## Temporary File Management
Manage temporary files easily:

```python
# Write temp file
self.Temp.WriteTempFile("user_prefs.json", json.dumps(preferences))

# Read temp file
if self.Temp.TempExists("user_prefs.json"):
    data = self.Temp.ReadTempFile("user_prefs.json")
    preferences = json.loads(data)
```

### Logging Management

Keep track of application events:

```python
# Log different types of events
self.Log.WriteLog("app.log", "User logged in")
self.Log.WriteLog("error.log", f"Error: {str(exception)}")
self.Log.WriteLog("debug.log", f"Processing item {item_id}")
```
# SDK's

For Working with the ToolOS you need a SDK. 
Here are The SDK usage and guide:

Setting SDK version
```json
{
  "version": "1.0.0"
}
```

Setting SDK name
```json
{
  "name": "MyAppSDK"
}
```
Setting SDK settings path
```json
{
  "settings_path": "path/to/settings.json"
}
```

Setting SDK standard language library usage
```json
{
  "standard_language_library": true
}
```

# Example SDK (copy-paste)
```python
sdk = {
  "version": "1.0.0",
  "name": "MyAppSDK",
  "settings_path": "path/to/settings.json",
  "standard_language_library": True
}


## Next Steps

- Explore the [API Reference](api/overview.md) for detailed documentation
- Check out [Examples](examples.md) for more complex use cases
- Learn about creating mods and extensions
- Read the [Contributing Guide](contributing.md) to contribute to ToolOS SDK

## Best Practices

1. **Always initialize with settings file**: Use a proper `settings.json` configuration
2. **Handle language changes**: Implement `Language.Reload()` for dynamic language switching and use 'lang.json' files for translations
3. **Use state machine**: Organize your application flow with the built-in state machine
4. **Log important events**: Use the logging system for debugging and monitoring
5. **Clean up temporary files**: Use `Temp.RemoveTempFile()` to manage temporary data

## License

MIT