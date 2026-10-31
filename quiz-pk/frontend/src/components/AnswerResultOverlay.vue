<template>
  <div class="answer-result-overlay" :class="{ show: visible }">
    <div class="result-content">
      <div class="result-icon" :style="{ color: correct ? '#00e676' : '#ff5252' }">
        {{ correct ? '✓' : '✗' }}
      </div>
      <div class="result-score">{{ correct ? '+' + score : '+0' }}</div>
      <div v-if="isLast" class="result-double">双倍!</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  visible: Boolean,
  correct: Boolean,
  score: Number,
  isLast: Boolean
})
</script>

<style scoped>
.answer-result-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s;
  z-index: 1000;
}
.answer-result-overlay.show {
  opacity: 1;
}
.result-content {
  background: rgba(0, 0, 0, 0.8);
  border-radius: 20px;
  padding: 30px 50px;
  text-align: center;
}
.result-icon {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 10px;
}
.result-score {
  font-size: 24px;
  color: #fff;
  font-weight: 600;
}
.result-double {
  margin-top: 8px;
  font-size: 16px;
  color: #ffd740;
  font-weight: 600;
}
</style>
