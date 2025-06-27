# MCP Server for Big Query

## 目標

- Big Queryを操作するためのMCP Serverを構築する

## 目的

1. 技術観点: MCP Server for BQのための知見を蓄積する
2. チーム観点: テーブル調査業務を簡単にする

## Vertex AIの有効化

### 1. Vertex AIのAPIを有効化

### 2. Application Default Credentialを取得

```sh
$ gcloud auth application-default login
```

## Install Toolbox for Mac

- Version: [0.7.0](https://github.com/googleapis/genai-toolbox/releases/tag/v0.7.0)

```sh
$ wget https://storage.googleapis.com/genai-toolbox/v0.7.0/darwin/arm64/toolbox
$ chmod +x toolbox
```

## Running Toolbox Server

```sh
$ ./toolbox --tools-file tools.yml
```

## 参考

- [ADK と MCP Toolbox for Databases を使った BigQuery エージェントの開発 - Zenn](https://zenn.dev/hiracky16/articles/90162823db6a4b44a839)
- [google-toolbox - GitHub](https://github.com/googleapis/genai-toolbox) 
