# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\GitRepos\\DbInstaller\\Python\\DbInstaller.py'],
             pathex=['D:\\GitRepos\\DbInstaller\\Python'],
             binaries=[],
             datas=[('sqls/drop_all_objects.sql_not_execute','sqls')],
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
          exclude_binaries=True,
          name='DbInstaller',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='DbInstaller')
