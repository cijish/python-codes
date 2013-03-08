from distutils.core import setup
import py2exe

setup(
    windows = [
        {
            "script": "program.py",
            "icon_resources": [(1, "orange-block.ico")],
            "options":{"py2exe": {"bundle_files": 1,'compressed': True, }},
            "author":"Cijish Simon",
            "packages":["dir"],
            "version":"0.0.3",
            "name":"CompXLS",
            "description":"This application is indented to compare two exel files with specified column"
            
        }
    ],

)
