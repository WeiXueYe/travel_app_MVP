<template>
  <section class="hero-section">
    <div class="container">
      <h1 class="emotional-title">
        100种不可思议旅行
      </h1>
      <p class="visual-hook">
        在世界的边缘，发现内心的奇迹
      </p>
      <div class="hero-image">
        <img
          :src="heroImageUrl"
          alt="不可思议旅行"
          class="hover-glow"
        >
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// 随机英雄图片
const heroImageUrl = ref('https://picsum.photos/seed/hero-mystery/1200/600')
</script>

<style scoped>
.hero-section {
  padding: 80px 0;
  text-align: center;
  background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,0,0,0.6));
}

.emotional-title {
  font-size: 4rem;
  margin-bottom: 20px;
  background: linear-gradient(45deg, #fff, #ccc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 0 30px rgba(255, 255, 255, 0.1);
}

.visual-hook {
  font-size: 1.5rem;
  margin-bottom: 40px;
  opacity: 0.9;
  font-style: italic;
}

.hero-image img {
  border-radius: 15px;
  filter: grayscale(20%) brightness(0.8);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
  transition: all 0.4s ease;
}

.hero-image img:hover {
  filter: grayscale(0%) brightness(1);
  transform: scale(1.02);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .emotional-title {
    font-size: 2.5rem;
  }

  .visual-hook {
    font-size: 1.2rem;
  }

  .hero-section {
    padding: 60px 0;
  }
}
</style>