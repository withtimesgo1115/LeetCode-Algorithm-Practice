<template>
  <span v-if="rank" class="rank-badge">
    <span class="rank-icon">{{ rank.icon }}</span>
    <span class="rank-name">{{ rank.name }}</span>
  </span>
</template>

<script setup>
defineProps({
  rank: { type: Object, default: null }
})
</script>

<style scoped>
.rank-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  font-size: 12px;
}
.rank-icon {
  font-size: 14px;
}
.rank-name {
  color: rgba(255, 255, 255, 0.8);
}
</style>
