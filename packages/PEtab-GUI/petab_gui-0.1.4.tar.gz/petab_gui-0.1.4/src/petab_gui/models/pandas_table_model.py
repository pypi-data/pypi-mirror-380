from typing import Any

from PySide6.QtCore import (
    QAbstractTableModel,
    QMimeData,
    QModelIndex,
    QSortFilterProxyModel,
    Qt,
    Signal,
)
from PySide6.QtGui import QBrush, QColor, QPalette
from PySide6.QtWidgets import QApplication

from ..C import COLUMNS
from ..commands import (
    ModifyColumnCommand,
    ModifyDataFrameCommand,
    ModifyRowCommand,
    RenameIndexCommand,
)
from ..controllers.default_handler import DefaultHandlerModel
from ..settings_manager import settings_manager
from ..utils import (
    create_empty_dataframe,
    get_selected,
    is_invalid,
    validate_value,
)
from ..views.whats_this import column_whats_this
from .tooltips import cell_tip, header_tip


class PandasTableModel(QAbstractTableModel):
    """Basic table model for a pandas DataFrame.

    This class provides a Qt model interface for pandas DataFrames,
    allowing them to be displayed and edited in Qt table views. It handles
    data access, modification, and various table operations like
    adding/removing rows and columns.
    """

    # Signals
    relevant_id_changed = Signal(str, str, str)  # new_id, old_id, type
    new_log_message = Signal(str, str)  # message, color
    cell_needs_validation = Signal(int, int)  # row, column
    something_changed = Signal(bool)
    inserted_row = Signal(QModelIndex)
    plotting_needs_break = Signal(bool)

    def __init__(
        self,
        data_frame,
        allowed_columns,
        table_type,
        undo_stack=None,
        parent=None,
    ):
        """Initialize the pandas table model.

        Args:
        data_frame:
            The pandas DataFrame to be displayed in the table
        allowed_columns:
            Dictionary of allowed columns with their properties
        table_type:
            The type of table (e.g., 'observable', 'parameter', 'condition')
        undo_stack:
            Optional QUndoStack for undo/redo functionality
        parent:
            The parent QObject
        """
        super().__init__(parent)
        self._allowed_columns = allowed_columns
        self.table_type = table_type
        self._invalid_cells = set()
        self.highlighted_cells = set()
        self._has_named_index = False
        if data_frame is None:
            data_frame = create_empty_dataframe(allowed_columns, table_type)
        self._data_frame = data_frame
        # add a view here, access is needed for selectionModels
        self.view = None
        # offset for row and column to get from the data_frame to the view
        self.row_index_offset = 0
        self.column_offset = 0
        # default values setup
        self.config = settings_manager.get_table_defaults(table_type)
        self.default_handler = DefaultHandlerModel(self, self.config)
        self.undo_stack = undo_stack

    def rowCount(self, parent=None):
        """Return the number of rows in the model.

        Includes an extra row at the end for adding new entries.

        Args:
            parent: The parent model index (unused in table models)

        Returns:
            int: The number of rows in the model
        """
        if parent is None:
            parent = QModelIndex()
        return self._data_frame.shape[0] + 1  # empty row at the end

    def columnCount(self, parent=None):
        """Return the number of columns in the model.

        Includes any column offset (e.g., for index column).

        Args:
            parent: The parent model index (unused in table models)

        Returns:
            int: The number of columns in the model
        """
        if parent is None:
            parent = QModelIndex()
        return self._data_frame.shape[1] + self.column_offset

    def data(self, index, role=Qt.DisplayRole):
        """Return the data at the given index and role for the View.

        Handles different roles:
        - DisplayRole/EditRole: Returns the cell value as a string
        - BackgroundRole: Returns the background color for the cell
        - ForegroundRole: Returns the text color for the cell

        Args:
            index: The model index to get data for
            role: The data role (DisplayRole, EditRole, BackgroundRole, etc.)

        Returns:
            The requested data for the given index and role, or None
        """
        if not index.isValid():
            return None
        row, column = index.row(), index.column()
        if role == Qt.WhatsThisRole:
            if row == self._data_frame.shape[0]:
                return "Add a new row."
            if column == 0 and self._has_named_index:
                return None
            col_label = self._data_frame.columns[column - self.column_offset]
            return column_whats_this(self.table_type, col_label)
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if row == self._data_frame.shape[0]:
                if column == 0:
                    return f"New {self.table_type}"
                return ""
            if column == 0 and self._has_named_index:
                value = self._data_frame.index[row]
                return str(value)
            value = self._data_frame.iloc[row, column - self.column_offset]
            if is_invalid(value):
                return ""
            return str(value)
        if role == Qt.BackgroundRole:
            return self.determine_background_color(row, column)
        if role == Qt.ForegroundRole:
            # Return yellow text if this cell is a match
            if (row, column) in self.highlighted_cells:
                return QApplication.palette().color(QPalette.HighlightedText)
            return QBrush(QColor(0, 0, 0))  # Default black text
        if role == Qt.ToolTipRole:
            if row == self._data_frame.shape[0]:
                return "Add a new row"
            col_label = self._data_frame.columns[column - self.column_offset]
            if column == 0 and self._has_named_index:
                col_label = self._data_frame.index.name
            return cell_tip(self.table_type, col_label)
        return None

    def flags(self, index):
        """Return the item flags for the given index.

        Determines whether cells are editable, selectable, and enabled.

        Args:
            index: The model index to get flags for

        Returns:
            Qt.ItemFlags: The flags for the given index
        """
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Return the header data for the given section and orientation.

        Provides column and row headers for the table view.

        Args:
        section:
            The row or column number
        orientation:
            Qt.Horizontal for column headers, Qt.Vertical for row headers
        role:
            The data role (usually DisplayRole)

        Returns:
            The header text for the given section and orientation, or None.
        """
        if role not in (Qt.DisplayRole, Qt.ToolTipRole, Qt.WhatsThisRole):
            return None
        if orientation == Qt.Horizontal:
            if section == 0 and self._has_named_index:
                col_label = self._data_frame.index.name
            else:
                col_label = self._data_frame.columns[
                    section - self.column_offset
                ]
            if role == Qt.ToolTipRole:
                tooltip_header = header_tip(self.table_type, col_label)
                return tooltip_header
            if role == Qt.WhatsThisRole:
                return column_whats_this(self.table_type, col_label)
            return col_label
        if orientation == Qt.Vertical:
            return str(section)
        return None

    def insertRows(self, position, rows, parent=None) -> bool:
        """
        Insert new rows at the end of the DataFrame in-place.

        This function always adds rows at the end.

        Parameters:
        -----------
        position: Ignored, as rows are always inserted at the end.
        rows: The number of rows to add.
        parent: Unused in this implementation.

        Returns:
        --------
        bool: True if rows were added successfully.
        """
        if self.undo_stack:
            self.undo_stack.push(ModifyRowCommand(self, rows))
        else:
            # Fallback if undo stack isn't used
            command = ModifyRowCommand(self, rows)
            command.redo()
        return True

    def insertColumn(self, column_name: str):
        """Add a new column to the table.

        Always adds the column at the right (end) of the table. Checks if the
        column already exists or if it's not in the allowed columns list.

        Args:
            column_name: The name of the column to add

        Returns:
            bool: True if the column was added successfully, False otherwise

        Notes:
            If the column is not in the allowed columns list, a warning message
            is emitted but the column is still added.
        """
        if column_name in self._data_frame.columns:
            self.new_log_message.emit(
                f"Column '{column_name}' already exists", "red"
            )
            return False
        if not (
            column_name in self._allowed_columns
            or self.table_type == "condition"
        ):  # empty dict means all columns allowed
            self.new_log_message.emit(
                f"Column '{column_name}' will be ignored for the petab "
                f"problem but may still be used to store relevant information",
                "orange",
            )

        if self.undo_stack:
            self.undo_stack.push(ModifyColumnCommand(self, column_name))
        else:
            # Fallback if undo stack isn't used
            command = ModifyColumnCommand(self, column_name)
            command.redo()

        return True

    def setData(
        self, index, value, role=Qt.EditRole, check_multi: bool = True
    ):
        """Set the data for a specific model index.

        Updates the value at the given index in the model. If multiple rows are
        selected and check_multi is True, applies the change to all selected
        cells in the same column.

        Args:
            index: The model index to set data for
            value: The new value to set
            role: The data role (usually EditRole)
            check_multi: Whether to check for multi-row selection

        Returns:
            bool: True if the data was set successfully, False otherwise
        """
        if not (index.isValid() and role == Qt.EditRole):
            return False

        if role != Qt.EditRole:
            return False

        if is_invalid(value) or value == "":
            value = None
        self.plotting_needs_break.emit(True)  # Temp disable plotting
        multi_row_change = False
        if check_multi:
            # check whether multiple rows but only one column is selected
            multi_row_change, selected = self.check_selection()
        if not multi_row_change:
            self.undo_stack.beginMacro("Set data")
            success = self._set_data_single(index, value)
            self.undo_stack.endMacro()
            self.plotting_needs_break.emit(False)
            return success
        # multiple rows but only one column is selected
        all_set = []
        self.undo_stack.beginMacro("Set data")
        for index in selected:
            all_set.append(self._set_data_single(index, value))
        self.undo_stack.endMacro()
        self.plotting_needs_break.emit(False)
        return all(all_set)

    def _set_data_single(self, index, value):
        """Set the data of a single cell.

        Internal method used by setData to update a single cell's value.
        Handles special cases like new row creation, named index columns,
        and type validation.

        Args:
            index: The model index to set data for
            value: The new value to set

        Returns:
            bool: True if the data was set successfully, False otherwise
        """
        row, column = index.row(), index.column()
        fill_with_defaults = False

        # Handle new row creation
        if row == self._data_frame.shape[0]:
            self.insertRows(row, 1)
            fill_with_defaults = True
            next_index = self.index(row, 0)
            self.inserted_row.emit(next_index)

        # Handle named index column
        if column == 0 and self._has_named_index:
            return_this = self.handle_named_index(index, value)
            if fill_with_defaults:
                self.get_default_values(index)
            self.cell_needs_validation.emit(row, column)
            return return_this

        column_name = self._data_frame.columns[column - self.column_offset]
        old_value = self._data_frame.iloc[row, column - self.column_offset]

        # Handle invalid value
        if is_invalid(value):
            self._push_change_and_notify(
                row, column, column_name, old_value, None
            )
            return True

        # Type validation
        expected_info = self._allowed_columns.get(column_name)
        if expected_info:
            expected_type = expected_info["type"]
            validated, error = validate_value(value, expected_type)
            if error:
                self.new_log_message.emit(
                    f"Column '{column_name}' expects a value of type "
                    f"{expected_type.__name__}, but got '{value}'",
                    "red",
                )
                return False
            value = validated

        if value == old_value:
            return False

        # Special ID emitters
        if column_name == "observableId":
            if fill_with_defaults:
                self.get_default_values(index, {column_name: value})
            self.relevant_id_changed.emit(value, old_value, "observable")
            self._push_change_and_notify(
                row, column, column_name, old_value, value
            )
            return True

        if column_name in [
            "conditionId",
            "simulationConditionId",
            "preequilibrationConditionId",
        ]:
            if fill_with_defaults:
                self.get_default_values(index, {column_name: value})
            self.relevant_id_changed.emit(value, old_value, "condition")
            self._push_change_and_notify(
                row, column, column_name, old_value, value
            )
            return True

        # Default value setting
        if fill_with_defaults:
            self.get_default_values(index, {column_name: value})
        self._push_change_and_notify(
            row, column, column_name, old_value, value
        )
        return True

    def _push_change_and_notify(
        self, row, column, column_name, old_value, new_value
    ):
        """Push a dataframe change to the undo stack and emit signals.

        Creates a ModifyDataFrameCommand for the change and adds it to the
        undo stack. Also emits signals to notify views and other components
        about the change.

        Args:
            row: The row index in the dataframe
            column: The column index in the view
            column_name: The name of the column being changed
            old_value: The previous value in the cell
            new_value: The new value to set in the cell
        """
        change = {
            (self._data_frame.index[row], column_name): (old_value, new_value)
        }
        self.undo_stack.push(ModifyDataFrameCommand(self, change))
        self.dataChanged.emit(
            self.index(row, column), self.index(row, column), [Qt.DisplayRole]
        )
        self.cell_needs_validation.emit(row, column)
        self.something_changed.emit(True)

    def clear_cells(self, selected):
        """Clear the values in the selected cells.

        Sets all selected cells to None (empty) and groups the changes into a
        single undo command for better undo/redo functionality.

        Args:
        selected:
            A list of QModelIndex objects representing the selected cells
        """
        self.undo_stack.beginMacro("Clear cells")
        for index in selected:
            if index.isValid():
                self.setData(index, None, Qt.EditRole, False)
        self.undo_stack.endMacro()

    def handle_named_index(self, index, value):
        """Handle changes to the named index column.

        This is a placeholder method in the base class. Subclasses that use
        named indices (like IndexedPandasTableModel) override this method to
        implement the actual behavior.

        Args:
            index: The model index of the cell being edited
            value: The new value for the index

        Returns:
            bool: True if the index was successfully changed, False otherwise
        """
        pass

    def get_default_values(self, index, changed: dict | None = None):
        """Fill a row with default values based on the table's configuration.

        This is a placeholder method in the base class. Subclasses override
        this method to implement the actual behavior for filling default
        values.

        Args:
        index:
            The model index where the first change occurs
        changed:
            Dictionary of changes made to the DataFrame not yet registered
        """
        pass

    def replace_text(self, old_text: str, new_text: str):
        """Replace all occurrences of a text string in the table.

        Searches for and replaces all instances of old_text with new_text in
        both the data cells and index values (if using named indices).
        Efficiently updates the view by emitting dataChanged signals only
        for the affected cells.

        Args:
            old_text: The text to search for
            new_text: The text to replace it with
        """
        # find all occurrences of old_text and save indices
        mask = self._data_frame.eq(old_text)
        if mask.any().any():
            self._data_frame.replace(old_text, new_text, inplace=True)
            # Get first and last modified cell for efficient `dataChanged` emit
            changed_cells = mask.stack()[
                mask.stack()
            ].index.tolist()  # Extract (row, col) pairs
            if changed_cells:
                first_row, first_col = changed_cells[0]
                last_row, last_col = changed_cells[-1]
                if self._has_named_index:
                    first_col += 1
                    last_col += 1
                top_left = self.index(first_row, first_col)
                bottom_right = self.index(last_row, last_col)
                self.dataChanged.emit(top_left, bottom_right, [Qt.DisplayRole])
        # also replace in the index
        if self._has_named_index and old_text in self._data_frame.index:
            self._data_frame.rename(index={old_text: new_text}, inplace=True)
            index_row = self._data_frame.index.get_loc(new_text)
            index_top_left = self.index(index_row, 0)
            index_bottom_right = self.index(index_row, 0)
            self.dataChanged.emit(
                index_top_left, index_bottom_right, [Qt.DisplayRole]
            )

    def get_df(self):
        """Return the underlying pandas DataFrame.

        Provides direct access to the DataFrame that this model wraps.

        Returns:
            pd.DataFrame: The DataFrame containing the table data
        """
        return self._data_frame

    def add_invalid_cell(self, row, column):
        """Mark a cell as invalid, giving it a special background color.

        Adds the cell coordinates to the _invalid_cells set and triggers a UI
        update to show the cell with an error background color. Performs
        several validity checks before adding the cell.

        Args:
            row: The row index of the cell
            column: The column index of the cell
        """
        # check that the index is valid
        if not self.index(row, column).isValid():
            return
        # return if it is the last row
        if row == self._data_frame.shape[0]:
            return
        # return if it is already invalid
        if (row, column) in self._invalid_cells:
            return
        self._invalid_cells.add((row, column))
        self.dataChanged.emit(
            self.index(row, column),
            self.index(row, column),
            [Qt.BackgroundRole],
        )

    def discard_invalid_cell(self, row, column):
        """Remove a cell from the invalid cells set, restoring its state.

        Removes the cell coordinates from the _invalid_cells set and triggers
        a UI update to restore the cell's normal background color.

        Args:
            row: The row index of the cell
            column: The column index of the cell
        """
        self._invalid_cells.discard((row, column))
        self.dataChanged.emit(
            self.index(row, column),
            self.index(row, column),
            [Qt.BackgroundRole],
        )

    def update_invalid_cells(self, selected, mode: str = "rows"):
        """Update invalid cell coordinates when rows or columns are deleted.

        When rows or columns are deleted, the coordinates of invalid cells need
        to be adjusted to account for the shifted indices. This method
        recalculates the coordinates of all invalid cells based on the
        deleted indices.

        Args:
        selected:
            A set or list of indices (row or column) that are being deleted
        mode:
            Either "rows" or "columns" to indicate what is being deleted
        """
        if not selected:
            return
        old_invalid_cells = self._invalid_cells.copy()
        new_invalid_cells = set()
        sorted_to_del = sorted(selected)
        for a, b in old_invalid_cells:
            if mode == "rows":
                to_be_change = a
                not_changed = b
            elif mode == "columns":
                to_be_change = b
                not_changed = a
            if to_be_change in selected:
                continue
            smaller_count = sum(1 for x in sorted_to_del if x < to_be_change)
            new_val = to_be_change - smaller_count
            if mode == "rows":
                new_invalid_cells.add((new_val, not_changed))
            if mode == "columns":
                new_invalid_cells.add((not_changed, new_val))
        self._invalid_cells = new_invalid_cells

    def notify_data_color_change(self, row, column):
        """Notify the view that a cell's background color needs to be updated.

        Emits a dataChanged signal with the BackgroundRole to trigger the view
        to redraw the cell with its current background color.

        Args:
            row: The row index of the cell
            column: The column index of the cell
        """
        self.dataChanged.emit(
            self.index(row, column),
            self.index(row, column),
            [Qt.BackgroundRole],
        )

    def get_value_from_column(self, column_name, row):
        """Retrieve the value from a specific column and row in the DataFrame.

        Handles special cases like the "new row" at the end of the table and
        accessing values from the index column.

        Args:
            column_name: The name of the column to get the value from
            row: The row index to get the value from

        Returns:
            The value at the specified column and row, or an empty string
        """
        # if row is a new row return ""
        if row == self._data_frame.shape[0]:
            return ""
        if column_name in self._data_frame.columns:
            return self._data_frame.loc[row, column_name]
        if column_name == self._data_frame.index.name:
            return self._data_frame.index[row]
        return ""

    def return_column_index(self, column_name):
        """Return the view column index for a given column name.

        This is a placeholder method in the base class. Subclasses override
        this method to implement the actual behavior for mapping column
        names to view indices.

        Args:
            column_name: The name of the column to find the index for

        Returns:
            int: The view column index for the given column name, or -1
        """
        if column_name in self._data_frame.columns:
            return self._data_frame.columns.get_loc(column_name)
        return -1

    def unique_values(self, column_name):
        """Return a list of unique values in a specified column.

        Used for providing suggestions in autocomplete fields/dropdown lists.
        Handles both regular columns and the index column.

        Args:
            column_name: The name of the column to get unique values from

        Returns:
            list: A list of unique values from the column, or an empty list
        """
        if column_name in self._data_frame.columns:
            return list(self._data_frame[column_name].dropna().unique())
        if column_name == self._data_frame.index.name:
            return list(self._data_frame.index.dropna().unique())
        return []

    def delete_row(self, row):
        """Delete a row from the table.

        Creates a ModifyRowCommand for the deletion and adds it to the stack
        to support undo/redo functionality.

        Args:
            row: The index of the row to delete
        """
        if self.undo_stack:
            self.undo_stack.push(ModifyRowCommand(self, row, False))
        else:
            # Fallback if undo stack isn't used
            command = ModifyRowCommand(self, row, False)
            command.redo()

    def delete_column(self, column_index):
        """Delete a column from the table.

        Maps the view column index to the actual DataFrame column name and
        creates a ModifyColumnCommand for the deletion. Adds the command to
        the stack to support undo/redo functionality.

        Args:
            column_index: The view index of the column to delete
        """
        column_name = self._data_frame.columns[
            column_index - self.column_offset
        ]
        if self.undo_stack:
            self.undo_stack.push(ModifyColumnCommand(self, column_name, False))
        else:
            # Fallback if undo stack isn't used
            command = ModifyColumnCommand(self, column_name, False)
            command.redo()

    def clear_table(self):
        """Clear all data from the table."""
        self.beginResetModel()
        self._data_frame.drop(self._data_frame.index, inplace=True)
        self._data_frame.drop(
            self._data_frame.columns.difference(
                COLUMNS[self.table_type].keys()
            ),
            axis=1,
            inplace=True,
        )
        self.endResetModel()

    def check_selection(self):
        """Check if multiple rows but only one column is selected in the view.

        Used to determine if a multi-row edit operation should be performed,
        when setting data. This allows for efficiently applying the same
        change to multiple cells in the same column.

        Returns:
            tuple: A tuple containing:
                - bool: True if multiple rows but only one column is selected
                - list: The list of selected QModelIndex objects, or None
        """
        if self.view is None:
            return False, None
        selected = get_selected(self.view, mode="index")
        cols = {index.column() for index in selected}
        rows = {index.row() for index in selected}
        return len(rows) > 1 and len(cols) == 1, selected

    def reset_invalid_cells(self):
        """Clear all invalid cell markings and update their appearance.

        Removes all cells from the _invalid_cells set and triggers UI updates
        to restore their normal background colors.
        This is useful when reloading data or when validation state needs to be
         reset.
        """
        if not self._invalid_cells:
            return

        invalid_cells = list(self._invalid_cells)
        self._invalid_cells.clear()  # Clear invalid cells set

        for row, col in invalid_cells:
            index = self.index(row, col)
            self.dataChanged.emit(index, index, [Qt.BackgroundRole])

    def mimeData(self, rectangle, start_index):
        """Return the data to be copied to the clipboard.

        Formats the selected cells' data as tab-separated text for clipboard
        operations.

        Args:
        rectangle:
            A numpy array representing the selected cells, where True values
            indicate selected cells within the minimum bounding rectangle
        start_index:
            A tuple (row, col) indicating the top-left corner of the selection

        Returns:
            QMimeData: A mime data object containing the formatted text data
        """
        copied_data = ""
        for row in range(rectangle.shape[0]):
            for col in range(rectangle.shape[1]):
                if rectangle[row, col]:
                    copied_data += self.data(
                        self.index(start_index[0] + row, start_index[1] + col),
                        Qt.DisplayRole,
                    )
                else:
                    copied_data += "SKIP"
                if col < rectangle.shape[1] - 1:
                    copied_data += "\t"
            copied_data += "\n"
        mime_data = QMimeData()
        mime_data.setText(copied_data.strip())
        return mime_data

    def setDataFromText(self, text, start_row, start_column):
        """Set table data from tab-separated text.

        Used for pasting clipboard content into the table. Parses the text as
        tab-separated values and sets the data in the table starting from the
        specified position. Groups all changes into a single undo command.

        Args:
            text: The tab-separated text to parse and set in the table
            start_row: The row index where to start setting data
            start_column: The column index where to start setting data
        """
        lines = text.split("\n")
        self.undo_stack.beginMacro("Paste from Clipboard")
        self.maybe_add_rows(start_row, len(lines))
        for row_offset, line in enumerate(lines):
            values = line.split("\t")
            for col_offset, value in enumerate(values):
                if value == "SKIP":
                    continue
                self.setData(
                    self.index(
                        start_row + row_offset, start_column + col_offset
                    ),
                    value,
                    Qt.EditRole,
                )
        self.undo_stack.endMacro()

    def maybe_add_rows(self, start_row, n_rows):
        """Add rows to the table if there aren't enough.

        Used during paste operations to ensure there are enough rows for the
        pasted data. Adds rows if the current number of rows is insufficient.

        Args:
            start_row: The row index where data insertion begins
            n_rows: The number of rows needed for the data
        """
        if start_row + n_rows > self._data_frame.shape[0]:
            self.insertRows(
                self._data_frame.shape[0],
                start_row + n_rows - self._data_frame.shape[0],
            )

    def determine_background_color(self, row, column):
        """Determine the background color for a specific cell.

        Applies different background colors based on cell properties:
        - Light green for the "New row" cell (first column of last row)
        - System highlight color for cells that match search criteria
        - Red for cells marked as invalid
        - Alternating light blue and light green for even/odd rows

        Args:
            row: The row index of the cell
            column: The column index of the cell

        Returns:
            QColor: The background color to use for the cell
        """
        if (row, column) == (self._data_frame.shape[0], 0):
            return QColor(144, 238, 144, 150)
        if (row, column) in self.highlighted_cells:
            return QApplication.palette().color(QPalette.Highlight)
        if (row, column) in self._invalid_cells:
            return QColor(255, 100, 100, 150)
        if row % 2 == 0:
            return QColor(144, 190, 109, 102)
        return QColor(177, 217, 231, 102)

    def allow_column_deletion(
        self, column: int
    ) -> tuple[bool, Any] | tuple[Any, Any]:
        """Check whether a column can safely be deleted from the table.

        Prevents deletion of required columns and the index column.
        Used to validate column deletion requests before they are processed.

        Args:
            column: The view index of the column to check

        Returns:
            tuple: A tuple containing:
                - bool: True if the column can be deleted, False otherwise
                - str: The name of the column
        """
        if column == 0 and self._has_named_index:
            return False, self._data_frame.index.name
        column_name = self._data_frame.columns[column - self.column_offset]
        if column_name not in self._allowed_columns:
            return True, column_name
        return self._allowed_columns[column_name]["optional"], column_name

    def endResetModel(self):
        """Override endResetModel to reset the default handler."""
        super().endResetModel()
        self.config = settings_manager.get_table_defaults(self.table_type)
        sbml_model = self.default_handler._sbml_model
        self.default_handler = DefaultHandlerModel(
            self, self.config, sbml_model=sbml_model
        )

    def fill_row(self, row_position: int, data: dict):
        """Fill a row with data.

        Parameters
        ----------
        row_position:
            The position of the row to fill.
        data:
            The data to fill the row with. Gets updated with default values.
        """
        data_to_add = dict.fromkeys(self._data_frame.columns, "")
        unknown_keys = set(data) - set(self._data_frame.columns)
        index_key = None
        for key in unknown_keys:
            if key == self._data_frame.index.name:
                index_key = data.pop(key)
                continue
            data.pop(key, None)
        data_to_add.update(data)
        if index_key and self._has_named_index:
            self.undo_stack.push(
                RenameIndexCommand(
                    self,
                    self._data_frame.index.tolist()[row_position],
                    index_key,
                    self.index(row_position, 0),
                )
            )
        if index_key is None:
            index_key = self._data_frame.index.tolist()[row_position]

        changes = {
            (index_key, col): (self._data_frame.at[index_key, col], val)
            for col, val in data_to_add.items()
            if val not in [self._data_frame.at[index_key, col], "", None]
        }
        self.undo_stack.push(
            ModifyDataFrameCommand(self, changes, "Fill values")
        )
        # rename changes keys to only the col names
        changes = {col: val for (_, col), val in changes.items()}
        self.get_default_values(
            self.index(row_position, 0),
            changed=changes,
        )


class IndexedPandasTableModel(PandasTableModel):
    """Table model for tables with named index."""

    condition_2be_renamed = Signal(str, str)  # Signal to mother controller

    def __init__(self, data_frame, allowed_columns, table_type, parent=None):
        super().__init__(
            data_frame=data_frame,
            allowed_columns=allowed_columns,
            table_type=table_type,
            parent=parent,
        )
        self._has_named_index = True
        self.column_offset = 1

    def get_default_values(self, index, changed: dict | None = None):
        """Return the default values for a the row in a new index."""
        row_idx = index.row()
        df = self._data_frame
        row_key = df.index[row_idx] if isinstance(row_idx, int) else row_idx
        changes = {}
        rename_needed = False
        old_index = row_key
        new_index = row_key

        columns_with_index = [df.index.name] if df.index.name else []
        columns_with_index += list(df.columns)
        # ensure parameterScale is before lowerBound and upperBound (potential)
        if "parameterScale" in columns_with_index:
            columns_with_index.remove("parameterScale")
            columns_with_index.insert(1, "parameterScale")

        for colname in columns_with_index:
            if changed and colname in changed:
                continue
            if colname == df.index.name:
                # Generate default index name if empty
                default_value = self.default_handler.get_default(
                    colname, row_key, changed=changed
                )
                if (
                    not row_key or f"new_{self.table_type}" in row_key
                ) and bool(default_value):
                    rename_needed = True
                    new_index = default_value
            elif colname in ["upperBound", "lowerBound"]:
                par_scale = (
                    changes[(row_key, "parameterScale")][1]
                    if (row_key, "parameterScale") in changes
                    else changed["parameterScale"]
                )
                default_value = self.default_handler.get_default(
                    colname, row_key, par_scale
                )
                changes[(row_key, colname)] = ("", default_value)
            else:
                default_value = self.default_handler.get_default(
                    colname, row_key
                )
                changes[(row_key, colname)] = ("", default_value)

        commands = []
        if changes:
            commands.append(
                ModifyDataFrameCommand(self, changes, "Fill default values")
            )
        if rename_needed:
            commands.append(
                RenameIndexCommand(self, old_index, new_index, index)
            )
        if not commands:
            return
        if not self.undo_stack:
            for command in commands:
                command.redo()
            return
        self.undo_stack.beginMacro("Fill default values")
        for command in commands:
            self.undo_stack.push(command)
        self.undo_stack.endMacro()

    def handle_named_index(self, index, value):
        """Handle the named index column."""
        row = index.row()
        old_value = self._data_frame.index[row]
        if value == old_value:
            return False
        if value in self._data_frame.index:
            base = 0
            value = None
            while value is None:
                idx = f"new_{self.table_type}_{base}"
                if idx not in set(self._data_frame.index.astype(str)):
                    value = idx
                base += 1
            self.new_log_message.emit(
                f"Duplicate index value '{value}'. Renaming to default "
                f"value '{value}'",
                "orange",
            )
        try:
            self.undo_stack.push(
                RenameIndexCommand(self, old_value, value, index)
            )
            self.relevant_id_changed.emit(value, old_value, self.table_type)
            self.something_changed.emit(True)
            return True
        except Exception as e:
            self.new_log_message.emit(
                f"Error renaming index value '{old_value}' to '{value}': {e}",
                "red",
            )
            return False

    def return_column_index(self, column_name):
        """Return the index of a column."""
        if column_name in self._data_frame.columns:
            return self._data_frame.columns.get_loc(column_name) + 1
        if column_name == self._data_frame.index.name:
            return 0
        return -1


class MeasurementModel(PandasTableModel):
    """Table model for the measurement data."""

    possibly_new_condition = Signal(str)  # Signal for new condition
    possibly_new_observable = Signal(str)  # Signal for new observable

    def __init__(self, data_frame, type: str = "measurement", parent=None):
        allowed_columns = COLUMNS[type]
        super().__init__(
            data_frame=data_frame,
            allowed_columns=allowed_columns,
            table_type=type,
            parent=parent,
        )

    def get_default_values(self, index, changed: dict | None = None):
        """Fill missing values in a row without modifying the index."""
        row = index.row()
        df = self._data_frame
        row_key = self._data_frame.index[row] if isinstance(row, int) else row

        changes = {}
        for colname in df.columns:
            if colname in changed:
                continue
            default = self.default_handler.get_default(colname, row_key)
            changes[(row_key, colname)] = ("", default)
        command = ModifyDataFrameCommand(self, changes, "Fill default values")
        if self.undo_stack:
            self.undo_stack.push(command)
        else:
            command.redo()


class ObservableModel(IndexedPandasTableModel):
    """Table model for the observable data."""

    def __init__(self, data_frame, parent=None):
        super().__init__(
            data_frame=data_frame,
            allowed_columns=COLUMNS["observable"],
            table_type="observable",
            parent=parent,
        )


class ParameterModel(IndexedPandasTableModel):
    """Table model for the parameter data."""

    def __init__(self, data_frame, parent=None, sbml_model=None):
        super().__init__(
            data_frame=data_frame,
            allowed_columns=COLUMNS["parameter"],
            table_type="parameter",
            parent=parent,
        )
        self.default_handler = DefaultHandlerModel(
            self, self.config, sbml_model=sbml_model
        )


class ConditionModel(IndexedPandasTableModel):
    """Table model for the condition data."""

    def __init__(self, data_frame, parent=None):
        super().__init__(
            data_frame=data_frame,
            allowed_columns=COLUMNS["condition"],
            table_type="condition",
            parent=parent,
        )
        self._allowed_columns.pop("conditionId")


class PandasTableFilterProxy(QSortFilterProxyModel):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.source_model = model
        self.setSourceModel(model)

    def filterAcceptsRow(self, source_row, source_parent):
        """Apply global filtering across all columns."""
        source_model = self.sourceModel()

        # Always accept the last row (for "add new row")
        if source_row == source_model.rowCount() - 1:
            return True

        regex = self.filterRegularExpression()
        if regex.pattern() == "":
            return True

        for column in range(source_model.columnCount()):
            index = source_model.index(source_row, column, QModelIndex())
            data_str = str(source_model.data(index) or "")
            if regex.match(data_str).hasMatch():
                return True
        return False  # No match found

    def mimeData(self, rectangle, start_index):
        """Return the data to be copied to the clipboard."""
        return self.source_model.mimeData(rectangle, start_index)

    def setDataFromText(self, text, start_row, start_column):
        """Set the data from text."""
        return self.source_model.setDataFromText(text, start_row, start_column)

    @property
    def _invalid_cells(self):
        return self.source_model._invalid_cells


class VisualizationModel(PandasTableModel):
    """Table model for the visualization data."""

    def __init__(self, data_frame, parent=None):
        super().__init__(
            data_frame=data_frame,
            allowed_columns=COLUMNS["visualization"],
            table_type="visualization",
            parent=parent,
        )
