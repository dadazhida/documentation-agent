from app.services.llm_service import call_llm

def generate_document(task: str, k: int):
    
    prompt = f"""
以下の要求から、プロダクトの要件定義書を作成してください。

# 入力
{task}

# 出力形式
- プロジェクト概要
- 主要機能（最低{k}個）
- 非機能要件
- 制約条件
- ターゲットユーザー
- 優先順位
- リスクと対策

必ずMarkdown形式で出力してください。
"""

    return call_llm(prompt)