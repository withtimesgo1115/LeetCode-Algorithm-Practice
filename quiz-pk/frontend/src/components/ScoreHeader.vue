<template>
  <div class="score-header">
    <div class="player-score player-left">
      <AvatarBadge :nickname="myNickname" />
      <div class="score-info">
        <span class="player-name">{{ myNickname }}</span>
        <RankBadge :rank="myRank" />
        <span class="score-value">{{ myScore }}</span>
      </div>
    </div>
    <div class="game-center">
      <div class="question-counter">{{ qIndex + 1 }}/{{ totalQ }}</div>
      <TimerCircle :remaining="timerRemaining" :total="timerTotal" />
    </div>
    <div class="player-score player-right">
      <div class="score-info score-info-right">
        <span class="player-name">{{ oppNickname }}</span>
        <RankBadge :rank="oppRank" />
        <span class="score-value">{{ oppScore }}</span>
      </div>
      <AvatarBadge :nickname="oppNickname" />
    </div>
  </div>
</template>

<script setup>
import AvatarBadge from './AvatarBadge.vue'
import RankBadge from './RankBadge.vue'
import TimerCircle from './TimerCircle.vue'

defineProps({
  myNickname: String,
  myRank: Object,
  myScore: Number,
  oppNickname: String,
  oppRank: Object,
  oppScore: Number,
  qIndex: Number,
  totalQ: Number,
  timerRemaining: Number,
  timerTotal: Number
})
</script>

<style scoped>
.score-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.05);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.player-score {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
}
.player-right {
  justify-content: flex-end;
}
.score-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.score-info-right {
  align-items: flex-end;
}
.player-name {
  font-size: 13px;
  font-weight: 500;
  color: #fff;
}
.score-value {
  font-size: 18px;
  font-weight: 700;
  color: #ffd740;
}
.game-center {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}
.question-counter {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
  font-weight: 500;
}
</style>
