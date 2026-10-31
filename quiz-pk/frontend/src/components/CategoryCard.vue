<template>
  <div
    class="category-card"
    :class="{ disabled }"
    :style="{ background: gradient + '30', borderColor: gradient + '60' }"
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
  background: rgba(255, 255, 255, 0.15);
  border: 2px solid rgba(255, 255, 255, 0.3);
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
  opacity: 0.4;
  cursor: not-allowed;
  filter: grayscale(0.5);
}
.category-icon {
  font-size: 36px;
  margin-bottom: 10px;
}
.category-name {
  font-size: 15px;
  font-weight: 600;
  color: #fff;
  letter-spacing: 0.5px;
}
</style>
