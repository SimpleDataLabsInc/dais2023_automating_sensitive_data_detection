from setuptools import setup, find_packages
setup(
    name = 'packaged_pipeline',
    version = '1.0',
    packages = find_packages(include = ('packaged_pipeline*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'cryptography', 'prophecy-libs==1.5.5'],
    entry_points = {
'console_scripts' : [
'main = packaged_pipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
