import { ref, onUnmounted } from 'vue'

export function useTimer() {
  const remaining = ref(0)
  const isRunning = ref(false)
  let intervalId = null

  function start(seconds, onTick, onEnd) {
    stop()
    remaining.value = seconds
    isRunning.value = true

    intervalId = setInterval(() => {
      remaining.value--
      onTick?.(remaining.value)
      if (remaining.value <= 0) {
        stop()
        onEnd?.()
      }
    }, 1000)
  }

  function stop() {
    if (intervalId) {
      clearInterval(intervalId)
      intervalId = null
    }
    isRunning.value = false
  }

  onUnmounted(stop)

  return { remaining, isRunning, start, stop }
}
