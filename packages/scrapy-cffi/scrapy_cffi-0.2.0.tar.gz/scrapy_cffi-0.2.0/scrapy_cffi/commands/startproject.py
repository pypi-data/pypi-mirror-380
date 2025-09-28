import shutil, toml
from pathlib import Path

def run(project_name, is_demo=False):
    base = Path(__file__).parent.parent # scrapy_cffi
    template_dir = base / "templates"
    target: Path = Path.cwd() / project_name

    if target.exists():
        print(f"Error: Project '{project_name}' already exists.")
        return False
    
    spiders_dir =  target
    shutil.copytree(template_dir / "spiders", spiders_dir)
    shutil.copytree(template_dir / "js_path", target / "js_path")

    # docker
    for docker_file in ["Dockerfile", "docker-compose.yml", ".gitignore", ".dockerignore"]:
        dockerfile_path = template_dir / "config" / docker_file
        target_docker_path = target / docker_file
        docker_code = dockerfile_path.read_text(encoding='utf-8')
        target_docker_path.write_text(docker_code, encoding='utf-8')
    
    config_data = {
        "default": {
            "project_name": project_name,
        }
    }
    config_path = target / "scrapy_cffi.toml"
    with config_path.open("w", encoding="utf-8") as f:
        toml.dump(config_data, f)
    if not is_demo:
        print(f"Project '{project_name}' created.")
        print(f"\tcd {project_name}")
        print(f"\tscrapy-cffi genspider <spider_name> <domain>")