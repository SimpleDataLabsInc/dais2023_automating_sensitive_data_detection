from setuptools import setup, find_packages
setup(
    name = 'Aggregate_Data_Pipeline',
    version = '1.0',
    packages = find_packages(include = ('aggregate_data_pipeline*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.5.5'],
    entry_points = {
'console_scripts' : [
'main = aggregate_data_pipeline.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
