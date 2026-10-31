<template>
  <div class="question-card">
    <div class="question-header">
      <t-tag v-if="category" theme="primary" variant="light" size="small">
        {{ category }}
      </t-tag>
      <div v-if="isLast" class="double-badge">双倍题!</div>
    </div>
    <div class="question-text">{{ text }}</div>
  </div>
</template>

<script setup>
defineProps({
  text: String,
  category: String,
  isLast: Boolean
})
</script>

<style scoped>
.question-card {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 20px;
}
.question-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}
.double-badge {
  background: linear-gradient(135deg, #f093fb, #f5576c);
  color: #fff;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  animation: pulse 1.5s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}
.question-text {
  font-size: 16px;
  line-height: 1.6;
  color: #fff;
}
</style>
