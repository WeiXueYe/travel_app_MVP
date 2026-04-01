<template>
  <div id="app">
    <HeroSection />
    <FilterBar />
    <div class="container">
      <div v-if="loading" class="loading">加载中...</div>
      <div v-else class="travel-grid">
        <TravelCard
          v-for="travel in travelStore.travels"
          :key="travel.id"
          :travel="travel"
          @click="showDetail(travel)"
        />
      </div>
    </div>

    <!-- 详情弹窗 -->
    <Teleport to="body">
      <div v-if="selectedTravel" class="modal-overlay" @click.self="closeDetail">
        <ImmersiveGallery :travel="selectedTravel" @close="closeDetail" />
      </div>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import HeroSection from './components/HeroSection.vue'
import FilterBar from './components/FilterBar.vue'
import TravelCard from './components/TravelCard.vue'
import ImmersiveGallery from './components/ImmersiveGallery.vue'
import { useTravelStore } from './stores/travel'

const travelStore = useTravelStore()
// const { loading, fetchTravels, getTravelBySlug } = travelStore
const { loading, fetchTravels } = travelStore

// 监听 travels 变化
watch(() => travelStore.travels, (newTravels) => {
  console.log('App.vue - travels 变化:', newTravels)
}, { deep: true })

const selectedTravel = ref<any>(null)

const showDetail = (travel: any) => {
  selectedTravel.value = travel
}

const closeDetail = () => {
  selectedTravel.value = null
}

onMounted(() => {
  fetchTravels()
})
</script>

<style>
#app {
  min-height: 100vh;
  background: #000;
  color: #fff;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
}

.travel-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 30px;
  padding: 40px 0;
}

.loading {
  text-align: center;
  font-size: 1.3rem;
  opacity: 0.8;
  padding: 80px;
  background: rgba(255, 255, 255, 0.02);
  border-radius: 15px;
  backdrop-filter: blur(10px);
}

.modal-overlay {
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
  backdrop-filter: blur(5px);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .container {
    padding: 0 15px;
  }

  .travel-grid {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 20px 0;
  }

  .loading {
    padding: 40px 20px;
  }
}

/* 滚动条美化 */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
}

::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.5);
}
</style>