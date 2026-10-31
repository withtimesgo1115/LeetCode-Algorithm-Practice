const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const cookieParser = require('cookie-parser');
const { v4: uuidv4 } = require('uuid');
const {
  initializeDatabase,
  findOrCreateUser,
  getUserById,
  getRandomQuestions,
  getRandomQuestionsAll,
  getCategories,
  createGameRoom,
  updateGameResult,
  incrementUserGames,
  getLeaderboard,
  getRank,
} = require('./database');

initializeDatabase();

const app = express();
app.use(cookieParser());
app.use(express.json());
app.use(express.static('frontend/dist'));

const server = http.createServer(app);
const io = new Server(server, {
  cors: { origin: '*' },
  pingTimeout: 20000,
  pingInterval: 10000,
});

// ── In-memory state ────────────────────────────────────────────────
const connectedUsers = new Map();   // socketId → { userId, nickname }
const matchingQueue  = new Map();   // category → [{ socketId, userId, nickname, timer }]
const activeGames    = new Map();   // roomId → Game

const QUESTION_TIME   = 15;         // seconds per question
const QUESTIONS_PER_GAME = 5;
const MATCH_TIMEOUT   = 30000;      // ms
const RANDOM_CATEGORY = '随机模式';

// ── REST API ───────────────────────────────────────────────────────
app.get('/api/categories', (_req, res) => {
  res.json(getCategories());
});

app.get('/api/leaderboard', (_req, res) => {
  res.json(getLeaderboard());
});

// ── Scoring ────────────────────────────────────────────────────────
function calculateScore(answerTimeMs, isCorrect) {
  if (!isCorrect) return 0;
  const seconds = Math.floor(answerTimeMs / 1000);
  if (seconds <= 3) return 100;
  return Math.max(0, 100 - seconds * 5);
}

// ── Matching ───────────────────────────────────────────────────────
const BOT_NAMES = ['小学霸', '答题达人', '知识王者', '百科博士', '刷题高手', '学霸联盟', '答题小能手', '知识星球'];

function addToQueue(socketId, userId, nickname, category, mode) {
  if (!matchingQueue.has(category)) matchingQueue.set(category, []);
  const queue = matchingQueue.get(category);

  const timer = setTimeout(() => {
    const idx = queue.findIndex(p => p.socketId === socketId);
    if (idx !== -1) {
      queue.splice(idx, 1);
      io.to(socketId).emit('match_timeout');
    }
  }, MATCH_TIMEOUT);

  const player = { socketId, userId, nickname, timer, mode };
  queue.push(player);

  // First, try to match with any available human player
  if (queue.length >= 2) {
    // Find players available for human matching (pvp mode, or single mode without botTimer fired yet)
    const availableHumans = queue.filter(p => {
      if (p.mode === 'pvp') return true;
      // Single mode players can still be matched with humans if their bot hasn't spawned yet
      if (p.mode === 'single' && !p.botSpawned) return true;
      return false;
    });
    
    if (availableHumans.length >= 2) {
      const p1 = availableHumans[0];
      const p2 = availableHumans[1];
      queue.splice(queue.indexOf(p1), 1);
      queue.splice(queue.indexOf(p2), 1);
      clearTimeout(p1.timer);
      clearTimeout(p2.timer);
      if (p1.botTimer) clearTimeout(p1.botTimer);
      if (p2.botTimer) clearTimeout(p2.botTimer);
      createGame(p1, p2, category);
      return; // Match found, exit early
    }
  }

  // No human match found, if single mode then schedule bot spawn
  if (mode === 'single') {
    player.botTimer = setTimeout(() => {
      const idx = queue.findIndex(p => p.socketId === socketId);
      if (idx !== -1) {
        queue.splice(idx, 1);
        clearTimeout(timer);
        player.botSpawned = true;
        spawnBot(player, category);
      }
    }, 3000);
  }

  if (queue.length < 2 || mode === 'single') {
    io.to(socketId).emit('waiting');
  }
}

function spawnBot(player, category) {
  const botName = BOT_NAMES[Math.floor(Math.random() * BOT_NAMES.length)];
  const botPlayer = {
    socketId: 'bot_' + player.userId,
    userId: 'bot_' + player.userId,
    nickname: botName,
    isBot: true,
  };
  createGame(player, botPlayer, category);
}

function removeFromQueue(socketId) {
  for (const [category, queue] of matchingQueue) {
    const idx = queue.findIndex(p => p.socketId === socketId);
    if (idx !== -1) {
      clearTimeout(queue[idx].timer);
      clearTimeout(queue[idx].botTimer);
      queue.splice(idx, 1);
      return;
    }
  }
}

// ── Game lifecycle ─────────────────────────────────────────────────
function createGame(p1, p2, category) {
  const roomId = uuidv4();
  let rawQuestions;

  if (category === RANDOM_CATEGORY) {
    rawQuestions = getRandomQuestionsAll(QUESTIONS_PER_GAME);
  } else {
    rawQuestions = getRandomQuestions(category, QUESTIONS_PER_GAME);
  }

  if (rawQuestions.length < QUESTIONS_PER_GAME) {
    if (!p1.isBot) io.to(p1.socketId).emit('match_error', { message: '题目不足，请重试' });
    if (!p2.isBot) io.to(p2.socketId).emit('match_error', { message: '题目不足，请重试' });
    return;
  }

  const questions = rawQuestions.map(q => ({
    id: q.id,
    text: q.question_text,
    options: JSON.parse(q.options),
    correctAnswer: q.correct_answer,
    category: q.category,
  }));

  const hasBot = p1.isBot || p2.isBot;
  if (!hasBot) {
    createGameRoom(roomId, p1.userId, p2.userId, category);
  }

  const p1User = p1.isBot ? null : getUserById(p1.userId);
  const p2User = p2.isBot ? null : getUserById(p2.userId);

  const game = {
    id: roomId,
    category,
    hasBot,
    players: [
      { socketId: p1.socketId, userId: p1.userId, nickname: p1.nickname, score: 0, currentAnswer: null, isBot: !!p1.isBot },
      { socketId: p2.socketId, userId: p2.userId, nickname: p2.nickname, score: 0, currentAnswer: null, isBot: !!p2.isBot },
    ],
    questions,
    currentQuestion: 0,
    questionStartTime: null,
    questionTimer: null,
    botTimers: [],
  };

  activeGames.set(roomId, game);

  const p1Rank = p1.isBot ? { name: '青铜', icon: '🥉' } : getRank(p1User.games_played, p1User.games_won);
  const p2Rank = p2.isBot ? { name: '青铜', icon: '🥉' } : getRank(p2User.games_played, p2User.games_won);

  if (!p1.isBot) {
    io.to(p1.socketId).emit('matched', {
      opponent: p2.nickname,
      opponentRank: p2Rank,
      roomId,
      totalQuestions: QUESTIONS_PER_GAME,
    });
  }
  if (!p2.isBot) {
    io.to(p2.socketId).emit('matched', {
      opponent: p1.nickname,
      opponentRank: p1Rank,
      roomId,
      totalQuestions: QUESTIONS_PER_GAME,
    });
  }

  setTimeout(() => sendQuestion(roomId, 0), 2000);
}

function sendQuestion(roomId, index) {
  const game = activeGames.get(roomId);
  if (!game) return;

  game.currentQuestion = index;
  game.players.forEach(p => { p.currentAnswer = null; });
  game.questionStartTime = Date.now();

  const q = game.questions[index];
  const isLast = index === QUESTIONS_PER_GAME - 1;
  const payload = {
    index,
    text: q.text,
    options: q.options,
    totalTime: QUESTION_TIME,
    isLast,
    category: q.category,
  };

  game.players.forEach(p => {
    if (!p.isBot) io.to(p.socketId).emit('question', payload);
  });

  // Schedule bot answers
  game.botTimers.forEach(t => clearTimeout(t));
  game.botTimers = [];
  game.players.filter(p => p.isBot).forEach(bot => {
    const delay = 2000 + Math.random() * 6000; // 2-8 seconds
    const t = setTimeout(() => {
      const currentGame = activeGames.get(roomId);
      if (!currentGame || currentGame.currentQuestion !== index) return;
      if (bot.currentAnswer !== null) return;
      const correct = Math.random() < 0.6; // 60% accuracy
      const optionIndex = correct
        ? q.correctAnswer
        : [0, 1, 2, 3].filter(i => i !== q.correctAnswer)[Math.floor(Math.random() * 3)];
      processAnswer(roomId, bot.socketId, index, optionIndex);
    }, delay);
    game.botTimers.push(t);
  });

  game.questionTimer = setTimeout(() => handleTimeUp(roomId), QUESTION_TIME * 1000);
}

function handleTimeUp(roomId) {
  const game = activeGames.get(roomId);
  if (!game) return;

  game.players.forEach(p => {
    if (p.currentAnswer === null) {
      p.currentAnswer = { optionIndex: -1, correct: false, score: 0, answerTime: QUESTION_TIME * 1000 };
    }
  });

  emitQuestionResult(roomId);
}

function processAnswer(roomId, socketId, questionIndex, optionIndex) {
  const game = activeGames.get(roomId);
  if (!game) return;
  if (questionIndex !== game.currentQuestion) return;

  const player = game.players.find(p => p.socketId === socketId);
  if (!player || player.currentAnswer !== null) return;

  const answerTime = Date.now() - game.questionStartTime;
  const q = game.questions[questionIndex];
  const correct = optionIndex === q.correctAnswer;
  let score = calculateScore(answerTime, correct);

  // Last question doubles the score
  const isLast = questionIndex === QUESTIONS_PER_GAME - 1;
  if (isLast) score *= 2;

  player.currentAnswer = { optionIndex, correct, score, answerTime };
  player.score += score;

  if (!player.isBot) {
    io.to(socketId).emit('answer_ack', { questionIndex, correct, score, totalScore: player.score, isLast });
  }

  const opponent = game.players.find(p => p.socketId !== socketId);
  if (opponent && !opponent.isBot) {
    io.to(opponent.socketId).emit('opponent_answered', { questionIndex });
  }

  if (game.players.every(p => p.currentAnswer !== null)) {
    clearTimeout(game.questionTimer);
    emitQuestionResult(roomId);
  }
}

function emitQuestionResult(roomId) {
  const game = activeGames.get(roomId);
  if (!game) return;

  const [p1, p2] = game.players;
  const q = game.questions[game.currentQuestion];
  const isLast = game.currentQuestion === QUESTIONS_PER_GAME - 1;

  const resultPayload = {
    questionIndex: game.currentQuestion,
    correctAnswer: q.correctAnswer,
    playerScore: p1.score,
    opponentScore: p2.score,
    playerAnswer: p1.currentAnswer ? p1.currentAnswer.optionIndex : -1,
    opponentAnswer: p2.currentAnswer ? p2.currentAnswer.optionIndex : -1,
    playerCorrect: p1.currentAnswer ? p1.currentAnswer.correct : false,
    opponentCorrect: p2.currentAnswer ? p2.currentAnswer.correct : false,
    isLast,
  };

  if (!p1.isBot) io.to(p1.socketId).emit('question_result', resultPayload);
  if (!p2.isBot) io.to(p2.socketId).emit('question_result', {
    ...resultPayload,
    playerScore: p2.score,
    opponentScore: p1.score,
    playerAnswer: p2.currentAnswer ? p2.currentAnswer.optionIndex : -1,
    opponentAnswer: p1.currentAnswer ? p1.currentAnswer.optionIndex : -1,
    playerCorrect: p2.currentAnswer ? p2.currentAnswer.correct : false,
    opponentCorrect: p1.currentAnswer ? p1.currentAnswer.correct : false,
  });

  if (game.currentQuestion < QUESTIONS_PER_GAME - 1) {
    setTimeout(() => sendQuestion(roomId, game.currentQuestion + 1), 2500);
  } else {
    setTimeout(() => finishGame(roomId), 2500);
  }
}

function finishGame(roomId) {
  const game = activeGames.get(roomId);
  if (!game) return;

  // Clear bot timers
  game.botTimers.forEach(t => clearTimeout(t));

  const [p1, p2] = game.players;

  if (!game.hasBot) {
    let winnerId = null;
    if (p1.score > p2.score) winnerId = p1.userId;
    else if (p2.score > p1.score) winnerId = p2.userId;

    updateGameResult(roomId, p1.score, p2.score, winnerId);
    incrementUserGames(p1.userId, p1.score > p2.score);
    incrementUserGames(p2.userId, p2.score > p1.score);
  }

  const p1User = p1.isBot ? null : getUserById(p1.userId);
  const p2User = p2.isBot ? null : getUserById(p2.userId);
  const p1Rank = p1.isBot ? { name: '青铜', icon: '🥉' } : getRank(p1User.games_played, p1User.games_won);
  const p2Rank = p2.isBot ? { name: '青铜', icon: '🥉' } : getRank(p2User.games_played, p2User.games_won);

  if (!p1.isBot) {
    io.to(p1.socketId).emit('game_over', {
      playerScore: p1.score,
      opponentScore: p2.score,
      result: p1.score > p2.score ? 'win' : p1.score < p2.score ? 'lose' : 'draw',
      opponentNickname: p2.nickname,
      playerRank: p1Rank,
      opponentRank: p2Rank,
    });
  }

  if (!p2.isBot) {
    io.to(p2.socketId).emit('game_over', {
      playerScore: p2.score,
      opponentScore: p1.score,
      result: p2.score > p1.score ? 'win' : p2.score < p1.score ? 'lose' : 'draw',
      opponentNickname: p1.nickname,
      playerRank: p2Rank,
      opponentRank: p1Rank,
    });
  }

  activeGames.delete(roomId);
}

// ── Socket.IO ──────────────────────────────────────────────────────
io.on('connection', (socket) => {
  console.log('[SOCKET] New connection:', socket.id);

  socket.on('join', (data) => {
    console.log('[JOIN]', data.nickname, 'userId:', data.userId);
    const nickname = (data.nickname || '').trim().slice(0, 8);
    if (!nickname) return socket.emit('auth_error', { message: '昵称不能为空' });

    let userId = data.userId || socket.handshake.cookies?.quiz_uid;
    if (!userId) {
      userId = uuidv4();
      socket.emit('set_cookie', { userId });
    }

    const user = findOrCreateUser(userId, nickname);
    const rank = getRank(user.games_played, user.games_won);
    connectedUsers.set(socket.id, { userId, nickname });
    console.log('[JOINED]', nickname, 'socket:', socket.id);
    socket.emit('auth_success', { userId, nickname, rank });
  });

  socket.on('select_category', (data) => {
    console.log('[SELECT_CATEGORY]', data.category, 'mode:', data.mode, 'socket:', socket.id);
    const user = connectedUsers.get(socket.id);
    if (!user) {
      console.log('[ERROR] User not found in connectedUsers for socket:', socket.id);
      return;
    }

    const categories = getCategories().map(c => c.category);
    if (data.category !== RANDOM_CATEGORY && !categories.includes(data.category)) return;

    removeFromQueue(socket.id);
    addToQueue(socket.id, user.userId, user.nickname, data.category, data.mode || 'pvp');
    console.log('[QUEUE] Added to queue, mode:', data.mode);
  });

  socket.on('cancel_match', () => {
    removeFromQueue(socket.id);
  });

  socket.on('answer', (data) => {
    const user = connectedUsers.get(socket.id);
    if (!user) return;

    for (const [roomId, game] of activeGames) {
      const player = game.players.find(p => p.socketId === socket.id);
      if (player) {
        processAnswer(roomId, socket.id, data.questionIndex, data.optionIndex);
        return;
      }
    }
  });

  socket.on('disconnect', () => {
    const user = connectedUsers.get(socket.id);
    if (!user) return;

    removeFromQueue(socket.id);

    for (const [roomId, game] of activeGames) {
      const player = game.players.find(p => p.socketId === socket.id);
      if (player) {
        const opponent = game.players.find(p => p.socketId !== socket.id);
        if (opponent) {
          io.to(opponent.socketId).emit('opponent_disconnected');
        }
        activeGames.delete(roomId);
        break;
      }
    }

    connectedUsers.delete(socket.id);
  });
});

// ── Start ──────────────────────────────────────────────────────────
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Quiz PK server running on http://localhost:${PORT}`);
});
