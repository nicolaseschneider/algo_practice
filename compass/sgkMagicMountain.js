     
function Arr2D(r, c, val) {
    return new Array(r).fill(val).map(x => new Array(c).fill(val)); 
 }
  
 function magicMountain(nums) {    
     const R = nums.length;
     const C = nums[0].length;
     
     function* neighbors(r, c) {
         for (let [nr, nc] of [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]) {
             if ((0 <= nr && nr < R) && (0 <= nc && nc < C))
                 if (nums[r][c] <= nums[nr][nc])
                     yield [nr, nc];
         }
     }
  
     function searchFrom(r, c, seen) {
         seen[r][c] = true;
         for (let [nr, nc] of neighbors(r, c)) {
             if (!seen[nr][nc])
                 searchFrom(nr, nc, seen);
         }
     }
  
     const reachableFromLake = Arr2D(R, C, false);
     const reachableFromOcean = Arr2D(R, C, false);
     
     // searchFromOcean
     for (let r = 0; r < R; ++r) 
         searchFrom(r, 0, reachableFromLake);
     for (let c = 0; c < C; ++c) 
         searchFrom(0, c, reachableFromLake);
     
     // searchFromLake
     for (let r = 0; r < R; ++r) 
         searchFrom(r, C - 1, reachableFromOcean);
     for (let c = 0; c < C - 1; ++c) 
         searchFrom(R - 1, c, reachableFromOcean);
     
     const reachableNodes = [];
     for (let r = 0; r < R; ++r) {
         for (let c = 0; c < C; ++c) {
             if (reachableFromLake[r][c] && reachableFromOcean[r][c])
                 reachableNodes.push([r, c]);
         }
     }
     return reachableNodes;
 }