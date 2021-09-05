# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:


# # YAML
# - The Dagger 'Narthanc'
# - The Dagger 'Nimthanc'
# - The Dagger 'Dethanc'
#
# # Python
# ["The Dagger 'Narthanc'", "The Dagger 'Nimthanc'", "The Dagger 'Dethanc'"]


# # YAML
# -
#   - HTML
#   - LaTeX
#   - SGML
#   - VRML
#   - XML
#   - YAML
# -
#   - BSD
#   - GNU Hurd
#   - Linux
#
# # Python
# [
#    ['HTML', 'LaTeX', 'SGML', 'VRML', 'XML', 'YAML'],
#    ['BSD', 'GNU Hurd', 'Linux']
# ]