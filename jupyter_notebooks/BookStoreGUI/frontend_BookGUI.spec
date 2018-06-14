# -*- mode: python -*-

block_cipher = None


a = Analysis(['frontend_BookGUI.py'],
             pathex=['/Users/vikas/learn/python_projects/jupyter_notebooks/BookStoreGUI'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='frontend_BookGUI',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='frontend_BookGUI.app',
             icon=None,
             bundle_identifier=None)
