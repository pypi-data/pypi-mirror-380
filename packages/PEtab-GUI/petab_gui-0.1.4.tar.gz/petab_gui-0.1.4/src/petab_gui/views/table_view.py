from PySide6.QtCore import QPropertyAnimation, QRect, Qt
from PySide6.QtGui import QColor, QGuiApplication
from PySide6.QtWidgets import (
    QComboBox,
    QCompleter,
    QDockWidget,
    QHeaderView,
    QLineEdit,
    QStyledItemDelegate,
    QTableView,
)

from ..utils import get_selected_rectangles
from .context_menu_mananger import ContextMenuManager


class TableViewer(QDockWidget):
    """A dock widget that contains a table view for displaying tabular data.

    This class provides a container for a CustomTableView and handles clipboard
    operations for copying and pasting data.
    """

    def __init__(self, title, parent=None):
        """Initialize the table viewer.

        Args:
            title: The title of the dock widget
            parent: The parent widget
        """
        super().__init__(title, parent)
        self.title = title
        self.setObjectName(title)
        self.setAllowedAreas(Qt.AllDockWidgetAreas)
        # Create the QTableView for the table content
        self.table_view = CustomTableView()
        self.setWidget(self.table_view)
        # Dictionary to store column-specific completers
        self.completers = {}
        self.table_view.setAlternatingRowColors(True)

    def copy_to_clipboard(self):
        """Copy selected cells to the clipboard.

        Gets the selected cells from the table view and copies their content
        to the system clipboard in a format suitable for pasting into other
        applications.
        """
        selected_rect, rect_start = get_selected_rectangles(self.table_view)
        if selected_rect.any():
            mime_data = self.table_view.model().mimeData(
                selected_rect, rect_start
            )
            clipboard = QGuiApplication.clipboard()
            clipboard.setMimeData(mime_data)

    def paste_from_clipboard(self):
        """Paste clipboard content into the table.

        Retrieves text from the system clipboard and pastes it into the table
        starting at the current selection. The text is parsed as tab-separated
        values, with each line representing a row.

        The method handles:
        - Mapping between proxy and source models
        - Parsing clipboard data into rows and columns
        - Identifying and handling cells that will be overridden
        - Handling invalid cells that might be affected by the paste operation
        """
        clipboard = QGuiApplication.clipboard()
        text = clipboard.text()
        if not text:
            return

        # Get the proxy and source models
        proxy_model = self.table_view.model()
        source_model = proxy_model.sourceModel()

        # Get the start index from the current selection
        start_index = self.table_view.selectionModel().currentIndex()
        if not start_index.isValid():
            return

        # Map the start index to the source model
        source_index = proxy_model.mapToSource(start_index)
        row_start, col_start = source_index.row(), source_index.column()

        # Parse clipboard data
        pasted_data = [
            line.split("\t") for line in text.split("\n") if line.strip()
        ]
        num_rows = len(pasted_data)
        num_cols = max(len(line) for line in pasted_data)

        # Identify which cells are being overridden
        overridden_cells = {
            (row_start + r, col_start + c)
            for r in range(num_rows)
            for c in range(num_cols)
            if source_model.index(row_start + r, col_start + c).isValid()
        }

        # Handle invalid cells
        if hasattr(source_model, "_invalid_cells"):
            invalid_overridden_cells = overridden_cells.intersection(
                source_model._invalid_cells
            )
            for row_invalid, col_invalid in invalid_overridden_cells:
                source_model.discard_invalid_cell(row_invalid, col_invalid)

        # Paste the data into the source model
        source_model.setDataFromText(text, row_start, col_start)


class ComboBoxDelegate(QStyledItemDelegate):
    """A delegate that provides a combo box for editing table cells.

    This delegate is used to provide a dropdown list of predefined options
    when editing cells in a table view.
    """

    def __init__(self, options, parent=None):
        """Initialize the combo box delegate.

        Args:
            options: A list of strings to display in the combo box
            parent: The parent widget
        """
        super().__init__(parent)
        self.options = options

    def createEditor(self, parent, option, index):
        """Create a QComboBox for inline editing.

        Args:
            parent: The parent widget for the editor
            option: The style options for the editor
            index: The model index of the cell being edited

        Returns:
            QComboBox: A combo box containing the predefined options
        """
        editor = QComboBox(parent)
        editor.addItems(self.options)
        return editor


class SingleSuggestionDelegate(QStyledItemDelegate):
    """
    Single Option Suggestion Delegate.

    Suggest a single option based the current row and the value in
    `column_name`.
    """

    def __init__(self, model, suggestions_column, afix=None, parent=None):
        """Initialize the single suggestion delegate.

        Args:
        model:
            The data model to retrieve suggestions from
        suggestions_column:
            The column name or index to get suggestion values from
        afix:
            Optional prefix to add to the suggestion value
        parent:
            The parent widget
        """
        super().__init__(parent)
        self.model = model  # The main model to retrieve data from
        self.suggestions_column = suggestions_column
        self.afix = afix

    def createEditor(self, parent, option, index):
        """Create a QLineEdit for inline editing with a single suggestion."""
        editor = QLineEdit(parent)

        # Get the conditionId of the current row
        row = index.row()
        suggestion = self.model.get_value_from_column(
            self.suggestions_column, row
        )
        if self.afix:
            suggestion = self.afix + suggestion

        # Set up the completer with a single suggestion
        completer = QCompleter([suggestion], parent)
        completer.setCompletionMode(QCompleter.InlineCompletion)
        editor.setCompleter(completer)

        return editor


class ColumnSuggestionDelegate(QStyledItemDelegate):
    """Suggest options based on all unique values in the specified column."""

    def __init__(
        self,
        model,
        suggestions_column,
        suggestion_mode=QCompleter.PopupCompletion,
        parent=None,
    ):
        """Initialize the column suggestion delegate.

        Args:
        model:
            The data model to retrieve suggestions from
        suggestions_column:
            The column name or index to get unique values from
        suggestion_mode:
            The completion mode for the QCompleter (default: PopupCompletion)
        parent:
            The parent widget
        """
        super().__init__(parent)
        self.model = model  # The main model to retrieve data from
        self.suggestions_column = suggestions_column
        self.suggestion_mode = suggestion_mode

    def createEditor(self, parent, option, index):
        """Create a QLineEdit for inline editing with suggestions."""
        editor = QLineEdit(parent)

        # Get unique suggestions from the specified column
        suggestions = self.model.unique_values(self.suggestions_column)

        # Set up the completer with the unique values
        completer = QCompleter(suggestions, parent)
        completer.setCompletionMode(self.suggestion_mode)
        editor.setCompleter(completer)

        return editor


class ParameterIdSuggestionDelegate(QStyledItemDelegate):
    """Suggest options based on all unique values in the specified column."""

    def __init__(self, par_model, sbml_model, parent=None):
        """Initialize the parameter ID suggestion delegate.

        Args:
        par_model:
            The parameter table model to retrieve current parameter IDs from
        sbml_model:
            The SBML model to retrieve valid parameter suggestions from
        parent:
            The parent widget
        """
        super().__init__(parent)
        self.par_model = par_model
        self.sbml_model = sbml_model  # The main model to retrieve data from

    def createEditor(self, parent, option, index):
        """Create an editor for the parameterId column."""
        editor = QLineEdit(parent)

        # Get unique suggestions from the specified column
        curr_model = self.sbml_model.get_current_sbml_model()
        suggestions = None
        if curr_model:  # only if model is valid
            suggestions = curr_model.get_valid_parameters_for_parameter_table()
            # substract the current parameter ids except for the current row
            row = index.row()
            selected_parameter_id = self.par_model.get_value_from_column(
                "parameterId", row
            )
            current_parameter_ids = self.par_model.get_df().index.tolist()
            if selected_parameter_id in current_parameter_ids:
                current_parameter_ids.remove(selected_parameter_id)
            suggestions = list(set(suggestions) - set(current_parameter_ids))

        # Set up the completer with the unique values
        completer = QCompleter(suggestions, parent)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        editor.setCompleter(completer)

        return editor


class CustomTableView(QTableView):
    """Custom Table View to Handle Copy Paste events, resizing policies etc."""

    def __init__(self, parent=None):
        """Initialize the custom table view.

        Sets up the table view with appropriate size adjustment policies,
        resize modes, and connects signals for column resizing.

        Args:
            parent: The parent widget
        """
        super().__init__(parent)
        self.setSizeAdjustPolicy(QTableView.AdjustToContents)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.horizontalHeader().setStretchLastSection(
            False
        )  # Prevent last column from stretching

        self.horizontalHeader().sectionDoubleClicked.connect(
            self.autofit_column
        )

    def setup_context_menu(self, actions):
        """Setup the context menu for the table view.

        Creates a context menu manager and connects it to the table view's
        context menu request signal.

        Args:
            actions: A list of QAction objects to include in the context menu
        """
        self.context_menu_manager = ContextMenuManager(
            actions, self, self.parent
        )
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(
            self.context_menu_manager.create_context_menu
        )

    def setModel(self, model):
        """Set the model for the table view.

        Overrides the base class method to ensure that signals are connected
        only after the selection model exists.

        Args:
            model: The model to set for this view
        """
        super().setModel(model)
        if self.selectionModel():
            self.selectionModel().currentColumnChanged.connect(
                self.highlight_active_column
            )

    def reset_column_sizes(self):
        """Reset column sizes with intelligent width adjustments.

        This method:
        1. Initially resizes all columns to fit their content
        2. Enforces a maximum width (1/4 of the viewport width) for any column
        3. Collapses empty columns to save space
        4. Updates the table geometry to reflect the new column sizes

        The result is a table with columns, appropriately sized for their
        content while maintaining a reasonable overall width.
        """
        header = self.horizontalHeader()
        total_width = self.viewport().width()
        max_width = total_width // 4  # 1/4th of total table width

        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.resizeColumnsToContents()
        header.setSectionResizeMode(QHeaderView.Interactive)

        # Enforce max width but allow expanding into empty neighbors
        for col in range(self.model().columnCount()):
            optimal_width = self.columnWidth(col)
            if optimal_width > max_width:
                self.setColumnWidth(col, max_width)
            else:
                self.setColumnWidth(col, optimal_width)

        self.collapse_empty_columns()
        self.updateGeometry()

    def adjust_for_empty_neighbors(self):
        """Expands column if adjacent columns are empty."""
        model = self.model()
        for col in range(model.columnCount()):
            if (
                self.columnWidth(col) == self.viewport().width() // 4
            ):  # If maxed out
                next_col = col + 1
                if next_col < model.columnCount() and all(
                    model.index(row, next_col).data() in [None, ""]
                    for row in range(model.rowCount())
                ):
                    new_width = self.columnWidth(col) + self.columnWidth(
                        next_col
                    )
                    self.setColumnWidth(col, new_width)
                    self.setColumnWidth(next_col, 0)  # Hide empty column

    def collapse_empty_columns(self):
        """Collapses columns that only contain empty values."""
        model = self.model()
        for col in range(model.columnCount()):
            if all(
                model.index(row, col).data() in [None, "", " "]
                for row in range(model.rowCount())
            ):
                self.setColumnWidth(col, 10)  # Minimal width

    def autofit_column(self, col):
        """Expands column width to fit its content when double-clicked.

        Temporarily sets the column's resize mode to ResizeToContents,
        resizes it, then sets it back to Interactive mode to allow manual
        resizing.

        Args:
            col: The index of the column to resize
        """
        self.horizontalHeader().setSectionResizeMode(
            col, QHeaderView.ResizeToContents
        )
        self.resizeColumnToContents(col)
        self.horizontalHeader().setSectionResizeMode(
            col, QHeaderView.Interactive
        )

    def highlight_active_column(self, index):
        """Highlights the active column with a light blue background.

        This method is connected to the selectionModel's currentColumnChanged
        signal and applies a background color to all cells in the column of
        the current index.

        Args:
            index: The model index of the currently selected cell
        """
        for row in range(self.model().rowCount()):
            self.model().setData(
                self.model().index(row, index.column()),
                QColor("#cce6ff"),
                Qt.BackgroundRole,
            )

    def animate_column_resize(self, col, new_width):
        """Smoothly animates column resizing with a visual transition effect.

        Creates a QPropertyAnimation that gradually changes the column width
        from its current value to the new width over a short duration.

        Args:
            col: The index of the column to resize
            new_width: The target width for the column in pixels
        """
        anim = QPropertyAnimation(self, b"geometry")
        anim.setDuration(200)
        anim.setStartValue(
            QRect(
                self.columnViewportPosition(col),
                0,
                self.columnWidth(col),
                self.height(),
            )
        )
        anim.setEndValue(
            QRect(
                self.columnViewportPosition(col), 0, new_width, self.height()
            )
        )
        anim.start()
