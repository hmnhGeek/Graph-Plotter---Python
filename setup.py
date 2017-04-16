import cx_Freeze

executables = [cx_Freeze.Executable('Graph Maker.py', icon = 'icon.ico')]

cx_Freeze.setup(
    name='Graph Maker',
    options={"build_exe": {"packages":["matplotlib", "FileDialog","math", "PIL.ImageTk", "PIL.Image", "Tkinter", "ttk", "matplotlib.backends.backend_tkagg", "matplotlib.figure", "matplotlib.animation"], "include_files":["abt.txt", "help.txt", "icon.ico", "m.jpg", "sampleData.txt"], 'excludes':['collections.abc']}},

    description="Graph Maker",
    executables = executables
    )
