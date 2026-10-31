export const CATEGORY_ICONS = {
  '文学艺术': '📚',
  '法律': '⚖️',
  '历史地理': '🌍',
  '物理化学生物': '🔬',
  '科技创新': '💡',
  '成语辨析': '✍️',
  '时事政治': '📰'
}

export const CATEGORY_GRADIENTS = [
  'linear-gradient(135deg, #667eea, #764ba2)',
  'linear-gradient(135deg, #f093fb, #f5576c)',
  'linear-gradient(135deg, #4facfe, #00f2fe)',
  'linear-gradient(135deg, #43e97b, #38f9d7)',
  'linear-gradient(135deg, #fa709a, #fee140)',
  'linear-gradient(135deg, #a18cd1, #fbc2eb)',
  'linear-gradient(135deg, #fccb90, #d57eeb)'
]

export const AVATAR_COLORS = [
  '#667eea', '#f093fb', '#4facfe', '#43e97b',
  '#fa709a', '#a18cd1', '#fccb90', '#f5576c',
  '#00f2fe', '#38f9d7', '#fee140', '#d57eeb'
]

export const RANK_TIERS = [
  { name: '王者', icon: '👑', minRate: 95 },
  { name: '宗师', icon: '💎', minRate: 85 },
  { name: '大师', icon: '🏅', minRate: 75 },
  { name: '钻石', icon: '💠', minRate: 65 },
  { name: '铂金', icon: '🔷', minRate: 55 },
  { name: '黄金', icon: '🥇', minRate: 40 },
  { name: '白银', icon: '🥈', minRate: 25 },
  { name: '青铜', icon: '🥉', minRate: 0 }
]

export const GAME_EVENTS = {
  // Client -> Server
  JOIN: 'join',
  SELECT_CATEGORY: 'select_category',
  CANCEL_MATCH: 'cancel_match',
  ANSWER: 'answer',
  // Server -> Client
  SET_COOKIE: 'set_cookie',
  AUTH_SUCCESS: 'auth_success',
  AUTH_ERROR: 'auth_error',
  WAITING: 'waiting',
  MATCHED: 'matched',
  MATCH_TIMEOUT: 'match_timeout',
  MATCH_ERROR: 'match_error',
  QUESTION: 'question',
  ANSWER_ACK: 'answer_ack',
  OPPONENT_ANSWERED: 'opponent_answered',
  QUESTION_RESULT: 'question_result',
  GAME_OVER: 'game_over',
  OPPONENT_DISCONNECTED: 'opponent_disconnected'
}

export const SCREENS = {
  HOME: 'home',
  MATCHING: 'matching',
  PLAYING: 'playing',
  RESULT: 'result'
}
