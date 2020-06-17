---
layout: post
title: Stalled work
latex
---

Cleaning out my desk, I came across some plans for further work on [predictive policing](https://matthewdaws.github.io/comp.html#ds).  It now seems rather unlikely I will have time to pursue these (what with a fixed number of hours in a day, and a desire to be a research in Mathematics, at least at the moment).  I thought I might as well record the ideas here.

<!--more-->

### Patrol plans

The goal of the original research project was to write open source implementations of various [predictive policing](https://en.wikipedia.org/wiki/Predictive_policing) algorithms.  I was only interested in time and space predictions of (relative risk of) crime: e.g. "this area of a city is more likely to suffer burglaries in the next few days".  If such predictions are to be made use of, then they probably inform police "patrol plans" (which is my understanding of how they have been used in trials in the UK).

The follow-on research idea is to look at predictions thru the lense of producing useful patrol plans.  For example, if a prediction is incredibly finely grained, perhaps flagging up 100s of small areas to be at risk, then it might score well on a some metric on "prediction", but be useless for planning patrols: police forces do not have the resources to make a visible police presence around 100s of disparate areas.

- What are some good "usability" metrics?  There is some literature on this.
- Are there some algorithms for producing patrol plans out of predictions?
- Does the prediction actually matter that much, once a patrol plan has been produced?  (In an extreme case, maybe a police force only have resources to, each day, prioritise 3, 5, 10 (??) general areas.  If we are only highlighting 3 areas to patrol, does the prediction matter that much?)

Some [hand-written notes](public/patrol_plans_plan.pdf) of further ideas.


### KDEs on a network

This project is more mathematical (though applied statistics).  There is interest in performing various geospatial analysis on networks, instead of, for example, using a grid overlaid on a city.  By a network, I mean both a mathematical "graph" (almost always with distances, often embedding into the plane) and the real-world notion of a "street network" or a "road network", with the former obviously being a good model of the latter.

As far as modelling crime goes, there is probably still some work to be done on how to accurately model "informal networks".  By this, I mean unofficial paths across common land, or a broken fence which people cross over.  This means that _only_ knowing the road network is not enough to model how people really move around a city (especially if said people are moving on foot, and trying not to be detected).

In particular, I was interested in [Kernel density estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation) on a network, which I'll take to mean a connected graph embedded into the plane, with the induced distance metric.  A couple of relevant papers are:

- "A kernel density estimation method for networks, its computational method and a GIS-based tool" [Okabe, Satoh, Sugihara](https://doi.org/10.1080/13658810802475491).  Some [hand-written notes](public/okabe_comments.pdf) with some criticisms of their method.
- "Kernel Density Estimation on a Linear Network" [McSwiggan, Baddeley, Nair](https://doi.org/10.1111/sjos.12255).  I don't have any notes.
- Would need to do a further literature review.

[Some more hand-written notes](public/kde_plans.pdf) on plans.  I think a key thing here would be to have some application in mind (which need not be policing, and could be a little artificial) in order to illustrate what existing methods do well, and not so well.  Also, writing some decent software would be useful.
