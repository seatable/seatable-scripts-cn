# Plugins

## getPluginSettings

获取插件的配置参数

```javascript
window.dtableSDK.getPluginSettings(pluginName);
```

其中

* pluginName: 插件名字

例子

```javascript
const pluginName = 'gallery';
const pluginSetting = window.dtableSDK.getPluginSettings(pluginName);
```

## updatePluginSettings

更新插件的配置参数

```javascript
window.dtableSDK.updatePluginSettings(pluginName, pluginSettings);
```

其中

* pluginName: 插件名字
* pluginSettings: 插件的配置参数

例子

```javascript
const pluginName = 'gallery';
const pluginSettings = {};
window.dtableSDK.updatePluginSettings(pluginName, pluginSettings);
```
