<template>
  <div
    class="category-card"
    :class="{ disabled }"
    :style="{ background: gradient + '20', borderColor: gradient + '40' }"
    @click="$emit('click')"
  >
    <div class="category-icon">{{ icon }}</div>
    <div class="category-name">{{ name }}</div>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  icon: String,
  gradient: String,
  disabled: Boolean
})

defineEmits(['click'])
</script>

<style scoped>
.category-card {
  background: rgba(255, 255, 255, 0.08);
  border: 2px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px;
  padding: 20px 16px;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}
.category-card:not(.disabled):active {
  transform: scale(0.95);
}
.category-card.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.category-icon {
  font-size: 32px;
  margin-bottom: 8px;
}
.category-name {
  font-size: 14px;
  font-weight: 500;
  color: #fff;
}
</style>
