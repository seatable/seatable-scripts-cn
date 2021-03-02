# Context 对象

当脚本运行时, context 对象提供了上下文环境。使用方法如下:

```javascript
base.context.currentTable // 用户运行一个脚本的时候，当前用户正在查看的子表的名称
base.context.currentRow // 用户运行一个脚本的时候，当前光标所在的行
```