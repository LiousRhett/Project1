# Project1

whatsapp自动回复机器人

## How to Run

项目增加了 `Makefile`，本地调试时执行：

```shell
# 同步依赖和环境
uv sync

# 启动
make run
```

构建过程使用 Docker，并将 HTTP Server 同时打包到镜像内，默认使用 80 端口。构建发布执行：

```shell
# 默认构建
make build

# 指定tag
export TAG=1.0.0
make build

# 运行
docker run -d -p 80:80 whatsapp-bot:$TAG
```
