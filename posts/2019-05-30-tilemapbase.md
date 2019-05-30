---
layout: post
title: TileMapBase
---

My little Python project [TileMapBase](https://github.com/MatthewDaws/TileMapBase) automates the process of downloading (and caching locally) map tiles from OpenStreetMap (and similar) and assembling these into the background for a [matplotkib](https://matplotlib.org/) plot.  I wrote this when working in Geographic Data Science and wanting to show longitude latitude locations on a map, inside of a Jupyter Notebook.

Anyway, recently OpenStreetMap started to enforce [User Agents](https://en.wikipedia.org/wiki/User_agent) in HTTP requests, which broke my package.  A [pull request later](https://github.com/MatthewDaws/TileMapBase/pull/10) and we're back on the road.

I have spent the last 12 months concentrating on Mathematics, and so am _very_ rusty.  It took me a couple of hours to update my Python distribution, get the tests fixed, get Travis building again, and remembering how to upload to PyPi.  And this is for a trivial change to a small package.  I now understand how Open Source Software becomes unmaintained...