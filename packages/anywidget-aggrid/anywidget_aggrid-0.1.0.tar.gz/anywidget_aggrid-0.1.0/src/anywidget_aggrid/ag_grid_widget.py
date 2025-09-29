from pathlib import Path

import anywidget
import traitlets

class AgGridWidget(anywidget.AnyWidget):
    _esm = Path(__file__).resolve().parent / "dist/index.js"
    _css = Path(__file__).resolve().parent / "dist/index.js"
    height = traitlets.Unicode(default_value="400px").tag(sync=True)
    column_defs = traitlets.List().tag(sync=True)
    row_data = traitlets.List().tag(sync=True)
    default_column_def = traitlets.Dict().tag(sync=True)
    grid_options = traitlets.Dict(None).tag(sync=True)
    selected_row = traitlets.List(default_value=[]).tag(sync=True)
