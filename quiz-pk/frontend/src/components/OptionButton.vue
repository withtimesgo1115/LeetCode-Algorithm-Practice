<template>
  <button
    class="option-btn"
    :class="{ selected, correct, wrong, disabled }"
    @click="$emit('click')"
  >
    <span class="option-label">{{ label }}</span>
    <span class="option-text">{{ text }}</span>
  </button>
</template>

<script setup>
defineProps({
  label: String,
  text: String,
  selected: Boolean,
  correct: Boolean,
  wrong: Boolean,
  disabled: Boolean
})

defineEmits(['click'])
</script>

<style scoped>
.option-btn {
  width: 100%;
  background: rgba(255, 255, 255, 0.08);
  border: 2px solid rgba(255, 255, 255, 0.15);
  border-radius: 10px;
  padding: 16px 20px;
  color: #fff;
  font-size: 15px;
  cursor: pointer;
  text-align: left;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: border-color 0.2s, background 0.2s;
}
.option-btn:active:not(.disabled) {
  transform: scale(0.98);
}
.option-btn.selected {
  border-color: #667eea;
  background: rgba(102, 126, 234, 0.2);
}
.option-btn.correct {
  border-color: #00e676;
  background: rgba(0, 230, 118, 0.15);
}
.option-btn.wrong {
  border-color: #ff5252;
  background: rgba(255, 82, 82, 0.15);
}
.option-btn.disabled {
  pointer-events: none;
  opacity: 0.6;
}
.option-label {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  flex-shrink: 0;
}
.option-text {
  flex: 1;
}
</style>
