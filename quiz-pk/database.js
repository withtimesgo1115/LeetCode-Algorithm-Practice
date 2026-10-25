const Database = require('better-sqlite3');
const path = require('path');

const DB_PATH = path.join(__dirname, 'data', 'quiz.db');

let db;

function getDb() {
  if (!db) {
    db = new Database(DB_PATH);
    db.pragma('journal_mode = WAL');
    db.pragma('foreign_keys = ON');
  }
  return db;
}

function initializeDatabase() {
  const db = getDb();

  db.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY,
      nickname TEXT UNIQUE NOT NULL,
      games_played INTEGER DEFAULT 0,
      games_won INTEGER DEFAULT 0,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS questions (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      category TEXT NOT NULL,
      question_text TEXT NOT NULL,
      options TEXT NOT NULL,
      correct_answer INTEGER NOT NULL,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS game_rooms (
      id TEXT PRIMARY KEY,
      player1_id TEXT NOT NULL,
      player2_id TEXT NOT NULL,
      category TEXT NOT NULL,
      player1_score INTEGER DEFAULT 0,
      player2_score INTEGER DEFAULT 0,
      status TEXT DEFAULT 'playing',
      winner_id TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      finished_at DATETIME,
      FOREIGN KEY (player1_id) REFERENCES users(id),
      FOREIGN KEY (player2_id) REFERENCES users(id)
    );

    CREATE INDEX IF NOT EXISTS idx_questions_category ON questions(category);
  `);

  return db;
}

function findOrCreateUser(id, nickname) {
  const db = getDb();
  const insert = db.prepare(
    'INSERT OR IGNORE INTO users (id, nickname) VALUES (?, ?)'
  );
  insert.run(id, nickname);
  return db.prepare('SELECT * FROM users WHERE id = ?').get(id);
}

function getUserById(id) {
  const db = getDb();
  return db.prepare('SELECT * FROM users WHERE id = ?').get(id);
}

function getRandomQuestions(category, count) {
  const db = getDb();
  return db.prepare(
    'SELECT * FROM questions WHERE category = ? ORDER BY RANDOM() LIMIT ?'
  ).all(category, count);
}

function getRandomQuestionsAll(count) {
  const db = getDb();
  return db.prepare(
    'SELECT * FROM questions ORDER BY RANDOM() LIMIT ?'
  ).all(count);
}

function getCategories() {
  const db = getDb();
  const rows = db.prepare(
    'SELECT DISTINCT category, COUNT(*) as count FROM questions GROUP BY category'
  ).all();
  return rows;
}

function createGameRoom(roomId, player1Id, player2Id, category) {
  const db = getDb();
  db.prepare(
    'INSERT INTO game_rooms (id, player1_id, player2_id, category) VALUES (?, ?, ?, ?)'
  ).run(roomId, player1Id, player2Id, category);
}

function updateGameResult(roomId, player1Score, player2Score, winnerId) {
  const db = getDb();
  db.prepare(`
    UPDATE game_rooms
    SET player1_score = ?, player2_score = ?, status = 'finished',
        winner_id = ?, finished_at = CURRENT_TIMESTAMP
    WHERE id = ?
  `).run(player1Score, player2Score, winnerId, roomId);
}

function incrementUserGames(userId, won) {
  const db = getDb();
  if (won) {
    db.prepare(
      'UPDATE users SET games_played = games_played + 1, games_won = games_won + 1 WHERE id = ?'
    ).run(userId);
  } else {
    db.prepare(
      'UPDATE users SET games_played = games_played + 1 WHERE id = ?'
    ).run(userId);
  }
}

const RANK_TIERS = [
  { name: '王者', icon: '👑', minRate: 95 },
  { name: '宗师', icon: '🏆', minRate: 85 },
  { name: '大师', icon: '💎', minRate: 75 },
  { name: '钻石', icon: '💠', minRate: 65 },
  { name: '铂金', icon: '🔮', minRate: 55 },
  { name: '黄金', icon: '🥇', minRate: 40 },
  { name: '白银', icon: '🥈', minRate: 25 },
  { name: '青铜', icon: '🥉', minRate: 0 },
];

function getRank(gamesPlayed, gamesWon) {
  if (gamesPlayed === 0) return { name: '未定级', icon: '⬜' };
  const winRate = (gamesWon / gamesPlayed) * 100;
  for (const tier of RANK_TIERS) {
    if (winRate >= tier.minRate) return { name: tier.name, icon: tier.icon };
  }
  return { name: '青铜', icon: '🥉' };
}

function getLeaderboard(limit = 20) {
  const db = getDb();
  const rows = db.prepare(`
    SELECT nickname, games_played, games_won,
           CASE WHEN games_played > 0
                THEN ROUND(CAST(games_won AS FLOAT) / games_played * 100, 1)
                ELSE 0 END as win_rate
    FROM users
    WHERE games_played > 0
    ORDER BY games_won DESC, win_rate DESC
    LIMIT ?
  `).all(limit);
  return rows.map(r => ({ ...r, rank: getRank(r.games_played, r.games_won) }));
}

module.exports = {
  initializeDatabase,
  getDb,
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
};
