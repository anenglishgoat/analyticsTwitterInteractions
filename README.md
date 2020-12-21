# analyticsTwitterInteractions
Python scripts to grab interactions between members of analytics twitter and a couple of adjacent communities (some Arsenal Twitter accounts and some FPL accounts).

The interaction data is stored in 3 pickled lists stored in `pickles.zip`.

If you extract `pickles.zip` to your working directory, you should be able to run `buildNetwork.py` to form a networkx graph and compute PageRank scores. Don't know if the gephi project will work on other people's machines, but you can try loading it and playing around.

You can use `get_interactions` in `scrapeTwitter.py` to generate your own pickled lists of authors, mentions and users. Beware, it takes about 4 hours to run.
