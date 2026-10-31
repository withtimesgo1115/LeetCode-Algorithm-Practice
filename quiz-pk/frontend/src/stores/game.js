import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useGameStore = defineStore('game', () => {
  const screen = ref('home')
  const category = ref(null)
  const singleMode = ref(false)
  const opponent = ref(null)
  const opponentRank = ref(null)
  const myScore = ref(0)
  const oppScore = ref(0)
  const qIndex = ref(0)
  const totalQ = ref(5)
  const answered = ref(false)
  const myRank = ref(null)
  const matchStatus = ref('idle')
  const categories = ref([])
  const currentQuestion = ref(null)
  const myAnswer = ref(null)
  const myProgressState = ref('')
  const oppProgressState = ref('')
  const resultData = ref(null)
  const showToast = ref(null)

  const isLastQuestion = computed(() => qIndex.value === totalQ.value - 1)

  function applyQuestion(data) {
    qIndex.value = data.index
    answered.value = false
    currentQuestion.value = data
    myAnswer.value = null
    myProgressState.value = ''
    oppProgressState.value = ''
  }

  function applyAnswerAck(data) {
    answered.value = true
    myScore.value = data.totalScore
    myProgressState.value = data.correct ? 'correct' : 'wrong'
  }

  function applyQuestionResult(data) {
    myScore.value = data.playerScore
    oppScore.value = data.opponentScore
  }

  function applyGameOver(data) {
    myRank.value = data.playerRank
    opponentRank.value = data.opponentRank
    resultData.value = data
  }

  function reset() {
    myScore.value = 0
    oppScore.value = 0
    qIndex.value = 0
    answered.value = false
    currentQuestion.value = null
    myAnswer.value = null
    myProgressState.value = ''
    oppProgressState.value = ''
    matchStatus.value = 'idle'
  }

  return {
    screen, category, singleMode, opponent, opponentRank,
    myScore, oppScore, qIndex, totalQ, answered, myRank,
    matchStatus, categories, currentQuestion, myAnswer,
    myProgressState, oppProgressState, resultData, showToast,
    isLastQuestion,
    applyQuestion, applyAnswerAck, applyQuestionResult, applyGameOver, reset
  }
})
