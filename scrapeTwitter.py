def get_interactions(consumer_key, consumer_secret, access_token, access_token_secret):
    """
    Arguments are Twitter API credentials. To get them you can go here http://apps.twitter.com/.
    Saves pickled lists of tweet authors and users they mention, and a list of users considered.
    """
    from twarc import Twarc
    from tqdm import tqdm
    import pickle

    t = Twarc(consumer_key,
            consumer_secret,
            access_token,
            access_token_secret)

    list_ids = ["1335885096063295488",
                "1288082572195639296",
                "1287444819015618561",
                "1283739792702713856",
                "1081734288368898048",
                "910757441855459328",
                "193445218",
                "90205656",
                "85315110"]

    users = set([m['screen_name'] for lid in list_ids for m in t.list_members(lid)])

    users_to_exclude = ['premierleague',
                        'SpursOfficial',
                        'Arsenal',
                        'ManCity',
                        'sterling7',
                        'kylewalker2',
                        'HKane',
                        'benmendy23',
                        'dele_official',
                        'RobHolding95',
                        'm8arteta']

    [users.remove(u) for u in users_to_exclude]

    authors = []
    mentions = []

    for user in tqdm(users):
        tl = t.timeline(screen_name=user)
        tweets = [tt for tt in tl]
        m = [u['screen_name'] for tw in tweets for u in tw['entities']['user_mentions']]
        a = [user] * len(m)
        mentions.append(m)
        authors.append(a)

    flat_a = [item for sublist in authors for item in sublist]
    flat_m = [item for sublist in mentions for item in sublist]

    pickle.dump(flat_a, open('authors.p', 'wb'))
    pickle.dump(flat_m, open('mentions.p', 'wb'))
    pickle.dump(users, open('users.p', 'wb'))
