import { defineStore } from 'pinia'
import { ref } from 'vue'
import { getTravels, getTravelDetail } from '../api/travel'

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

export const useTravelStore = defineStore('travel', () => {
  // 状态
  const travels = ref<Travel[]>([])
  const loading = ref(false)
  const selectedTravel = ref<Travel | null>(null)
  const filters = ref({
    experience_types: [] as string[],
    visual_styles: [] as string[],
    rarity_levels: [] as string[],
    emotional_tones: [] as string[]
  })

  // 所有可能的筛选选项
  const allOptions = ref({
    experience_types: ['Extreme', 'Sensory', 'Cultural', 'Healing', 'Nature'],
    visual_styles: ['BlackWhite', 'Dramatic', 'Surreal', 'Warm', 'Vibrant'],
    rarity_levels: ['Rare', 'Unique'],
    emotional_tones: ['Awe', 'Adrenaline', 'Mystery', 'Peace', 'Wonder']
  })

  // 获取旅行列表
  async function fetchTravels() {
    loading.value = true
    try {
      // 总是获取所有数据，然后在前端进行筛选
      const allData = await getTravels()

      console.log('所有数据:', allData)
      
      // 确保 allData 是一个数组
      if (!Array.isArray(allData)) {
        console.error('获取的数据不是数组:', allData)
        travels.value = []
        return
      }
      
      console.log('所有数据:', allData)
      console.log('筛选条件:', filters.value)
      
      // 在前端实现筛选
      // 只要卡片满足任何一个筛选条件，就显示出来
      const filteredData = allData.filter((t: Travel) => {
        // 检查是否有任何筛选条件被选中
        const hasActiveFilters = Object.values(filters.value).some((arr: string[]) => arr.length > 0)
        

        console.log('当前卡片:', t, '是否有筛选条件:', hasActiveFilters)

        // 如果没有筛选条件，显示所有卡片
        if (!hasActiveFilters) {
          return true
        }
        
        // 检查卡片是否满足任何一个筛选条件
        // 按体验类型筛选
        if (filters.value.experience_types.length > 0 && t.experience_type) {
          if (filters.value.experience_types.some(filter => t.experience_type?.includes(filter))) {
            return true
          }
        }
        
        // 按视觉风格筛选
        if (filters.value.visual_styles.length > 0 && t.visual_style) {
          if (filters.value.visual_styles.some(filter => t.visual_style?.includes(filter))) {
            return true
          }
        }
        
        // 按小众程度筛选
        if (filters.value.rarity_levels.length > 0 && t.rarity_level) {
          if (filters.value.rarity_levels.some(filter => t.rarity_level?.includes(filter))) {
            return true
          }
        }
        
        // 按情感基调筛选
        if (filters.value.emotional_tones.length > 0 && t.emotional_tone) {
          if (filters.value.emotional_tones.some(filter => t.emotional_tone?.includes(filter))) {
            return true
          }
        }
        
        // 如果没有满足任何筛选条件，不显示
        return false
      })
      
      console.log('最终筛选后的数据:', filteredData)
      travels.value = filteredData
      console.log('travels.value:', travels.value)
    } catch (error) {
      console.error('获取旅行数据失败:', error)
      // 出错时设置为空数组，避免页面显示错误
      travels.value = []
    } finally {
      loading.value = false
    }
  }

  // 根据slug获取单个旅行详情
  async function getTravelBySlug(slug: string) {
    try {
      const data = await getTravelDetail(slug)
      return data
    } catch (error) {
      console.error('获取旅行详情失败:', error)
      return null
    }
  }

  // 更新筛选条件并重新获取
  async function updateFiltersAndFetch(newFilters: Partial<typeof filters.value>) {
    filters.value = { ...filters.value, ...newFilters }
    await fetchTravels()
  }

  // 清空筛选条件并重新获取
  async function clearFiltersAndFetch() {
    filters.value = {
      experience_types: [],
      visual_styles: [],
      rarity_levels: [],
      emotional_tones: []
    }
    await fetchTravels()
  }

  return {
    travels,
    loading,
    selectedTravel,
    filters,
    allOptions,
    fetchTravels,
    getTravelBySlug,
    updateFiltersAndFetch,
    clearFiltersAndFetch
  }
})