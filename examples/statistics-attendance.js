const originTableName = 'Table1';
const originViewName = '默认视图';
const originNameColumnName = '名称';
const originDepartmentColumnName = '部门';
const originDateColumnName = '日期';
const originTimeColumnName = '打卡时间';

const targetTableName = '考勤统计表';
const targetNameColumnName = 'Name';
const targetDepartmentColumnName = '部门';
const targetDateColumnName = '日期';
const targetStartTimeColumnName = '上班打卡';
const targetEndTimeColumnName = '下班打卡';
const targetTable = base.getTableByName(targetTableName);

const table = base.getTableByName(originTableName);
const view = base.getViewByName(table, originViewName);
const rows = base.getRows(table, view);

// sort rows by date;
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
 group rows by date
 return an object formated as {'2020-09-01': [row1, ...], '2020-09-02': [row1, ...]}
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

// traverse the groups to statistic daily work hours of staffs
dateKeys.forEach((dateKey) => { 
  const dateRows = groupedRows[dateKey];
  const staffDateStatItem = {};
  // traverse rows of each date to calculate the start and end time per person per day 
  // and save to the staffDateStatItem, formatted as 
  // {'name1': { 名称: name, 日期: 'date', 部门: 'department name', 下班打卡: 'end time', 上班打卡: 'start time'}, name2: ...}
  dateRows.forEach((row)=> {
    const name = row[originNameColumnName];
    if (!staffDateStatItem[name]) {
      staffDateStatItem[name] = { [targetNameColumnName]: name, [targetDateColumnName]: row[originDateColumnName], [targetDepartmentColumnName]: row[originDepartmentColumnName], [targetEndTimeColumnName]: row[originTimeColumnName], [targetStartTimeColumnName]: row[originTimeColumnName]};
    } else {
      const time = row[originTimeColumnName];
      const staffItem = staffDateStatItem[name];
      if (compareTime(staffItem[targetStartTimeColumnName], time)) {
        staffItem[targetStartTimeColumnName] = time;
      } else if (compareTime(time, staffItem[targetEndTimeColumnName])) {
        staffItem[targetEndTimeColumnName] = time;
      } 
    }
  });
  
  // write the result of the date of all staffs to the new table
  Object.keys(staffDateStatItem).forEach((name) => {
    base.addRow(targetTable, staffDateStatItem[name]);
  });  
});

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