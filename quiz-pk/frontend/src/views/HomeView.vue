<template>
  <div class="home-view">
    <div class="home-container">
      <h1 class="game-title gradient-text">知识PK</h1>
      <p class="subtitle">实时对战知识问答</p>

      <div v-if="userStore.rank" class="user-rank-display">
        <span class="rank-icon">{{ userStore.rank.icon }}</span>
        <span class="rank-name">{{ userStore.rank.name }}</span>
      </div>

      <div class="nickname-input-group">
        <t-input
          v-model="nickname"
          placeholder="输入你的昵称"
          :maxlength="8"
          :disabled="!!userStore.nickname"
          @enter="enterNickname"
        />
        <t-button
          theme="primary"
          :disabled="!nickname.trim() || !!userStore.nickname"
          @click="enterNickname"
        >
          进入
        </t-button>
      </div>

      <div class="category-grid">
        <CategoryCard
          v-for="(cat, i) in categories"
          :key="cat.category"
          :name="cat.category"
          :icon="CATEGORY_ICONS[cat.category] || '📖'"
          :gradient="CATEGORY_GRADIENTS[i % CATEGORY_GRADIENTS.length]"
          :disabled="!canPlay"
          @click="selectCategory(cat.category)"
        />
        <CategoryCard
          name="随机模式"
          icon="🎲"
          :gradient="CATEGORY_GRADIENTS[0]"
          :disabled="!canPlay"
          class="random-mode"
          @click="selectCategory('随机模式')"
        />
      </div>

      <div class="home-footer">
        <t-button
          :theme="singleMode ? 'primary' : 'warning'"
          variant="outline"
          @click="singleMode = !singleMode"
        >
          {{ singleMode ? '单人模式 ✓' : '单人练习' }}
        </t-button>
        <t-button theme="success" variant="outline" @click="leaderboardStore.show()">
          🏆 排行榜
        </t-button>
      </div>
    </div>

    <LeaderboardModal />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useGameStore } from '@/stores/game'
import { useLeaderboardStore } from '@/stores/leaderboard'
import { useSocket } from '@/composables/useSocket'
import { CATEGORY_ICONS, CATEGORY_GRADIENTS } from '@/utils/constants'
import CategoryCard from '@/components/CategoryCard.vue'
import LeaderboardModal from '@/components/LeaderboardModal.vue'

const userStore = useUserStore()
const gameStore = useGameStore()
const leaderboardStore = useLeaderboardStore()
const socket = useSocket()
const router = useRouter()

const nickname = ref(userStore.nickname)
const categories = ref([])
const singleMode = ref(false)

const canPlay = computed(() => !!userStore.nickname)

onMounted(async () => {
  await loadCategories()
})

async function loadCategories() {
  try {
    const res = await fetch('/api/categories')
    categories.value = await res.json()
  } catch (e) {
    console.error('Failed to load categories:', e)
  }
}

function enterNickname() {
  const name = nickname.value.trim()
  if (name.length < 1 || name.length > 8) return
  userStore.nickname = name
  localStorage.setItem('quiz_nickname', name)
  socket.join(name, userStore.userId)
}

function selectCategory(category) {
  if (!canPlay.value) return
  gameStore.category = category
  gameStore.singleMode = singleMode.value
  gameStore.screen = 'matching'
  router.push('/matching')
  socket.selectCategory(category, singleMode.value ? 'single' : 'pvp')
}
</script>

<style scoped>
.home-view {
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.home-container {
  max-width: 500px;
  width: 100%;
}
.game-title {
  font-size: 52px;
  font-weight: 800;
  text-align: center;
  margin-bottom: 8px;
  text-shadow: 0 2px 10px rgba(102, 126, 234, 0.3);
}
.subtitle {
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 32px;
  font-size: 16px;
}
.user-rank-display {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  background: rgba(102, 126, 234, 0.2);
  border: 2px solid rgba(102, 126, 234, 0.5);
  border-radius: 24px;
  margin: 0 auto 24px;
  width: fit-content;
}
.rank-icon {
  font-size: 22px;
}
.rank-name {
  font-size: 15px;
  color: #fff;
  font-weight: 600;
}
.nickname-input-group {
  display: flex;
  gap: 12px;
  margin-bottom: 32px;
}
.nickname-input-group :deep(.t-input) {
  flex: 1;
  background: rgba(255, 255, 255, 0.15);
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 12px;
  color: #fff;
  font-size: 16px;
  padding: 0 16px;
}
.nickname-input-group :deep(.t-input) input {
  color: #fff;
}
.nickname-input-group :deep(.t-input) input::placeholder {
  color: rgba(255, 255, 255, 0.6);
}
.nickname-input-group :deep(.t-input--disabled) {
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.15);
}
.nickname-input-group :deep(.t-button) {
  min-width: 80px;
  height: 48px;
  font-size: 16px;
  font-weight: 600;
}
.nickname-input-group :deep(.t-button--disabled) {
  background: rgba(102, 126, 234, 0.3);
  border-color: rgba(102, 126, 234, 0.4);
  color: rgba(255, 255, 255, 0.5);
}
.category-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-bottom: 32px;
}
.random-mode {
  grid-column: 1 / -1;
}
.home-footer {
  display: flex;
  gap: 12px;
  margin-top: 8px;
}
.home-footer :deep(.t-button) {
  flex: 1;
  height: 48px;
  font-size: 15px;
  font-weight: 600;
}
.home-footer :deep(.t-button--theme-warning) {
  background: rgba(255, 215, 64, 0.15);
  border-color: rgba(255, 215, 64, 0.5);
  color: #ffd740;
}
.home-footer :deep(.t-button--theme-success) {
  background: rgba(0, 230, 118, 0.15);
  border-color: rgba(0, 230, 118, 0.5);
  color: #00e676;
}
</style>
