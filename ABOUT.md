# 健康経営ROI試算ツール（HTML版）

## 一言で言うと
**従業員数と平均年収を入れるだけで、健康経営の損失コストとROIを即時試算する静的Webツール**。Vercel / Cloudflare Pages / GitHub Pagesなどで無料デプロイ可能。Streamlit版から完全HTML/JSに書き直し、バッジなし・認証なし・スリープなしで運用する。

## 何ができるのか
1. **損失コスト試算**
   - プレゼンティーズム損失（年収 × 11%）
   - アブセンティーズム損失（年収 × 2%）
   - 年間合計（年収の13%相当）を従業員数倍で算出
2. **ROI試算**
   - 投資額とスライダー（1〜50%）で改善率を調整
   - 改善見込額・純効果額・ROI% を即時計算
3. **提案用サマリー出力**
   - コピー or `.txt` ダウンロードで提案資料にそのまま貼れる

## 構成
| ファイル | 役割 |
|----------|------|
| `index.html` | 全部入り（HTML + CSS + JS、単一ファイル） |
| `.gitignore` | 基本除外ルール |

**以上。** Pythonもビルドも不要、静的ファイル1つで完結。

## 使い方
### ローカルで動かす
```bash
cd "/Users/hayatokagami/⭐Claude専用/020_health-roi-calculator"
open index.html
```
ブラウザに直接ドラッグしてもOK。

### 本番公開（Vercel推奨）
1. https://vercel.com/ にGitHubアカウントでログイン
2. 「Add New → Project」→ `kagami-fit/health-roi-calculator` を選択
3. Framework Preset：`Other` のまま、他はデフォルトで Deploy
4. `[名前].vercel.app` のURLが発行される

## 技術メモ
- 依存ゼロ（フォントだけGoogle Fontsから読み込み）
- レスポンシブ対応（スマホで縦並び、PCで3カラム）
- FRACTALブランドカラー（白背景＋ピンクアクセント #E4006F）
- Noto Sans JP + Oswald

## 元ツールとの違い
- Streamlit版（Python）→ 完全HTML/JSに書き直し
- 認証問題、スリープ問題、バッジ問題、全て消滅
- ロード速度：Streamlit版より10倍以上速い（体感1秒未満）
- 運用コスト：0円（Vercel/Cloudflare Pages無料枠）

## 状態
- **稼働中**：ローカルで `open index.html` で即動作確認可
- 次のステップ：Vercelへデプロイ → 公開URL取得 → QRコード生成
