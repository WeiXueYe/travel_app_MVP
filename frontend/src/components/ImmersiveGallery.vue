<template>
  <div class="immersive-gallery" @click.self="$emit('close')">
    <div class="gallery-content">
      <!-- 主图片展示 -->
      <div class="main-image">
        <img :src="travel?.cover_url" :alt="travel?.title">
      </div>

      <!-- 图片画廊 -->
      <div v-if="travel?.gallery_urls && travel.gallery_urls.length > 0" class="image-gallery">
        <div
          v-for="(url, index) in travel.gallery_urls"
          :key="index"
          class="gallery-thumbnail"
          @click="selectImage(index)"
        >
          <img :src="url" :alt="'Gallery image ' + (index + 1)">
        </div>
      </div>

      <!-- 内容详情 -->
      <div class="content-details">
        <h1>{{ travel?.title }}</h1>
        <p class="visual-hook">{{ travel?.visual_hook }}</p>

        <!-- 标签信息 -->
        <div class="travel-info">
          <div v-if="travel?.experience_type" class="info-item">
            <span>体验类型</span>
            <span>{{ travel.experience_type }}</span>
          </div>
          <div v-if="travel?.visual_style" class="info-item">
            <span>视觉风格</span>
            <span>{{ travel.visual_style }}</span>
          </div>
          <div v-if="travel?.rarity_level" class="info-item">
            <span>小众程度</span>
            <span>{{ travel.rarity_level }}</span>
          </div>
          <div v-if="travel?.emotional_tone" class="info-item">
            <span>情感基调</span>
            <span>{{ travel.emotional_tone }}</span>
          </div>
        </div>

        <!-- 完整故事 -->
        <div class="story-content">
          <h2>沉浸式体验</h2>
          <p>{{ travel?.content_story }}</p>
        </div>
      </div>

      <!-- 关闭按钮 -->
      <button class="close-button" @click="$emit('close')">✕</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Travel {
  id: number
  title: string
  slug: string
  visual_hook: string
  content_story: string
  cover_url: string
  gallery_urls?: string[]
  experience_type?: string
  visual_style?: string
  rarity_level?: string
  emotional_tone?: string
}

const props = defineProps<{
  travel?: Travel
}>()

defineEmits<{
  close: []
}>()

// 当前选中的图片索引
const currentImageIndex = ref(0)

// 选择图片
const selectImage = (index: number) => {
  currentImageIndex.value = index
}
</script>

<style scoped>
.immersive-gallery {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.95);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 40px;
  overflow-y: auto;
}

.gallery-content {
  max-width: 1200px;
  width: 100%;
  background: rgba(0, 0, 0, 0.8);
  border-radius: 20px;
  padding: 40px;
  position: relative;
  backdrop-filter: blur(20px);
}

.main-image {
  text-align: center;
  margin-bottom: 30px;
}

.main-image img {
  max-width: 100%;
  max-height: 500px;
  object-fit: contain;
  border-radius: 15px;
}

.image-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 15px;
  margin-bottom: 40px;
}

.gallery-thumbnail {
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 10px;
  overflow: hidden;
}

.gallery-thumbnail:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 30px rgba(255, 255, 255, 0.2);
}

.gallery-thumbnail img {
  width: 100%;
  height: 120px;
  object-fit: cover;
}

.content-details h1 {
  font-size: 2.5rem;
  margin-bottom: 15px;
  text-align: center;
  background: linear-gradient(45deg, #fff, #ccc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.visual-hook {
  text-align: center;
  font-style: italic;
  font-size: 1.3rem;
  opacity: 0.9;
  margin-bottom: 30px;
  color: #ddd;
}

.travel-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.info-item span:first-child {
  font-weight: bold;
  opacity: 0.7;
  font-size: 0.9rem;
}

.info-item span:last-child {
  color: #fff;
  font-size: 1.1rem;
}

.story-content h2 {
  font-size: 1.8rem;
  margin-bottom: 20px;
  color: #fff;
}

.story-content p {
  line-height: 1.8;
  font-size: 1.1rem;
  color: #ddd;
  text-align: justify;
}

.close-button {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 40px;
  height: 40px;
  border: none;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
  font-size: 1.5rem;
  cursor: pointer;
  border-radius: 50%;
  transition: all 0.3s ease;
}

.close-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .immersive-gallery {
    padding: 20px;
  }

  .gallery-content {
    padding: 20px;
  }

  .content-details h1 {
    font-size: 2rem;
  }

  .travel-info {
    grid-template-columns: 1fr;
  }
}
</style>