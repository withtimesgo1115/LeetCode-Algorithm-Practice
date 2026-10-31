import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useLeaderboardStore = defineStore('leaderboard', () => {
  const items = ref([])
  const loading = ref(false)
  const visible = ref(false)

  async function fetchLeaderboard() {
    loading.value = true
    try {
      const res = await fetch('/api/leaderboard')
      items.value = await res.json()
    } catch (e) {
      console.error('Failed to fetch leaderboard:', e)
    } finally {
      loading.value = false
    }
  }

  function show() {
    visible.value = true

    fetchLeaderboard()
  }

  function hide() {
    visible.value = false
  }

  return { items, loading, visible, fetchLeaderboard, show, hide }
})
