document.getElementById('analyzeBtn').addEventListener('click', async () => {
  const txt = document.getElementById('inputText').value;
  if (!txt.trim()) { alert("Enter some text!"); return; }

  const res = await fetch('/api/analyze', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({text: txt})
  });

  const j = await res.json();
  document.getElementById('result').style.display = 'block';
  document.getElementById('emotion').innerText = "Detected Emotion: " + j.emotion;
  const ul = document.getElementById('recs');
  ul.innerHTML = '';
  j.recommendations.forEach(r => {
    const li = document.createElement('li');
    li.innerText = r;
    ul.appendChild(li);
  });
});
