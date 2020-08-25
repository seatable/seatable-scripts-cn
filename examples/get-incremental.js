
const tableName = '某表格';
const viewName = '默认视图';

// name of the column that records total number at a specific time
const columnName = '累计关注用户数';

// name of the column that need to calculate incremental value
const incrementalColumnName = '关注用户数增量';

// get table
const table = base.getTableByName(tableName);
// get view 
const view = base.getViewByName(table, viewName);

// if current view is a grouped view
if (view.groupbys && view.groupbys.length > 0) {
  // get group view rows
  const groupViewRows = base.getGroupedRows(table, view);
  
  groupViewRows.map((group) => {
  	group.rows.map((row, index, rows) => {
      	// get current row value
    	const currentNumber = row[columnName];
      	if (!currentNumber) return;
        // caculate increment
        const previousRow = rows[index - 1];
        // if there is no previousRow, set increaseCount to 0
        const previousNumber = previousRow ? previousRow[columnName] : currentNumber;
      	const increaseCount = currentNumber - previousNumber;
        // set caculated increment to row
      	base.modifyRow(table, row, {[incrementalColumnName]: increaseCount});
    });
  });
} else {
    // get current view rows
    const rows = base.getRows(table, view);
    rows.map((row, rowIndex, rows) => {
    // caculate increment
    const currentNumber = row[columnName];
    if (!currentNumber) return;
    const previousRow = rows[rowIndex - 1];
    // if there is no previousRow, set increaseCount to 0
    const previousNumber = previousRow ? previousRow[columnName] : currentNumber;
    const increaseCount = currentNumber - previousNumber;
    // set caculated increment to row
    base.modifyRow(table, row, {[incrementalColumnName]: increaseCount});
  });
}
