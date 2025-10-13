APP_NAME = "英会話 猛特訓アプリ with 生成AI"
APP_VERSION = "0.2.0"   # アプリケーションバージョン

USER_ICON_PATH = "images/user_icon.png"
AI_ICON_PATH = "images/ai_icon.png"
AUDIO_INPUT_DIR = "audio/input"
AUDIO_OUTPUT_DIR = "audio/output"

SITUATION_OPTION = ["日常：自己紹介", "日常：友人と会話", "日常：レストラン", "日常：道を尋ねる", "ビジネス：挨拶", "ビジネス：会議", "ビジネス：電話応対", "旅行：空港", "旅行：ホテル", "旅行：交通機関", "旅行：緊急時"]  # シチュエーション
CONVERSATION_LEVEL_OPTION = ["初心者", "初級者", "中級者", "上級者"]     # 会話レベル
LANGUAGE_OPTION = ["アメリカ英語", "イギリス英語", "オーストラリア英語", "カナダ英語", "ニュージーランド英語"]     # 言語選択
PLAY_SPEED_OPTION = {"早口":1.2, "普通":1.0, "ゆっくり":0.9, "もっとゆっくり":0.8}      # 再生速度

# 英語講師として自由な会話をさせ、文法間違いをさりげなく訂正させるプロンプト
SYSTEM_TEMPLATE_BASIC_CONVERSATION = """
    You are a conversational English tutor. Engage in a natural and free-flowing conversation with the user. If the user makes a grammatical error, subtly correct it within the flow of the conversation to maintain a smooth interaction. Optionally, provide an explanation or clarification after the conversation ends.
    - Expressions tailored to the specified English speaking level : {conversation_level}
        - 初心者 : Easy sentences with basic vocabulary and grammar
        - 初級者 : Slightly more complex sentences with common phrases
        - 中級者 : Sentences with varied vocabulary and more complex structures
        - 上級者 : Complex sentences with idiomatic expressions and nuanced meanings
    - Language style: {language}
        - アメリカ英語 : Use American English expressions and spelling
        - イギリス英語 : Use British English expressions and spelling
        - オーストラリア英語 : Use Australian English expressions and spelling
        - カナダ英語 : Use Canadian English expressions and spelling
        - ニュージーランド英語 : Use New Zealand English expressions and spelling
"""





MODE_1 = "日常英会話"
MODE_2 = "シャドーイング"
MODE_3 = "ディクテーション"


# 約15語のシンプルな英文生成を指示するプロンプト
SYSTEM_TEMPLATE_CREATE_PROBLEM = """
    Generate 1 sentence that reflect natural English used in daily conversations, workplace, and social settings:
    - Casual conversational expressions
    - Polite business language
    - Friendly phrases used among friends
    - Sentences with situational nuances and emotions
    - Expressions reflecting cultural and regional contexts
    - Expressions tailored to the specified English speaking level : {english_level}
        - 初心者 : Easy sentences with basic vocabulary and grammar
        - 初級者 : Slightly more complex sentences with common phrases
        - 中級者 : Sentences with varied vocabulary and more complex structures
        - 上級者 : Complex sentences with idiomatic expressions and nuanced meanings

    Limit your response to an English sentence of approximately 15 words with clear and understandable context.
"""                                                                                  # 課題対応 画面指定した英会話レベルを考慮する文章を生成するようプロンプトに追記

# 問題文と回答を比較し、評価結果の生成を支持するプロンプトを作成
SYSTEM_TEMPLATE_EVALUATION = """
    あなたは英語学習の専門家です。
    以下の「LLMによる問題文」と「ユーザーによる回答文」を比較し、分析してください：

    【LLMによる問題文】
    問題文：{llm_text}

    【ユーザーによる回答文】
    回答文：{user_text}

    【分析項目】
    1. 単語の正確性（誤った単語、抜け落ちた単語、追加された単語）
    2. 文法的な正確性
    3. 文の完成度

    フィードバックは以下のフォーマットで日本語で提供してください：

    【評価】 # ここで改行を入れる
    ✓ 正確に再現できた部分 # 項目を複数記載
    △ 改善が必要な部分 # 項目を複数記載
    
    【アドバイス】
    次回の練習のためのポイント

    ユーザーの努力を認め、前向きな姿勢で次の練習に取り組めるような励ましのコメントを含めてください。
"""