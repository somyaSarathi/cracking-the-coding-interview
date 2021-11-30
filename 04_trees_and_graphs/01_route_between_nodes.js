const prompt = require('prompt-sync')();

const dfs = (graph, start, end, visited=new Set()) => {
    if(start === end) return true;

    if(visited.has(start)) return false;

    visited.add(start)

    for(let conn of graph[start]) {
        if (dfs(graph, conn, end, visited)) return true;
    }

    return false;
}


function bfs(graph, start, end) {
    if(start === end) return true;

    const visited = new Set()
    const queue = [ start ]

    while(queue.length > 0) {
        let curr = queue.shift()
        visited.add(curr)

        for(let conn of graph[curr]) {
            if(conn === end) return true;
            if(!visited.has(conn)) queue.push(conn);
        }
    }

    return false;
}

/**
    (f) → (g) → (h)
     ↓  ↗
    (i) ← (j)
     ↓
    (k)
 */

const graph = {
    f: ['g', 'i'],
    g: ['h'],
    h: [],
    i: ['g', 'k'],
    j: ['i'],
    k: [],
};

console.log(bfs(graph, 'f', 'k'));  // true
console.log(bfs(graph, 'f', 'j'));  // false

console.log(dfs(graph, 'i', 'h'));  // true
console.log(dfs(graph, 'k', 'f'));  // false
