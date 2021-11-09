# Utils

常用工具函数

## formatDurationToNumber

将 十分/时分秒 的字符串 格式化为数值类型

```javascript
import { formatDurationToNumber } from 'dtable-sdk';

// number: 4800 = 1 * 3600 + 20 * 60
const data = {duration_format: 'h:mm' };
const number = formatDurationToNumber('1:20', format);


// number: 4830 = 1 * 3600 + 20 * 60 + 30
const data = {duration_format: 'h:mm:ss' };
const number = formatDurationToNumber('1:20:30', data);

// 注: duration_format 可取值
// 1. h:mm
// 2. h:mm:ss
// 3. h:mm:ss.s
// 4. h:mm:ss.ss
// 5. h:mm:ss.sss
```