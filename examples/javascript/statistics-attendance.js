const originTableName = '原始表';
const originViewName = '默认视图';
const originNameColumnName = '名称';
const originDepartmentColumnName = '部门';
const originDateColumnName = '日期';
const originTimeColumnName = '打卡时间';

const targetTableName = '考勤统计表';
const targetNameColumnName = '名称';
const targetDepartmentColumnName = '部门';
const targetDateColumnName = '日期';
const targetStartTimeColumnName = '上班打卡';
const targetEndTimeColumnName = '下班打卡';
const targetTable = base.getTableByName(targetTableName);

const table = base.getTableByName(originTableName);
const view = base.getViewByName(table, originViewName);
const rows = base.getRows(table, view);

// 将表格中的行按照日期列进行排序;
rows.sort((row1, row2) => {
	if (row1[originDateColumnName] < row2[originDateColumnName]) {
      return -1;
    } else if (row1[originDateColumnName] > row2[originDateColumnName]) {
      return 1;	
    } else {
      return 0;
    }
});

/*
 将所有的行按照日期进行分组保存到 groupedRows，对象中
 格式为 {'2020-09-01': [row, ...], '2020-09-02': [row, ...]}
*/
const groupedRows = {};
rows.forEach((row) => {
  const date = row[originDateColumnName]; 
  if (!groupedRows[date]) {
    groupedRows[date] = [];
  }
  groupedRows[date].push(row);
});

const dateKeys = Object.keys(groupedRows);

// 遍历 groupedRows 中的所有的组
dateKeys.forEach((dateKey) => { 
  // 获取当前日期的所有算工的所有打卡数据
  const dateRows = groupedRows[dateKey];
  const staffDateStatItem = {};
  // 遍历这些行数据并且以员工的名称进行分组，获取每个员工，当天的上班打卡和下班打卡时间，保存到 staffDateStatItem 中
  // 格式为 { a1: {姓名: 'a1', 日期: '2020-09-01', 上班打卡: '08:00', 下班打卡: '18:00'},... }
  dateRows.forEach((row)=> {
    const name = row[originNameColumnName];
    if (!staffDateStatItem[name]) {
      // 根据原始的行数据生成生成一个新的行, 并在新生成的行中添加上班打卡，下班打卡列
      staffDateStatItem[name] = { [targetNameColumnName]: name, [targetDateColumnName]: row[originDateColumnName], [targetDepartmentColumnName]: row[originDepartmentColumnName], [targetEndTimeColumnName]: row[originTimeColumnName], [targetStartTimeColumnName]: row[originTimeColumnName]};
    } else {
      // 当行的名称列重复时，进行时间比较，选择最大的作为下班打卡时间，做小的作为上班打卡时间
      const time = row[originTimeColumnName];
      const staffItem = staffDateStatItem[name];
      if (compareTime(staffItem[targetStartTimeColumnName], time)) {
        staffItem[targetStartTimeColumnName] = time;
      } else if (compareTime(time, staffItem[targetEndTimeColumnName])) {
        staffItem[targetEndTimeColumnName] = time;
      } 
    }
  });
  
  // 将当前日期的所有员工的考勤数据写入表格
  Object.keys(staffDateStatItem).forEach((name) => {
    base.addRow(targetTable, staffDateStatItem[name]);
  });  
});

// 比较两个字符串格式时间的大小
function compareTime(time1, time2) {
  const t1 = time1.split(':');
  const t2 = time2.split(':');
  if (parseInt(t1[0]) > parseInt(t2[0])) {
    return true;
  } else if (parseInt(t1[0]) < parseInt(t2[0])) {
    return false; 
  } else if (parseInt(t1[0]) == parseInt(t2[0])) {
    if (parseInt(t1[1]) > parseInt(t2[1])) {
      return true;
    } else {
      return false;
    }
  }
}