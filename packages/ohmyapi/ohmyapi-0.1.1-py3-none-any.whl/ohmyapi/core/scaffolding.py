import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Base templates directory
TEMPLATE_DIR = Path(__file__).parent / "templates"
env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))


def render_template_file(template_path: Path, context: dict, output_path: Path):
    """Render a single Jinja2 template file to disk."""
    template = env.get_template(str(template_path.relative_to(TEMPLATE_DIR)).replace("\\", "/"))
    content = template.render(**context)
    os.makedirs(output_path.parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)


def render_template_dir(template_subdir: str, target_dir: Path, context: dict, subdir_name: str | None = None):
    """
    Recursively render all *.j2 templates from TEMPLATE_DIR/template_subdir into target_dir.
    If subdir_name is given, files are placed inside target_dir/subdir_name.
    """
    template_dir = TEMPLATE_DIR / template_subdir
    for root, _, files in os.walk(template_dir):
        root_path = Path(root)
        rel_root = root_path.relative_to(template_dir)  # path relative to template_subdir

        for f in files:
            if not f.endswith(".j2"):
                continue

            template_rel_path = rel_root / f
            output_rel_path = Path(*template_rel_path.parts).with_suffix("")  # remove .j2

            # optionally wrap in subdir_name
            if subdir_name:
                output_path = target_dir / subdir_name / output_rel_path
            else:
                output_path = target_dir / output_rel_path

            render_template_file(template_dir / template_rel_path, context, output_path)


def startproject(name: str):
    """Create a new project: flat structure, all project templates go into <name>/"""
    target_dir = Path(name).resolve()
    os.makedirs(target_dir, exist_ok=True)
    render_template_dir("project", target_dir, {"project_name": name})
    print(f"✅ Project '{name}' created successfully.")
    print(f"🔧 Next, configure your project in {target_dir / 'settings.py'}")


def startapp(name: str, project: str):
    """Create a new app inside a project: templates go into <project_dir>/<name>/"""
    target_dir = Path(project)
    os.makedirs(target_dir, exist_ok=True)
    render_template_dir("app", target_dir, {"project_name": project, "app_name": name}, subdir_name=name)
    print(f"✅ App '{name}' created in project '{target_dir}' successfully.")
    print(f"🔧 Remember to add '{name}' to your INSTALLED_APPS!")

