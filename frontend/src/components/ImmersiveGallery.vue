<template>
  <div class="immersive-gallery" @click.self="$emit('close')">
    <div class="gallery-content">
      <!-- 主图片展示 -->
      <div class="main-image">
        <img :src="mainImageUrl" :alt="travel?.title">
      </div>

      <!-- 图片画廊 -->
      <div v-if="displayGalleryUrls.length > 0" class="image-gallery">
        <div
          v-for="(url, index) in displayGalleryUrls"
          :key="index"
          class="gallery-thumbnail"
          :class="{ active: url === mainImageUrl }"
          @click="swapImage(url, index)"
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
import { ref, computed } from 'vue'

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

// 主图片URL（响应式，可以在详情页内交换）
const mainImageUrl = ref(props.travel?.cover_url || '')

// 原始画廊图片列表
const originalGalleryUrls = computed(() => props.travel?.gallery_urls || [])

// 原始封面图片
const originalCoverUrl = computed(() => props.travel?.cover_url || '')

// 画廊图片列表（包含所有非主图片）
const displayGalleryUrls = computed(() => {
  const allImages = [originalCoverUrl.value, ...originalGalleryUrls.value]
  // 过滤掉当前主图片，返回其他所有图片
  return allImages.filter(url => url !== mainImageUrl.value)
})

// 交换主图片和画廊图片
const swapImage = (clickedUrl: string, index: number) => {
  mainImageUrl.value = clickedUrl
  index
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
  align-items: flex-start;
  z-index: 1000;
  padding: 20px;
  overflow-y: auto;
  box-sizing: border-box;
  padding-top: 40px;
}

.gallery-content {
  max-width: 1200px;
  width: 100%;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.9) 0%, rgba(0, 0, 0, 0.7) 100%);
  border-radius: 25px;
  padding: 60px;
  position: relative;
  backdrop-filter: blur(20px);
  box-sizing: border-box;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
  overflow: hidden;
}

.gallery-content::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at 50% 20%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

.main-image {
  text-align: center;
  margin-bottom: 30px;
  width: 100%;
  overflow: hidden;
  position: relative;
  border-radius: 15px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
  transition: all 0.3s ease;
}

.main-image:hover {
  transform: translateY(-5px);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6);
}

.main-image img {
  width: 100%;
  max-height: 600px;
  object-fit: cover;
  border-radius: 15px;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.main-image::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.1) 0%, rgba(0, 0, 0, 0.3) 100%);
  border-radius: 15px;
  z-index: 1;
  pointer-events: none;
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
  position: relative;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
  background: rgba(0, 0, 0, 0.2);
}

.gallery-thumbnail:hover {
  transform: scale(1.08);
  box-shadow: 0 15px 30px rgba(255, 255, 255, 0.3);
  z-index: 20;
}

.gallery-thumbnail.active {
  border: 3px solid #fff;
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.6), 0 15px 30px rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
  z-index: 30;
}

.gallery-thumbnail img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: all 0.4s ease;
}

.gallery-thumbnail:hover img {
  transform: scale(1.1);
}

.gallery-thumbnail::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.1) 0%, rgba(0, 0, 0, 0.2) 100%);
  z-index: 1;
  pointer-events: none;
  transition: all 0.3s ease;
}

.gallery-thumbnail:hover::before {
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.05) 0%, rgba(0, 0, 0, 0.1) 100%);
}

.content-details h1 {
  font-size: 3rem;
  margin-bottom: 15px;
  text-align: center;
  background: linear-gradient(45deg, #fff, #ccc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 0 30px rgba(255, 255, 255, 0.3);
  letter-spacing: -0.5px;
  font-weight: 700;
  position: relative;
  z-index: 1;
}

.content-details {
  position: relative;
  z-index: 1;
}

.visual-hook {
  text-align: center;
  font-style: italic;
  font-size: 1.4rem;
  opacity: 0.9;
  margin-bottom: 40px;
  color: #ddd;
  font-weight: 300;
  letter-spacing: 0.5px;
}

.travel-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 25px;
  margin-bottom: 50px;
  padding: 30px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 20px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 12px;
  transition: all 0.3s ease;
}

.info-item:hover {
  transform: translateY(-3px);
  background: rgba(0, 0, 0, 0.4);
  box-shadow: 0 5px 15px rgba(255, 255, 255, 0.1);
}

.info-item span:first-child {
  font-weight: 600;
  opacity: 0.7;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.info-item span:last-child {
  color: #fff;
  font-size: 1.2rem;
  font-weight: 500;
}

.story-content h2 {
  font-size: 2.2rem;
  margin-bottom: 30px;
  color: #fff;
  text-align: center;
  position: relative;
  padding-bottom: 15px;
}

.story-content h2::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
  height: 3px;
  background: linear-gradient(90deg, #fff, transparent);
  border-radius: 2px;
}

.story-content p {
  line-height: 1.8;
  font-size: 1.15rem;
  color: #ddd;
  text-align: justify;
  background: rgba(0, 0, 0, 0.2);
  padding: 30px;
  border-radius: 15px;
  border-left: 4px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.close-button {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 45px;
  height: 45px;
  border: none;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
  color: #fff;
  font-size: 1.6rem;
  cursor: pointer;
  border-radius: 50%;
  transition: all 0.3s ease;
  z-index: 100;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 300;
}

.close-button:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.1) 100%);
  transform: scale(1.15);
  box-shadow: 0 8px 20px rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.2);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .immersive-gallery {
    padding: 10px;
    padding-top: 30px;
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
  
  .main-image img {
    max-height: 300px;
  }
}

@media (max-width: 480px) {
  .immersive-gallery {
    padding: 5px;
    padding-top: 20px;
  }

  .gallery-content {
    padding: 15px;
  }

  .content-details h1 {
    font-size: 1.5rem;
  }
  
  .visual-hook {
    font-size: 1rem;
  }
  
  .main-image img {
    max-height: 200px;
  }
}
</style>