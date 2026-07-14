import os

base_dir = r'C:/Users/jogip/OneDrive/Desktop/MY_ORGANIZED_DESKTOP/mcq'
os.chdir(base_dir)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace initQuiz
content = content.replace('''function initQuiz(mode) {
            quizMode = mode;
            currentIdx = 0;
            userAnswers = new Array(quizData.length).fill(null);
            
            document.getElementById('start-screen').classList.add('hidden');
            document.getElementById('quiz-ui').classList.remove('hidden');
            
            // Auto-fill answers if in "With Answer" mode
            if (mode === 'withAnswer') {
                quizData.forEach((item, i) => userAnswers[i] = item.a);
            }
            
            render();
        }''', '''function initQuiz(mode) {
            try {
                quizMode = mode;
                currentIdx = 0;
                userAnswers = new Array(quizData.length).fill(null);
                
                document.getElementById('start-screen').classList.add('hidden');
                document.getElementById('quiz-ui').classList.remove('hidden');
                
                // Auto-fill answers if in "With Answer" mode
                if (mode === 'withAnswer') {
                    quizData.forEach((item, i) => userAnswers[i] = item.a);
                }
                
                render();
            } catch(e) {
                console.error("Critical error in initQuiz:", e);
                alert("An error occurred during initialization.");
            }
        }''')

# Replace render
content = content.replace('''function render() {
            const q = quizData[currentIdx];
            const displayNum = currentIdx >= 45 ? currentIdx + 2 : currentIdx + 1; // Skip 46 handling

            document.getElementById('progress-text').textContent = `${currentIdx + 1}/${quizData.length}`;
            document.getElementById('q-number').textContent = `Question ${displayNum}/89`;
            document.getElementById('question-text').innerHTML = q.q;

            const list = document.getElementById('options-list');
            list.innerHTML = "";

            q.o.forEach((opt, idx) => {
                const btn = document.createElement('button');
                btn.className = "opt";
                
                // Mode logic
                if (userAnswers[currentIdx] !== null) {
                    if (quizMode === 'withAnswer') {
                        if (idx === q.a) btn.classList.add('correct');
                    } else {
                        // Exam Mode: Reveal result on selection
                        if (idx === q.a) btn.classList.add('correct');
                        if (userAnswers[currentIdx] === idx && idx !== q.a) btn.classList.add('wrong');
                    }
                    btn.disabled = true;
                }

                btn.innerHTML = `<span class="tag">${String.fromCharCode(97 + idx)}</span><span>${opt}</span>`;
                btn.onclick = () => select(idx);
                list.appendChild(btn);
            });

            document.getElementById('next-btn').textContent = currentIdx === quizData.length - 1 ? "Finish" : "Next";
            
            if (window.MathJax) MathJax.typesetPromise();
        }''', '''function render() {
            try {
                const q = quizData[currentIdx];
                const displayNum = currentIdx >= 45 ? currentIdx + 2 : currentIdx + 1; // Skip 46 handling

                document.getElementById('progress-text').textContent = `${currentIdx + 1}/${quizData.length}`;
                document.getElementById('q-number').textContent = `Question ${displayNum}/89`;
                document.getElementById('question-text').innerHTML = q.q;

                const list = document.getElementById('options-list');
                list.innerHTML = "";

                q.o.forEach((opt, idx) => {
                    const btn = document.createElement('button');
                    btn.className = "opt";
                    
                    // Mode logic
                    if (userAnswers[currentIdx] !== null) {
                        if (quizMode === 'withAnswer') {
                            if (idx === q.a) btn.classList.add('correct');
                        } else {
                            // Exam Mode: Reveal result on selection
                            if (idx === q.a) btn.classList.add('correct');
                            if (userAnswers[currentIdx] === idx && idx !== q.a) btn.classList.add('wrong');
                        }
                        btn.disabled = true;
                    }

                    btn.innerHTML = `<span class="tag">${String.fromCharCode(97 + idx)}</span><span>${opt}</span>`;
                    btn.onclick = () => select(idx);
                    list.appendChild(btn);
                });

                document.getElementById('next-btn').textContent = currentIdx === quizData.length - 1 ? "Finish" : "Next";
                
                if (window.MathJax) MathJax.typesetPromise();
            } catch(e) {
                console.error("Error during rendering:", e);
            }
        }''')

# Replace select
content = content.replace('''function select(idx) {
            if (quizMode === 'withAnswer') return;
            if (userAnswers[currentIdx] !== null) return;
            
            userAnswers[currentIdx] = idx;
            render();
        }''', '''function select(idx) {
            try {
                if (quizMode === 'withAnswer') return;
                if (userAnswers[currentIdx] !== null) return;
                
                userAnswers[currentIdx] = idx;
                render();
            } catch(e) {
                console.error("Error during selection:", e);
            }
        }''')

# Replace nav
content = content.replace('''function nav(dir) {
            if (dir === -1 && currentIdx === 0) {
                location.reload();
                return;
            }

            if (dir === 1 && currentIdx === quizData.length - 1) {
                showResults();
                return;
            }

            const next = currentIdx + dir;
            if (next >= 0 && next < quizData.length) {
                currentIdx = next;
                render();
                document.querySelector('.scroll-area').scrollTop = 0;
            }
        }''', '''function nav(dir) {
            try {
                if (dir === -1 && currentIdx === 0) {
                    location.reload();
                    return;
                }

                if (dir === 1 && currentIdx === quizData.length - 1) {
                    showResults();
                    return;
                }

                const next = currentIdx + dir;
                if (next >= 0 && next < quizData.length) {
                    currentIdx = next;
                    render();
                    document.querySelector('.scroll-area').scrollTop = 0;
                }
            } catch(e) {
                console.error("Error during navigation:", e);
            }
        }''')

# Replace showResults
content = content.replace('''function showResults() {
            document.getElementById('quiz-ui').classList.add('hidden');
            document.getElementById('result-screen').classList.remove('hidden');
            
            const score = userAnswers.reduce((acc, curr, i) => acc + (curr === quizData[i].a ? 1 : 0), 0);
            const percent = Math.round((score / quizData.length) * 100);
            
            document.getElementById('final-score').textContent = `${percent}%`;
            document.getElementById('result-desc').textContent = `Correct: ${score} | Total: ${quizData.length}`;
        }''', '''function showResults() {
            try {
                document.getElementById('quiz-ui').classList.add('hidden');
                document.getElementById('result-screen').classList.remove('hidden');
                
                const score = userAnswers.reduce((acc, curr, i) => acc + (curr === quizData[i].a ? 1 : 0), 0);
                const percent = Math.round((score / quizData.length) * 100);
                
                document.getElementById('final-score').textContent = `${percent}%`;
                document.getElementById('result-desc').textContent = `Correct: ${score} | Total: ${quizData.length}`;
            } catch(e) {
                console.error("Error showing results:", e);
            }
        }''')

import os
os.makedirs('src', exist_ok=True)
os.makedirs('tests', exist_ok=True)
os.makedirs('.github/workflows', exist_ok=True)

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

os.remove('index.html')
