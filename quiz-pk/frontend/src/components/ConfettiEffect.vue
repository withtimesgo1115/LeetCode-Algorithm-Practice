<template>
  <div v-if="active" class="confetti-container">
    <div
      v-for="i in 50"
      :key="i"
      class="confetti-piece"
      :style="getConfettiStyle(i)"
    />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const props = defineProps({
  active: Boolean
})

const colors = ['#667eea', '#f093fb', '#4facfe', '#43e97b', '#fa709a', '#ffd740']

function getConfettiStyle(i) {
  return {
    left: Math.random() * 100 + '%',
    backgroundColor: colors[i % colors.length],
    animationDuration: (Math.random() * 2 + 2) + 's',
    animationDelay: Math.random() * 0.5 + 's'
  }
}
</script>

<style scoped>
.confetti-container {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 9999;
  overflow: hidden;
}
</style>
