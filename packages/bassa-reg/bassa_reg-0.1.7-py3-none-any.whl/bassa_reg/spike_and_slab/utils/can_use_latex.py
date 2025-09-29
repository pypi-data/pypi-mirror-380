import shutil

def can_use_latex():
    return all(shutil.which(cmd) for cmd in ["latex", "dvipng", "gs"])