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
