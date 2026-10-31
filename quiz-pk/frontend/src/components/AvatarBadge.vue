<template>
  <div class="avatar-badge" :style="{ backgroundColor: color }">
    <span class="avatar-initial">{{ initial }}</span>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useAvatar } from '@/composables/useAvatar'

const props = defineProps({
  nickname: { type: String, default: '' }
})

const { getColor, getInitial } = useAvatar()
const color = computed(() => getColor(props.nickname))
const initial = computed(() => getInitial(props.nickname))
</script>

<style scoped>
.avatar-badge {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: 600;
  font-size: 16px;
  flex-shrink: 0;
}
.avatar-initial {
  user-select: none;
}
</style>
