from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('jogo.py', base=base, target_name = 'Vader Rush')
]

setup(name='Vader Rush',
      version = '1.0',
      description = 'Game',
      options = {'build_exe': build_options},
      executables = executables)
