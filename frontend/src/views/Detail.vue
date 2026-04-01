<template>
  <div class="detail-page">
    <div v-if="loading" class="loading">加载中...</div>
    <div v-else-if="travel" class="detail-content">
      <!-- 主视觉区域 -->
      <div class="hero-section">
        <img :src="travel.cover_url" :alt="travel.title" class="main-image">
        <div class="hero-overlay">
          <h1>{{ travel.title }}</h1>
          <p class="visual-hook">{{ travel.visual_hook }}</p>
        </div>
      </div>

      <!-- 内容区域 -->
      <div class="content-section">
        <!-- 旅行信息标签 -->
        <div class="info-tags">
          <span v-if="travel.experience_type" class="tag primary">{{ travel.experience_type }}</span>
          <span v-if="travel.visual_style" class="tag secondary">{{ travel.visual_style }}</span>
          <span v-if="travel.rarity_level" class="tag accent">{{ travel.rarity_level }}</span>
          <span v-if="travel.emotional_tone" class="tag tertiary">{{ travel.emotional_tone }}</span>
        </div>

        <!-- 沉浸式故事内容 -->
        <div class="story-content">
          <h2>沉浸式体验</h2>
          <p class="story-text">{{ travel.content_story }}</p>
        </div>

        <!-- 图片画廊 -->
        <div v-if="travel.gallery_urls && travel.gallery_urls.length > 0" class="gallery-section">
          <h3>视觉画廊</h3>
          <div class="gallery-grid">
            <div
              v-for="(url, index) in travel.gallery_urls"
              :key="index"
              class="gallery-item"
            >
              <img :src="url" :alt="'Gallery image ' + (Number(index) + 1)">
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="error-state">
      <h2>旅行内容未找到</h2>
      <p>抱歉，我们找不到您要查看的旅行内容。</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useTravelStore } from '../stores/travel'

const route = useRoute()
const travelStore = useTravelStore()
const { getTravelBySlug } = travelStore

const travel = ref<any>(null)
const loading = ref(true)

onMounted(async () => {
  const slug = route.params.slug as string
  if (slug) {
    travel.value = await getTravelBySlug(slug)
  }
  loading.value = false
})
</script>

<style scoped>
.detail-page {
  min-height: 100vh;
  background: #000;
  color: #fff;
}

.loading,
.error-state {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 50vh;
  text-align: center;
  font-size: 1.2rem;
  opacity: 0.8;
}

.hero-section {
  position: relative;
  height: 60vh;
  min-height: 400px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: grayscale(20%) brightness(0.7);
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.3),
    rgba(0, 0, 0, 0.7)
  );
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 40px;
}

.hero-overlay h1 {
  font-size: 4rem;
  margin-bottom: 20px;
  background: linear-gradient(45deg, #fff, #ccc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 0 30px rgba(255, 255, 255, 0.2);
}

.visual-hook {
  font-size: 1.5rem;
  font-style: italic;
  opacity: 0.9;
  max-width: 600px;
}

.content-section {
  max-width: 1000px;
  margin: 0 auto;
  padding: 60px 20px;
}

.info-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 40px;
}

.tag {
  padding: 8px 20px;
  border-radius: 25px;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
}

.tag.primary {
  background: linear-gradient(45deg, #fff, #ddd);
  color: #000;
}

.tag.secondary {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.tag.accent {
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
  border: 1px solid rgba(255, 255, 255, 0.4);
}

.tag.tertiary {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.story-content h2 {
  font-size: 2.5rem;
  margin-bottom: 30px;
  color: #fff;
}

.story-text {
  line-height: 1.8;
  font-size: 1.1rem;
  color: #ddd;
  text-align: justify;
}

.gallery-section {
  margin-top: 60px;
}

.gallery-section h3 {
  font-size: 2rem;
  margin-bottom: 30px;
  color: #fff;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.gallery-item img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.gallery-item img:hover {
  transform: scale(1.05);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .hero-section {
    height: 50vh;
    min-height: 300px;
  }

  .hero-overlay h1 {
    font-size: 2.5rem;
  }

  .visual-hook {
    font-size: 1.2rem;
  }

  .content-section {
    padding: 40px 15px;
  }

  .story-content h2,
  .gallery-section h3 {
    font-size: 2rem;
  }

  .gallery-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .hero-overlay h1 {
    font-size: 2rem;
  }

  .info-tags {
    gap: 10px;
  }

  .tag {
    padding: 6px 16px;
    font-size: 0.8rem;
  }
}
</style>