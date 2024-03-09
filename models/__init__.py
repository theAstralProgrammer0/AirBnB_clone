"""This package defines all module variables in
the models' package and reloads the objects
dictionary from a JSON file
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
