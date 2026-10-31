<template>
  <div class="game-view">
    <ScoreHeader
      :my-nickname="userStore.nickname"
      :my-rank="gameStore.myRank || userStore.rank"
      :my-score="gameStore.myScore"
      :opp-nickname="gameStore.opponent"
      :opp-rank="gameStore.opponentRank"
      :opp-score="gameStore.oppScore"
      :q-index="gameStore.qIndex"
      :total-q="gameStore.totalQ"
      :timer-remaining="timerRemaining"
      :timer-total="timerTotal"
    />

    <div class="progress-bar-container">
      <div class="progress-bar" :class="gameStore.myProgressState">
        <span class="progress-label">我</span>
      </div>
      <div class="progress-bar" :class="gameStore.oppProgressState">
        <span class="progress-label">对手</span>
      </div>
    </div>

    <div class="game-content">
      <QuestionCard
        v-if="gameStore.currentQuestion"
        :text="gameStore.currentQuestion.text"
        :category="gameStore.currentQuestion.category"
        :is-last="gameStore.isLastQuestion"
      />

      <div class="options-container">
        <OptionButton
          v-for="(opt, i) in gameStore.currentQuestion?.options || []"
          :key="i"
          :label="String.fromCharCode(65 + i)"
          :text="opt"
          :selected="gameStore.myAnswer === i"
          :correct="showResult && correctAnswer === i"
          :wrong="showResult && gameStore.myAnswer === i && correctAnswer !== i"
          :disabled="gameStore.answered"
          @click="selectAnswer(i)"
        />
      </div>
    </div>

    <AnswerResultOverlay
      :visible="showOverlay"
      :correct="overlayCorrect"
      :score="overlayScore"
      :is-last="gameStore.isLastQuestion"
    />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useUserStore } from '@/stores/user'
import { useGameStore } from '@/stores/game'
import { useSocket } from '@/composables/useSocket'
import { useTimer } from '@/composables/useTimer'
import ScoreHeader from '@/components/ScoreHeader.vue'
import QuestionCard from '@/components/QuestionCard.vue'
import OptionButton from '@/components/OptionButton.vue'
import AnswerResultOverlay from '@/components/AnswerResultOverlay.vue'

const userStore = useUserStore()
const gameStore = useGameStore()
const socket = useSocket()
const { remaining: timerRemaining, start: startTimer, stop: stopTimer } = useTimer()

const timerTotal = ref(15)
const showResult = ref(false)
const correctAnswer = ref(null)
const showOverlay = ref(false)
const overlayCorrect = ref(false)
const overlayScore = ref(0)

watch(() => gameStore.currentQuestion, (q) => {
  if (q) {
    showResult.value = false
    correctAnswer.value = null
    timerTotal.value = q.totalTime
    startTimer(q.totalTime, null, () => {})
  }
})

watch(() => gameStore.myProgressState, (state) => {
  if (state === 'correct' || state === 'wrong') {
    stopTimer()
  }
})

function selectAnswer(index) {
  if (gameStore.answered) return
  gameStore.myAnswer = index
  socket.answer(gameStore.qIndex, index)
}

socket.on('answer_ack', (data) => {
  overlayCorrect.value = data.correct
  overlayScore.value = data.score
  showOverlay.value = true
  setTimeout(() => {
    showOverlay.value = false
  }, 1200)
})

socket.on('question_result', (data) => {
  showResult.value = true
  correctAnswer.value = data.correctAnswer
  setTimeout(() => {
    gameStore.myProgressState = ''
    gameStore.oppProgressState = ''
  }, 1500)
})
</script>

<style scoped>
.game-view {
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  flex-direction: column;
}
.progress-bar-container {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.03);
}
.progress-bar {
  height: 8px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  position: relative;
  overflow: hidden;
  transition: background 0.3s;
}
.progress-bar::after {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 0;
  background: linear-gradient(90deg, #667eea, #764ba2);
  transition: width 0.3s;
}
.progress-bar.answered::after {
  width: 100%;
}
.progress-bar.correct::after {
  width: 100%;
  background: #00e676;
}
.progress-bar.wrong::after {
  width: 100%;
  background: #ff5252;
}
.progress-label {
  position: absolute;
  left: 8px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 10px;
  color: rgba(255, 255, 255, 0.6);
  z-index: 1;
}
.game-content {
  flex: 1;
  padding: 20px 16px;
  overflow-y: auto;
}
.options-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
</style>
