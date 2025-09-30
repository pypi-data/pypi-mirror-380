# QQ-Robot

QQ 群机器人 SDK，支持 NapCat 协议、FastAPI 接口、OBS 云存储。

## 安装
```bash
pip install tianxiadatong-qq-robot
```

## 快速开始
```bash
import tianxiadatong_qq_robot
robot = tianxiadatong_qq_robot.qqApp()
robot.init(host="0.0.0.0", port=8099)
```

## 配置
运行目录下放置 config.json 即可。

```bash
{
  "base_url": "localhost:8081",
  "sentry_sdk_url": "http://af018d0bf71f4ab091aab4181d10a49d@10.7.115.88:9000/4",
  "OBSConfig": {
    "ENDPOINT": "xxxxxxxx",
    "ACCESS_KEY": "xxxxxxxx",
    "SECRET_KEY": "xxxxxxxx",
    "BUCKET": "xxxxx"
  }
}
```