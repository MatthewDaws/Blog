---
layout: post
title: Overleaf and Git
latex
---

More of a note to myself than anything else.  Lancaster University has recently obtained a uni-wide <a href="https://www.overleaf.com/">Overleaf</a> license.  Overleaf is of course the online LaTeX editing system (as an aside, I didn't realise until now that the underlying web-app is <a href="https://github.com/overleaf/">Open Source</a>).  I haven't used Overleaf much, as I don't like the idea of needing a stable internet connection to work on my LaTeX files, and have a reasonable system going with MikTeX and VSCode with the LaTeX plugin.

One advantage, however, is collaboration, especially as I can't convince collaborators to work with GitHub.  The license is needed to have more than one collaborator, but it also gets you Git integration.  Basically, the Overleaf project will act as a Git repository which you can push/pull from (but not _branch_; still, if I get a collaborator who is up for using branches, then (a) we can just use GitHub; and (b) I need to worry about why my Mathematics article is some complex...)

<!--more-->

Some notes to self:

- <a href="https://www.overleaf.com/learn/how-to/Git_integration">Git Integration</a> docs
- I use an auth token.  On my personal computers, I seem to have configured Git for Windows to store passwords / tokens, and nothing needs to be done after the first clone.
- On my work laptop, I seem to need to run `git credential-manager-core configure` in the cloned directory.  Then things will work as expected.
- For a new project, now setup a suitable `.gitignore` file and commit it.
- You can also sync to Github.  Make a new, empty repository on Github, and then use `git remote add github <url>` where `github` is an arbitrary name for this remote, and `<url>` points to the repository on github.  You can now pull and push via `git push github` and `git pull github master`, the later manually specifying the branch on the Github repository to push to.

Thus, at least in principle, I can now work just on Github, occasionally pushing back to Overleaf.  Even better

- Running `git branch -u github/master master` now makes git track the Github repository, and `git pull` and `git push` now use Github, ignoring Overleaf.
- `git push origin` will update to Overleaf.
- `git pull origin master` will pull from Overleaf.

