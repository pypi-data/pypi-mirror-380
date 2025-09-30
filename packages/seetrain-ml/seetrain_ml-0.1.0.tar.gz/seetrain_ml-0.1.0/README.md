# SeeTrain

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/seetrain.svg)](https://pypi.org/project/seetrain/)
[![Downloads](https://pepy.tech/badge/seetrain)](https://pepy.tech/project/seetrain)

**SeeTrain** 是一个强大的深度学习实验跟踪和框架集成工具，提供统一的接口来适配各种深度学习框架，实现无缝的实验管理和数据记录。

## ✨ 特性

- 🔗 **多框架集成** - 支持 PyTorch Lightning、TensorFlow/Keras、Hugging Face、MMEngine 等主流框架
- 📊 **统一实验跟踪** - 提供一致的 API 来记录指标、图像、音频、文本等多媒体数据
- 🎯 **多种适配模式** - Callback、Tracker、VisBackend、Autolog 四种集成模式
- 🚀 **自动日志记录** - 支持 OpenAI、智谱 AI 等 API 的自动拦截和记录
- 📈 **实时监控** - 硬件资源监控、性能指标跟踪
- 🎨 **丰富可视化** - 基于 Rich 库的美观终端输出

## 🚀 快速开始

### 安装

```bash
pip install seetrain
```

### 基本使用

```python
from seetrain import init, log, log_scalar, log_image, finish

# 初始化实验
experiment = init(
    project="my_project",
    experiment_name="experiment_1",
    description="我的第一个实验"
)

# 记录标量指标
log_scalar('loss', 0.5, step=100)
log_scalar('accuracy', 0.95, step=100)

# 记录图像
import numpy as np
image = np.random.rand(224, 224, 3)
log_image('prediction', image, step=100)

# 记录字典数据
log({
    'train/loss': 0.3,
    'train/accuracy': 0.98,
    'val/loss': 0.4,
    'val/accuracy': 0.96
}, step=100)

# 完成实验
finish()
```

## 🔧 框架集成

### PyTorch Lightning

```python
from seetrain.integration import init_pytorch_lightning

# 初始化集成
integration = init_pytorch_lightning(
    project="pytorch_project",
    experiment_name="lightning_training"
)

# 获取回调函数
callback = integration.get_callback()

# 在训练器中使用
from pytorch_lightning import Trainer
trainer = Trainer(callbacks=[callback])
```

### TensorFlow/Keras

```python
from seetrain.integration import init_keras

# 初始化集成
integration = init_keras(
    project="keras_project",
    experiment_name="keras_training"
)

# 获取回调函数
callback = integration.get_callback()

# 在模型训练中使用
model.fit(
    x_train, y_train,
    callbacks=[callback],
    epochs=10
)
```

### Hugging Face Transformers

```python
from seetrain.integration import init_transformers

# 初始化集成
integration = init_transformers(
    project="transformers_project",
    experiment_name="bert_training"
)

# 获取回调函数
callback = integration.get_callback()

# 在训练器中使用
from transformers import Trainer
trainer = Trainer(
    model=model,
    callbacks=[callback],
    # ... 其他参数
)
```

### API 自动日志记录

```python
from seetrain.integration import enable_openai_autolog

# 启用 OpenAI 自动日志记录
autolog = enable_openai_autolog(
    project="openai_project",
    experiment_name="chat_completion"
)

# 正常使用 OpenAI API，会自动记录
import openai
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=100
)

# 禁用自动日志记录
autolog.disable()
```

## 📚 支持的框架

| 框架 | 集成模式 | 状态 |
|------|----------|------|
| PyTorch Lightning | Callback | ✅ |
| TensorFlow/Keras | Callback | ✅ |
| Hugging Face Transformers | Callback | ✅ |
| Hugging Face Accelerate | Tracker | ✅ |
| MMEngine/MMDetection | VisBackend | ✅ |
| Ultralytics | Callback | ✅ |
| OpenAI API | Autolog | ✅ |
| 智谱 AI API | Autolog | ✅ |
| Anthropic API | Autolog | ✅ |

## 🛠️ 高级功能

### 硬件监控

```python
from seetrain import init
from seetrain.setting import set_settings, Settings

# 配置硬件监控
settings = Settings(
    hardware_monitor=True,
    hardware_interval=10  # 每10秒收集一次硬件信息
)
set_settings(settings)

# 初始化实验时会自动开始硬件监控
experiment = init(project="monitored_project")
```

### 多媒体数据记录

```python
# 记录音频
import numpy as np
audio_data = np.random.randn(16000)  # 1秒的音频
log_audio('speech', audio_data, sample_rate=16000, step=100)

# 记录文本
log_text('prediction', "这是一个预测结果", step=100)

# 记录视频
video_frames = np.random.rand(10, 224, 224, 3)  # 10帧视频
log_video('animation', video_frames, fps=30, step=100)
```

### 配置管理

```python
from seetrain import update_config

# 记录超参数
update_config({
    'learning_rate': 0.001,
    'batch_size': 32,
    'model_architecture': 'ResNet50',
    'optimizer': 'Adam'
})
```

## 📦 安装选项

### 基础安装
```bash
pip install seetrain
```

### 特定框架支持
```bash
# PyTorch 支持
pip install seetrain[pytorch]

# TensorFlow 支持
pip install seetrain[tensorflow]

# Hugging Face 支持
pip install seetrain[transformers]

# MMEngine 支持
pip install seetrain[mmcv]

# API 集成支持
pip install seetrain[api]

# 开发依赖
pip install seetrain[dev]

# 文档依赖
pip install seetrain[docs]
```

## 🤝 贡献

我们欢迎社区贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目开发。

## 📄 许可证

本项目采用 MIT 许可证。详情请查看 [LICENSE](LICENSE) 文件。

## 🔗 相关链接
- [PyPI 包](https://pypi.org/project/seetrain/)

## 🙏 致谢

感谢所有为 SeeTrain 项目做出贡献的开发者和社区成员！

---

**SeeTrain** - 让深度学习实验跟踪变得简单而强大！
