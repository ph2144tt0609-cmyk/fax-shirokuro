# FAX白黒

スマホで撮った書類の写真を、FAXで黒くつぶれない白黒画像に変換する1ページのツール。
画像はブラウザ内（canvas）だけで処理し、外部には送信しない。

- 公開: https://ph2144tt0609-cmyk.github.io/fax-shirokuro/
- 変換: 周囲の平均明るさとの差で白黒を分ける適応的二値化（Bradley 法・積分画像）
- アイコン再生成: `py -X utf8 _make_icons.py`
- 更新: main へ push すると GitHub Pages に反映（main 直配信）
