<template>
  <router-view v-slot="{ Component }">
    <transition name="page-fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
  <t-toast v-model:visible="toastVisible" :content="toastMsg" :duration="2000" />
</template>

<script setup>
import { ref, onMounted, provide } from 'vue'
import { useUserStore } from '@/stores/user'
import { useGameStore } from '@/stores/game'
import { useSocket } from '@/composables/useSocket'
import { GAME_EVENTS, SCREENS } from '@/utils/constants'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const gameStore = useGameStore()
const router = useRouter()
const socket = useSocket()

const toastVisible = ref(false)
const toastMsg = ref('')

function showToast(msg) {
  toastMsg.value = msg
  toastVisible.value = true
}

provide('showToast', showToast)

onMounted(() => {
  userStore.loadFromStorage()
  socket.connect()

  if (userStore.userId && userStore.nickname) {
    socket.join(userStore.nickname, userStore.userId)
  }
})
</script>

<style>
html, body {
  overscroll-behavior: none;
}
</style>
