# Plugins

## getPluginSettings

获取插件的配置参数

```javascript
dtable.getPluginSettings(pluginName);
```

其中

* pluginName: 插件名字

例子

```javascript
const pluginName = 'gallery';
const pluginSetting = dtable.getPluginSettings(pluginName);
```

## updatePluginSettings

更新插件的配置参数

```javascript
dtable.updatePluginSettings(pluginName, pluginSettings);
```

其中

* pluginName: 插件名字
* pluginSettings: 插件的配置参数

例子

```javascript
const pluginName = 'gallery';
const pluginSettings = {};
dtable.updatePluginSettings(pluginName, pluginSettings);
```

## deletePluginSettings

删除插件的配置参数

```javascript
dtable.deletePluginSettings(pluginName);
```

其中

* pluginName: 插件名字

例子

```javascript
const pluginName = 'gallery';
dtable.deletePluginSettings(pluginName);
```
