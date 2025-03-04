# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Magiskpatcher.py'],
    pathex=[],
    binaries=[],
    datas=[('bin/logo.png', 'bin'), 
           ('bin/logo.ico', 'bin'),
           ('bin/wechat.png', 'bin'), 
           ('bin/alipay.png', 'bin'), 
           ('bin/zfbhb.png', 'bin'), 
           ('bin/get_config.sh', 'bin'),
           ('bin/windows/x86_64/magiskboot.exe', 'bin/windows/x86_64'),
           ('bin/windows/x86_64/cygwin1.dll', 'bin/windows/x86_64'),
           ('bin/windows/x86_64/adb.exe', 'bin/windows/x86_64'),
           ('bin/windows/x86_64/AdbWinApi.dll', 'bin/windows/x86_64'),
           ('bin/windows/x86_64/AdbWinUsbApi.dll', 'bin/windows/x86_64'),
           ('gitmirrorlist.txt', './')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
splash = Splash(
    '.\\bin\\splash.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='Magiskpatcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['bin\\logo.ico'],
)
