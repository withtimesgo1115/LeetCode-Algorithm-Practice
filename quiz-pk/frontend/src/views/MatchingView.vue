<template>
  <div class="matching-view">
    <div class="matching-container">
      <MatchingAnimation />
      <h2>正在匹配对手...</h2>
      <p class="matching-text">{{ statusText }}</p>

      <div class="matching-players">
        <div class="matching-player">
          <AvatarBadge :nickname="userStore.nickname" />
          <span class="player-name">{{ userStore.nickname }}</span>
          <RankBadge :rank="userStore.rank" />
        </div>

        <span class="vs-text">VS</span>

        <div class="matching-player">
          <AvatarBadge v-if="gameStore.opponent" :nickname="gameStore.opponent" />
          <div v-else class="avatar-badge unknown">?</div>
          <span class="player-name">{{ gameStore.opponent || '等待中...' }}</span>
          <RankBadge v-if="gameStore.opponentRank" :rank="gameStore.opponentRank" />
        </div>
      </div>

      <t-button theme="danger" variant="outline" @click="cancelMatch">
        取消匹配
      </t-button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useGameStore } from '@/stores/game'
import { useSocket } from '@/composables/useSocket'
import MatchingAnimation from '@/components/MatchingAnimation.vue'
import AvatarBadge from '@/components/AvatarBadge.vue'
import RankBadge from '@/components/RankBadge.vue'

const userStore = useUserStore()
const gameStore = useGameStore()
const socket = useSocket()
const router = useRouter()

const statusText = computed(() => {
  if (gameStore.matchStatus === 'waiting') {
    const label = gameStore.category === '随机模式' ? '随机模式' : `「${gameStore.category}」`
    return `正在等待对手选择${label}...`
  }
  const label = gameStore.category === '随机模式' ? '随机模式' : `「${gameStore.category}」`
  return `正在寻找${label}的对手...`
})

function cancelMatch() {
  socket.cancelMatch()
  gameStore.screen = 'home'
  gameStore.reset()
  router.push('/')
}
</script>

<style scoped>
.matching-view {
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.matching-container {
  max-width: 500px;
  width: 100%;
  text-align: center;
}
.matching-container h2 {
  font-size: 24px;
  margin-bottom: 12px;
  color: #fff;
}
.matching-text {
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 40px;
}
.matching-players {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 30px;
  margin-bottom: 40px;
}
.matching-player {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.player-name {
  font-size: 14px;
  color: #fff;
  font-weight: 500;
}
.vs-text {
  font-size: 32px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.3);
}
.avatar-badge.unknown {
  background: rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.5);
  font-size: 24px;
}
</style>
