const fs = require('fs');
const path = require('path');
const { initializeDatabase, getDb } = require('./database');

function seedQuestions() {
  initializeDatabase();
  const db = getDb();

  const questionsPath = path.join(__dirname, 'data', 'questions.json');
  const questionsData = JSON.parse(fs.readFileSync(questionsPath, 'utf-8'));

  db.prepare('DELETE FROM questions').run();

  const insert = db.prepare(
    'INSERT INTO questions (category, question_text, options, correct_answer) VALUES (?, ?, ?, ?)'
  );

  const insertMany = db.transaction((data) => {
    let count = 0;
    for (const [category, questions] of Object.entries(data)) {
      for (const q of questions) {
        insert.run(category, q.question, JSON.stringify(q.options), q.answer);
        count++;
      }
    }
    return count;
  });

  const total = insertMany(questionsData);
  console.log(`Seeded ${total} questions.`);

  const counts = db.prepare(
    'SELECT category, COUNT(*) as count FROM questions GROUP BY category'
  ).all();
  for (const row of counts) {
    console.log(`  ${row.category}: ${row.count} questions`);
  }
}

seedQuestions();
