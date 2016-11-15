import shutil

shutil.move("{{cookiecutter.migration_script_name}}.py", "..")
shutil.rmtree("../{{cookiecutter.migration_script_name}}")
