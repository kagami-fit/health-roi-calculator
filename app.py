"""健康経営ROI試算ツール（スタンドアロン版）"""

import streamlit as st

st.set_page_config(
    page_title="健康経営ROI試算ツール",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from theme import apply_theme, page_header, section_header, metric_card, COLORS

apply_theme()

page_header(
    "健康経営ROI試算ツール",
    "従業員数と平均年収から、健康経営の損失コストと投資対効果を試算します",
)

# ==============================================
# INPUT
# ==============================================
section_header("INPUT", "試算条件の入力")

company_name = st.text_input("企業名（任意）", value="")

col1, col2 = st.columns(2)
with col1:
    employee_count = st.number_input(
        "従業員数",
        min_value=1,
        max_value=1_000_000,
        value=100,
        step=10,
    )
with col2:
    avg_salary = st.number_input(
        "平均年収（円）",
        min_value=1_000_000,
        max_value=50_000_000,
        value=5_000_000,
        step=100_000,
        format="%d",
    )

# ==============================================
# LOSS COST
# ==============================================
PRESENTEEISM_RATE = 0.11
ABSENTEEISM_RATE = 0.02

presenteeism_cost = avg_salary * PRESENTEEISM_RATE * employee_count
absenteeism_cost = avg_salary * ABSENTEEISM_RATE * employee_count
total_loss = presenteeism_cost + absenteeism_cost

section_header("LOSS COST", "損失コスト試算")

col1, col2, col3 = st.columns(3)
with col1:
    metric_card(
        "PRESENTEEISM",
        f"¥{presenteeism_cost:,.0f}",
        f"年収の11% × {employee_count:,}名",
    )
with col2:
    metric_card(
        "ABSENTEEISM",
        f"¥{absenteeism_cost:,.0f}",
        f"年収の2% × {employee_count:,}名",
    )
with col3:
    metric_card(
        "TOTAL LOSS / YEAR",
        f"¥{total_loss:,.0f}",
        "プレゼンティーズム + アブセンティーズム",
        accent=True,
    )

st.markdown(
    f"""
    <table class="fr-table" style="margin:1.5rem 0;">
        <thead>
            <tr>
                <th>項目</th>
                <th>計算式</th>
                <th>1人あたり</th>
                <th>全社合計</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>プレゼンティーズム</th>
                <td>¥{avg_salary:,} × 11%</td>
                <td>¥{avg_salary * PRESENTEEISM_RATE:,.0f}</td>
                <td class="accent">¥{presenteeism_cost:,.0f}</td>
            </tr>
            <tr>
                <th>アブセンティーズム</th>
                <td>¥{avg_salary:,} × 2%</td>
                <td>¥{avg_salary * ABSENTEEISM_RATE:,.0f}</td>
                <td class="accent">¥{absenteeism_cost:,.0f}</td>
            </tr>
            <tr>
                <th>合計</th>
                <td>年収 × 13%</td>
                <td>¥{avg_salary * (PRESENTEEISM_RATE + ABSENTEEISM_RATE):,.0f}</td>
                <td class="accent" style="font-size:1.2rem; font-weight:700;">¥{total_loss:,.0f}</td>
            </tr>
        </tbody>
    </table>
    """,
    unsafe_allow_html=True,
)

# ==============================================
# ROI
# ==============================================
section_header("ROI", "投資対効果の試算")

col1, col2 = st.columns(2)
with col1:
    investment = st.number_input(
        "健康経営への投資額（年間・円）",
        min_value=0,
        max_value=10_000_000_000,
        value=min(int(total_loss * 0.05), 100_000_000),
        step=100_000,
        format="%d",
    )
with col2:
    improvement_rate = st.slider(
        "損失改善率（%）",
        min_value=1,
        max_value=50,
        value=10,
    )

improvement_amount = total_loss * (improvement_rate / 100)
net_benefit = improvement_amount - investment
roi = (net_benefit / investment * 100) if investment > 0 else 0

col1, col2, col3 = st.columns(3)
with col1:
    metric_card(
        "IMPROVEMENT",
        f"¥{improvement_amount:,.0f}",
        f"損失額 × 改善率{improvement_rate}%",
    )
with col2:
    bg = COLORS["primary_dark"] if net_benefit >= 0 else COLORS["accent"]
    st.markdown(
        f"""<div class="fr-metric-card" style="background:{bg};">
            <div class="fr-metric-label">NET BENEFIT</div>
            <div class="fr-metric-value">¥{net_benefit:,.0f}</div>
            <div class="fr-metric-sub">改善見込額 − 投資額</div>
        </div>""",
        unsafe_allow_html=True,
    )
with col3:
    roi_bg = COLORS["primary_dark"] if roi >= 0 else COLORS["accent"]
    st.markdown(
        f"""<div class="fr-metric-card" style="background:{roi_bg};">
            <div class="fr-metric-label">ROI</div>
            <div class="fr-metric-value" style="font-size:2.8rem;">{roi:,.1f}%</div>
            <div class="fr-metric-sub">{'投資対効果あり' if roi > 0 else '投資超過'}</div>
        </div>""",
        unsafe_allow_html=True,
    )

# ==============================================
# SUMMARY
# ==============================================
section_header("PROPOSAL SUMMARY", "提案用サマリー")

target_label = f"（{company_name}様）" if company_name else ""

summary_text = f"""【健康経営ROI試算{target_label}】

■ 試算条件
・従業員数: {employee_count:,}名
・平均年収: ¥{avg_salary:,}

■ 現状の推定損失額（年間）
・プレゼンティーズム損失（年収×11%）: ¥{presenteeism_cost:,.0f}
・アブセンティーズム損失（年収×2%）: ¥{absenteeism_cost:,.0f}
・合計: ¥{total_loss:,.0f}
・1人あたり: ¥{avg_salary * (PRESENTEEISM_RATE + ABSENTEEISM_RATE):,.0f}

■ 施策導入後の効果試算
・投資額: ¥{investment:,}
・改善率: {improvement_rate}%
・改善見込額: ¥{improvement_amount:,.0f}
・純効果額: ¥{net_benefit:,.0f}
・ROI: {roi:,.1f}%"""

st.text_area("コピーして提案資料にお使いください", value=summary_text, height=320)

st.download_button(
    label="テキストファイルでダウンロード",
    data=summary_text,
    file_name=f"ROI試算_{company_name or '企業名'}.txt",
    mime="text/plain",
)

st.markdown(
    f"""<div class="fr-footer">
        健康経営ROI試算ツール
    </div>""",
    unsafe_allow_html=True,
)
