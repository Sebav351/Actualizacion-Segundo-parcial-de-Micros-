from pathlib import Path
import shutil

src = Path('C:/Users/User/Downloads/minitanque_documentacion')
dst = Path('C:/Users/User/Downloads/minitanque_entrega')
dst.mkdir(exist_ok=True)
shutil.copytree(src, dst, dirs_exist_ok=True)
print('copied', dst.exists(), len(list(dst.iterdir())))
