import { io } from 'socket.io-client'
import { useUserStore } from '@/stores/user'
import { useGameStore } from '@/stores/game'
import { GAME_EVENTS } from '@/utils/constants'

let socket = null
const listeners = new Map()
let pendingJoin = null // Store join params to send after connection

export function useSocket() {
  const userStore = useUserStore()
  const gameStore = useGameStore()

  function connect() {
    if (socket?.connected) {
      console.log('[SOCKET] Already connected')
      return
    }
    console.log('[SOCKET] Connecting...')
    socket = io({ withCredentials: true })

    socket.on('connect', () => {
      console.log('[SOCKET] Connected:', socket.id)
      // Send pending join if exists
      if (pendingJoin) {
        console.log('[SOCKET] Sending pending join:', pendingJoin)
        socket.emit(GAME_EVENTS.JOIN, pendingJoin)
        pendingJoin = null
      }
    })

    socket.on('disconnect', () => {
      console.log('[SOCKET] Disconnected')
    })

    socket.on('connect_error', (error) => {
      console.error('[SOCKET] Connection error:', error)
    })

    const events = Object.values(GAME_EVENTS)
    events.forEach(ev => {
      socket.on(ev, (data) => {
        console.log('[SOCKET] Received:', ev, data)
        dispatch(ev, data)
        listeners.get(ev)?.forEach(cb => cb(data))
      })
    })
  }

  function dispatch(event, data) {
    switch (event) {
      case GAME_EVENTS.SET_COOKIE:
        userStore.userId = data.userId
        localStorage.setItem('quiz_uid', data.userId)
        break
      case GAME_EVENTS.AUTH_SUCCESS:
        userStore.userId = data.userId
        userStore.nickname = data.nickname || userStore.nickname
        userStore.rank = data.rank
        localStorage.setItem('quiz_uid', data.userId)
        break
      case GAME_EVENTS.AUTH_ERROR:
        break
      case GAME_EVENTS.WAITING:
        gameStore.matchStatus = 'waiting'
        break
      case GAME_EVENTS.MATCHED:
        gameStore.opponent = data.opponent
        gameStore.opponentRank = data.opponentRank
        gameStore.totalQ = data.totalQuestions
        gameStore.matchStatus = 'matched'
        setTimeout(() => {
          gameStore.screen = 'playing'
          window.location.hash = '#/game'
        }, 1200)
        break
      case GAME_EVENTS.MATCH_TIMEOUT:
        gameStore.showToast('匹配超时，请重试')
        gameStore.screen = 'home'
        window.location.hash = '#/'
        break
      case GAME_EVENTS.MATCH_ERROR:
        gameStore.showToast(data.message || '匹配失败')
        gameStore.screen = 'home'
        window.location.hash = '#/'
        break
      case GAME_EVENTS.QUESTION:
        gameStore.applyQuestion(data)
        break
      case GAME_EVENTS.ANSWER_ACK:
        gameStore.applyAnswerAck(data)
        break
      case GAME_EVENTS.OPPONENT_ANSWERED:
        gameStore.oppProgressState = 'answered'
        break
      case GAME_EVENTS.QUESTION_RESULT:
        gameStore.applyQuestionResult(data)
        break
      case GAME_EVENTS.GAME_OVER:
        gameStore.applyGameOver(data)
        gameStore.screen = 'result'
        window.location.hash = '#/result'
        break
      case GAME_EVENTS.OPPONENT_DISCONNECTED:
        gameStore.showToast('对手已断开连接')
        gameStore.screen = 'home'
        window.location.hash = '#/'
        break
    }
  }

  function join(nickname, userId) {
    console.log('[SOCKET] Emitting join:', nickname, userId)
    const joinData = { nickname, userId }
    if (socket?.connected) {
      socket.emit(GAME_EVENTS.JOIN, joinData)
    } else {
      // Store as pending to send after connection
      pendingJoin = joinData
      console.log('[SOCKET] Join queued (not connected yet)')
    }
  }

  function selectCategory(category, mode) {
    console.log('[SOCKET] Emitting select_category:', category, mode)
    socket?.emit(GAME_EVENTS.SELECT_CATEGORY, { category, mode })
  }

  function cancelMatch() {
    socket?.emit(GAME_EVENTS.CANCEL_MATCH)
  }

  function answer(questionIndex, optionIndex) {
    socket?.emit(GAME_EVENTS.ANSWER, { questionIndex, optionIndex })
  }

  function on(event, callback) {
    if (!listeners.has(event)) listeners.set(event, new Set())
    listeners.get(event)?.add(callback)
  }

  function off(event, callback) {
    listeners.get(event)?.delete(callback)
  }

  return { connect, join, selectCategory, cancelMatch, answer, on, off }
}
