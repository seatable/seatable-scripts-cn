# SeaTable 插件开发流程

在这个指南中，我们会一步步的演示怎么给 SeaTable 写一个扩展。这个扩展可以显示表格基本信息，包括

- 子表的个数
- 总的记录数
- 协作人数目

插件开发实例的代码很简单，你可以点击这个 [github链接](https://github.com/seatable/seatable-plugin-table-info) 获取源码

插件开发流程如下。

## 插件开发基本流程

### 1. 安装插件开发脚手架

```bash
npm install -g create-dtable-plugin
```

### 2. 通过脚手架创建插件

```bash
create-dtable-plugin init seatable-plugin-table-info
```

安装依赖

~~~bash
cd seatable-plugin-table-info
npm install
~~~

### 3. 修改插件配置

修改 plugin-config 文件夹中 info.json 配置文件

```
"name": '',                   // 插件英文名字，只能包含字母、数字、下划线、中划线
"version": '',                // 插件版本号
"display_type: '',            // 插件展示类型 "dialog" | 'overlay'
"display_name": '',           // 插件显示的名字
"description": '',            // 插件功能相关描述
```

这里不需要添加其他配置参数，其他参数由打包工具自动生成。

可选操作

- 在 plugin-config 文件夹中添加自定义的 icon.png 作为插件的图标（可不提供，采用默认图标。icon.png 要求是 128x128 像素)
- 在 plugin-config 文件夹中添加自定义的 card_image.png 作为插件图标的背景图（可不提供，显示默认背景。card_image.png 要求是 560x240 像素)
  
### 4. 修改entry.js文件中的插件注册函数 

```
  更新 window.app.registerPluginItemCallback('test', TaskList.execute);
  ⬇️
  为： window.app.registerPluginItemCallback(name, TaskList.execute);  此处的 name 值为 plugin-config/info.json 中的 “name” 值
```

### 5. 添加插件开发配置文件

在项目 src 文件夹中有一个文件 setting.local.dist.js, 将其 copy 一份 并命名为 setting.local.js
文件内容如下, 按照注释进行修改即可

```js
const config = {
  APIToken: "**",               // 需添加插件的 dtable 的 apiToken
  server: "**",                 // 需添加插件的 dtable 的部署网址
  workspaceID: "**",            // 需添加插件的 dtable 所在的 workspace 的 id 值
  dtableName: "**",             // 需添加插件的 dtable 的名字
  lang: "**"                    // 插件默认语言类型，en 或者 zh-cn
};
```


### 6. 开始开发

运行本地开发环境

```bash
npm start
```

在浏览器上打开 localhost:3000 可以看到插件对话框已经打开，对话框中默认显示通过 dtable-sdk 组件库提供的接口函数
1. (getTables)获取的dtable表格的子表信息
2. (getRelatedUsers)获取的dtable协作人的详细信息

主要代码及用途

* /src/index.js 本地开发插件的入口文件
* /src/entry.js 按照到 SeaTable 后作为插件运行时的入口文件
* /src/app.js 插件主要代码

### 7. 显示表格基本信息

写一个 TableInfo 的组件，这个组件需要传入 tables 和 collaborators 两个 Props

```jsx
class TableInfo extends React.Component {
}

const propTypes = {
  tables: PropTypes.array.isRequired,
  collaborators: PropTypes.array.isRequired,
};

TableInfo.propTypes = propTypes;

export default TableInfo;
```

获取子表的个数

```js
getTablesNumber = (tables) => {
  return (tables && Array.isArray(tables)) ? tables.length : 0;
}
```

获取总的记录数

```js
getRecords = (tables) => {
  let recordsNumber = 0;
  if (!tables) return recordsNumber;
  for (let i = 0; i < tables.length; i++) {
    const table = tables[i];
    const rows = table.rows;
    if (rows && Array.isArray(rows)) {
      recordsNumber += rows.length;
    }
  }
  return recordsNumber;
}
```

获取协作人及数量

```jsx
renderCollaborators = (collaborators) => {
  if (!collaborators || !Array.isArray(collaborators)) {
    return null;
  }
  return collaborators.map((collaborator, index) => {
    return (
      <div key={index} className="collaborator">
        <span className="collaborator-avatar-container">
          <img className="collaborator-avatar" alt='' src={collaborator.avatar_url}/>
        </span>
        <span className="collaborator-name">{collaborator.name}</span>
      </div>
    );
  });
}
```

界面渲染：子表的个数、总的记录数、协作人数目

```jsx
render() {
  const { tables, collaborators } = this.props;
  return (
    <div>
      <div>{'子表的个数: '}{this.getTablesNumber(tables)}</div><br/>
      <div>{'总的记录数: '}{this.getRecords(tables)}</div><br/>
      <div>{'协作人数量: '}{collaborators ? collaborators.length : 0}</div><br/>
      <div className="plugin-collaborators">{this.renderCollaborators(collaborators)}</div>
    </div>
  );
}
```

在父组件 app.js 中调用 TableInfo 组件，并修改 app.js 中的 render 函数，传入 tables 和 collaborators。

```jsx
import PropTypes from 'prop-types';
import TableInfo from './table-info';

class App extends React.Component{
  let tables = window.dtableSDK..getTables();
  let collaborators = window.dtableSDK.getRelatedUsers();
  render() {
    return (
      <Modal isOpen={showDialog} toggle={this.onPluginToggle} contentClassName="dtable-plugin plugin-container" size='lg'>
        <ModalHeader className="test-plugin-header" toggle={this.onPluginToggle}>{'插件'}</ModalHeader>
        <ModalBody className="test-plugin-content">
          <TableInfo tables={tables} collaborators={collaborators}/>
        </ModalBody>
      </Modal>
    );
  }
}

App.propTypes = {
  row: PropTypes.object, // 如果插件是通过按钮打开的，会有一个row参数
}
```

增加 css/table-info.css 文件，修改插件的样式。

再次运行 `npm start `，即可在浏览器上 localhost: 3000 看到下面的信息。

```md
子表的个数: X
总的记录数: XXX
协作人数量: X
```

### 8. 打包上传插件

1. 执行 `npm run build-plugin` 打包插件，打包后插件的路径为 /plugin/task.zip 

2. 将插件 task.zip 上传到 dtable 中

## 官方提供的插件开发工具库

1. dtable-sdk
2. dtable-utils
3. dtable-ui-component

### dtable-sdk
> 覆写 Base 应用向插件提供的 api. 主要用于插件开发阶段，用于获取，删除，更新 Base 数据,本地开发时使用 dtable-sdk 提供的 api, 集成后使用 Base 的 api

dtable-sdk 提供了对数据操作的接口

* [初始化插件](./dtable-sdk/base.md)
* [Tables](./dtable-sdk/tables.md)
* [Views](./dtable-sdk/views.md)
* [Columns](./dtable-sdk/columns.md)
* [Rows](./dtable-sdk/rows.md)
* [Plugins](./dtable-sdk/plugins.md)
* [Links](./dtable-sdk/links.md)

### dtable-utils
> 插件开发工具函数库，提供一些常量，数据格式化工具，数据获取工具，方便用户完成插件的开发

* [Tables](./dtable-utils/tables.md)
* [Views](./dtable-utils/views.md)
* [Columns](./dtable-utils/columns.md)
* [Rows](./dtable-utils/rows.md)
* [Cells](./dtable-utils/cells.md)
* [Constants](./dtable-utils/constants.md)



### dtable-ui-component

dtable-ui-component 提供了格式化显示不同类型的数据单元和对数据进行编辑的 UI 控件。

详情可以查看: <https://seatable.github.io/dtable-ui-component/docs/>

