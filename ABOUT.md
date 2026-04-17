# 健康経営ROI試算ツール

## 一言で言うと
**従業員数と平均年収を入力するだけで、健康経営の損失コスト（プレゼンティーズム＋アブセンティーズム）と投資対効果（ROI）を試算する Streamlit 単体アプリ**。`015_mf-company-analysis` のROI試算ページを切り出して独立ツール化したもの。企業マスターやGoogle Sheets連携などの前提なしで、単体で動く。

## 何ができるのか
1. **損失コスト試算**
   - プレゼンティーズム損失（年収 × 11%）
   - アブセンティーズム損失（年収 × 2%）
   - 年間合計（年収の13%相当）を従業員数倍で算出
2. **ROI試算**
   - 投資額と損失改善率（1〜50%）をスライダーで調整
   - 改善見込額・純効果額・ROI% を即時計算
3. **提案用サマリー出力**
   - そのまま提案資料に貼れる整形済みテキスト生成
   - `.txt` ダウンロードボタン付き

## 構成
| ファイル | 役割 |
|----------|------|
| `app.py` | Streamlitメインアプリ（入力・損失試算・ROI試算・サマリー出力すべて） |
| `theme.py` | FRACTALブランドカラーのカスタムCSS＋ヘッダー/メトリクスカード関数 |
| `requirements.txt` | `streamlit` のみ |
| `.gitignore` | Python/Streamlit用の基本除外 |

## 使い方
```bash
cd "/Users/hayatokagami/⭐Claude専用/020_health-roi-calculator"
pip install -r requirements.txt
streamlit run app.py
```
ブラウザで http://localhost:8501 が開く。企業名（任意）＋従業員数＋平均年収を入れれば自動で全数値が更新される。

## 元ツールとの違い
- `015_mf-company-analysis/ui/pages/07_ROI試算.py` が元
- 「分析済み企業から選択」モードを削除（`sheets.sync` 依存を撤廃）→ 手動入力のみ
- サイドバーのワークフロー文脈を外し、単独ページとして自立
- デザイン・計算ロジック・出力文面は完全に同一

## 状態
- **稼働中**：単体で `streamlit run app.py` だけで動作確認可
- 外部API不要、認証不要、依存も `streamlit` 1つだけ
