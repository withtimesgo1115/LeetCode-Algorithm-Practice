<template>
  <t-popup v-model:visible="visible" placement="bottom" :close-on-overlay-click="true">
    <div class="leaderboard-modal">
      <div class="modal-header">
        <h3>排行榜</h3>
        <t-button theme="default" variant="text" size="small" @click="visible = false">
          ✕
        </t-button>
      </div>
      <div class="modal-content">
        <div v-if="loading" class="loading">加载中...</div>
        <div v-else-if="items.length === 0" class="empty">暂无数据</div>
        <t-cell-group v-else>
          <t-cell
            v-for="(item, index) in items"
            :key="index"
            :title="item.nickname"
            :description="`${item.games_won}胜 / ${item.games_played}场 (${item.win_rate}%)`"
          >
            <template #leftIcon>
              <div class="rank-number" :class="getRankClass(index)">
                {{ index + 1 }}
              </div>
            </template>
            <template #rightIcon>
              <RankBadge :rank="item.rank" />
            </template>
          </t-cell>
        </t-cell-group>
      </div>
    </div>
  </t-popup>
</template>

<script setup>
import { computed } from 'vue'
import { useLeaderboardStore } from '@/stores/leaderboard'
import RankBadge from './RankBadge.vue'

const store = useLeaderboardStore()
const visible = computed({
  get: () => store.visible,
  set: (val) => val ? store.show() : store.hide()
})
const items = computed(() => store.items)
const loading = computed(() => store.loading)

function getRankClass(index) {
  if (index === 0) return 'gold'
  if (index === 1) return 'silver'
  if (index === 2) return 'bronze'
  return ''
}
</script>

<style scoped>
.leaderboard-modal {
  background: #1a1a2e;
  border-radius: 16px 16px 0 0;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
}
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.modal-header h3 {
  margin: 0;
  font-size: 18px;
  color: #fff;
}
.modal-content {
  overflow-y: auto;
  padding: 16px 0;
}
.loading, .empty {
  text-align: center;
  padding: 40px 20px;
  color: rgba(255, 255, 255, 0.6);
}
.rank-number {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 14px;
  background: rgba(255, 255, 255, 0.1);
  color: #fff;
}
.rank-number.gold {
  background: linear-gradient(135deg, #ffd700, #ffed4e);
  color: #000;
}
.rank-number.silver {
  background: linear-gradient(135deg, #c0c0c0, #e8e8e8);
  color: #000;
}
.rank-number.bronze {
  background: linear-gradient(135deg, #cd7f32, #e8a87c);
  color: #000;
}
</style>
