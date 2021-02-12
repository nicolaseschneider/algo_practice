/*
    input: 2d grid of integers representing heights
    tops and left borders represent an ocean,
    bottom and right represent a lake
    should return the indicies of all magic mountains,
  
    magic mountains flow downward to other indicies vertical/horizontal

    magic mountains can flow to both ocean and lake
*/

const exampleMountains = [
    [0,1,1],
    [-1,3,2],
    [0,1,2],
];

const exampleMountain = [
    [5,0,5],
    [0,2,0],
    [5,0,5],
];

const fourXFour = [
    [5,0,0,5],
    [0,5,5,0],
    [0,5,5,0],
    [5,0,0,5],
]; // [ [0,3], [1,1], [1,2], [2,1], [2,2], [3,0] ]

const fiveXFive = [
    [5,0,0,0,5],
    [0,5,5,5,0],
    [0,5,5,5,0],
    [0,5,5,5,0],
    [5,0,0,0,5],
]

const fuckinGeoarge = [
    [1,2,3,4,5],
    [5,5,4,5,5],
    [5,2,3,5,5],
    [5,1,5,1,5],
    [1,1,1,1,1],
];

const betterExample = [
    [0,1,2],
    [-1,0,0],
]

const betterMountainFinder = (map) => {
    const mapRes = [];

    for(let i = 0; i < map.length; i++) {
        mapRes.push([]);
        for(let j = 0; j < map[i].length; j++) {
            mapRes[i][j] = [false, false];
        }
    }

    fromTop(map, mapRes);
    fromBottom(map, mapRes);
    const result = [];

    for (let idx = 0; idx < mapRes.length; idx++) {
        for (let jdx = 0; jdx < mapRes[idx].length; jdx++) {
            const current = mapRes[idx][jdx]
            if (current[0] && current[1]) {
                result.push([idx, jdx]);
            }
        }
    }
    return result;
}

const findPath = (map, mapRes, i, j, fromTop) => {
    const current = map[i][j];

    const hasSeen = mapRes[i][j][fromTop]
    if (hasSeen) return;
    mapRes[i][j][fromTop] = true;

    if (map[i - 1] && map[i - 1][j] >= current) {
        findPath(map, mapRes, i - 1, j, fromTop);
    }
    if (map[i + 1] && map[i + 1][j] >= current) {
        findPath(map, mapRes, i + 1, j, fromTop);
    }
    if (map[i][j - 1] && map[i][j - 1] >= current) {
        findPath(map, mapRes, i, j - 1, fromTop);
    }
    if (map[i][j + 1] && map[i][j + 1] >= current) {
        findPath(map, mapRes, i, j + 1, fromTop);
    }
}

const fromTop = (map, mapRes) => {
    // all nodes where i index === 0
    // all nodes where j index === 0
    for (let i = 0; i < map.length; i++) {
        let j = 0;
        if (i === 0) {
            while (j < map[i].length) {
                //top row
                findPath(map, mapRes, i, j, 1);
                j++;
            }
        } else {
            // left column
            findPath(map, mapRes, i, j, 1);
        }
    }
}
const fromBottom = (map, mapRes) => {
    for (let i = map.length - 1; i >= 0; i--) {
        let j = map[i].length - 1;
        if (i === map.length - 1) {
            while (j >= 0) {
                findPath(map, mapRes, i, j, 0);
                j--;
            }
        } else {
            findPath(map, mapRes, i, j, 0)
        }
    }
}
console.log(betterMountainFinder(fourXFour))
// const mountainFinder = (map) => {
//     const results = [];
//     for(let i = 0; i < map.length; i++) {
//         for(let j = 0; j < map[i].length; j++) {
//             if (isMagicMountain(map, i, j)) {
//                 results.push([i, j]);
//             }
//         }
//     }
//     return results;
// }



// const isMagicMountain = (map, i, j) => {
//     return canReachOcean(map, i, j) && canReachLake(map, i, j);
// }

// const canReachOcean = (map, i, j, hasSeen = {}) => {
//     if (j < 0 || j > map[i].length - 1) return false;
//     if (i === 0 || j === 0) return true

//     if (hasSeen[`${i},${j}`]) return false
//     const current = map[i][j];
//     hasSeen[`${i},${j}`] = true;

//     const results = [];
//     if (map[i - 1] && map[i - 1][j] <= current) {
//         results.push(canReachOcean(map, i - 1, j, { ...hasSeen }));
//     }
//     if (map[i + 1] && map[i + 1][j] <= current) {
//         results.push(canReachOcean(map, i + 1, j, { ...hasSeen }));
//     }
//     if (map[i][j - 1] <= current) {
//         results.push(canReachOcean(map, i, j - 1, { ...hasSeen }));
//     }
//     if (map[i][j + 1] <= current) {
//         results.push(canReachOcean(map, i, j + 1, { ...hasSeen }));
//     }
//     return results.some(val => (val === true));
// }

// const canReachLake = (map, i, j, hasSeen = {}) => {
//     if (j < 0 || j > map[i].length - 1) return false;
//     if (i === map.length - 1 || j === map[i].length - 1) return true
//     if (hasSeen[`${i},${j}`]) return false
//     const current = map[i][j];
//     hasSeen[`${i},${j}`] = true;
//     const results = [];
//     if (map[i - 1] && map[i - 1][j] <= current) {
//         results.push(canReachLake(map, i - 1, j, { ...hasSeen }));
//     }
//     if (map[i + 1] && map[i + 1][j] <= current) {
//         results.push(canReachLake(map, i + 1, j, { ...hasSeen }));
//     }
//     if (map[i][j - 1] <= current) {
//         results.push(canReachLake(map, i, j - 1, { ...hasSeen }));
//     }
//     if (map[i][j + 1] <= current) {
//         results.push(canReachLake(map, i, j + 1, { ...hasSeen }));
//     }
//     return results.some(val => (val === true));
// }
// console.log(mountainFinder(fuckinGeoarge))
// betterMountainFinder(exampleMountain)
// console.log(mountainFinder(exampleMountain)) // [[0,2], [1,1], [2,0]]