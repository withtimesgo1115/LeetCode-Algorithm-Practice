<template>
  <div class="timer-circle">
    <svg class="timer-svg" viewBox="0 0 100 100">
      <circle class="timer-bg" cx="50" cy="50" r="45" />
      <circle
        class="timer-fg"
        :class="{ danger: remaining <= 5 }"
        cx="50" cy="50" r="45"
        :style="{ strokeDashoffset: offset }"
      />
    </svg>
    <span class="timer-text">{{ remaining }}</span>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  remaining: { type: Number, default: 15 },
  total: { type: Number, default: 15 }
})

const circumference = 2 * Math.PI * 45
const offset = computed(() => {
  const progress = props.remaining / props.total
  return circumference * (1 - progress)
})
</script>

<style scoped>
.timer-circle {
  position: relative;
  width: 60px;
  height: 60px;
}
.timer-svg {
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
}
.timer-bg {
  fill: none;
  stroke: rgba(255, 255, 255, 0.1);
  stroke-width: 6;
}
.timer-fg {
  fill: none;
  stroke: #ffd740;
  stroke-width: 6;
  stroke-linecap: round;
  stroke-dasharray: 283;
  transition: stroke-dashoffset 1s linear, stroke 0.3s;
}
.timer-fg.danger {
  stroke: #ff5252;
}
.timer-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 18px;
  font-weight: 700;
  color: #fff;
}
</style>
