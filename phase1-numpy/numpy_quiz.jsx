import { useState } from "react";

const questions = [
  {
    topic: "Array Creation",
    question: "What does np.arange(2, 10, 3) produce?",
    options: ["[2, 5, 8]", "[2, 4, 6, 8]", "[2, 5, 8, 11]", "[3, 6, 9]"],
    answer: 0,
    explanation: "np.arange(start, stop, step) starts at 2, steps by 3, and stops BEFORE 10. So: 2, 5, 8. The next would be 11 which exceeds 10, so it stops.",
  },
  {
    topic: "Array Properties",
    question: "What is the output of:\narr = np.array([[1,2,3],[4,5,6]])\nprint(arr.shape)",
    options: ["(6,)", "(3, 2)", "(2, 3)", "(2, 2)"],
    answer: 2,
    explanation: "shape returns (rows, columns). The array has 2 rows and 3 columns → (2, 3). Remember: rows first, columns second!",
  },
  {
    topic: "Array Properties",
    question: "What does arr.ndim return for a 3D array?",
    options: ["1", "2", "3", "The shape tuple"],
    answer: 2,
    explanation: "ndim returns the NUMBER of dimensions. A 3D array has 3 dimensions — think of it like a cube of numbers.",
  },
  {
    topic: "Indexing & Slicing",
    question: "Given matrix = np.array([[1,2,3],[4,5,6],[7,8,9]]), what does matrix[:, 1] return?",
    options: ["[1, 2, 3]", "[2, 5, 8]", "[4, 5, 6]", "[1, 4, 7]"],
    answer: 1,
    explanation: "matrix[:, 1] means 'all rows, column at index 1'. Column index 1 is the second column: 2, 5, 8. Remember indexing starts at 0!",
  },
  {
    topic: "Indexing & Slicing",
    question: "What does arr[::2] do to array [10, 20, 30, 40, 50]?",
    options: ["[10, 30, 50]", "[20, 40]", "[10, 20]", "[30, 40, 50]"],
    answer: 0,
    explanation: "arr[::2] means start from beginning, go to end, step by 2. So it picks every 2nd element: index 0, 2, 4 → 10, 30, 50.",
  },
  {
    topic: "Array Math",
    question: "What is the difference between A * B and A @ B in NumPy?",
    options: [
      "They are the same",
      "* is matrix multiply, @ is element-wise",
      "* is element-wise, @ is matrix multiply",
      "* works on 1D, @ works on 2D",
    ],
    answer: 2,
    explanation: "* performs element-wise multiplication (each element multiplied with corresponding element). @ performs true matrix multiplication (dot product). This is one of the most common mistakes in ML!",
  },
  {
    topic: "Array Math",
    question: "What does np.sum(arr, axis=0) do on a 2D array?",
    options: [
      "Sums all elements into one number",
      "Sums across rows → one value per column",
      "Sums across columns → one value per row",
      "Sums only the first row",
    ],
    answer: 1,
    explanation: "axis=0 goes DOWN the rows (vertically), giving one sum per column. axis=1 goes ACROSS columns (horizontally), giving one sum per row. Think: axis=0 collapses rows, axis=1 collapses columns.",
  },
  {
    topic: "Reshape",
    question: "arr = np.arange(12). What does arr.reshape(-1, 4) produce?",
    options: ["Shape (4, 3)", "Shape (3, 4)", "Shape (12, 4)", "Error"],
    answer: 1,
    explanation: "-1 tells NumPy to figure out that dimension automatically. We have 12 elements and 4 columns, so 12/4 = 3 rows. Result is shape (3, 4).",
  },
  {
    topic: "Boolean Masking",
    question: "Given arr = np.array([5, 15, 25, 35]), what does arr[arr > 10] return?",
    options: ["[5]", "[15, 25, 35]", "[True, False, False]", "[25, 35]"],
    answer: 1,
    explanation: "arr > 10 creates a boolean mask [False, True, True, True]. Applying it to arr filters and returns only elements where mask is True → [15, 25, 35].",
  },
  {
    topic: "Boolean Masking",
    question: "What is the correct way to find elements between 10 and 30 in NumPy?",
    options: [
      "arr[10 < arr < 30]",
      "arr[arr > 10 and arr < 30]",
      "arr[(arr > 10) & (arr < 30)]",
      "arr[arr.between(10, 30)]",
    ],
    answer: 2,
    explanation: "In NumPy you must use & (bitwise AND) with parentheses around each condition. Python's 'and' keyword doesn't work on arrays. arr[10 < arr < 30] also fails for the same reason.",
  },
  {
    topic: "Random",
    question: "Why do we use np.random.seed(42)?",
    options: [
      "To generate exactly 42 random numbers",
      "To make random numbers reproducible",
      "To set the maximum random value to 42",
      "To speed up random generation",
    ],
    answer: 1,
    explanation: "Setting a seed makes 'random' results reproducible — everyone running the code gets the same numbers. 42 is just a convention (a hitchhiker's guide reference!). Critical in ML for consistent experiments.",
  },
  {
    topic: "Array Manipulation",
    question: "What is the difference between np.vstack and np.hstack?",
    options: [
      "vstack joins side by side, hstack joins top to bottom",
      "vstack joins top to bottom, hstack joins side by side",
      "They are the same",
      "vstack works on 1D, hstack works on 2D",
    ],
    answer: 1,
    explanation: "vstack (vertical stack) stacks arrays ON TOP of each other — increases rows. hstack (horizontal stack) stacks arrays SIDE BY SIDE — increases columns. Think v = vertical, h = horizontal.",
  },
  {
    topic: "Array Creation",
    question: "What does np.linspace(0, 1, 5) return?",
    options: [
      "[0, 0.2, 0.4, 0.6, 0.8]",
      "[0, 0.25, 0.5, 0.75, 1.0]",
      "[0, 1, 2, 3, 4]",
      "[0.2, 0.4, 0.6, 0.8, 1.0]",
    ],
    answer: 1,
    explanation: "linspace(start, stop, num) generates 'num' evenly spaced values INCLUSIVE of both start and stop. 5 points between 0 and 1: 0, 0.25, 0.5, 0.75, 1.0. Unlike arange, the stop IS included!",
  },
  {
    topic: "Transpose",
    question: "If matrix.shape is (3, 4), what is matrix.T.shape?",
    options: ["(3, 4)", "(4, 4)", "(4, 3)", "(12,)"],
    answer: 2,
    explanation: "Transpose flips rows and columns. A (3, 4) matrix has 3 rows and 4 columns. After transposing, rows become columns and columns become rows → (4, 3).",
  },
  {
    topic: "Real World",
    question: "In ML, what does reshape(-1, 1) typically do?",
    options: [
      "Flattens array to 1D",
      "Converts a 1D array to a single column (2D)",
      "Converts a 1D array to a single row (2D)",
      "Removes all dimensions",
    ],
    answer: 1,
    explanation: "reshape(-1, 1) converts a 1D array like [1,2,3] into a column vector [[1],[2],[3]] with shape (n, 1). This is used constantly in ML when algorithms expect 2D input!",
  },
];

const topicColors = {
  "Array Creation": "bg-blue-100 text-blue-700",
  "Array Properties": "bg-purple-100 text-purple-700",
  "Indexing & Slicing": "bg-pink-100 text-pink-700",
  "Array Math": "bg-yellow-100 text-yellow-700",
  "Reshape": "bg-orange-100 text-orange-700",
  "Boolean Masking": "bg-green-100 text-green-700",
  "Random": "bg-teal-100 text-teal-700",
  "Array Manipulation": "bg-indigo-100 text-indigo-700",
  "Transpose": "bg-red-100 text-red-700",
  "Real World": "bg-emerald-100 text-emerald-700",
};

export default function NumpyQuiz() {
  const [current, setCurrent] = useState(0);
  const [selected, setSelected] = useState(null);
  const [score, setScore] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const [answers, setAnswers] = useState([]);
  const [confirmed, setConfirmed] = useState(false);

  const q = questions[current];

  const handleSelect = (idx) => { if (!confirmed) setSelected(idx); };

  const handleConfirm = () => {
    if (selected === null) return;
    const correct = selected === q.answer;
    if (correct) setScore((s) => s + 1);
    setAnswers((prev) => [...prev, { selected, correct, answer: q.answer }]);
    setConfirmed(true);
  };

  const handleNext = () => {
    if (current + 1 < questions.length) {
      setCurrent((c) => c + 1);
      setSelected(null);
      setConfirmed(false);
    } else {
      setShowResult(true);
    }
  };

  const handleRestart = () => {
    setCurrent(0); setSelected(null); setScore(0);
    setShowResult(false); setAnswers([]); setConfirmed(false);
  };

  const getGrade = () => {
    const pct = (score / questions.length) * 100;
    if (pct >= 90) return { label: "NumPy Master! 🏆", color: "text-emerald-600" };
    if (pct >= 75) return { label: "Great job! 🎉", color: "text-blue-600" };
    if (pct >= 60) return { label: "Good effort! 👍", color: "text-yellow-600" };
    return { label: "Keep practicing! 💪", color: "text-red-500" };
  };

  if (showResult) {
    const grade = getGrade();
    const pct = Math.round((score / questions.length) * 100);
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
        <div className="bg-white rounded-2xl shadow-lg p-8 max-w-lg w-full text-center">
          <div className="text-6xl mb-4">🔢</div>
          <h2 className="text-2xl font-bold text-gray-800 mb-1">Phase 1 — NumPy Complete!</h2>
          <p className={`text-xl font-semibold mb-6 ${grade.color}`}>{grade.label}</p>
          <div className="bg-gray-50 rounded-xl p-6 mb-6">
            <p className="text-5xl font-bold text-gray-800">{score}<span className="text-2xl text-gray-400">/{questions.length}</span></p>
            <p className="text-gray-500 mt-1">{pct}% correct</p>
            <div className="w-full bg-gray-200 rounded-full h-3 mt-4">
              <div className="h-3 rounded-full transition-all duration-700"
                style={{ width: `${pct}%`, backgroundColor: pct >= 75 ? "#10b981" : pct >= 60 ? "#f59e0b" : "#ef4444" }} />
            </div>
          </div>
          <div className="text-left mb-6 space-y-3 max-h-72 overflow-y-auto pr-1">
            {questions.map((q, i) => (
              <div key={i} className="flex items-start gap-2 text-sm border-b border-gray-100 pb-3">
                <span className={answers[i]?.correct ? "text-emerald-500 mt-0.5 text-base" : "text-red-400 mt-0.5 text-base"}>
                  {answers[i]?.correct ? "✓" : "✗"}
                </span>
                <div className="flex-1">
                  <span className={`text-xs px-2 py-0.5 rounded-full font-medium mr-1 ${topicColors[q.topic] || "bg-gray-100 text-gray-600"}`}>{q.topic}</span>
                  <span className="text-gray-600">{q.question.split('\n')[0]}</span>
                  {!answers[i]?.correct && (
                    <>
                      <p className="text-emerald-600 text-xs mt-1 font-medium">✓ Correct: {q.options[q.answer]}</p>
                      <p className="text-gray-400 text-xs mt-0.5 italic">{q.explanation}</p>
                    </>
                  )}
                </div>
              </div>
            ))}
          </div>
          <button onClick={handleRestart}
            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-3 rounded-xl transition">
            Retake Quiz
          </button>
          <p className="text-xs text-gray-400 mt-3">Ready for Phase 2 — Pandas? 🐼</p>
        </div>
      </div>
    );
  }

  const isCorrect = confirmed && selected === q.answer;

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-lg p-6 max-w-xl w-full">
        <div className="flex items-center justify-between mb-2">
          <span className="text-xs font-semibold text-indigo-500 tracking-wide uppercase">⚡ NumPy — Phase 1 Quiz</span>
          <span className="text-sm font-semibold text-indigo-600">Score: {score}</span>
        </div>
        <div className="flex items-center justify-between mb-4">
          <span className="text-sm font-medium text-gray-400">Question {current + 1} of {questions.length}</span>
        </div>
        <div className="w-full bg-gray-100 rounded-full h-2 mb-5">
          <div className="bg-indigo-500 h-2 rounded-full transition-all duration-500"
            style={{ width: `${(current / questions.length) * 100}%` }} />
        </div>
        <span className={`text-xs font-semibold px-3 py-1 rounded-full ${topicColors[q.topic] || "bg-gray-100 text-gray-600"}`}>
          {q.topic}
        </span>
        <pre className="mt-3 mb-5 text-gray-800 font-sans text-base font-semibold whitespace-pre-wrap leading-snug">
          {q.question}
        </pre>
        <div className="space-y-3 mb-4">
          {q.options.map((opt, idx) => {
            let style = "border-gray-200 bg-white text-gray-700 hover:border-indigo-400 hover:bg-indigo-50";
            if (confirmed) {
              if (idx === q.answer) style = "border-emerald-400 bg-emerald-50 text-emerald-800";
              else if (idx === selected) style = "border-red-400 bg-red-50 text-red-700";
              else style = "border-gray-100 bg-gray-50 text-gray-400";
            } else if (selected === idx) {
              style = "border-indigo-500 bg-indigo-50 text-indigo-800";
            }
            return (
              <button key={idx} onClick={() => handleSelect(idx)}
                className={`w-full text-left px-4 py-3 rounded-xl border-2 font-medium transition-all duration-150 ${style}`}>
                <span className="mr-2 text-xs font-bold opacity-50">{["A", "B", "C", "D"][idx]}.</span>
                {opt}
                {confirmed && idx === q.answer && <span className="float-right">✓</span>}
                {confirmed && idx === selected && idx !== q.answer && <span className="float-right">✗</span>}
              </button>
            );
          })}
        </div>
        {confirmed && (
          <div className={`rounded-xl p-4 mb-4 text-sm leading-relaxed border ${isCorrect ? "bg-emerald-50 border-emerald-200 text-emerald-900" : "bg-amber-50 border-amber-200 text-amber-900"}`}>
            <p className="font-semibold mb-1">
              {isCorrect ? "✅ Correct!" : `❌ Not quite — correct answer: ${q.options[q.answer]}`}
            </p>
            <p className="text-sm opacity-90">{q.explanation}</p>
          </div>
        )}
        {!confirmed ? (
          <button onClick={handleConfirm} disabled={selected === null}
            className={`w-full py-3 rounded-xl font-semibold transition ${selected === null ? "bg-gray-200 text-gray-400 cursor-not-allowed" : "bg-indigo-600 hover:bg-indigo-700 text-white"}`}>
            Confirm Answer
          </button>
        ) : (
          <button onClick={handleNext}
            className="w-full py-3 rounded-xl font-semibold bg-indigo-600 hover:bg-indigo-700 text-white transition">
            {current + 1 < questions.length ? "Next Question →" : "See Results 🎉"}
          </button>
        )}
      </div>
    </div>
  );
}
