import MeCab

# 形態素解析を行い、すべての文章から固有名詞だけを抽出したリストを作成
def get_propernounes(data):
    mecab = MeCab.Tagger('')
    nouns = []
    for sentence in data:
        t = sentence.replace(",", "")
        node = mecab.parseToNode(t)
        while node:
            f = node.feature
            ns = node.surface
            p = f.split(',')[0]
            if p == '名詞' and not ns.isnumeric():  # 数字も除外
                nouns.append(node.surface)
            node = node.next
    return nouns
