# FastAPI AgentRouter

マルチプラットフォーム対応のFastAPI向けシンプルなAIエージェント統合ライブラリ。

## 概要

FastAPI AgentRouterを使用すると、AIエージェントをFastAPIアプリケーションに非常に簡単に統合できます。わずか2行のコードで、Slack、Discord、Webhookなど複数のプラットフォームを通じてエージェントを公開できます。

## 主な機能

- 🚀 **シンプルな統合** - たった1行でFastAPIアプリにエージェントを追加
- 🤖 **Vertex AI ADKサポート** - GoogleのAgent Development Kitをネイティブサポート
- 🔌 **マルチプラットフォーム** - Slack、Discord、Webhookエンドポイントを内蔵
- 🎯 **プロトコルベース** - `stream_query`メソッドを実装した任意のエージェントで動作
- ⚡ **非同期＆ストリーミング** - ストリーミングレスポンスで完全な非同期サポート
- 🔒 **適切な無効化** - 無効化されたエンドポイントはHTTP 404 Not Foundを返す

## クイックサンプル

```python
from fastapi import FastAPI
from fastapi_agentrouter import create_agent_router

def get_agent():
    # エージェントを返す（例：Vertex AI AdkApp）
    return your_agent

app = FastAPI()

# これだけです！たった1行
app.include_router(create_agent_router(get_agent))
```

エージェントは以下のエンドポイントで利用可能になります：
- `/agent/webhook` - 汎用Webhookエンドポイント
- `/agent/slack/events` - SlackイベントとSlashコマンド
- `/agent/discord/interactions` - Discordインタラクション

## なぜFastAPI AgentRouterなのか？

### 課題
AIエージェントを異なるプラットフォーム（Slack、Discordなど）と統合するには以下が必要です：
- 各プラットフォームの認証と検証の理解
- 異なるメッセージフォーマットの処理
- ストリーミングレスポンスの管理
- 複数のエンドポイントの設定

### ソリューション
FastAPI AgentRouterは、プラットフォーム固有の複雑さをすべて処理します。あなたはエージェントを提供するだけで、残りは私たちが処理します。

## インストール

```bash
pip install fastapi-agentrouter

# 特定のプラットフォームと一緒に
pip install "fastapi-agentrouter[slack]"
pip install "fastapi-agentrouter[discord]"
pip install "fastapi-agentrouter[vertexai]"
pip install "fastapi-agentrouter[all]"
```

## 次のステップ

最新のアップデートとリリースについては[変更履歴](changelog.md)をご覧ください。
