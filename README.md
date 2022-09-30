# 税関コード照会

[![codecov](https://codecov.io/gh/sheepzh/hscode/branch/master/graph/badge.svg?token=5DX131J0LI)](https://codecov.io/gh/sheepzh/hscode)
[![](https://img.shields.io/github/license/sheepzh/hscode)](https://github.com/sheepzh/hscode/blob/main/LICENSE)
[![](https://img.shields.io/github/v/release/sheepzh/hscode)](https://github.com/sheepzh/hscode/releases)


https://hsbianma.com

税関コード照会。**Python2 との互換性を意図していません**。


## 使用する

### 移行

1. インストール
```shell
  pip3 install hscode 
```
2. 導入
```python
from hscode import get_code_info
```
3. 単一の税関コード情報のクエリ

```python
code = get_code_info('123')
print(code)
# None
```
存在しない場合は None を返します
```python
code = get_code_info('2302500000')
print(code)
```
お問い合わせ [2302500000](https://hsbianma.com/Code/2302500000.html) 成功時に返される税関コード情報。
```json
# 以下はフォーマットされた表示です
{
    "code": "2302500000",
    "name": "豆类植物糠、麸及其他残渣",
    "outdated": false,
    "update_time": "2021/1/7",
    "tax_info": {   
        "unit": "千克",
        "export": "0%",
        "ex_rebate": "0%",
        "ex_provisional": "",
        "vat": "9%",
        "preferential": "5%",
        "im_provisional": "",
        "import": "30%",
        "consumption": ""
    },
    "declarations": [
        "品名",
        "品牌类型",
        "出口享惠情况",
        "种类[玉米的、小麦的等]",
        "GTIN",
        "CAS",
        "其他"
    ],
    "supervisions": ["A", "B"],
    "quarantines": ["P", "Q"],
    "ciq_codes": {
        "2302500000999": "豆类植物糠、麸及其他残渣"
    }
}
```

### 爬虫類

クローラー スクリプトを使用して税関コード情報をバッチでクロールする

1. リポジトリをクローンして依存関係をインストールする
```shell
git clone https://github.com/lazyliang/hscode_spider.git
cd hscode

pip3 install BeautifulSoup4
pip3 install lxml
pip3 install requests
```

2. ヘルプ情報を表示する

```shell
python3 main.py --help
```

```txt
参数列表：
  --help|-h                                 ヘルプ情報を表示する
  --search|-s [chapter]         特定の章のコンテンツ (製品コードの最初の 2 桁) をクロールします。デフォルトは 01 です
  --all|-a                                     すべての章のコンテンツをクロールします。 このスイッチがオンの場合、 --search は効果がありません
  --file-root [dir]                     ファイルを保存するルートパス
                                                     デフォルト [ホーム]/hascode_file  for linux
                                                     ファイル名の形式: 
                                                       hscode_[chapter]_YYYYMMDD_HH:mm.txt
                                                       hscode_[chapter]_latest.txt
  --no-latest                            最新のファイルを生成 (または元の上書き) しない
  --quiet|-q                              サイレント モード、ログ情報は出力されません
  --outdated                           [期限切れ] データを含む
  --proxy|-p [proxy-url]      プロキシを使用する
                                                       --proxy https://www.baidu.com?s={url}
                                                    {url} 元のリクエスト URL です
```

3. 例: クロール [第 97 章 - 艺术品、收藏品及古物](https://hsbianma.com/search?keywords=97) の税関コード

```shell
python3 main.py -s 97 --outdated
```

```
Query page:chapter=97, page=1
Query page:chapter=97, page=2
Query page:chapter=97, page=3
{ "code": "9701210000", "name": "超过100年的油画、粉画及其他手绘画", "outdated": false, "update_time": "正常", "tax_info": { "unit": "幅/千克", "export": "0%", "ex_rebate": "0%", "ex_provisional": "", "vat": "13%", "preferential": "无", "im_provisional": "0%", "import": "50%", "consumption": "" }, "declarations": ["品牌类型", "出口享惠情况", "创作年份", "尺寸大小", "GTIN", "CAS", "其他"], "ciq_codes": {"澳大利亚": "0%","文莱": "0%","柬埔寨": "0%","韩国": "10.8%","老挝": "0%","马来西亚": "0%","新西兰": "0%","新加坡": "0%","泰国": "0%","越南": "0%","日本": "10.9%"}, "charter_label": ["第21类", "97", "9701"], "charter_txt": ["艺术品、收藏品及古物", "艺术品、收藏品及古物", "油画、粉画及其他手绘画,但带有手工绘制及手工描饰的制品或税目49.06的图纸除外;拼贴画及类似装饰板:"] }
{ "code": "9701220010", "name": "含濒危动物成分的超过100年的镶嵌画", "outdated": false, "update_time": "正常", "tax_info": { "unit": "幅/千克", "export": "0%", "ex_rebate": "0%", "ex_provisional": "", "vat": "13%", "preferential": "无", "im_provisional": "0%", "import": "50%", "consumption": "" }, "declarations": ["品牌类型", "出口享惠情况", "创作年份", "尺寸大小", "GTIN", "CAS", "其他"], "supervisions": ["A", "B", "F", "E"], "quarantines": ["P", "Q"], "ciq_codes": {"澳大利亚": "0%","文莱": "0%","柬埔寨": "0%","韩国": "12.6%","老挝": "0%","马来西亚": "0%","新西兰": "0%","新加坡": "0%","泰国": "0%","越南": "0%","日本": "12.7%"}, "charter_label": ["第21类", "97", "9701"], "charter_txt": ["艺术品、收藏品及古物", "艺术品、收藏品及古物", "油画、粉画及其他手绘画,但带有手工绘制及手工描饰的制品或税目49.06的图纸除外;拼贴画及类似装饰板:"] }
{ "code": "9706100090", "name": "其他超过250年的古物", "outdated": false, "update_time": "正常", "tax_info": { "unit": "件/千克", "export": "0%", "ex_rebate": "0%", "ex_provisional": "", "vat": "13%", "preferential": "无", "im_provisional": "", "import": "0%", "consumption": "" }, "declarations": ["品牌类型", "出口享惠情况", "年代", "是否野生动物产品", "GTIN", "CAS", "其他"], "quarantines": ["P", "Q"], "ciq_codes": {"澳大利亚": "0%","文莱": "0%","柬埔寨": "0%","韩国": "0%","老挝": "0%","马来西亚": "0%","新西兰": "0%","新加坡": "0%","泰国": "0%","越南": "0%","日本": "0%"}, "charter_label": ["第21类", "97", "9706"], "charter_txt": ["艺术品、收藏品及古物", "艺术品、收藏品及古物", "超过100年的古物:"] }
{ "code": "9706900010", "name": "其他超过100年的濒危动植古物", "outdated": false, "update_time": "正常", "tax_info": { "unit": "件/千克", "export": "0%", "ex_rebate": "0%", "ex_provisional": "", "vat": "13%", "preferential": "无", "im_provisional": "", "import": "0%", "consumption": "" }, "declarations": ["品牌类型", "出口享惠情况", "年代", "是否野生动物产品", "GTIN", "CAS", "其他"], "supervisions": ["A", "B", "F", "E"], "quarantines": ["P", "Q"], "ciq_codes": {"澳大利亚": "0%","文莱": "0%","柬埔寨": "0%","韩国": "0%","老挝": "0%","马来西亚": "0%","新西兰": "0%","新加坡": "0%","泰国": "0%","越南": "0%","日本": "0%"}, "charter_label": ["第21类", "97", "9706"], "charter_txt": ["艺术品、收藏品及古物", "艺术品、收藏品及古物", "超过100年的古物:"] }
{ "code": "9706900090", "name": "其他超过100年的古物", "outdated": false, "update_time": "正常", "tax_info": { "unit": "件/千克", "export": "0%", "ex_rebate": "0%", "ex_provisional": "", "vat": "13%", "preferential": "无", "im_provisional": "", "import": "0%", "consumption": "" }, "declarations": ["品牌类型", "出口享惠情况", "年代", "是否野生动物产品", "GTIN", "CAS", "其他"], "quarantines": ["P", "Q"], "ciq_codes": {"澳大利亚": "0%","文莱": "0%","柬埔寨": "0%","韩国": "0%","老挝": "0%","马来西亚": "0%","新西兰": "0%","新加坡": "0%","泰国": "0%","越南": "0%","日本": "0%"}, "charter_label": ["第21类", "97", "9706"], "charter_txt": ["艺术品、收藏品及古物", "艺术品、收藏品及古物", "超过100年的古物:"] }
Item (with searching "97") num: 41
```
```
クロールされたコンテンツはローカルファイルに保存され、ファイルの出力場所はargument.pyに設定されます

```shell
cat ~/hscode_file/latest/hscode_97.txt
```

各行には、税関コードが json 形式で格納されます,内容は、上記のログが出力するものと同じです

