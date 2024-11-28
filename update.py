import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='')

parser.add_argument('--kitty', required=False, action='store_true', help='update the kitty configuration')
parser.add_argument('--omf', required=False, action='store_true', help='update the oh my fish init script')
parser.add_argument('--rime', required=False, action='store_true', help='update the rime configuration')

# 定义目录
current_dir = os.getcwd()
home_dir = os.path.expanduser('~')

kitty_config_dir = os.path.join(home_dir, '.config', 'kitty', 'kitty.conf') # ~/.config/kitty/kitty.conf
omf_init_dir = os.path.join(home_dir, '.config', 'omf', 'init.fish') # ~/.config/omf/init.fish
rime_dir = os.path.join(home_dir, '.config', 'ibus', 'rime') # ~/.config/ibus/rime/*

args = parser.parse_args()

# 根据布尔值复制文件
if args.kitty:
    try:
        shutil.copy(os.path.join(current_dir, 'kitty.conf'), kitty_config_dir)
        print(f"kitty.conf has been copied to {kitty_config_dir}")
    except Exception as e:
        print(f"An error occurred while copying kitty.conf: {e}")

if args.omf:
    try:
        shutil.copy(os.path.join(current_dir, 'omf', 'init.fish'), omf_init_dir)
        print(f"init.fish has been copied to {omf_init_dir}")
    except Exception as e:
        print(f"An error occurred while copying init.fish: {e}")

if args.rime:
    try:
        shutil.copytree(os.path.join(current_dir, 'rime'), rime_dir)
        print(f"rime has been copied to {rime_dir}")
    except Exception as e:
        print(f"An error occurred while copying rime: {e}")