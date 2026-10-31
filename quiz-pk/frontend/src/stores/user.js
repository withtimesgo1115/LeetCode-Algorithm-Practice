import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUserStore = defineStore('user', () => {
  const userId = ref(null)
  const nickname = ref('')
  const rank = ref(null)

  function loadFromStorage() {
    userId.value = localStorage.getItem('quiz_uid')
    nickname.value = localStorage.getItem('quiz_nickname') || ''
  }

  function saveToStorage() {
    if (userId.value) localStorage.setItem('quiz_uid', userId.value)
    if (nickname.value) localStorage.setItem('quiz_nickname', nickname.value)
  }

  function setFromAuth(data) {
    userId.value = data.userId
    nickname.value = data.nickname || nickname.value
    rank.value = data.rank
    saveToStorage()
  }

  return { userId, nickname, rank, loadFromStorage, saveToStorage, setFromAuth }
})
