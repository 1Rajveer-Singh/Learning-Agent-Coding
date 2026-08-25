const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
const n = Number(input);

function fibonacci(n) {
    if (n <= 1) {
        return n;
    }

    let prev = 0;
    let curr = 1;

    for (let i = 2; i <= n; i++) {
        const next = prev + curr;
        prev = curr;
        curr = next;
    }

    return curr;
}

console.log(fibonacci(n));