"""TEST_LUFile.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     TEST_LUFile_pathlib.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import datetime
import pathlib

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import lyrpy.LUFile as LUFile
import lyrpy.LUos as LUos
import lyrpy.LUErrors as LUErrors
from lyrpy.LUDoc import *

def TEST_LUFile_pathlib ():
    """TEST_LUFile_pathlib"""
#beginfunction
    PrintInfoObject('---------TEST_LUFile_pathlib----------')
    PrintInfoObject(TEST_LUFile_pathlib)
    PrintInfoObject(LUFile)
#endfunction

#-------------------------------------------------------------------------------
# TEST_pathlib
#-------------------------------------------------------------------------------
def TEST_pathlib ():
    """TEST_pathlib"""
#beginfunction
    #Finding Files in the Current Directory
    # list_dirs.py
    here = pathlib.Path (".")
    files = here.glob ("*")
    for item in files:
        print (item)
    #endfor

    #Searching for Files Recursively in Python
    # list_dirs_recursive.py
    here = pathlib.Path (".")
    files = here.glob ("**/*")
    for item in files:
        print (item)
    #endfor

    #Finding a Single File Recursively
    # find_file.py
    here = pathlib.Path (".")
    files = here.glob ("**/something.txt")
    for item in files:
        print (item)

    #Finding an Absolute Path
    """Display some known relative and absolute paths"""
    here = pathlib.Path (".")
    file_path = Path ("my_subdirectory/something.txt")
    print (f"The absolute path to {here} is {here.resolve ()}")
    print (f"The absolute path to {file_path} is {file_path.resolve ()}")
    # Output:
    # The absolute path to . is /Users/johnlockwood/paths-demo
    # The absolute path to my_subdirectory/something.txt is /Users/johnlockwood/paths-demo/my_subdirectory/something.txt

    #Getting the Directory of the Currently Executing File
    # print_path.py
    print (__file__)
    # Output:
    # /Users/johnlockwood/paths-demo/print_path.py

    # print_directory.py
    file_path = pathlib.Path(__file__)
    print(f"The file {file_path.name} is located in directory {file_path.parent}.")
    # Output:
    # The file print_directory.py is located in directory /Users/johnlockwood/paths-demo.

    #Creating a File In the Same Directory As a Python File
    output_path = pathlib.Path (__file__).parent/"output.txt"

    #Working with Files and Directories

    """Display the current and parent directory"""
    here = pathlib.Path (".").resolve ()
    print (f"You are here: {here}, a sub-directory of {here.parent}.")
    # output:
    # You are here: /Users/johnlockwood/paths-demo, a sub - directory of/Users/ johnlockwood.

    #Recursively Listing Files and Directories in Python:
    """Recursively list files and directories"""
    here = pathlib.Path (".")
    for path in sorted (here.glob ("**/*")):
        path_type = "?"
        if path.is_file ():
            path_type = "F"
        elif path.is_dir ():
            path_type = "D"
        print (f"{path_type} {path}")

    #Finding Other Files and Directories

    #Get the User’s Home Directory in Python
    """Display the user's home directory"""
    print (pathlib.Path.home ())

    #Getting the Current Working Directory
    default = pathlibPath.home ()/".aws"
    print (default.exists ())

    #Creating a Directory in the User Home Directory in Python
    """Creates a .codesolid directory in the user's home directory"""
    DIRECTORY_NAME = ".codesolid"
    config_directory = pathlib.Path.home () / DIRECTORY_NAME
    if not config_directory.exists ():
        config_directory.mkdir ()
        print (f"Directory {config_directory} created.")
    else:
        print (f"Directory {config_directory} already exists, skipping.")

    #Finding Python Module Paths and Files

    #Exploring the PYTHONPATH and sys.path Variables
    # $ export PYTHONPATH=/Users/johnlockwood/source/CodeSolid
    # $ python
    # ...
    # >>> import os
    # >>> os.environ ["PYTHONPATH"]
    # '/Users/johnlockwood/source/CodeSolid'

    #>>> import sys
    # >>> sys.path
    # ['', '/Users/johnlockwood/source/CodeSolid', '/Users/johnlockwood/.pyenv/versions/3.11.0a6/lib/python311.zip', '/Users/johnlockwood/.pyenv/versions/3.11.0a6/lib/python3.11', '/Users/johnlockwood/.pyenv/versions/3.11.0a6/lib/python3.11/lib-dynload', '/Users/johnlockwood/.pyenv/versions/3.11.0a6/lib/python3.11/site-packages']

    #Finding the Filename from Which a Python Module Was Loaded
    # >>> import json
    # >>> json.__file__
    # '/Users/johnlockwood/.pyenv/versions/3.11.0a6/lib/python3.11/json/__init__.py'

    """Shows how find_spec can sometimes be used to get a file load location path"""
    from importlib.util import find_spec
    for module in ['os', 'json', 'module.file_in_module']:
        spec = find_spec (module)
        print (f"{module} origin: {spec.origin}")
    #Sample output:
    # os origin: frozen
    # json origin: /Users/johnlockwood/.pyenv/versions/3.11.0a6/lib/python3.11/json/__init__.py
    # module.file_in_module origin: /Users/johnlockwood/paths-demo/module/file_in_module.py

    #pathlib — Object-oriented filesystem paths

    #Basic use

    #Importing the main class:

    # >>>
    # from pathlib import Path
    # Listing subdirectories:
    #
    # >>>
    # p = Path('.')
    # [x for x in p.iterdir() if x.is_dir()]
    # [PosixPath('.hg'), PosixPath('docs'), PosixPath('dist'),
    #  PosixPath('__pycache__'), PosixPath('build')]
    # Listing Python source files in this directory tree:
    #
    # >>>
    # list(p.glob('**/*.py'))
    # [PosixPath('test_pathlib.py'), PosixPath('setup.py'),
    #  PosixPath('pathlib.py'), PosixPath('docs/conf.py'),
    #  PosixPath('build/lib/pathlib.py')]
    # Navigating inside a directory tree:
    #
    # >>>
    # p = Path('/etc')
    # q = p / 'init.d' / 'reboot'
    # q
    # PosixPath('/etc/init.d/reboot')
    # q.resolve()
    # PosixPath('/etc/rc.d/init.d/halt')
    # Querying path properties:
    #
    # >>>
    # q.exists()
    # True
    # q.is_dir()
    # False
    # Opening a file:
    #
    # >>>
    # with q.open() as f: f.readline()
    #
    # '#!/bin/bash\n'

    #Pure paths

    #---------------------------------------------------------------------------
    #class pathlib.PurePath(*pathsegments)
    #---------------------------------------------------------------------------
    # A generic class that represents the system’s path flavour (instantiating it creates either a PurePosixPath or a PureWindowsPath):
    #
    # >>>
    # PurePath('setup.py')      # Running on a Unix machine
    # PurePosixPath('setup.py')
    # Each element of pathsegments can be either a string representing a path segment, or an object implementing the os.PathLike interface where the __fspath__() method returns a string, such as another path object:
    #
    # >>>
    # PurePath('foo', 'some/path', 'bar')
    # PurePosixPath('foo/some/path/bar')
    # PurePath(Path('foo'), Path('bar'))
    # PurePosixPath('foo/bar')
    # When pathsegments is empty, the current directory is assumed:
    #
    # >>>
    # PurePath()
    # PurePosixPath('.')
    # If a segment is an absolute path, all previous segments are ignored (like os.path.join()):
    #
    # >>>
    # PurePath('/etc', '/usr', 'lib64')
    # PurePosixPath('/usr/lib64')
    # PureWindowsPath('c:/Windows', 'd:bar')
    # PureWindowsPath('d:bar')
    # On Windows, the drive is not reset when a rooted relative path segment (e.g., r'\foo') is encountered:
    #
    # >>>
    # PureWindowsPath('c:/Windows', '/Program Files')
    # PureWindowsPath('c:/Program Files')
    # Spurious slashes and single dots are collapsed, but double dots ('..') and leading double slashes ('//') are not, since this would change the meaning of a path for various reasons (e.g. symbolic links, UNC paths):
    #
    # >>>
    # PurePath('foo//bar')
    # PurePosixPath('foo/bar')
    # PurePath('//foo/bar')
    # PurePosixPath('//foo/bar')
    # PurePath('foo/./bar')
    # PurePosixPath('foo/bar')
    # PurePath('foo/../bar')
    # PurePosixPath('foo/../bar')
    # (a naïve approach would make PurePosixPath('foo/../bar') equivalent to PurePosixPath('bar'), which is wrong if foo is a symbolic link to another directory)
    #
    # Pure path objects implement the os.PathLike interface, allowing them to be used anywhere the interface is accepted.

    #---------------------------------------------------------------------------
    #class pathlib.PurePosixPath(*pathsegments)¶
    #---------------------------------------------------------------------------
    # A subclass of PurePath, this path flavour represents non-Windows filesystem paths:
    #
    # >>>
    # PurePosixPath('/etc')
    # PurePosixPath('/etc')

    #---------------------------------------------------------------------------
    #class pathlib.PureWindowsPath(*pathsegments)
    #---------------------------------------------------------------------------
    # A subclass of PurePath, this path flavour represents Windows filesystem paths, including UNC paths:
    #
    # >>>
    # PureWindowsPath('c:/Program Files/')
    # PureWindowsPath('c:/Program Files')
    # PureWindowsPath('//server/share/file')
    # PureWindowsPath('//server/share/file')

    #---------------------------------------------------------------------------
    #General properties
    #---------------------------------------------------------------------------
    #Paths are immutable and hashable. Paths of a same flavour are comparable and orderable. These properties respect the flavour’s case-folding semantics:
    # >>>
    # PurePosixPath('foo') == PurePosixPath('FOO')
    # False
    # PureWindowsPath('foo') == PureWindowsPath('FOO')
    # True
    # PureWindowsPath('FOO') in { PureWindowsPath('foo') }
    # True
    # PureWindowsPath('C:') < PureWindowsPath('d:')
    # True
    # Paths of a different flavour compare unequal and cannot be ordered:
    #
    # >>>
    # PureWindowsPath('foo') == PurePosixPath('foo')
    # False
    # PureWindowsPath('foo') < PurePosixPath('foo')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: '<' not supported between instances of 'PureWindowsPath' and 'PurePosixPat

    #Operators

    #The slash operator helps create child paths, like os.path.join(). If the argument is an absolute path, the previous path is ignored. On Windows, the drive is not reset when the argument is a rooted relative path (e.g., r'\foo'):
    # >>>
    # p = PurePath('/etc')
    # p
    # PurePosixPath('/etc')
    # p / 'init.d' / 'apache2'
    # PurePosixPath('/etc/init.d/apache2')
    # q = PurePath('bin')
    # '/usr' / q
    # PurePosixPath('/usr/bin')
    # p / '/an_absolute_path'
    # PurePosixPath('/an_absolute_path')
    # PureWindowsPath('c:/Windows', '/Program Files')
    # PureWindowsPath('c:/Program Files')
    # A path object can be used anywhere an object implementing os.PathLike is accepted:
    #
    # >>>
    # import os
    # p = PurePath('/etc')
    # os.fspath(p)
    # '/etc'
    # The string representation of a path is the raw filesystem path itself (in native form, e.g. with backslashes under Windows), which you can pass to any function taking a file path as a string:
    #
    # >>>
    # p = PurePath('/etc')
    # str(p)
    # '/etc'
    # p = PureWindowsPath('c:/Program Files')
    # str(p)
    # 'c:\\Program Files'
    # Similarly, calling bytes on a path gives the raw filesystem path as a bytes object, as encoded by os.fsencode():
    #
    # >>>
    # bytes(p)
    # b'/etc'
    # Note Calling bytes is only recommended under Unix. Under Windows, the unicode form is the canonical representation of filesystem paths.

    #Accessing individual parts

    #To access the individual “parts” (components) of a path, use the following property:

    # PurePath.parts
    # A tuple giving access to the path’s various components:
    #
    # >>>
    # p = PurePath('/usr/bin/python3')
    # p.parts
    # ('/', 'usr', 'bin', 'python3')
    #
    # p = PureWindowsPath('c:/Program Files/PSF')
    # p.parts
    # ('c:\\', 'Program Files', 'PSF')

    #Methods and properties

    #Pure paths provide the following methods and properties:

    # PurePath.drive
    # A string representing the drive letter or name, if any:
    #
    # >>>
    # PureWindowsPath('c:/Program Files/').drive
    # 'c:'
    # PureWindowsPath('/Program Files/').drive
    # ''
    # PurePosixPath('/etc').drive
    # ''
    # UNC shares are also considered drives:
    #
    # >>>
    # PureWindowsPath('//host/share/foo.txt').drive
    # '\\\\host\\share'
    # PurePath.root
    # A string representing the (local or global) root, if any:
    #
    # >>>
    # PureWindowsPath('c:/Program Files/').root
    # '\\'
    # PureWindowsPath('c:Program Files/').root
    # ''
    # PurePosixPath('/etc').root
    # '/'
    # UNC shares always have a root:
    #
    # >>>
    # PureWindowsPath('//host/share').root
    # '\\'
    # If the path starts with more than two successive slashes, PurePosixPath collapses them:
    #
    # >>>
    # PurePosixPath('//etc').root
    # '//'
    # PurePosixPath('///etc').root
    # '/'
    # PurePosixPath('////etc').root
    # '/'
    # Note This behavior conforms to The Open Group Base Specifications Issue 6, paragraph 4.11 Pathname Resolution:
    # “A pathname that begins with two successive slashes may be interpreted in an implementation-defined manner, although more than two leading slashes shall be treated as a single slash.”
    #
    # PurePath.anchor
    # The concatenation of the drive and root:
    #
    # >>>
    # PureWindowsPath('c:/Program Files/').anchor
    # 'c:\\'
    # PureWindowsPath('c:Program Files/').anchor
    # 'c:'
    # PurePosixPath('/etc').anchor
    # '/'
    # PureWindowsPath('//host/share').anchor
    # '\\\\host\\share\\'
    # PurePath.parents
    # An immutable sequence providing access to the logical ancestors of the path:
    #
    # >>>
    # p = PureWindowsPath('c:/foo/bar/setup.py')
    # p.parents[0]
    # PureWindowsPath('c:/foo/bar')
    # p.parents[1]
    # PureWindowsPath('c:/foo')
    # p.parents[2]
    # PureWindowsPath('c:/')
    # Changed in version 3.10: The parents sequence now supports slices and negative index values.
    #
    # PurePath.parent
    # The logical parent of the path:
    #
    # >>>
    # p = PurePosixPath('/a/b/c/d')
    # p.parent
    # PurePosixPath('/a/b/c')
    # You cannot go past an anchor, or empty path:
    #
    # >>>
    # p = PurePosixPath('/')
    # p.parent
    # PurePosixPath('/')
    # p = PurePosixPath('.')
    # p.parent
    # PurePosixPath('.')
    # Note This is a purely lexical operation, hence the following behaviour:
    # >>>
    # p = PurePosixPath('foo/..')
    # p.parent
    # PurePosixPath('foo')
    # If you want to walk an arbitrary filesystem path upwards, it is recommended to first call Path.resolve() so as to resolve symlinks and eliminate ".." components.
    #
    # PurePath.name
    # A string representing the final path component, excluding the drive and root, if any:
    #
    # >>>
    # PurePosixPath('my/library/setup.py').name
    # 'setup.py'
    # UNC drive names are not considered:
    #
    # >>>
    # PureWindowsPath('//some/share/setup.py').name
    # 'setup.py'
    # PureWindowsPath('//some/share').name
    # ''
    # PurePath.suffix
    # The file extension of the final component, if any:
    #
    # >>>
    # PurePosixPath('my/library/setup.py').suffix
    # '.py'
    # PurePosixPath('my/library.tar.gz').suffix
    # '.gz'
    # PurePosixPath('my/library').suffix
    # ''
    # PurePath.suffixes
    # A list of the path’s file extensions:
    #
    # >>>
    # PurePosixPath('my/library.tar.gar').suffixes
    # ['.tar', '.gar']
    # PurePosixPath('my/library.tar.gz').suffixes
    # ['.tar', '.gz']
    # PurePosixPath('my/library').suffixes
    # []
    # PurePath.stem
    # The final path component, without its suffix:
    #
    # >>>
    # PurePosixPath('my/library.tar.gz').stem
    # 'library.tar'
    # PurePosixPath('my/library.tar').stem
    # 'library'
    # PurePosixPath('my/library').stem
    # 'library'
    # PurePath.as_posix()
    # Return a string representation of the path with forward slashes (/):
    #
    # >>>
    # p = PureWindowsPath('c:\\windows')
    # str(p)
    # 'c:\\windows'
    # p.as_posix()
    # 'c:/windows'
    # PurePath.as_uri()
    # Represent the path as a file URI. ValueError is raised if the path isn’t absolute.
    #
    # >>>
    # p = PurePosixPath('/etc/passwd')
    # p.as_uri()
    # 'file:///etc/passwd'
    # p = PureWindowsPath('c:/Windows')
    # p.as_uri()
    # 'file:///c:/Windows'
    # PurePath.is_absolute()
    # Return whether the path is absolute or not. A path is considered absolute if it has both a root and (if the flavour allows) a drive:
    #
    # >>>
    # PurePosixPath('/a/b').is_absolute()
    # True
    # PurePosixPath('a/b').is_absolute()
    # False
    #
    # PureWindowsPath('c:/a/b').is_absolute()
    # True
    # PureWindowsPath('/a/b').is_absolute()
    # False
    # PureWindowsPath('c:').is_absolute()
    # False
    # PureWindowsPath('//some/share').is_absolute()
    # True
    # PurePath.is_relative_to(other)
    # Return whether or not this path is relative to the other path.
    #
    # >>>
    # p = PurePath('/etc/passwd')
    # p.is_relative_to('/etc')
    # True
    # p.is_relative_to('/usr')
    # False
    # This method is string-based; it neither accesses the filesystem nor treats “..” segments specially. The following code is equivalent:
    #
    # >>>
    # u = PurePath('/usr')
    # u == p or u in p.parents
    # False
    # New in version 3.9.
    #
    # Deprecated since version 3.12, will be removed in version 3.14: Passing additional arguments is deprecated; if supplied, they are joined with other.
    #
    # PurePath.is_reserved()
    # With PureWindowsPath, return True if the path is considered reserved under Windows, False otherwise. With PurePosixPath, False is always returned.
    #
    # >>>
    # PureWindowsPath('nul').is_reserved()
    # True
    # PurePosixPath('nul').is_reserved()
    # False
    # File system calls on reserved paths can fail mysteriously or have unintended effects.
    #
    # PurePath.joinpath(*pathsegments)
    # Calling this method is equivalent to combining the path with each of the given pathsegments in turn:
    #
    # >>>
    # PurePosixPath('/etc').joinpath('passwd')
    # PurePosixPath('/etc/passwd')
    # PurePosixPath('/etc').joinpath(PurePosixPath('passwd'))
    # PurePosixPath('/etc/passwd')
    # PurePosixPath('/etc').joinpath('init.d', 'apache2')
    # PurePosixPath('/etc/init.d/apache2')
    # PureWindowsPath('c:').joinpath('/Program Files')
    # PureWindowsPath('c:/Program Files')
    # PurePath.match(pattern, *, case_sensitive=None)
    # Match this path against the provided glob-style pattern. Return True if matching is successful, False otherwise.
    #
    # If pattern is relative, the path can be either relative or absolute, and matching is done from the right:
    #
    # >>>
    # PurePath('a/b.py').match('*.py')
    # True
    # PurePath('/a/b/c.py').match('b/*.py')
    # True
    # PurePath('/a/b/c.py').match('a/*.py')
    # False
    # If pattern is absolute, the path must be absolute, and the whole path must match:
    #
    # >>>
    # PurePath('/a.py').match('/*.py')
    # True
    # PurePath('a/b.py').match('/*.py')
    # False
    # The pattern may be another path object; this speeds up matching the same pattern against multiple files:
    #
    # >>>
    # pattern = PurePath('*.py')
    # PurePath('a/b.py').match(pattern)
    # True
    # Changed in version 3.12: Accepts an object implementing the os.PathLike interface.
    #
    # As with other methods, case-sensitivity follows platform defaults:
    #
    # >>>
    # PurePosixPath('b.py').match('*.PY')
    # False
    # PureWindowsPath('b.py').match('*.PY')
    # True
    # Set case_sensitive to True or False to override this behaviour.
    #
    # Changed in version 3.12: The case_sensitive parameter was added.
    #
    # PurePath.relative_to(other, walk_up=False)
    # Compute a version of this path relative to the path represented by other. If it’s impossible, ValueError is raised:
    #
    # >>>
    # p = PurePosixPath('/etc/passwd')
    # p.relative_to('/')
    # PurePosixPath('etc/passwd')
    # p.relative_to('/etc')
    # PurePosixPath('passwd')
    # p.relative_to('/usr')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File "pathlib.py", line 941, in relative_to
    #     raise ValueError(error_message.format(str(self), str(formatted)))
    # ValueError: '/etc/passwd' is not in the subpath of '/usr' OR one path is relative and the other is absolute.
    # When walk_up is False (the default), the path must start with other. When the argument is True, .. entries may be added to form the relative path. In all other cases, such as the paths referencing different drives, ValueError is raised.:
    #
    # >>>
    # p.relative_to('/usr', walk_up=True)
    # PurePosixPath('../etc/passwd')
    # p.relative_to('foo', walk_up=True)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File "pathlib.py", line 941, in relative_to
    #     raise ValueError(error_message.format(str(self), str(formatted)))
    # ValueError: '/etc/passwd' is not on the same drive as 'foo' OR one path is relative and the other is absolute.
    # Warning This function is part of PurePath and works with strings. It does not check or access the underlying file structure. This can impact the walk_up option as it assumes that no symlinks are present in the path; call resolve() first if necessary to resolve symlinks.
    # Changed in version 3.12: The walk_up parameter was added (old behavior is the same as walk_up=False).
    #
    # Deprecated since version 3.12, will be removed in version 3.14: Passing additional positional arguments is deprecated; if supplied, they are joined with other.
    #
    # PurePath.with_name(name)
    # Return a new path with the name changed. If the original path doesn’t have a name, ValueError is raised:
    #
    # >>>
    # p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    # p.with_name('setup.py')
    # PureWindowsPath('c:/Downloads/setup.py')
    # p = PureWindowsPath('c:/')
    # p.with_name('setup.py')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File "/home/antoine/cpython/default/Lib/pathlib.py", line 751, in with_name
    #     raise ValueError("%r has an empty name" % (self,))
    # ValueError: PureWindowsPath('c:/') has an empty name
    # PurePath.with_stem(stem)
    # Return a new path with the stem changed. If the original path doesn’t have a name, ValueError is raised:
    #
    # >>>
    # p = PureWindowsPath('c:/Downloads/draft.txt')
    # p.with_stem('final')
    # PureWindowsPath('c:/Downloads/final.txt')
    # p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    # p.with_stem('lib')
    # PureWindowsPath('c:/Downloads/lib.gz')
    # p = PureWindowsPath('c:/')
    # p.with_stem('')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File "/home/antoine/cpython/default/Lib/pathlib.py", line 861, in with_stem
    #     return self.with_name(stem + self.suffix)
    #   File "/home/antoine/cpython/default/Lib/pathlib.py", line 851, in with_name
    #     raise ValueError("%r has an empty name" % (self,))
    # ValueError: PureWindowsPath('c:/') has an empty name
    # New in version 3.9.
    #
    # PurePath.with_suffix(suffix)
    # Return a new path with the suffix changed. If the original path doesn’t have a suffix, the new suffix is appended instead. If the suffix is an empty string, the original suffix is removed:
    #
    # >>>
    # p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    # p.with_suffix('.bz2')
    # PureWindowsPath('c:/Downloads/pathlib.tar.bz2')
    # p = PureWindowsPath('README')
    # p.with_suffix('.txt')
    # PureWindowsPath('README.txt')
    # p = PureWindowsPath('README.txt')
    # p.with_suffix('')
    # PureWindowsPath('README')
    # PurePath.with_segments(*pathsegments)
    # Create a new path object of the same type by combining the given pathsegments. This method is called whenever a derivative path is created, such as from parent and relative_to(). Subclasses may override this method to pass information to derivative paths, for example:
    #
    # from pathlib import PurePosixPath
    #
    # class MyPath(PurePosixPath):
    #     def __init__(self, *pathsegments, session_id):
    #         super().__init__(*pathsegments)
    #         self.session_id = session_id
    #
    #     def with_segments(self, *pathsegments):
    #         return type(self)(*pathsegments, session_id=self.session_id)
    #
    # etc = MyPath('/etc', session_id=42)
    # hosts = etc / 'hosts'
    # print(hosts.session_id)  # 42
    # New in version 3.12.
    #
    # Concrete paths
    # Concrete paths are subclasses of the pure path classes. In addition to operations provided by the latter, they also provide methods to do system calls on path objects. There are three ways to instantiate concrete paths:
    #
    # class pathlib.Path(*pathsegments)
    # A subclass of PurePath, this class represents concrete paths of the system’s path flavour (instantiating it creates either a PosixPath or a WindowsPath):
    #
    # >>>
    # Path('setup.py')
    # PosixPath('setup.py')
    # pathsegments is specified similarly to PurePath.
    #
    # class pathlib.PosixPath(*pathsegments)
    # A subclass of Path and PurePosixPath, this class represents concrete non-Windows filesystem paths:
    #
    # >>>
    # PosixPath('/etc')
    # PosixPath('/etc')
    # pathsegments is specified similarly to PurePath.
    #
    # class pathlib.WindowsPath(*pathsegments)
    # A subclass of Path and PureWindowsPath, this class represents concrete Windows filesystem paths:
    #
    # >>>
    # WindowsPath('c:/Program Files/')
    # WindowsPath('c:/Program Files')
    # pathsegments is specified similarly to PurePath.
    #
    # You can only instantiate the class flavour that corresponds to your system (allowing system calls on non-compatible path flavours could lead to bugs or failures in your application):
    #
    # >>>
    # import os
    # os.name
    # 'posix'
    # Path('setup.py')
    # PosixPath('setup.py')
    # PosixPath('setup.py')
    # PosixPath('setup.py')
    # WindowsPath('setup.py')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File "pathlib.py", line 798, in __new__
    #     % (cls.__name__,))
    # NotImplementedError: cannot instantiate 'WindowsPath' on your system
    # Methods
    # Concrete paths provide the following methods in addition to pure paths methods. Many of these methods can raise an OSError if a system call fails (for example because the path doesn’t exist).
    #
    # Changed in version 3.8: exists(), is_dir(), is_file(), is_mount(), is_symlink(), is_block_device(), is_char_device(), is_fifo(), is_socket() now return False instead of raising an exception for paths that contain characters unrepresentable at the OS level.
    #
    # classmethod Path.cwd()
    # Return a new path object representing the current directory (as returned by os.getcwd()):
    #
    # >>>
    # Path.cwd()
    # PosixPath('/home/antoine/pathlib')
    # classmethod Path.home()
    # Return a new path object representing the user’s home directory (as returned by os.path.expanduser() with ~ construct). If the home directory can’t be resolved, RuntimeError is raised.
    #
    # >>>
    # Path.home()
    # PosixPath('/home/antoine')
    # New in version 3.5.
    #
    # Path.stat(*, follow_symlinks=True)
    # Return a os.stat_result object containing information about this path, like os.stat(). The result is looked up at each call to this method.
    #
    # This method normally follows symlinks; to stat a symlink add the argument follow_symlinks=False, or use lstat().
    #
    # >>>
    # p = Path('setup.py')
    # p.stat().st_size
    # 956
    # p.stat().st_mtime
    # 1327883547.852554
    # Changed in version 3.10: The follow_symlinks parameter was added.
    #
    # Path.chmod(mode, *, follow_symlinks=True)
    # Change the file mode and permissions, like os.chmod().
    #
    # This method normally follows symlinks. Some Unix flavours support changing permissions on the symlink itself; on these platforms you may add the argument follow_symlinks=False, or use lchmod().
    #
    # >>>
    # p = Path('setup.py')
    # p.stat().st_mode
    # 33277
    # p.chmod(0o444)
    # p.stat().st_mode
    # 33060
    # Changed in version 3.10: The follow_symlinks parameter was added.
    #
    # Path.exists(*, follow_symlinks=True)
    # Return True if the path points to an existing file or directory.
    #
    # This method normally follows symlinks; to check if a symlink exists, add the argument follow_symlinks=False.
    #
    # >>>
    # Path('.').exists()
    # True
    # Path('setup.py').exists()
    # True
    # Path('/etc').exists()
    # True
    # Path('nonexistentfile').exists()
    # False
    # Changed in version 3.12: The follow_symlinks parameter was added.
    #
    # Path.expanduser()
    # Return a new path with expanded ~ and ~user constructs, as returned by os.path.expanduser(). If a home directory can’t be resolved, RuntimeError is raised.
    #
    # >>>
    # p = PosixPath('~/films/Monty Python')
    # p.expanduser()
    # PosixPath('/home/eric/films/Monty Python')
    # New in version 3.5.
    #
    # Path.glob(pattern, *, case_sensitive=None)
    # Glob the given relative pattern in the directory represented by this path, yielding all matching files (of any kind):
    #
    # >>>
    # sorted(Path('.').glob('*.py'))
    # [PosixPath('pathlib.py'), PosixPath('setup.py'), PosixPath('test_pathlib.py')]
    # sorted(Path('.').glob('*/*.py'))
    # [PosixPath('docs/conf.py')]
    # Patterns are the same as for fnmatch, with the addition of “**” which means “this directory and all subdirectories, recursively”. In other words, it enables recursive globbing:
    #
    # >>>
    # sorted(Path('.').glob('**/*.py'))
    # [PosixPath('build/lib/pathlib.py'),
    #  PosixPath('docs/conf.py'),
    #  PosixPath('pathlib.py'),
    #  PosixPath('setup.py'),
    #  PosixPath('test_pathlib.py')]
    # This method calls Path.is_dir() on the top-level directory and propagates any OSError exception that is raised. Subsequent OSError exceptions from scanning directories are suppressed.
    #
    # By default, or when the case_sensitive keyword-only argument is set to None, this method matches paths using platform-specific casing rules: typically, case-sensitive on POSIX, and case-insensitive on Windows. Set case_sensitive to True or False to override this behaviour.
    #
    # Note Using the “**” pattern in large directory trees may consume an inordinate amount of time.
    # Raises an auditing event pathlib.Path.glob with arguments self, pattern.
    #
    # Changed in version 3.11: Return only directories if pattern ends with a pathname components separator (sep or altsep).
    #
    # Changed in version 3.12: The case_sensitive parameter was added.
    #
    # Path.group()
    # Return the name of the group owning the file. KeyError is raised if the file’s gid isn’t found in the system database.
    #
    # Path.is_dir()
    # Return True if the path points to a directory (or a symbolic link pointing to a directory), False if it points to another kind of file.
    #
    # False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.
    #
    # Path.is_file()
    # Return True if the path points to a regular file (or a symbolic link pointing to a regular file), False if it points to another kind of file.
    #
    # False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.
    #
    # Path.is_junction()
    # Return True if the path points to a junction, and False for any other type of file. Currently only Windows supports junctions.
    #
    # New in version 3.12.
    #
    # Path.is_mount()
    # Return True if the path is a mount point: a point in a file system where a different file system has been mounted. On POSIX, the function checks whether path’s parent, path/.., is on a different device than path, or whether path/.. and path point to the same i-node on the same device — this should detect mount points for all Unix and POSIX variants. On Windows, a mount point is considered to be a drive letter root (e.g. c:\), a UNC share (e.g. \\server\share), or a mounted filesystem directory.
    #
    # New in version 3.7.
    #
    # Changed in version 3.12: Windows support was added.
    #
    # Path.is_symlink()
    # Return True if the path points to a symbolic link, False otherwise.
    #
    # False is also returned if the path doesn’t exist; other errors (such as permission errors) are propagated.
    #
    # Path.is_socket()
    # Return True if the path points to a Unix socket (or a symbolic link pointing to a Unix socket), False if it points to another kind of file.
    #
    # False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.
    #
    # Path.is_fifo()
    # Return True if the path points to a FIFO (or a symbolic link pointing to a FIFO), False if it points to another kind of file.
    #
    # False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.
    #
    # Path.is_block_device()
    # Return True if the path points to a block device (or a symbolic link pointing to a block device), False if it points to another kind of file.
    #
    # False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.
    #
    # Path.is_char_device()
    # Return True if the path points to a character device (or a symbolic link pointing to a character device), False if it points to another kind of file.
    #
    # False is also returned if the path doesn’t exist or is a broken symlink; other errors (such as permission errors) are propagated.
    #
    # Path.iterdir()
    # When the path points to a directory, yield path objects of the directory contents:
    #
    # >>>
    # p = Path('docs')
    # for child in p.iterdir(): child
    #
    # PosixPath('docs/conf.py')
    # PosixPath('docs/_templates')
    # PosixPath('docs/make.bat')
    # PosixPath('docs/index.rst')
    # PosixPath('docs/_build')
    # PosixPath('docs/_static')
    # PosixPath('docs/Makefile')
    # The children are yielded in arbitrary order, and the special entries '.' and '..' are not included. If a file is removed from or added to the directory after creating the iterator, whether a path object for that file be included is unspecified.
    #
    # Path.walk(top_down=True, on_error=None, follow_symlinks=False)
    # Generate the file names in a directory tree by walking the tree either top-down or bottom-up.
    #
    # For each directory in the directory tree rooted at self (including self but excluding ‘.’ and ‘..’), the method yields a 3-tuple of (dirpath, dirnames, filenames).
    #
    # dirpath is a Path to the directory currently being walked, dirnames is a list of strings for the names of subdirectories in dirpath (excluding '.' and '..'), and filenames is a list of strings for the names of the non-directory files in dirpath. To get a full path (which begins with self) to a file or directory in dirpath, do dirpath / name. Whether or not the lists are sorted is file system-dependent.
    #
    # If the optional argument top_down is true (which is the default), the triple for a directory is generated before the triples for any of its subdirectories (directories are walked top-down). If top_down is false, the triple for a directory is generated after the triples for all of its subdirectories (directories are walked bottom-up). No matter the value of top_down, the list of subdirectories is retrieved before the triples for the directory and its subdirectories are walked.
    #
    # When top_down is true, the caller can modify the dirnames list in-place (for example, using del or slice assignment), and Path.walk() will only recurse into the subdirectories whose names remain in dirnames. This can be used to prune the search, or to impose a specific order of visiting, or even to inform Path.walk() about directories the caller creates or renames before it resumes Path.walk() again. Modifying dirnames when top_down is false has no effect on the behavior of Path.walk() since the directories in dirnames have already been generated by the time dirnames is yielded to the caller.
    #
    # By default, errors from os.scandir() are ignored. If the optional argument on_error is specified, it should be a callable; it will be called with one argument, an OSError instance. The callable can handle the error to continue the walk or re-raise it to stop the walk. Note that the filename is available as the filename attribute of the exception object.
    #
    # By default, Path.walk() does not follow symbolic links, and instead adds them to the filenames list. Set follow_symlinks to true to resolve symlinks and place them in dirnames and filenames as appropriate for their targets, and consequently visit directories pointed to by symlinks (where supported).
    #
    # Note Be aware that setting follow_symlinks to true can lead to infinite recursion if a link points to a parent directory of itself. Path.walk() does not keep track of the directories it has already visited.
    # Note Path.walk() assumes the directories it walks are not modified during execution. For example, if a directory from dirnames has been replaced with a symlink and follow_symlinks is false, Path.walk() will still try to descend into it. To prevent such behavior, remove directories from dirnames as appropriate.
    # Note Unlike os.walk(), Path.walk() lists symlinks to directories in filenames if follow_symlinks is false.
    # This example displays the number of bytes used by all files in each directory, while ignoring __pycache__ directories:
    #
    # from pathlib import Path
    # for root, dirs, files in Path("cpython/Lib/concurrent").walk(on_error=print):
    #   print(
    #       root,
    #       "consumes",
    #       sum((root / file).stat().st_size for file in files),
    #       "bytes in",
    #       len(files),
    #       "non-directory files"
    #   )
    #   if '__pycache__' in dirs:
    #         dirs.remove('__pycache__')
    # This next example is a simple implementation of shutil.rmtree(). Walking the tree bottom-up is essential as rmdir() doesn’t allow deleting a directory before it is empty:
    #
    # # Delete everything reachable from the directory "top".
    # # CAUTION:  This is dangerous! For example, if top == Path('/'),
    # # it could delete all of your files.
    # for root, dirs, files in top.walk(top_down=False):
    #     for name in files:
    #         (root / name).unlink()
    #     for name in dirs:
    #         (root / name).rmdir()
    # New in version 3.12.
    #
    # Path.lchmod(mode)
    # Like Path.chmod() but, if the path points to a symbolic link, the symbolic link’s mode is changed rather than its target’s.
    #
    # Path.lstat()
    # Like Path.stat() but, if the path points to a symbolic link, return the symbolic link’s information rather than its target’s.
    #
    # Path.mkdir(mode=0o777, parents=False, exist_ok=False)
    # Create a new directory at this given path. If mode is given, it is combined with the process’ umask value to determine the file mode and access flags. If the path already exists, FileExistsError is raised.
    #
    # If parents is true, any missing parents of this path are created as needed; they are created with the default permissions without taking mode into account (mimicking the POSIX mkdir -p command).
    #
    # If parents is false (the default), a missing parent raises FileNotFoundError.
    #
    # If exist_ok is false (the default), FileExistsError is raised if the target directory already exists.
    #
    # If exist_ok is true, FileExistsError will not be raised unless the given path already exists in the file system and is not a directory (same behavior as the POSIX mkdir -p command).
    #
    # Changed in version 3.5: The exist_ok parameter was added.
    #
    # Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
    # Open the file pointed to by the path, like the built-in open() function does:
    #
    # >>>
    # p = Path('setup.py')
    # with p.open() as f:
    #     f.readline()
    #
    # '#!/usr/bin/env python3\n'
    # Path.owner()
    # Return the name of the user owning the file. KeyError is raised if the file’s uid isn’t found in the system database.
    #
    # Path.read_bytes()
    # Return the binary contents of the pointed-to file as a bytes object:
    #
    # >>>
    # p = Path('my_binary_file')
    # p.write_bytes(b'Binary file contents')
    # 20
    # p.read_bytes()
    # b'Binary file contents'
    # New in version 3.5.
    #
    # Path.read_text(encoding=None, errors=None)
    # Return the decoded contents of the pointed-to file as a string:
    #
    # >>>
    # p = Path('my_text_file')
    # p.write_text('Text file contents')
    # 18
    # p.read_text()
    # 'Text file contents'
    # The file is opened and then closed. The optional parameters have the same meaning as in open().
    #
    # New in version 3.5.
    #
    # Path.readlink()
    # Return the path to which the symbolic link points (as returned by os.readlink()):
    #
    # >>>
    # p = Path('mylink')
    # p.symlink_to('setup.py')
    # p.readlink()
    # PosixPath('setup.py')
    # New in version 3.9.
    #
    # Path.rename(target)
    # Rename this file or directory to the given target, and return a new Path instance pointing to target. On Unix, if target exists and is a file, it will be replaced silently if the user has permission. On Windows, if target exists, FileExistsError will be raised. target can be either a string or another path object:
    #
    # >>>
    # p = Path('foo')
    # p.open('w').write('some text')
    # 9
    # target = Path('bar')
    # p.rename(target)
    # PosixPath('bar')
    # target.open().read()
    # 'some text'
    # The target path may be absolute or relative. Relative paths are interpreted relative to the current working directory, not the directory of the Path object.
    #
    # It is implemented in terms of os.rename() and gives the same guarantees.
    #
    # Changed in version 3.8: Added return value, return the new Path instance.
    #
    # Path.replace(target)
    # Rename this file or directory to the given target, and return a new Path instance pointing to target. If target points to an existing file or empty directory, it will be unconditionally replaced.
    #
    # The target path may be absolute or relative. Relative paths are interpreted relative to the current working directory, not the directory of the Path object.
    #
    # Changed in version 3.8: Added return value, return the new Path instance.
    #
    # Path.absolute()
    # Make the path absolute, without normalization or resolving symlinks. Returns a new path object:
    #
    # >>>
    # p = Path('tests')
    # p
    # PosixPath('tests')
    # p.absolute()
    # PosixPath('/home/antoine/pathlib/tests')
    # Path.resolve(strict=False)
    # Make the path absolute, resolving any symlinks. A new path object is returned:
    #
    # >>>
    # p = Path()
    # p
    # PosixPath('.')
    # p.resolve()
    # PosixPath('/home/antoine/pathlib')
    # “..” components are also eliminated (this is the only method to do so):
    #
    # >>>
    # p = Path('docs/../setup.py')
    # p.resolve()
    # PosixPath('/home/antoine/pathlib/setup.py')
    # If the path doesn’t exist and strict is True, FileNotFoundError is raised. If strict is False, the path is resolved as far as possible and any remainder is appended without checking whether it exists. If an infinite loop is encountered along the resolution path, RuntimeError is raised.
    #
    # Changed in version 3.6: The strict parameter was added (pre-3.6 behavior is strict).
    #
    # Path.rglob(pattern, *, case_sensitive=None)
    # Glob the given relative pattern recursively. This is like calling Path.glob() with “**/” added in front of the pattern, where patterns are the same as for fnmatch:
    #
    # >>>
    # sorted(Path().rglob("*.py"))
    # [PosixPath('build/lib/pathlib.py'),
    #  PosixPath('docs/conf.py'),
    #  PosixPath('pathlib.py'),
    #  PosixPath('setup.py'),
    #  PosixPath('test_pathlib.py')]
    # By default, or when the case_sensitive keyword-only argument is set to None, this method matches paths using platform-specific casing rules: typically, case-sensitive on POSIX, and case-insensitive on Windows. Set case_sensitive to True or False to override this behaviour.
    #
    # Raises an auditing event pathlib.Path.rglob with arguments self, pattern.
    #
    # Changed in version 3.11: Return only directories if pattern ends with a pathname components separator (sep or altsep).
    #
    # Changed in version 3.12: The case_sensitive parameter was added.
    #
    # Path.rmdir()
    # Remove this directory. The directory must be empty.
    #
    # Path.samefile(other_path)
    # Return whether this path points to the same file as other_path, which can be either a Path object, or a string. The semantics are similar to os.path.samefile() and os.path.samestat().
    #
    # An OSError can be raised if either file cannot be accessed for some reason.
    #
    # >>>
    # p = Path('spam')
    # q = Path('eggs')
    # p.samefile(q)
    # False
    # p.samefile('spam')
    # True
    # New in version 3.5.
    #
    # Path.symlink_to(target, target_is_directory=False)
    # Make this path a symbolic link pointing to target.
    #
    # On Windows, a symlink represents either a file or a directory, and does not morph to the target dynamically. If the target is present, the type of the symlink will be created to match. Otherwise, the symlink will be created as a directory if target_is_directory is True or a file symlink (the default) otherwise. On non-Windows platforms, target_is_directory is ignored.
    #
    # >>>
    # p = Path('mylink')
    # p.symlink_to('setup.py')
    # p.resolve()
    # PosixPath('/home/antoine/pathlib/setup.py')
    # p.stat().st_size
    # 956
    # p.lstat().st_size
    # 8
    # Note The order of arguments (link, target) is the reverse of os.symlink()’s.
    # Path.hardlink_to(target)
    # Make this path a hard link to the same file as target.
    #
    # Note The order of arguments (link, target) is the reverse of os.link()’s.
    # New in version 3.10.
    #
    # Path.touch(mode=0o666, exist_ok=True)
    # Create a file at this given path. If mode is given, it is combined with the process’ umask value to determine the file mode and access flags. If the file already exists, the function succeeds if exist_ok is true (and its modification time is updated to the current time), otherwise FileExistsError is raised.
    #
    # Path.unlink(missing_ok=False)
    # Remove this file or symbolic link. If the path points to a directory, use Path.rmdir() instead.
    #
    # If missing_ok is false (the default), FileNotFoundError is raised if the path does not exist.
    #
    # If missing_ok is true, FileNotFoundError exceptions will be ignored (same behavior as the POSIX rm -f command).
    #
    # Changed in version 3.8: The missing_ok parameter was added.
    #
    # Path.write_bytes(data)
    # Open the file pointed to in bytes mode, write data to it, and close the file:
    #
    # >>>
    # p = Path('my_binary_file')
    # p.write_bytes(b'Binary file contents')
    # 20
    # p.read_bytes()
    # b'Binary file contents'
    # An existing file of the same name is overwritten.
    #
    # New in version 3.5.
    #
    # Path.write_text(data, encoding=None, errors=None, newline=None)
    # Open the file pointed to in text mode, write data to it, and close the file:
    #
    # >>>
    # p = Path('my_text_file')
    # p.write_text('Text file contents')
    # 18
    # p.read_text()
    # 'Text file contents'
    # An existing file of the same name is overwritten. The optional parameters have the same meaning as in open().

    #Correspondence to tools in the os module
    #-----------------------------------------------------------------------------
    # os and os.path                      pathlib
    # -----------------------------------------------------------------------------
    # os.path.abspath()                   Path.absolute() [1]
    # os.path.realpath()                  Path.resolve()
    # os.chmod()                          Path.chmod()
    # os.mkdir()                          Path.mkdir()
    # os.makedirs()                       Path.mkdir()
    # os.rename()                         Path.rename()
    # os.replace()                        Path.replace()
    # os.rmdir()                          Path.rmdir()
    # os.remove(), os.unlink()            Path.unlink()
    # os.getcwd()                         Path.cwd()
    # os.path.exists()                    Path.exists()
    # os.path.expanduser()                Path.expanduser() and Path.home()
    # os.listdir()                        Path.iterdir()
    # os.walk()                           Path.walk()
    # os.path.isdir()                     Path.is_dir()
    # os.path.isfile()                    Path.is_file()
    # os.path.islink()                    Path.is_symlink()
    # os.link()                           Path.hardlink_to()
    # os.symlink()                        Path.symlink_to()
    # os.readlink()                       Path.readlink()
    # os.path.relpath()                   PurePath.relative_to() [2]
    # os.stat()                           Path.stat(), Path.owner(), Path.group()
    # os.path.isabs()                     PurePath.is_absolute()
    # os.path.join()                      PurePath.joinpath()
    # os.path.basename()                  PurePath.name
    # os.path.dirname()                   PurePath.parent
    # os.path.samefile()                  Path.samefile()
    # os.path.splitext()                  PurePath.stem and PurePath.suffix
#endfunction


#------------------------------------------
def main ():
#beginfunction
    # LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
    #                     'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\DESKTOP\Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    PrintInfoObject('-----main----')
    PrintInfoObject(main)
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
