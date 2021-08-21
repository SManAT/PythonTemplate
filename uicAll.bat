pyside6-uic src/ui_main.ui > ui_main.py
pyside6-uic src/ui_error.ui > ui_error.py
pyside6-uic src/ui_dialog.ui > ui_dialog.py

pyside6-rcc --compress 9 --compress-algo zlib --threshold 20 src/resources.qrc -o resources_rc.py