<template>
  <div class="result-view">
    <ConfettiEffect :active="isWin" />

    <div class="result-container">
      <div class="result-badge">{{ resultEmoji }}</div>
      <h2 class="result-title" :style="{ color: resultColor }">{{ resultText }}</h2>

      <div class="result-players">
        <div class="result-player">
          <AvatarBadge :nickname="userStore.nickname" />
          <div class="player-info">
            <div class="player-name">{{ userStore.nickname }}</div>
            <RankBadge :rank="gameStore.myRank || userStore.rank" />
          </div>
          <div class="player-score">{{ gameStore.myScore }}</div>
        </div>

        <div class="result-player">
          <AvatarBadge :nickname="gameStore.opponent" />
          <div class="player-info">
            <div class="player-name">{{ gameStore.opponent }}</div>
            <RankBadge :rank="gameStore.opponentRank" />
          </div>
          <div class="player-score">{{ gameStore.oppScore }}</div>
        </div>
      </div>

      <div class="result-actions">
        <t-button theme="primary" @click="playAgain">再来一局</t-button>
        <t-button theme="default" @click="backHome">返回首页</t-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useGameStore } from '@/stores/game'
import { useSocket } from '@/composables/useSocket'
import AvatarBadge from '@/components/AvatarBadge.vue'
import RankBadge from '@/components/RankBadge.vue'
import ConfettiEffect from '@/components/ConfettiEffect.vue'

const userStore = useUserStore()
const gameStore = useGameStore()
const socket = useSocket()
const router = useRouter()

const result = computed(() => gameStore.resultData?.result || 'draw')
const isWin = computed(() => result.value === 'win')

const resultEmoji = computed(() => {
  if (result.value === 'win') return '🏆'
  if (result.value === 'lose') return '😢'
  return '🤝'
})

const resultText = computed(() => {
  if (result.value === 'win') return '你赢了！'
  if (result.value === 'lose') return '你输了'
  return '平局！'
})

const resultColor = computed(() => {
  if (result.value === 'win') return '#00e676'
  if (result.value === 'lose') return '#ff5252'
  return '#ffd740'
})

function playAgain() {
  gameStore.reset()
  gameStore.screen = 'matching'
  router.push('/matching')
  socket.selectCategory(gameStore.category, gameStore.singleMode ? 'single' : 'pvp')
}

function backHome() {
  gameStore.reset()
  gameStore.screen = 'home'
  router.push('/')
}
</script>

<style scoped>
.result-view {
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.result-container {
  max-width: 500px;
  width: 100%;
  text-align: center;
}
.result-badge {
  font-size: 80px;
  margin-bottom: 20px;
  animation: bounce 0.6s ease-out;
}
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}
.result-title {
  font-size: 32px;
  font-weight: 800;
  margin-bottom: 40px;
}
.result-players {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 40px;
}
.result-player {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px;
}
.player-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-align: left;
}
.player-name {
  font-size: 16px;
  font-weight: 600;
  color: #fff;
}
.player-score {
  font-size: 28px;
  font-weight: 800;
  color: #ffd740;
}
.result-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.result-actions :deep(.t-button) {
  width: 100%;
}
</style>
