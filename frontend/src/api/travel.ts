import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
})

// 构建筛选参数
function buildFilterParams(filters: {
  experience_types?: string[]
  visual_styles?: string[]
  rarity_levels?: string[]
  emotional_tones?: string[]
}) {
  const params: any = {}

  if (filters.experience_types?.length) {
    params.experience_types = filters.experience_types.join(',')
  }
  if (filters.visual_styles?.length) {
    params.visual_styles = filters.visual_styles.join(',')
  }
  if (filters.rarity_levels?.length) {
    params.rarity_levels = filters.rarity_levels.join(',')
  }
  if (filters.emotional_tones?.length) {
    params.emotional_tones = filters.emotional_tones.join(',')
  }

  return params
}

export const getTravels = async () => {
  const response = await api.get('/travels')
  return response.data
}

export const getTravelDetail = async (slug: string) => {
  const response = await api.get(`/travels/${slug}`)
  return response.data
}