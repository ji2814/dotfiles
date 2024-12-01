import argparse
import os
import shutil
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(description='Update configuration scripts.')
    parser.add_argument('--kitty', required=False, action='store_true', help='update the kitty configuration')
    parser.add_argument('--omf', required=False, action='store_true', help='update the oh my fish init script')
    parser.add_argument('--rime', required=False, action='store_true', help='update the rime configuration')
    parser.add_argument('--vimrc', required=False, action='store_true', help='update all configurations')
    return parser.parse_args()

def get_config_paths():
    home_dir = os.path.expanduser('~')
    return {
        'kitty': os.path.join(home_dir, '.config', 'kitty', 'kitty.conf'),
        'omf': os.path.join(home_dir, '.config', 'omf', 'init.fish'),
        'rime': os.path.join(home_dir, '.config', 'ibus', 'rime'),
        'vimrc': os.path.join(home_dir, '.vimrc')
    }

def copy_file(src, dst):
    if os.path.exists(dst):
        logging.warning(f"Backup existing configuration file: {dst}")
        shutil.copy(dst, dst + ".bak")
    try:
        shutil.copy(src, dst)
        logging.info(f"{os.path.basename(src)} has been copied to {dst}")
    except Exception as e:
        logging.error(f"An error occurred while copying {os.path.basename(src)}: {e}")

def copy_directory(src, dst):
    if os.path.exists(dst):
        logging.warning(f"Backup existing configuration directory: {dst}")
        shutil.copytree(dst, dst + ".bak")
    try:
        shutil.copytree(src, dst)
        logging.info(f"{os.path.basename(src)} has been copied to {dst}")
    except Exception as e:
        logging.error(f"An error occurred while copying {os.path.basename(src)}: {e}")

def main():
    args = parse_args()
    config_paths = get_config_paths()
    current_dir = os.getcwd()

    if args.kitty:
        src = os.path.join(current_dir, 'kitty.conf')
        dst = config_paths['kitty']
        copy_file(src, dst)

    if args.omf:
        src = os.path.join(current_dir, 'omf', 'init.fish')
        dst = config_paths['omf']
        copy_file(src, dst)

    if args.rime:
        src = os.path.join(current_dir, 'rime')
        dst = config_paths['rime']
        copy_directory(src, dst)

    if args.vimrc:
        src = os.path.join(current_dir, 'vim', '.vimrc')
        dst = config_paths['vimrc']
        copy_file(src, dst)

if __name__ == '__main__':
    main()
