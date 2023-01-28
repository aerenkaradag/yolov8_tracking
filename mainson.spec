# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(5000)

block_cipher = None

added_files = [
         ( 'yolov5s.pt', '.' ),
         ( 'creds.json', '.' )
         ]

a = Analysis(['mainson.py'],
             pathex=['C:\\Users\ali_e\AppData\Local\Programs\Python\Python39\libs', 'C:\\Users\ali_e\AppData\Local\Programs\Python\Python39\Lib', 'C:\\Users\ali_e\AppData\Local\Programs\Python\Python39\Lib\site-packages', 'D:\\EyediusSayma-v2'],
             binaries=[],
             datas=[
             (".\\creds.json","."),
             (".\\mainson.ui",".")
             ],
             hiddenimports=['PyQt5.QtWidgets', 'PyQt5.QtCore', 'tqdm', 'pyyaml', 'matplotlib', 'seaborn', 'scipy', 'tensorflow', 'numba', 'google-cloud-core'],
             hookspath=['./core', './data', './utils', './models', './easydict', './filterpy', './weights', './runs'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Eyedius Say',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon = "loader-logo.ico")
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Eyedius Say')
