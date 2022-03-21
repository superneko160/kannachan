import kannachan
import twitterapi
import filters
import json
import random
import morphological_analysis

if __name__ == '__main__':
    # Twitterへのログイン
    client = twitterapi.get_twitterclient()
    if (client):
        # タイムラインの取得
        tweets = twitterapi.get_timeline(client)
       # @マーク（リプライ）とhttp（リンクと画像）以外の文章だけを抽出
        data = []
        for tweet in tweets:
            text = filters.filter_ngwords(tweet.text)
            if filters.filter_links(text):
                data.append(text)
       # 形態素解析を行い固有名詞だけを抽出
        nouns = morphological_analysis.get_propernounes(data)
       # カンナちゃんにしゃべらせる 
        word = nouns[int(random.uniform(0, len(nouns)))]
        template = json.load(open('opt/template.json', 'r'))
        twitterapi.tweet(client, kannachan.talk(word, template))
