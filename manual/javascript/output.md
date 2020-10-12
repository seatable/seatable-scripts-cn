## Output 对象

Output 对象支持输出文本格式或者 Markdwon 格式的内容

##### Text

```javascript
const table = base.getActiveTable();
output.text(table.name);
```

##### Markdown

```javascript
const table = base.getActiveTable()；
output.markdown(`##### ${table.name}`);
```