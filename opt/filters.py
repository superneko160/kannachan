import re
import json

# NGワードリスト作成
with open('opt/ng_word.json', 'r') as file:
    ng_words = json.load(file)

# @マーク（リプライ）とhttp（リンクと画像）以外の文章だけを抽出
def filter_links(text):
    replyMatch = re.compile(r"@\w+")
    urlMatch = re.compile(r"https?://")
    if replyMatch.search(text) or urlMatch.search(text):
        return False
    return True

# 単語のNGワード箇所のみ除去
def filter_ngwords(text):
    for ng_word in ng_words:
        text = text.replace(ng_word, '')
    return text