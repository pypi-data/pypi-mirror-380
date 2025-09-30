"""Main Window View."""

import copy

from PySide6.QtCore import QSettings, Qt
from PySide6.QtWidgets import (
    QDockWidget,
    QMainWindow,
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from ..C import APP_NAME
from ..models.tooltips import (
    COND_TABLE_TOOLTIP,
    DATA_PLOT_TOOLTIP,
    DATA_TABLES_TAB_TOOLTIP,
    INFO_TOOLTIP,
    MEAS_TABLE_TOOLTIP,
    OBS_TABLE_TOOLTIP,
    PAR_TABLE_TOOLTIP,
    SBML_MODEL_TAB_TOOLTIP,
    SIM_TABLE_TOOLTIP,
    VIS_TABLE_TOOLTIP,
)
from ..settings_manager import settings_manager
from .find_replace_bar import FindReplaceBar
from .logger import Logger
from .sbml_view import SbmlViewer
from .simple_plot_view import MeasurementPlotter
from .table_view import TableViewer
from .whats_this import WHATS_THIS


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.allow_close = False

        self.setWindowTitle(APP_NAME)
        self.setGeometry(100, 100, 1200, 800)

        # Logger: used in both tabs
        self.logger_views = [Logger(self), Logger(self)]

        # Main layout: Two tabs
        self.tab_widget = QTabWidget(self)

        # Tab for the data tables
        self.data_tab = QMainWindow()
        tab = self.tab_widget.addTab(self.data_tab, "Data Tables")
        self.tab_widget.setTabToolTip(tab, DATA_TABLES_TAB_TOOLTIP)
        self.tab_widget.setTabWhatsThis(tab, WHATS_THIS["tabs"]["data_tables"])

        # Tab for the SBML model
        self.sbml_viewer = SbmlViewer(logger_view=self.logger_views[0])
        tab = self.tab_widget.addTab(self.sbml_viewer, "SBML Model")
        self.tab_widget.setTabToolTip(tab, SBML_MODEL_TAB_TOOLTIP)
        self.tab_widget.setTabWhatsThis(tab, WHATS_THIS["tabs"]["sbml_model"])

        # Set the QTabWidget as the central widget
        self.setCentralWidget(self.tab_widget)

        # Create dock widgets for each table
        self.condition_dock = TableViewer("Condition Table")
        self.condition_dock.setToolTip(COND_TABLE_TOOLTIP)
        self.tab_widget.setTabWhatsThis(
            tab, WHATS_THIS["tables"]["condition"]["table"]
        )
        self.measurement_dock = TableViewer("Measurement Table")
        self.measurement_dock.setToolTip(MEAS_TABLE_TOOLTIP)
        self.observable_dock = TableViewer("Observable Table")
        self.observable_dock.setToolTip(OBS_TABLE_TOOLTIP)
        self.parameter_dock = TableViewer("Parameter Table")
        self.parameter_dock.setToolTip(PAR_TABLE_TOOLTIP)
        self.logger_dock = QDockWidget("Info")
        self.logger_dock.setToolTip(INFO_TOOLTIP)
        self.logger_dock.setObjectName("logger_dock")
        self.logger_dock.setWidget(self.logger_views[1])
        self.plot_dock = MeasurementPlotter(self)
        self.plot_dock.setToolTip(DATA_PLOT_TOOLTIP)
        self.visualization_dock = TableViewer("Visualization Table")
        self.visualization_dock.setToolTip(VIS_TABLE_TOOLTIP)
        self.simulation_dock = TableViewer("Simulation Table")
        self.simulation_dock.setToolTip(SIM_TABLE_TOOLTIP)

        self.dock_visibility = {
            self.condition_dock: self.condition_dock.isVisible(),
            self.measurement_dock: self.measurement_dock.isVisible(),
            self.observable_dock: self.observable_dock.isVisible(),
            self.parameter_dock: self.parameter_dock.isVisible(),
            self.logger_dock: self.logger_dock.isVisible(),
            self.plot_dock: self.plot_dock.isVisible(),
            self.visualization_dock: self.visualization_dock.isVisible(),
            self.simulation_dock: self.simulation_dock.isVisible(),
        }
        self.default_view()
        self.condition_dock.visibilityChanged.connect(
            self.save_dock_visibility
        )
        self.measurement_dock.visibilityChanged.connect(
            self.save_dock_visibility
        )
        self.observable_dock.visibilityChanged.connect(
            self.save_dock_visibility
        )
        self.parameter_dock.visibilityChanged.connect(
            self.save_dock_visibility
        )
        self.logger_dock.visibilityChanged.connect(self.save_dock_visibility)
        self.plot_dock.visibilityChanged.connect(self.save_dock_visibility)
        self.visualization_dock.visibilityChanged.connect(
            self.save_dock_visibility
        )
        self.simulation_dock.visibilityChanged.connect(
            self.save_dock_visibility
        )

        # Allow docking in multiple areas
        self.data_tab.setDockOptions(QMainWindow.AllowNestedDocks)

        self.tab_widget.currentChanged.connect(self.set_docks_visible)

        settings_manager.load_ui_settings(self)

        # drag drop
        self.setAcceptDrops(True)

        self.find_replace_bar = None

    def default_view(self):
        """Reset the view to a fixed 3x2 grid using manual geometry."""
        if hasattr(self, "dock_visibility"):
            for dock in self.dock_visibility:
                dock.setParent(None)  # fully remove from layout

        self.tab_widget.setCurrentIndex(0)
        self.data_tab.updateGeometry()
        self.data_tab.repaint()

        # Get available geometry
        available_rect = self.data_tab.contentsRect()
        width = available_rect.width() // 2
        height = available_rect.height() // 4
        x_left = available_rect.left()
        x_right = x_left + width
        y_positions = [available_rect.top() + i * height for i in range(4)]

        # Define dock + positions
        layout = [
            (self.measurement_dock, x_left, y_positions[0]),
            (self.parameter_dock, x_left, y_positions[1]),
            (self.logger_dock, x_left, y_positions[2]),
            (self.visualization_dock, x_left, y_positions[3]),
            (self.observable_dock, x_right, self.measurement_dock),
            (self.condition_dock, x_right, self.parameter_dock),
            (self.plot_dock, x_right, self.logger_dock),
            (self.simulation_dock, x_right, self.visualization_dock),
        ]

        for dock, x, y in layout:
            area = Qt.LeftDockWidgetArea
            if x == x_left:
                self.data_tab.addDockWidget(area, dock)
                dock.setFloating(True)
                dock.setGeometry(x, y, width, height)
                dock.setFloating(False)
            if x == x_right:
                self.data_tab.splitDockWidget(y, dock, Qt.Horizontal)

        if hasattr(self, "dock_visibility"):
            for dock in self.dock_visibility:
                dock.setVisible(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            return

        event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            self.controller.open_file(url.toLocalFile())
            return

        event.ignore()

    def setup_toolbar(self, actions):
        # add a toolbar with actions from self.task_bar
        tb = self.addToolBar("MainToolbar")
        tb.setObjectName("MainToolbar")
        self.setUnifiedTitleAndToolBarOnMac(True)
        # spacer for later
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        # first the normal open / save operations
        tb.addAction(actions["new"])
        tb.addAction(actions["open"])
        tb.addAction(actions["add"])
        tb.addAction(actions["save"])
        tb.addAction(actions["check_petab"])
        tb.addAction(actions["add_row"])
        tb.addAction(actions["delete_row"])
        tb.addAction(actions["add_column"])
        tb.addAction(actions["delete_column"])
        tb.addAction(actions["simulate"])
        tb.addWidget(spacer)
        tb.addWidget(actions["filter_widget"])
        tb.addAction(actions["whats_this"])

    def add_menu_action(self, dock_widget, name):
        """Add actions to the menu to show dock widgets."""
        action = self.view_menu.addAction(name)
        action.setCheckable(True)
        action.setChecked(True)

        # Show or hide the dock widget based on the menu action
        action.toggled.connect(lambda checked: dock_widget.setVisible(checked))

        # Sync the menu action with the visibility of the dock widget
        dock_widget.visibilityChanged.connect(action.setChecked)

    def save_dock_visibility(self, visible):
        """Save the visibility status of a QDockWidget when it changes."""
        # if current tab is not the data tab return
        if self.tab_widget.currentIndex() != 0:
            return
        dock = self.sender()  # Get the QDockWidget that emitted the signal
        self.dock_visibility[dock] = dock.isVisible()

    def set_docks_visible(self, index):
        """Set all QDockWidgets to their previous visibility on tab-change."""
        if index != 0:  # Another tab is selected
            for dock, visible in self.dock_visibility.items():
                dock.setVisible(visible)

    def closeEvent(self, event):
        """Override the closeEvent to emit additional signal."""
        self.controller.maybe_close()

        if self.allow_close:
            settings_manager.save_ui_settings(self)
            event.accept()
        else:
            event.ignore()

    def load_settings(self):
        """Load the settings from the QSettings object."""
        settings = QSettings("petab", "petab_gui")

        # Load the visibility of the dock widgets
        for dock, _ in self.dock_visibility.items():
            dock.setVisible(
                settings.value(f"docks/{dock.objectName()}", True, type=bool)
            )

        # Load the geometry of the main window
        self.restoreGeometry(settings.value("main_window/geometry"))

        # Restore the positions of the dock widgets
        self.restoreState(settings.value("main_window/state"))

        # restore the settings of the data tab
        self.data_tab.restoreGeometry(settings.value("data_tab/geometry"))
        self.data_tab.restoreState(settings.value("data_tab/state"))

    def save_settings(self):
        """Save the settings to the QSettings object."""
        settings = QSettings("petab", "petab_gui")

        # Save the visibility of the dock widgets
        for dock, _ in self.dock_visibility.items():
            settings.setValue(f"docks/{dock.objectName()}", dock.isVisible())

        # Save the geometry of the main window
        settings.setValue("main_window/geometry", self.saveGeometry())

        # Save the positions of the dock widgets
        settings.setValue("main_window/state", self.saveState())

        # save the settings of the data tab
        settings.setValue("data_tab/geometry", self.data_tab.saveGeometry())
        settings.setValue("data_tab/state", self.data_tab.saveState())

    def create_find_replace_bar(self):
        """Create the find/replace bar.

        Add it without replacing the tab widget.
        """
        self.find_replace_bar = FindReplaceBar(self.controller, self)
        # manually create a copy of the dock visibility
        dock_visibility_values = copy.deepcopy(
            list(self.dock_visibility.values())
        )

        # Create a layout to insert Find/Replace above the tabs
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove extra spacing
        layout.addWidget(self.find_replace_bar)
        layout.addWidget(self.tab_widget)  # Keep tab_widget in the layout

        self.setCentralWidget(container)
        # Restore the visibility of the docks
        for dock, visible in zip(
            self.dock_visibility.keys(), dock_visibility_values, strict=False
        ):
            self.dock_visibility[dock] = visible
            dock.setVisible(visible)

    def toggle_find(self):
        """Toggles the find-part of the Find.Replace Bar."""
        self.find_replace_bar.toggle_find()

    def toggle_replace(self):
        """Toggles the replace-part of the Find.Replace Bar."""
        self.find_replace_bar.toggle_replace()
