import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent  # yaml папка
config_path = BASE_DIR / 'config.yaml'


def get_config(path):
    with open(path) as f:
        parsed = yaml.safe_load(f)
    return parsed


config = get_config(config_path)

if __name__ == '__main__':
    print(config.get('postgres'))