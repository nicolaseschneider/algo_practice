
// https://www.hackerrank.com/challenges/contacts/problem

const add = (db, name) => {
  let current = db;
  name.split('').forEach(ch => {
    if (ch in current) {
      current = current[ch];
      current.count += 1;
    } else {
      current[ch] = { count: 1 };
      current = current[ch];
    }
  });
}

const find = (db, name) => {
  let current = db;
  name.split('').forEach(ch => {
    if (ch in current) {
      current = current[ch];
    } else {
      current[ch] = { count: 0 };
      current = current[ch]
    }
  })
  return current.count;
}


function contacts(queries) {
  const db = {};
  const results = [];

  queries.forEach(query => {
    const [type, string] = query
    switch (type) {
      case 'add':
        add(db, string);
        break;
      case 'find':
        results.push(find(db,string));
        break;
      default:
        break;
    }
  })

  return results;
}
