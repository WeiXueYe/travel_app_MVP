<template>
  <div class="travel-card" @click="$emit('click')">
    <div class="card-image">
      <img :src="travel.cover_url" :alt="travel.title" class="hover-glow">
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ travel.title }}</h3>
      <p class="visual-hook">{{ travel.visual_hook }}</p>
      <p class="story-preview">{{ storyPreview }}</p>
      <div class="card-tags">
        <span v-if="travel.experience_type" class="tag">{{ travel.experience_type }}</span>
        <span v-if="travel.visual_style" class="tag">{{ travel.visual_style }}</span>
        <span v-if="travel.emotional_tone" class="tag">{{ travel.emotional_tone }}</span>
      </div>
    </div>
  </div>
</template>
 
<script setup lang="ts">
import { computed } from 'vue'

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
  travel: Travel
}>()

defineEmits<{
  click: []
}>()

// 截取故事预览文本
const storyPreview = computed(() => {
  if (!props.travel.content_story) return ''
  const preview = props.travel.content_story.substring(0, 120)
  return preview + (preview.length >= 120 ? '...' : '')
})
</script>

<style scoped>
.travel-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 15px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.travel-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 40px rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.3);
}

.card-image {
  position: relative;
  height: 240px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.travel-card:hover .card-image img {
  transform: scale(1.1);
}

.card-content {
  padding: 24px;
}

.card-title {
  font-size: 1.4rem;
  font-weight: 300;
  margin-bottom: 12px;
  line-height: 1.3;
  color: #fff;
}

.visual-hook {
  font-style: italic;
  opacity: 0.9;
  margin-bottom: 16px;
  font-size: 1rem;
  color: #ddd;
}

.story-preview {
  opacity: 0.8;
  line-height: 1.6;
  margin-bottom: 20px;
  color: #ccc;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag {
  padding: 6px 14px;
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
  border-radius: 20px;
  font-size: 0.85rem;
  opacity: 0.8;
  transition: all 0.3s ease;
}

.tag:hover {
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
  transform: translateY(-2px);
}
</style>