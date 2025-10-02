import os
import shutil
import sys
from pathlib import Path
from pprint import pprint

from kabaret import flow
from kabaret.app import resources
from libreflow.baseflow.file import GenericRunAction
from libreflow.baseflow.task import Task

from . import scripts


class InitializeKritaFile(GenericRunAction):
    ICON = ("icons.libreflow", "krita")

    _task = flow.Parent()
    _shot = flow.Parent(3)
    _sequence = flow.Parent(5)

    def __init__(self, parent, name):
        super(InitializeKritaFile, self).__init__(parent, name)
        self.krita_script = None

    def allow_context(self, context):
        return context

    def runner_name_and_tags(self):
        return "KritaRunner", []

    def get_run_label(self):
        return "Build Krita file"

    def target_file_extension(self):
        return "kra"

    def needs_dialog(self):
        return True

    def get_buttons(self):
        msg = "<h2>Build Krita file</h2>"
        self.message.set(msg)
        buttons = ["Build", "Cancel"]

        return buttons

    def get_path_format(self, task_name, file_mapped_name):
        manager = self.root().project().get_task_manager()
        if not manager.default_tasks.has_mapped_name(task_name):
            return None

        default_task = manager.default_tasks[task_name]
        if not default_task.files.has_mapped_name(file_mapped_name):
            return default_task.path_format.get()

        default_file = default_task.files[file_mapped_name]
        return default_file.path_format.get()

    def ensure_krita_file(self):
        files = self._task.files
        name = "colo"
        extension = "kra"
        file_name = f"{name}_{extension}"
        path_format = self.get_path_format(self._task.name(), file_name)

        print(path_format)

        if files.has_file(name, extension):
            file = files[file_name]
        else:
            file = files.add_file(
                name=name,
                extension=extension,
                tracked=True,
                default_path_format=path_format,
            )

        revision = file.add_revision(comment="Created with init Krita file")
        os.makedirs(os.path.dirname(revision.get_path()), exist_ok=True)
        file.set_current_user_on_revision(revision.name())

        return revision.get_path()

    def extra_argv(self):
        project_settings = self.root().project().admin.project_settings

        # Get resolution
        resolution_width = project_settings.width.get()
        resolution_height = project_settings.height.get()

        # get FPS
        frame_rate = project_settings.frame_rate.get()

        # Nombre de frames
        kitsu = self.root().project().kitsu_api()
        frames = kitsu.get_shot_duration(self._shot.name(), self._sequence.name())

        revision_path = self.ensure_krita_file()

        file_name = os.path.basename(revision_path)

        script_name = os.path.basename(self.krita_script).replace(".py", "")

        args = [
            "-s",
            script_name,
            resolution_width,
            resolution_height,
            int(frame_rate),
            frames,
            revision_path,
            file_name,
        ]
        return args

    def run(self, button):
        self.krita_script = resources.get("scripts", "krita_setup_file.py")

        home = Path.home()

        if sys.platform == "win32":
            data_dir = home / "AppData/Roaming"
        elif sys.platform == "linux":
            data_dir = home / ".local/share"
        elif sys.platform == "darwin":
            data_dir = home / "Library/Application Support"

        kritarunner_path = Path(f"{data_dir}/kritarunner")
        if not kritarunner_path.exists():
            kritarunner_path.mkdir(parents=True, exist_ok=True)

        shutil.copy(self.krita_script, kritarunner_path)

        return super(InitializeKritaFile, self).run(button)


def initialize_krita_file(parent):
    if isinstance(parent, Task) and "colo" in parent.name():
        initialize_krita_file = flow.Child(InitializeKritaFile)
        initialize_krita_file.name = "initialize_krita_file"
        return initialize_krita_file

    return None


def install_extensions(session):
    return {
        "demo": [
            initialize_krita_file,
        ],
    }
