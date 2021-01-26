---
layout: post
title: TileMapBase
latex
---

Another release of [TileMapBase](https://github.com/MatthewDaws/TileMapBase) which fix some warnings which had started to be been displayed, because of changing APIs in some libraries which we use.  I also had some minor corrections to docstrings.  Released on PyPI.

A quick further retrospective.  Do I enjoy writing code?  Yes, still.  Do I enjoying fighting with the tools to get things to work?  No, not in the slightest.  Below are some notes to self for how I got various libraries installed.

<!--more-->

I couldn't get `conda` to install much for me, even after uninstalling Anaconda, downloading the most recent version, and reinstalling.
Instead, I installed it manually, using some of the binary builds available (still!) from [Christoph Gohlke's page](https://www.lfd.uci.edu/~gohlke/pythonlibs):

- Install [GDAL](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal).  I had to use the _exact_ version which Fiona wanted (so if the next step
doesn't work, see if it's because the wrong version of GDAL was installed).
- Install [Fiona](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona).  These can both be down by downloading the correct `.whl` file, and then
running `pip install file.whl`
- Finally run `pip install geopandas`.

I dimly recall that to get GDAL working properly, you might need to fiddle with `path` variables etc.  However, for the minimal usage I needed,
the above was enough.


## More problems

In another project, having updated Anaconda for the above work, I now faced the following error, when trying to use [strictyaml](https://pypi.org/project/strictyaml/):

    ModuleNotFoundError: No module named 'ruamel'

A massive battle then commenced.  I updated using `conda`:

    conda update --all

Apart from taking forever, this did nothing.  I tried to get pip to update, but even using:

    python -m pip install --upgrade pip

(You can't use the `pip` command to upgrade itself, as then, in the background, `pip.exe` will be running and hence cannot be overwritten.) didn't work.  Whatever.

Maybe the [ruamel.yaml](https://pypi.org/project/ruamel.yaml/) package is out of date?  Running

    python -m pip install ruamel.yaml -U

gave an error message that `pip` couldn't remove the old install.  Poking around the Anaconda file system and deleting any files related to `ruamel` in `Lib\site-packages`, and then running `pip` again, and success!  Everything now works.

I should say that when I used [WinPython](https://winpython.github.io/) instead, "it just worked".  Maybe it's time to move on from Anaconda...
