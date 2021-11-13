# Constants

在脚本中可能会有一些常量需要我们了解下

## ColumnTypes

列类型，当插入/追加列、更改列类型, 获取 formatter 等情况需要使用到

```javascript
import { CELL_TYPE } from 'dtable-sdk';

CELL_TYPE.NUMBER              // 数字
CELL_TYPE.TEXT                // 文本
CELL_TYPE.LONG_TEXT           // 长文本
CELL_TYPE.CHECKBOX            // 勾选
CELL_TYPE.DATE                // 日期时间
CELL_TYPE.SINGLE_SELECT       // 单选
CELL_TYPE.MULTIPLE_SELECT     // 多选
CELL_TYPE.LONG_TEXT           // 长文本
CELL_TYPE.IMAGE               // 图片
CELL_TYPE.FILE                // 文件
CELL_TYPE.COLLABORATOR        // 协作人
CELL_TYPE.LINK                // 链接其他记录
CELL_TYPE.FORMULA             // 公式
CELL_TYPE.LINK_FORMULA        // 链接公式
CELL_TYPE.CREATOR             // 创建者
CELL_TYPE.CTIME               // 创建时间
CELL_TYPE.LAST_MODIFIER       // 修改者
CELL_TYPE.MTIME               // 修改时间
CELL_TYPE.GEOLOCATION         // 地址
CELL_TYPE.AUTO_NUMBER         // 自动序号
CELL_TYPE.URL                 // 链接
CELL_TYPE.EMAIL               // 邮箱
CELL_TYPE.BUTTON              // 按钮
CELL_TYPE.RATE                // 等级
```

## Column icon configs

列类型对应的图标配置信息

```javascript
import { CELL_TYPE, COLUMNS_ICON_CONFIG } from 'dtable-store';

const text = CELL_TYPE.TEXT;
// value: 'dtable-font dtable-icon-single-line-text'
const textIconClass = COLUMNS_ICON_CONFIG[text];  

const single_select = CELL_TYPE.SINGLE_SELECT;
// value: 'dtable-font dtable-icon-single-election'
const singleSelectIconClass = COLUMNS_ICON_CONFIG[single_select]; 

...


// 注: iconClass 用来显示列的图标(需要引入dtable-font)
```

## Column options

列的基本配置信息, 获取列的 icon 配置和不同列类型的提示信息时需要使用到

```javascript
import { CELL_TYPE, COLUMN_OPTIONS } from 'dtable-sdk';

const text = CELL_TYPE.TEXT;
// textOption : 
// {
//    type: 'text',
//    iconClass: 'dtable-font dtable-icon-single-line-text'  
//    iconName: 'Text'
// }
const textOption = COLUMN_OPTIONS.find(option => option.type === text); 

const singleSelect = CELL_TYPE.SINGLE_SELECT;
// singleSelectOption : 
// {
//    type: 'single-select',
//    iconClass: 'dtable-font dtable-icon-single-election'  
//    iconName: 'Single_Select'
// }
const singleSelectOption = COLUMN_OPTIONS.find(option => option.type === singleSelect); 

...

// 注: iconClass 用来显示列的图标(需要引入dtable-font)
//     iconName 可以用来国际化, 显示提示信息或文本信息

```

## Formula result type

公式列, 链接公式列计算结果类型汇总, 用于确定与计算有关的列类型的计算结果

```javascript

import { FORMULA_RESULT_TYPE } from 'dtable-sdk';

FORMULA_RESULT_TYPE.NUMBER     // number
FORMULA_RESULT_TYPE.STRING     // string
FORMULA_RESULT_TYPE.DATE       // date
FORMULA_RESULT_TYPE.BOOL       // bool
FORMULA_RESULT_TYPE.ARRAY      // array

```

## Select option colors

创建, 修改单选列/多选列选项时, 提供选项的文本颜色, 背景颜色, 边框颜色

```javascript

import { SELECT_OPTION_COLORS } from 'dtable-sdk';

// const SELECT_OPTION_COLORS = [
//   {COLOR: '#FFFCB5', BORDER_COLOR: '#E8E79D', TEXT_COLOR: '#202428'},
//   {COLOR: '#FFEAB6', BORDER_COLOR: '#ECD084', TEXT_COLOR: '#202428'},
//   {COLOR: '#FFD9C8', BORDER_COLOR: '#EFBAA3', TEXT_COLOR: '#202428'},
//   {COLOR: '#FFDDE5', BORDER_COLOR: '#EDC4C1', TEXT_COLOR: '#202428'},
//   {COLOR: '#FFD4FF', BORDER_COLOR: '#E6B6E6', TEXT_COLOR: '#202428'},
//   {COLOR: '#DAD7FF', BORDER_COLOR: '#C3BEEF', TEXT_COLOR: '#202428'},
//   {COLOR: '#DDFFE6', BORDER_COLOR: '#BBEBCD', TEXT_COLOR: '#202428'},
//   {COLOR: '#DEF7C4', BORDER_COLOR: '#C5EB9E', TEXT_COLOR: '#202428'},
//   {COLOR: '#D8FAFF', BORDER_COLOR: '#B4E4E9', TEXT_COLOR: '#202428'},
//   {COLOR: '#D7E8FF', BORDER_COLOR: '#BAD1E9', TEXT_COLOR: '#202428'},
//   {COLOR: '#B7CEF9', BORDER_COLOR: '#96B2E1', TEXT_COLOR: '#202428'},
//   {COLOR: '#E9E9E9', BORDER_COLOR: '#DADADA', TEXT_COLOR: '#202428'},
//   {COLOR: '#FBD44A', BORDER_COLOR: '#E5C142', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#EAA775', BORDER_COLOR: '#D59361', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#F4667C', BORDER_COLOR: '#DC556A', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#DC82D2', BORDER_COLOR: '#D166C5', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#9860E5', BORDER_COLOR: '#844BD2', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#9F8CF1', BORDER_COLOR: '#8F75E2', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#59CB74', BORDER_COLOR: '#4EB867', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#ADDF84', BORDER_COLOR: '#9CCF72', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#89D2EA', BORDER_COLOR: '#7BC0D6', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#4ECCCB', BORDER_COLOR: '#45BAB9', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#46A1FD', BORDER_COLOR: '#3C8FE4', TEXT_COLOR: '#FFFFFF'},
//   {COLOR: '#C2C2C2', BORDER_COLOR: '#ADADAD', TEXT_COLOR: '#FFFFFF'},
// ];

// 创建选项时, 可以提供相关选项, 也可以通过随机函数, 自动生成相应的选项颜色

const colorIndex = (Math.random() * SELECT_OPTION_COLORS.length).toFix(0);
const selectColor = SELECT_OPTION_COLORS[colorIndex];

```

## Table permission type

子表的权限类型

```javascript

import { TABLE_PERMISSION_TYPE } from 'dtable-sdk';

TABLE_PERMISSION_TYPE.DEFAULT              // default 默认权限
TABLE_PERMISSION_TYPE.ADMINS               // admins  有管理权限的人
TABLE_PERMISSION_TYPE.SPECIFIC_USERS       // specific_users 特定用户
TABLE_PERMISSION_TYPE.NONE                 // none 谁都不能更改

```