#!/usr/bin/env python3
import re
import pandas as pd
import json
from nltk.tokenize import word_tokenize

def create_crypto_entity_dict(coingecko_path: str) -> dict:
    """
    returns dict of entities taken from raw coingecko list for quick entity lookup
    """
    coingecko_file = open(coingecko_path)
    coingecko = json.load(coingecko_file)
    cg_lookup = {}
    for i in coingecko:
        cg_lookup[i["name"].lower()] = "(?<!\$)\\b" + i["name"].lower() + "\\b"
        cg_lookup["$" + i["symbol"].lower()] = "\\B\$" + i["symbol"].lower() + "\\b"

    return cg_lookup

def preprocess_tweet(tweet: str):
    """
    remove hash and @ tags.
    replace &amp; with and
    """

def format_to_pyabsa(csv_path: str):
    """
    takes csv, outputs .tsv in pyabsa format
    using mask_entities function
    """

def mask_entities(tweet: str, cg_lookup: dict, not_entities: list) -> dict:
    """
    takes tweet and entity-dictionary
    replaces crypto entity with '$T$'
    returns dict with {masked_tweet: entity} entries
    """
    masked_tweets = {}
    for entity, pattern in cg_lookup.items():
        if entity not in not_entities:
            tweet_new = re.sub(pattern, "$T$", tweet)
            if tweet_new != tweet:
                masked_tweets[tweet_new] = entity

    return masked_tweets

def filter_unwanted_tweets(df: pd.DataFrame) -> pd.DataFrame:
    """
    remove tweets with spam-indicating words and tag-spam
    """

    df = df[~df["text"].str.contains('|'.join(spamwords), na=False)]
    df = df[df["text"].str.count("\$") < 5]
    df = df[df["text"].str.count("@") < 3]
    df = df[df["text"].str.count("#") < 4]
    preprocessed = df['text'].replace(r'http\S+|•', ' ', regex=True)
    preprocessed = preprocessed.replace(r'&amp;', 'and', regex=True)
    preprocessed = preprocessed.replace(r'\n', ' ', regex=True)
    preprocessed = preprocessed.replace(r'\s{2,}', ' ', regex=True)

    #preprocessed = preprocessed.apply(lambda tweet: twt.tokenize(tweet) if type(tweet) == str else "")
    #preprocessed = preprocessed.apply(lambda tweet: [word for word in tweet if word not in (stop)])
    df["PreprocessedTweetText"] = preprocessed
    return df



if __name__ == "__main__":

    not_entities = ["ark", "ren", "gas", "dai", "tor", "jet", "solve", "chain", "link", "just", "ftx",
                    "share", "amp", "compound", "spookyswap", "request"] #some token names set off false positives. cashtag is enough

    spamwords  = ["giveaway", "whitelist", "#lunarcrush", "keys of the house or car", "#hitbtc",
                  "altrank", "galaxy score", "scan results", "new market pair", "@deg_ape",
                  "#solanaairdrop", "chatroom", "signals", "social engagement", "strongest movers",
                  "top 5 mentions", "@diamond_boots", "choocolatier", "#stakely"] #wie kann ich die liste finessen?

    csv_path = "./data/crypto-twitter/manual_labelling_twitter.csv"
    coingecko_path = "./data/coingecko_list.json"

    cg_lookup = create_crypto_entity_dict(coingecko_path)
    df = pd.read_csv(csv_path)
    df_filterclean = filter_unwanted_tweets(df)

    print(len(df))
    print(len(df_filterclean))

    row = df.iloc[323]
    tweet = row.text
    masked_tweets = mask_entities(tweet, cg_lookup, not_entities)
    printdf = df["text"]
    #print(df_filterclean["PreprocessedTweetText"].to_markdown())
