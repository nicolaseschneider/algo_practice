const json = `{
  "hi":"h2i","comma":"comma,value",
  "colon":"colon:value",
  "empty":"",
  "numbers":123
}`;

const nums = '1234567890';

const parseJSON = (input) => {
  const peeled = input.slice(1, input.length - 1);
  const res = {};
  let beginKey;
  let endKey;
  let beginVal;
  let endVal;
  let isNum;

  for(let i = 0; i < peeled.length; i++) {
    if (!beginKey && peeled[i - 1] === '"') {
      beginKey = i;
    } else if (beginKey && !endKey && peeled[i] === '"') {
      endKey = i - 1;
    } else if (endKey && !beginVal && (peeled[i] === '"' || parseInt(peeled[i]) !== NaN)) {
      beginVal = i + 1;
    } else if (beginVal && (peeled[i] === '"' || parseInt(peeled[i]) === NaN)) {
      endVal = i - 1;
    }
    
    if (endVal) {
      const key = peeled.slice(beginKey, endKey + 1);
      const val = peeled.slice(beginVal, endVal + 1);
      res[key] = val;
      beginKey = null;
      endKey = null;
      beginVal = null;
      endVal = null;
      isNum = null;
      i += 1;
    }
  }
  
  return res;
  
}

console.log(parseJSON(json));