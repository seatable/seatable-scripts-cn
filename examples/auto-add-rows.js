// 自动往一个账本中记录每月的重复项

const table = base.getTableByName('日常费用');

// 获取当月 10 号和当月 20 号的日期对象
var date = new Date();
var date10 = new Date(date.setDate(10));
var date20 = new Date(date.setDate(20));

// 新建两个费用项
var feeAWS = {'名称': 'Amazon 云服务', 
              '日期': base.utils.formatDate(date10),
              '类别': '云服务'
             };
var feeBaoJie = { '名称': '保洁', 
                  '日期': base.utils.formatDate(date20),
                  '类别': '日常办公',
                  '费用': 260
                  };

// 自动添加数据               
base.addRow(table, feeAWS);
base.addRow(table, feeBaoJie);