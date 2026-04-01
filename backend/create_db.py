import sqlite3
import json

# 创建数据库连接
conn = sqlite3.connect('travels.db')
cursor = conn.cursor()

# 创建travels表
cursor.execute('''
CREATE TABLE IF NOT EXISTS travels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    visual_hook TEXT NOT NULL,
    content_story TEXT NOT NULL,
    cover_url TEXT NOT NULL,
    gallery_urls TEXT,
    experience_type TEXT NOT NULL,
    visual_style TEXT NOT NULL,
    rarity_level TEXT NOT NULL,
    emotional_tone TEXT NOT NULL
)
''')

# 准备数据
travel_data = [
    {
        "title": "在辐射与废墟之间，听见时间的停顿",
        "slug": "chernobyl-ruins",
        "visual_hook": "Pripyat silence heavier than death",
        "content_story": "我站在切尔诺贝利的废墟中，空气中弥漫着死亡的寂静。废弃的摩天轮在寒风中吱呀作响，像是在诉说着曾经的欢乐。我触摸着斑驳的墙壁，仿佛能感受到30年前那一场灾难的余温。时间在这里仿佛凝固了，每一块碎片都在讲述着人类的傲慢与自然的力量。",
        "cover_url": "https://picsum.photos/seed/chernobyl/800/600",
        "gallery_urls": ["https://picsum.photos/seed/chernobyl1/800/600", "https://picsum.photos/seed/chernobyl2/800/600"],
        "experience_type": "Extreme",
        "visual_style": "BlackWhite",
        "rarity_level": "Rare",
        "emotional_tone": "Awe"
    },
    {
        "title": "冰岛黑洞：与未知的深海对话",
        "slug": "iceland-black-hole",
        "visual_hook": "Ocean waves on black sand",
        "content_story": "站在冰岛的黑沙滩上，我凝视着眼前的黑洞。海水在洞口形成巨大的漩涡，仿佛要将一切吸入其中。黑色的玄武岩环绕着洞口，像是守护着某个神秘的秘密。我能感受到脚下的大地在震动，仿佛整个冰岛都在呼吸。这一刻，我与自然的力量直面相对，感受到了人类的渺小。",
        "cover_url": "https://picsum.photos/seed/iceland-black-hole/800/600",
        "gallery_urls": ["https://picsum.photos/seed/iceland1/800/600", "https://picsum.photos/seed/iceland2/800/600"],
        "experience_type": "Sensory",
        "visual_style": "Dramatic",
        "rarity_level": "Unique",
        "emotional_tone": "Adrenaline"
    },
    {
        "title": "土耳其地下城：穿越时空的隧道",
        "slug": "turkey-underground-cities",
        "visual_hook": "Byzantine breath in stone",
        "content_story": "走进土耳其的地下城，我仿佛穿越了时空。狭窄的隧道只能容一人通过，墙壁上的火把映出诡异的影子。空气中弥漫着潮湿的气息，仿佛能闻到千年的历史。我触摸着石壁上的刻痕，想象着古代居民在这里生活的场景。每一个拐角都可能藏着惊喜，每一步都踏在历史的尘埃上。",
        "cover_url": "https://picsum.photos/seed/underground/800/600",
        "gallery_urls": ["https://picsum.photos/seed/underground1/800/600", "https://picsum.photos/seed/underground2/800/600"],
        "experience_type": "Cultural",
        "visual_style": "Surreal",
        "rarity_level": "Rare",
        "emotional_tone": "Mystery"
    },
    {
        "title": "撒哈拉沙漠：在死亡之海中寻找生命",
        "slug": "sahara-desert",
        "visual_hook": "Golden waves of sand",
        "content_story": "在撒哈拉沙漠的中心，我独自面对无尽的沙海。太阳炙烤着大地，每一粒沙子都在发光。我踩着滚烫的沙子，感觉自己像是在另一个星球。突然，我看到了远处的绿洲，那是沙漠中的奇迹。我朝着它走去，每一步都充满了希望。在这片死亡之海中，生命以最顽强的方式存在着，让我对自然充满了敬畏。",
        "cover_url": "https://picsum.photos/seed/sahara/800/600",
        "gallery_urls": ["https://picsum.photos/seed/sahara1/800/600", "https://picsum.photos/seed/sahara2/800/600"],
        "experience_type": "Healing",
        "visual_style": "Warm",
        "rarity_level": "Rare",
        "emotional_tone": "Peace"
    },
    {
        "title": "亚马逊雨林：与野性的亲密接触",
        "slug": "amazon-rainforest",
        "visual_hook": "Green cathedral of life",
        "content_story": "深入亚马逊雨林，我被绿色包围。阳光透过树叶的缝隙洒下斑驳的光影，各种动物的叫声交织成一首自然的交响乐。我沿着小溪前行，脚边不时有色彩斑斓的蝴蝶飞过。突然，我看到了一只美洲豹在远处的树枝上休息，它的眼神与我交汇的瞬间，我感受到了野性的力量。在这片原始的森林中，我找回了与自然的连接。",
        "cover_url": "https://picsum.photos/seed/amazon/800/600",
        "gallery_urls": ["https://picsum.photos/seed/amazon1/800/600", "https://picsum.photos/seed/amazon2/800/600"],
        "experience_type": "Nature",
        "visual_style": "Vibrant",
        "rarity_level": "Unique",
        "emotional_tone": "Wonder"
    }
]

# 插入数据
for travel in travel_data:
    # 将gallery_urls转换为JSON字符串
    gallery_urls_json = json.dumps(travel['gallery_urls'])
    
    # 插入数据
    cursor.execute('''
    INSERT OR REPLACE INTO travels (title, slug, visual_hook, content_story, cover_url, gallery_urls, experience_type, visual_style, rarity_level, emotional_tone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        travel['title'],
        travel['slug'],
        travel['visual_hook'],
        travel['content_story'],
        travel['cover_url'],
        gallery_urls_json,
        travel['experience_type'],
        travel['visual_style'],
        travel['rarity_level'],
        travel['emotional_tone']
    ))

# 提交事务
conn.commit()

# 关闭连接
conn.close()

print("数据库创建成功，数据插入完成！")
