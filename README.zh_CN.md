# 应用智链 —— 百事通

能掐会算，通晓世间百事。博古通今，畅聊人生百态。

这是一个探索性项目，目的是让 AI 根据用户输入的内容调用相应的 API，整理出最终答案返回给用户。

## 超能力

- [x] 当前城市天气
- [x] 连接搜索引擎
- [x] 当前星座运势
- [ ] 查询快递信息
- [ ] 今日热点新闻
- [ ] 热门影视信息
- [ ] 生成图片

## 项目演示

[访问地址](https://beston.appchain.ai)

## 使用的框架

- LangChain is a framework for developing applications powered by language models.
- Chainlit is an open-source Python package that makes it incredibly fast to build and share LLM apps.

## 如何运行

本项目使用了 Poetry 创建虚拟环境，您也可以使用其他工具创建，如 Anaconda。

BestAI 默认使用 Azure OpenAI，您可以根据情况修改为 OpenAI，或者其他开源大模型。

- 使用如下命令安装依赖包：

```shell
> poetry install
```

- 进入虚拟环境

```shell
> poetry shell
```

- 启动项目

```shell
> chainlit run app.py -w
```

> 记得在运行之前，需要补充环境变量中的信息。
> .env.example 文件修改为 .env

另外，您也可以通过 requirements.txt 安装依赖，并使用其他虚拟工具运行起来。

requirements.txt 文件是通过 poetry 工具生成的：

```shell
> poetry export --without-hashes --format=requirements.txt > requirements.txt
```

## 如何部署

BestAI 提供了 Docker 部署方案:

```shell
> docker build -t best-appchain-ai:v1 .
```

BestAI 演示版已被部署到 Google Cloud：

```shell
> gcloud app deploy app.custom.yaml
```

## 商务合作

商务合作、项目交流或有其他想法，都可以通过邮件联系我。
<work@lalo.im>

## License

BestonAI is licensed under the MIT License. See the LICENSE file for more details.
