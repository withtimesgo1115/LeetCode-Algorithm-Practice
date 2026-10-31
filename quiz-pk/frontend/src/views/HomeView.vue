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
          :disabled="!!userStore.nickname"
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
          :theme="singleMode ? 'primary' : 'default'"
          @click="singleMode = !singleMode"
        >
          {{ singleMode ? '单人模式 ✓' : '单人练习' }}
        </t-button>
        <t-button theme="default" @click="leaderboardStore.show()">
          排行榜
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
  font-size: 48px;
  font-weight: 800;
  text-align: center;
  margin-bottom: 8px;
}
.subtitle {
  text-align: center;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 24px;
}
.user-rank-display {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  margin: 0 auto 24px;
  width: fit-content;
}
.rank-icon {
  font-size: 20px;
}
.rank-name {
  font-size: 14px;
  color: #fff;
}
.nickname-input-group {
  display: flex;
  gap: 12px;
  margin-bottom: 32px;
}
.nickname-input-group :deep(.t-input) {
  flex: 1;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 10px;
  color: #fff;
}
.category-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-bottom: 24px;
}
.random-mode {
  grid-column: 1 / -1;
}
.home-footer {
  display: flex;
  gap: 12px;
}
.home-footer :deep(.t-button) {
  flex: 1;
}
</style>
