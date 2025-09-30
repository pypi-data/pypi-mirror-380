import importlib
import importlib.util
import inspect
from pathlib import Path
from typing import Any, Protocol, Self, runtime_checkable


@runtime_checkable
class Plugin(Protocol):
    def get_name(self) -> str: ...
    def validate(self, *args: tuple[Any], **kwargs: dict[str, Any]) -> bool: ...
    def execute(self, *args: tuple[Any], **kwargs: dict[str, Any]) -> bool: ...


class PluginManager:
    def __init__(self, plugin_dir: Path | None = None) -> None:
        if plugin_dir is None:
            # Get the directory where this __init__.py file is located
            self.plugin_dir = Path(__file__).parent
        else:
            self.plugin_dir = plugin_dir
        self.plugins: dict[str, Plugin] = {}

    def discover_plugins(self) -> Self:
        for file_path in self.plugin_dir.glob("*.py"):
            if file_path.name != "__init__.py":
                self._load_plugin(file_path)
        print(f"Loaded {len(self.plugins)} plugins")
        return self

    def _load_plugin(self, module_file: Path) -> None:
        try:
            # Use importlib.util to load module directly from file path
            spec = importlib.util.spec_from_file_location(module_file.stem, module_file)
            if spec is None or spec.loader is None:
                raise ImportError(f"Cannot create spec for {module_file}")

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for _, klass in inspect.getmembers(module, inspect.isclass):
                if issubclass(klass, Plugin):
                    plugin_inst = klass()
                    plugin_name = plugin_inst.get_name()
                    self.plugins[plugin_name] = plugin_inst
                    print(f"Loaded plugin: {plugin_name}")
        except Exception as e:
            print(f"Error loading plugin module {module_file}: {e}")

    def get_plugins(self) -> list[str]:
        return list(self.plugins.keys())

    @staticmethod
    def get_full_module(module_file: Path, marker_file: str = "pyproject.toml") -> str:
        path = []
        path.append(module_file.stem)
        current = module_file.parent
        while current != current.parent:
            if (current / marker_file).exists():
                break
            path.append(current.name)
            current = current.parent

        return ".".join(reversed(path))

    def _run_method(
        self,
        plugin_name: str | None,
        method: str,
        *args: Any,
        **kwargs: Any,
    ) -> bool:
        success = True
        plugins = [plugin_name] if plugin_name else self.get_plugins()
        for plugin in plugins:
            try:
                plugin_method = getattr(self.plugins[plugin], method)
                plugin_method(*args, **kwargs)
            except KeyError:
                print(f"Plugin not found {plugin_name}")
                success = False
            except Exception as e:
                print(f"Failed to execute {plugin_name}.{method}(): {e}")
                success = False
        return success
