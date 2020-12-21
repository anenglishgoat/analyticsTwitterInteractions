import pandas as pd
import pickle
import numpy as np
import networkx as nx
from scrapeTwitter import get_interactions

## If you want to obtain up-to-date pickle files, run
## get_interactions() first.

authors = pickle.load(open('authors.p', 'rb'))
mentions = pickle.load(open('mentions.p', 'rb'))
users = list(pickle.load(open('users.p', 'rb')))

tweet_df = pd.DataFrame(list(zip(authors, mentions)), columns=['author', 'to'])
tweet_df = tweet_df[tweet_df['author'].isin(users)]
tweet_df = tweet_df[tweet_df['to'].isin(users)]
tweet_df = tweet_df[tweet_df['author'] != tweet_df['to']]
tweet_df['weight'] = tweet_df.groupby(['author', 'to'])['author'].transform('size')

G = nx.from_pandas_edgelist(tweet_df, 'author', 'to', create_using=nx.DiGraph(), edge_attr='weight')

communities = nx.community.asyn_lpa_communities(G, seed=42)
modularity_dict = {} 
for i,c in enumerate(communities): 
    for name in c: 
        modularity_dict[name] = i 

nx.set_node_attributes(G, modularity_dict, 'modularity')

## get pagerank rankings

pr = nx.pagerank(G)
pagerank = pd.Series(pr).sort_values(ascending=False).to_frame()
pagerank.columns = ['PageRank']
node_df = pd.concat([pagerank,pd.Series(modularity_dict)],axis=1)
pagerank.reset_index(inplace=True)
pagerank.query("index == 'AnEnglishGoat'")
