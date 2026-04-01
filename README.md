# TravelApp 项目说明

## 项目结构

```
TravelApp/
├── backend/             # 后端代码
│   └── simple_server.py # 极简HTTP服务器
├── frontend/            # 前端代码
│   ├── src/             # 源代码
│   │   ├── api/         # API调用
│   │   │   └── travel.ts # 旅行数据API
│   │   ├── components/  # 组件
│   │   │   ├── FilterBar.vue    # 筛选栏组件
│   │   │   ├── HeroSection.vue  # 英雄区组件
│   │   │   ├── ImmersiveGallery.vue # 沉浸式画廊组件
│   │   │   └── TravelCard.vue   # 旅行卡片组件
│   │   ├── stores/      # 状态管理
│   │   │   └── travel.ts # 旅行数据状态管理
│   │   ├── views/       # 页面
│   │   │   └── Detail.vue # 详情页面
│   │   ├── App.vue      # 应用入口
│   │   └── main.ts      # 主入口
│   ├── package.json     # 依赖配置
│   └── vite.config.ts   # Vite配置
└── README.md            # 项目说明
```

## 数据库表结构

由于项目使用的是 Python 极简 HTTP 服务器，没有使用传统的数据库，而是使用了内存中的数据结构。数据结构如下：

### 旅行数据结构

| 字段名 | 类型 | 描述 |
|-------|------|------|
| id | number | 旅行ID |
| title | string | 旅行标题 |
| slug | string | 旅行路径 |
| visual_hook | string | 视觉钩子 |
| content_story | string | 故事内容 |
| cover_url | string | 封面图片URL |
| gallery_urls | string[] | 画廊图片URL数组 |
| experience_type | string | 体验类型 |
| visual_style | string | 视觉风格 |
| rarity_level | string | 小众程度 |
| emotional_tone | string | 情感基调 |

## 实现功能

### 1. 旅行数据展示
- 首页展示旅行卡片列表
- 每个卡片显示旅行标题、视觉钩子、故事预览和标签
- 点击卡片可查看详情

### 2. 多维度筛选功能
- 按体验类型筛选（Extreme, Sensory, Cultural, Healing, Nature）
- 按视觉风格筛选（BlackWhite, Dramatic, Surreal, Warm, Vibrant）
- 按小众程度筛选（Rare, Unique）
- 按情感基调筛选（Awe, Adrenaline, Mystery, Peace, Wonder）
- 支持多选筛选
- 支持清空筛选

### 3. 详情查看功能
- 点击卡片后显示沉浸式画廊
- 展示旅行的详细信息，包括标题、视觉钩子、故事内容和画廊图片

### 4. 响应式设计
- 适配不同屏幕尺寸
- 移动端友好的布局

## 技术栈

### 前端
- Vue 3 + TypeScript
- Vite
- Pinia（状态管理）
- Axios（HTTP请求）
- Vue Router（路由）

### 后端
- Python 3
- 内置 HTTP 服务器

## 运行项目

### 启动后端服务器
```bash
cd backend
python simple_server.py
```
后端服务器将在 http://localhost:8000 运行。

### 启动前端服务器
```bash
cd frontend
npm install
npm run dev
```
前端服务器将在 http://localhost:5200 运行。

## API 接口

### 获取所有旅行数据
- URL: `/api/v1/travels`
- Method: GET
- Response: 旅行数据数组

### 获取单个旅行详情
- URL: `/api/v1/travels/{slug}`
- Method: GET
- Response: 单个旅行数据
