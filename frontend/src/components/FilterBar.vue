<template>
  <div class="filter-bar">
    <div class="container">
      <h2>多维筛选</h2>
      <div class="filter-groups">
        <div v-for="(options, groupName) in allOptions" :key="groupName" class="filter-group">
          <h3>{{ getGroupName(groupName) }}</h3>
          <div class="filter-tags">
            <button
              v-for="option in options"
              :key="option"
              :class="{ active: filters[groupName].includes(option) }"
              @click="toggleFilter(groupName, option)"
            >
              {{ option }}
            </button>
          </div>
        </div>
      </div>
      <button class="clear-filters" @click="clearAllFilters">清空所有筛选</button>

      <!-- 当前筛选状态显示 -->
      <div v-if="hasActiveFilters" class="active-filters">
        <span>当前筛选:</span>
        <div class="current-filters">
          <span v-for="filter in activeFiltersText" :key="filter" class="active-filter-tag">
            {{ filter }}
          </span>
        </div>
        <button class="clear-all-btn" @click="clearAllFilters">全部清除</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useTravelStore } from '../stores/travel'

const travelStore = useTravelStore()

const filters = computed(() => travelStore.filters)
const allOptions = computed(() => travelStore.allOptions)

const getGroupName = (key: string): string => {
  const names: Record<string, string> = {
    experience_types: '体验类型',
    visual_styles: '视觉风格',
    rarity_levels: '小众程度',
    emotional_tones: '情感基调'
  }
  return names[key] || key
}

// 是否有活跃的筛选条件
const hasActiveFilters = computed(() => {
  if (!filters.value) return false
  return Object.values(filters.value).some((arr: any[]) => arr.length > 0)
})

// 获取当前筛选条件的文本显示
const activeFiltersText = computed(() => {
  const texts: string[] = []

  if (filters.value) {
    Object.entries(filters.value).forEach(([key, values]) => {
      if ((values as any[]).length > 0) {
        (values as any[]).forEach((value: string) => {
          texts.push(`${getGroupName(key)}: ${value}`)
        })
      }
    })
  }

  return texts
})

const toggleFilter = async (groupName: string, option: string) => {
  if (!filters.value) return
  
  const currentFilters = [...(filters.value as any)[groupName]]
  const index = currentFilters.indexOf(option)

  if (index > -1) {
    currentFilters.splice(index, 1)
  } else {
    currentFilters.push(option)
  }

  // 如果有变化，更新筛选条件
  if (JSON.stringify(currentFilters) !== JSON.stringify((filters.value as any)[groupName])) {
    await travelStore.updateFiltersAndFetch({ [groupName]: currentFilters })
  }
}

const clearAllFilters = async () => {
  await travelStore.clearFiltersAndFetch()
}
</script>

<style scoped>
.filter-bar {
  padding: 40px 0;
  background: rgba(255, 255, 255, 0.02);
  backdrop-filter: blur(10px);
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.filter-bar h2 {
  text-align: center;
  margin-bottom: 40px;
  font-size: 2rem;
  opacity: 0.9;
  font-weight: 300;
}

.filter-groups {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  margin-bottom: 30px;
}

.filter-group h3 {
  margin-bottom: 15px;
  color: #fff;
  opacity: 0.8;
  font-size: 1.1rem;
  font-weight: 500;
}

.filter-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.filter-tags button {
  padding: 8px 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  background: transparent;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border-radius: 20px;
  font-size: 0.9rem;
  position: relative;
  overflow: hidden;
}

.filter-tags button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: left 0.5s;
}

.filter-tags button:hover {
  border-color: rgba(255, 255, 255, 0.5);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.filter-tags button:hover::before {
  left: 100%;
}

.filter-tags button.active {
  background: linear-gradient(45deg, #fff, #ddd);
  color: #000;
  border-color: transparent;
  box-shadow: 0 5px 20px rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

.clear-filters {
  display: block;
  margin: 0 auto;
  padding: 12px 24px;
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #fff;
  cursor: pointer;
  border-radius: 25px;
  transition: all 0.3s ease;
  font-size: 0.95rem;
}

.clear-filters:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.5);
  transform: translateY(-2px);
}

/* 活跃筛选状态 */
.active-filters {
  margin-top: 30px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 15px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.active-filters span {
  font-weight: bold;
  opacity: 0.8;
  margin-right: 15px;
}

.current-filters {
  display: inline-block;
  margin-right: 15px;
}

.active-filter-tag {
  display: inline-block;
  padding: 6px 12px;
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05));
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 15px;
  margin-right: 8px;
  margin-bottom: 8px;
  font-size: 0.85rem;
  transition: all 0.3s ease;
}

.active-filter-tag:hover {
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0.15));
  transform: translateY(-1px);
}

.clear-all-btn {
  padding: 6px 12px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #fff;
  border-radius: 15px;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.3s ease;
}

.clear-all-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-1px);
}

/* 响应式设计 */
@media (max-width: 768px) {
  .filter-bar {
    padding: 30px 0;
  }

  .filter-bar h2 {
    font-size: 1.6rem;
    margin-bottom: 30px;
  }

  .filter-groups {
    grid-template-columns: 1fr;
    gap: 25px;
  }

  .active-filters {
    padding: 15px;
  }
}
</style>